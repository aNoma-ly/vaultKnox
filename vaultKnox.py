import hashlib
import sqlite3
from tkinter import *
from tkinter import simpledialog
from functools import partial
import uuid
import pyperclip
import base64
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

#encryption

backend = default_backend()
salt = b'2444'

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=backend
)

encryptionKey = 0

def encrypt(message: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(message)

def decrypt(message: bytes, token: bytes) -> bytes:
    return Fernet(token).decrypt(message)


#  database

with sqlite3.connect("vaultKnox_passwords.db") as db:
    cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS masterpassword(
id INTEGER PRIMARY KEY,
password TEXT NOT NULL,
recoveryKey TEXT NOT NULL);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS passwordVault(
id INTEGER PRIMARY KEY,
service TEXT NOT NULL,
username TEXT NOT NULL,
password TEXT NOT NULL);
""")

#Popup dialogue

def popUp(text):
    userInput = simpledialog.askstring("Please enter string", text)
    return userInput


# from tkinter import ttk

window = Tk()
window.update()

window.title("Vault Knox Password Manager")

#  Init
frame = Frame(window)
frame.pack()

def hashPassword(input):
    hash = hashlib.sha256(input)
    hash = hash.hexdigest()

    return hash

def firstScreen():
    for widget in window.winfo_children():
        widget.destroy()

    topframe = Frame(window)
    topframe.pack(side=TOP)

    window.geometry("+{}+{}".format(500, 200))
    window.geometry("500x500")

    window.title("Create your master password")

    lbl = Label(topframe, text="Enter your master password")
    lbl.config(anchor=CENTER)
    lbl.pack()

    txt = Entry(topframe, width=20)
    txt.focus()
    txt.pack(side=LEFT)

    def hideT():
        txt.config(show="*")
        txt1.config(show="*")

    def showT():
        txt.config(show="")
        txt1.config(show="")

    def checkT():
        global x
        x += 1
        if x % 2 == 1:
            btn3['text'] = "Show"
            hideT()
        else:
            btn3['text'] = "Hide"
            showT()

    global x
    x = 0
    btn3 = Button(topframe, text="Hide", command=checkT)
    btn3.pack(side=RIGHT)

    lbl1 = Label(window, text="Repeat your master password")
    lbl1.config(anchor=CENTER)
    lbl1.pack()

    txt1 = Entry(window, width=20)
    txt1.pack()

    def checkMasterPW():
        if txt.get() == txt1.get():
            sql = "DELETE FROM masterpassword WHERE id = 1"

            cursor.execute(sql)

            hashedPassword = hashPassword(txt.get().encode('utf-8'))

            key = str(uuid.uuid4().hex)
            recoveryKey = hashPassword(key.encode('utf-8'))

            global encryptionKey
            encryptionKey = base64.urlsafe_b64encode(kdf.derive(txt.get().encode()))


            insert_password = """INSERT INTO masterpassword(password, recoveryKey)
            VALUES(?, ?)"""
            cursor.execute(insert_password, ((hashedPassword), (recoveryKey)))
            db.commit()

            recoveryScreen(key)
        else:
            txt.delete(0, 'end')
            txt1.delete(0, 'end')
            lbl2 = Label(window, text="Password do not match")
            lbl1.config(anchor=CENTER)
            lbl2.pack()
            txt.focus()

    btn2 = Button(window, text="Submit", command=checkMasterPW)
    btn2.pack(pady=5)


def recoveryScreen(key):
    for widget in window.winfo_children():
        widget.destroy()

    topframe = Frame(window)
    topframe.pack(side=TOP)

    window.geometry("500x500")

    window.title("Save this key to recover your account")

    lbl = Label(topframe, text="Enter your saved recovery key")
    lbl.config(anchor=CENTER)
    lbl.pack()

    lbl1 = Label(window, text=key)
    lbl1.config(anchor=CENTER)
    lbl1.pack()

    def copyKey():
        pyperclip.copy(lbl1.cget("text"))


    btn2 = Button(window, text="Copy Key", command=copyKey)
    btn2.pack(pady=5)

    def done():
        passwordVault()

    btn2 = Button(window, text="Done", command=done)
    btn2.pack()

def resetScreen():
    for widget in window.winfo_children():
        widget.destroy()

    topframe = Frame(window)
    topframe.pack(side=TOP)

    window.geometry("500x500")

    window.title("Enter Recovery Key")

    lbl = Label(topframe, text="Enter Recovery Key")
    lbl.config(anchor=CENTER)
    lbl.pack()

    txt = Entry(topframe, width=20)  # hide entry , show="*"
    txt.pack(side=LEFT)
    txt.focus()

    lbl1 = Label(window)
    lbl1.config(anchor=CENTER)
    lbl1.pack()

    def getRecoveryKey():
        recoveryKeyCheck = hashPassword(str(txt.get()).encode('utf-8'))
        cursor.execute("SELECT * FROM masterpassword WHERE id = 1 AND recoveryKey = ?", [(recoveryKeyCheck)])
        return cursor.fetchall()

    def checkRecoveryKey():
        checked = getRecoveryKey()

        if checked:
            firstScreen()
        else:
            txt.delete(0, 'end')
            lbl1.config(text='Wrong key')

    btn2 = Button(window, text="Check Key", command=checkRecoveryKey)
    btn2.pack(pady=5)


def loginScreen():
    for widget in window.winfo_children():
        widget.destroy()

    topframe = Frame(window)
    topframe.pack(side=TOP)

    window.geometry("+{}+{}".format(500, 200))

    window.geometry("500x500")

    window.title("Vault Knox Login")

    lbl = Label(topframe, text="Please enter your master password")
    lbl.config(anchor=CENTER)
    lbl.pack()

    txt = Entry(topframe, width=20)  # hide entry , show="*"
    txt.pack(side=LEFT)
    txt.focus()  # focus cursor at field

    lbl1 = Label(window)
    lbl1.pack()

    def getMasterPassword():
        checkHashedPW = hashPassword(txt.get().encode('utf-8'))

        global encryptionKey
        encryptionKey = base64.urlsafe_b64encode(kdf.derive(txt.get().encode()))

        cursor.execute("SELECT * FROM masterpassword WHERE id = 1 AND password = ?", [(checkHashedPW)])

        return cursor.fetchall()

    def checkPassword():
        match = getMasterPassword()

        if match:
            passwordVault()
        else:
            txt.delete(0, 'end')
            lbl1.config(text="Password is not valid.")

    def hideT():
        txt.config(show="*")

    def showT():
        txt.config(show="")

    def checkT():
        global x
        x += 1
        if x % 2 == 1:
            btn2['text'] = "Show"
            hideT()
        else:
            btn2['text'] = "Hide"
            showT()

    global x
    x = 0
    btn2 = Button(topframe, text="Hide", command=checkT)
    btn2.pack(side=RIGHT)

    def resetPassword():
        resetScreen()

    btn = Button(window, text="Submit", command=checkPassword)
    btn.pack()  # pady to add padding padx - left,right'''

    btn3 = Button(window, text="Reset Password", command=resetPassword)
    btn3.pack(pady=5)

def passwordVault():
    for widget in window.winfo_children():
        widget.destroy()

    def addEntry():
        textOne = "Service"
        textTwo = "Username"
        textThree = "Password"

        service = encrypt(popUp(textOne).encode(), encryptionKey)
        username = encrypt(popUp(textTwo).encode(), encryptionKey)
        password = encrypt(popUp(textThree).encode(), encryptionKey)

        insert_fields = """INSERT INTO passwordVault(service, username, password) 
        VALUES(?, ?, ?)"""


        cursor.execute(insert_fields, (service, username, password))
        db.commit()

        passwordVault()

    def removeEntry(input):
        cursor.execute("DELETE FROM passwordVault WHERE id = ?", (input,))

        db.commit()

        passwordVault()

    def updateEntry(input):

        textOne = "Service"
        textTwo = "Username"
        textThree = "Password"

        service = encrypt(popUp(textOne).encode(), encryptionKey)
        username = encrypt(popUp(textTwo).encode(), encryptionKey)
        password = encrypt(popUp(textThree).encode(), encryptionKey)

        sql = "UPDATE passwordVault SET service = ?, username = ?, password = ? WHERE id = ?"

        cursor.execute(sql, (service, username, password, input, ))

        db.commit()
        passwordVault()


    window.geometry("+{}+{}".format(150, 0))
    window.geometry("1100x750")

    window.title("Vault Knox Passwords")  # add name variable to title

    lbl = Label(window, text="Your password vault")
    lbl.grid(column=2)

    btn = Button(window, text="Add entry +", command=addEntry)
    btn.grid(column=2, pady=10)

    lbl = Label(window, text="Service")
    lbl.grid(column=0, row=2, padx=80)

    lbl = Label(window, text="Username")
    lbl.grid(column=1, row=2, padx=80)

    lbl = Label(window, text="Password")
    lbl.grid(column=2, row=2, padx=80)

    cursor.execute("SELECT * FROM passwordVault")
    if cursor.fetchall() != None:
        i = 0


        while True:
            cursor.execute("SELECT * FROM passwordVault")
            array = cursor.fetchall()

            if(len(array) == 0):
                break

            lblOne = Label(window, text=(decrypt(array[i][1], encryptionKey)), font=("Helvetica", 12))
            lblOne.grid(column=0, row=i+3)

            lblOne = Label(window, text=(decrypt(array[i][2], encryptionKey)), font=("Helvetica", 12))
            lblOne.grid(column=1, row=i+3)

            lblOne = Label(window, text=(decrypt(array[i][3], encryptionKey)), font=("Helvetica", 12))
            lblOne.grid(column=2, row=i+3)

            btn = Button(window, text="Delete entry", command=partial(removeEntry, array[i][0]))
            btn.grid(column=3, row=i+3, pady=10)

            btnOne = Button(window, text="Update entry", command=partial(updateEntry, array[i][0]))
            btnOne.grid(column=4, row=i + 3, pady=10)

            i += 1

            cursor.execute("SELECT * FROM passwordVault")
            if len(cursor.fetchall()) <= i:
                break

cursor.execute("SELECT * FROM masterpassword")

if cursor.fetchall():
    loginScreen()
else:
    firstScreen()

window.mainloop()


#TODO implement form validation for password entries and master password
#TODO comment and rename
#TODO attempt password and reset in same instance(bug)
#TODO strong password generator
#TODO error handling