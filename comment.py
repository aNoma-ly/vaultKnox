# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
'''import tkinter as tk
from tkinter import simpledialog

class MyDialog(tk.simpledialog.Dialog):
    def __init__(self, parent, title):
        self.my_username = None
        self.my_password = None
        super().__init__(parent, title)

    def body(self, frame):
        # print(type(frame)) # tkinter.Frame
        self.my_username_label = tk.Label(frame, width=25, text="Username")
        self.my_username_label.pack()
        self.my_username_box = tk.Entry(frame, width=25)
        self.my_username_box.pack()

        self.my_password_label = tk.Label(frame, width=25, text="Password")
        self.my_password_label.pack()
        self.my_password_box = tk.Entry(frame, width=25)
        self.my_password_box.pack()
        self.my_password_box['show'] = '*'

        return frame

    def ok_pressed(self):
        # print("ok")
        self.my_username = self.my_username_box.get()
        self.my_password = self.my_password_box.get()
        self.destroy()

    def cancel_pressed(self):
        # print("cancel")
        self.destroy()


    def buttonbox(self):
        self.ok_button = tk.Button(self, text='OK', width=5, command=self.ok_pressed)
        self.ok_button.pack(side="left")
        cancel_button = tk.Button(self, text='Cancel', width=5, command=self.cancel_pressed)
        cancel_button.pack(side="right")
        self.bind("<Return>", lambda event: self.ok_pressed())
        self.bind("<Escape>", lambda event: self.cancel_pressed())

def mydialog(app):
    dialog = MyDialog(title="Login", parent=app)
    return dialog.my_username, dialog.my_password


def main():
    app.title('Dialog')

    string_button = tk.Button(app, text='Show', width=25, command=show_dialog)
    string_button.pack()

    exit_button = tk.Button(app, text='Close', width=25, command=app.destroy)
    exit_button.pack()

    app.mainloop()

def show_dialog():
    answer = mydialog(app)
    # print(type(answer)) # tuple
    print(answer)

app = tk.Tk()

main()

from tkinter import *
from random import randint

window = Tk()
window.title('Codemy.com - Custom Messages Boxes')
window.geometry("300x300")
window.iconbitmap("VNPMIcon.ico")





def clicker():
    def pwGenChocie(input):
        if input == "yes":
            def new_rand():
                # Clear Our Entry Box
                genPW.delete(0, END)

                # Get PW Length and convert to integer
                genPWLength = int(my_entry.get())

                # create a variable to hold our password
                genPWVal = ''

                # Loop through password length
                for x in range(genPWLength):
                    genPWVal += chr(randint(33, 126))

                # Output password to the screen
                genPW.insert(0, genPWVal)

            # Copy to clipboard
            def clipper():
                # Clear the clipboard
                randomPWGen.clipboard_clear()
                # Copy to clipboard
                randomPWGen.clipboard_append(genPW.get())
                randomPWGen.destroy()

            # Label Frame
            lf = LabelFrame(randomPWGen, text="How Many Characters?")
            lf.pack(pady=20)

            # Create Entry Box To Designate Number of Characters
            my_entry = Entry(lf, text='This is good', font=("Helvetica", 24))
            my_entry.pack(pady=20, padx=20)

            # Create Entry Box For Our Returned Password
            genPW = Entry(randomPWGen, text='', font=("Helvetica", 24), bd=0)
            genPW.pack(pady=20)

            # Create a frame for our Buttons
            my_frame = Frame(randomPWGen)
            my_frame.pack(pady=20)

            # Create our Buttons
            my_button = Button(my_frame, text="Generate Strong Password", command=new_rand)
            my_button.grid(row=0, column=0, padx=10)

            clip_button = Button(my_frame, text="Copy To Clipboad", command=clipper)
            clip_button.grid(row=0, column=1, padx=10)

        else:
            pop_label.config(text="You Clicked No!!")

    global randomPWGen
    randomPWGen = Toplevel(window)
    randomPWGen.title("Password generator")
    randomPWGen.geometry("400x400")
    #randomPWGen.config(bg="green")
    # pop.grab_set()

  global creative
    creative = PhotoImage(file="VNPMIcon.ico")

    me_pic = Label(my_frame, image=creative, borderwidth=0)
    me_pic.grid(row=0, column=0, padx=10)


    pop_label = Label(randomPWGen, text="Would You Like To Generate a Random Password?", fg="white", font=("helvetica", 12))
    pop_label.pack(pady=10)

    my_frame = Frame(randomPWGen)
    my_frame.pack(pady=5)

    yes = Button(my_frame, text="YES", command=lambda: pwGenChocie("yes"), bg="orange")
    yes.grid(row=0, column=1, padx=10)

    no = Button(my_frame, text="NO", command=lambda: pwGenChocie("no"), bg="yellow")
    no.grid(row=0, column=2, padx=10)


my_button = Button(window, text="Click Me!", command=clicker)
my_button.pack(pady=50)






window.mainloop()

from tkinter import *

root = Tk()
root.title('Model Definition')
root.geometry('{}x{}'.format(460, 350))

# create all of the main containers
top_frame = Frame(root, bg='cyan', width=450, height=50, pady=3)
center = Frame(root, bg='gray2', width=50, height=40, padx=3, pady=3)
btm_frame = Frame(root, bg='white', width=450, height=45, pady=3)
btm_frame2 = Frame(root, bg='lavender', width=450, height=60, pady=3)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ew")
center.grid(row=1, sticky="nsew")
btm_frame.grid(row=3, sticky="ew")
btm_frame2.grid(row=4, sticky="ew")

# create the widgets for the top frame
model_label = Label(top_frame, text='Model Dimensions')
width_label = Label(top_frame, text='Width:')
length_label = Label(top_frame, text='Length:')
entry_W = Entry(top_frame, background="pink")
entry_L = Entry(top_frame, background="orange")

# layout the widgets in the top frame
model_label.grid(row=0, columnspan=3)
width_label.grid(row=1, column=0)
length_label.grid(row=1, column=2)
entry_W.grid(row=1, column=1)
entry_L.grid(row=1, column=3)

# create the center widgets
center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)

ctr_left = Frame(center, bg='blue', width=100, height=190)
ctr_mid = Frame(center, bg='yellow', width=250, height=190, padx=3, pady=3)
ctr_right = Frame(center, bg='green', width=100, height=190, padx=3, pady=3)

ctr_left.grid(row=0, column=0, sticky="ns")
ctr_mid.grid(row=0, column=1, sticky="nsew")
ctr_right.grid(row=0, column=2, sticky="ns")

root.mainloop()

import tkinter as tk
from tkinter import ttk


def create_input_frame(container):

    frame = ttk.Frame(container)

    # grid layout for the input frame
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=3)

    # Find what
    ttk.Label(frame, text='Find what:').grid(column=0, row=0, sticky=tk.W)
    keyword = ttk.Entry(frame, width=30)
    keyword.focus()
    keyword.grid(column=1, row=0, sticky=tk.W)

    # Replace with:
    ttk.Label(frame, text='Replace with:').grid(column=0, row=1, sticky=tk.W)
    replacement = ttk.Entry(frame, width=30)
    replacement.grid(column=1, row=1, sticky=tk.W)

    # Match Case checkbox
    match_case = tk.StringVar()
    match_case_check = ttk.Checkbutton(
        frame,
        text='Match case',
        variable=match_case,
        command=lambda: print(match_case.get()))
    match_case_check.grid(column=0, row=2, sticky=tk.W)

    # Wrap Around checkbox
    wrap_around = tk.StringVar()
    wrap_around_check = ttk.Checkbutton(
        frame,
        variable=wrap_around,
        text='Wrap around',
        command=lambda: print(wrap_around.get()))
    wrap_around_check.grid(column=0, row=3, sticky=tk.W)

    for widget in frame.winfo_children():
        widget.grid(padx=0, pady=5)

    return frame


def create_button_frame(container):
    frame = ttk.Frame(container)

    frame.columnconfigure(0, weight=1)

    ttk.Button(frame, text='Find Next').grid(column=0, row=0)
    ttk.Button(frame, text='Replace').grid(column=0, row=1)
    ttk.Button(frame, text='Replace All').grid(column=0, row=2)
    ttk.Button(frame, text='Cancel').grid(column=0, row=3)

    for widget in frame.winfo_children():
        widget.grid(padx=0, pady=3)

    return frame


def create_main_window():

    # root window
    root = tk.Tk()
    root.title('Replace')
    root.geometry('400x150')

    # windows only (remove the minimize/maximize button)


    # layout on the root window
    root.columnconfigure(0, weight=4)
    root.columnconfigure(1, weight=1)

    input_frame = create_input_frame(root)
    input_frame.grid(column=0, row=0)

    button_frame = create_button_frame(root)
    button_frame.grid(column=1, row=0)

    root.mainloop()


if __name__ == "__main__":
    create_main_window()


THREADING:
import threading
import datetime
import time
from tkinter import messagebox
from tkinter import *

root = Tk()

def main():
    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()
    def background():
        while True:
            print(datetime.datetime.now().strftime("%H:%M:%S"))
            time.sleep(1)

    b = threading.Thread(name='background', target=background, daemon=True)
    b.start()

    root.protocol("WM_DELETE_WINDOW", on_closing)

f = threading.Thread(name='main', target=main)

f.start()
root.mainloop()

def saveFile():
    new_file = asksaveasfile(mode = 'w', filetype = [('text files', '.txt')])
    if new_file is None:
        return
    text = str(entry.get(1.0, END))
    new_file.write(text)
    new_file.close()

def openFile():
    file = askopenfile(mode = 'r', filetype = [('text files', '*.txt')])
    if file is not None:
        content = file.read()
    entry.insert(INSERT, content)

def clearFile():
    entry.delete(1.0, END)

canvas = Tk()
canvas.geometry("400x600")
canvas.title("Notepad")
canvas.config(bg = "white")
top = Frame(canvas)
top.pack(padx=10, pady=5, anchor = 'nw')

b1 = Button(canvas, text="Open", bg = "white", command = openFile)
b1.pack(in_=top, side=LEFT)

b2 = Button(canvas, text="Save", bg = "white", command = saveFile)
b2.pack(in_=top, side=LEFT)

b3 = Button(canvas, text="Clear", bg = "white", command = clearFile)
b3.pack(in_=top, side=LEFT)

b4 = Button(canvas, text="Exit", bg = "white", command = exit)
b4.pack(in_=top, side=LEFT)

entry = Text(canvas, wrap = WORD, bg = "#F9DDA4", font = ("poppins", 15))
entry.pack(padx=10, pady = 5, expand = TRUE, fill = BOTH)

from functools import partial
from tkinter import messagebox, simpledialog
from tkinter.filedialog import *
from tkinter import *
import sqlite3


with sqlite3.connect("Scheduler.db") as db:
    cursor = db.cursor()

cursor.execute("""
        CREATE TABLE IF NOT EXISTS Diary(
        id INTEGER PRIMARY KEY,
        date DATE NOT NULL,
        grateful TEXT,
        plan TEXT,
        affirmation TEXT,
        deed TEXT,
        improvement TEXT,
        experiences TEXT);
        """)

cursor.execute("SELECT DATE('now')")
date = cursor.fetchall()

print (date)

def addBook():
    while True:
        newBookName = simpledialog.askstring("Please enter book name: ", "Book name:")

        if newBookName == None:
            break
        if newBookName == "":
            messagebox.showwarning("showwarning", "Please enter a valid activity")
            continue
        cursor.execute("INSERT INTO Books(book, chapter, summary, vocabulary) VALUES (?, ?, ?, ?)",
                       (newBookName, 1, "Chapter 1:\n\n================", ""))
        db.commit()
        cursor.execute('SELECT id FROM books ORDER BY id DESC LIMIT 1')
        choice = cursor.fetchall()

        cursor.execute('SELECT * FROM books WHERE id = ?', (choice[0]))
        activity = cursor.fetchall()

        bookName.delete(0, "end")
        bookName.insert(0, activity[0][1])
        bookChapter.delete(0, "end")
        bookChapter.insert(0, activity[0][2])
        bookSummary.delete(1.0, "end")
        bookSummary.insert(1.0, activity[0][3])
        bookVocabulary.delete(1.0, "end")
        bookVocabulary.insert(1.0, activity[0][4])

        global currentSel
        currentSel = activity
        butSave.config(command=partial(updateBook, currentSel))
        break

def selectBook():
    cursor.execute('SELECT id, book FROM Books')
    booksArr = cursor.fetchall()
    if booksArr == []:
        messagebox.showwarning("No book", "Please add a new book first.")
        return

    for widget in bookWindow.winfo_children():
        if ".!toplevel.!toplevel" in str(widget):
            exists = True
            if exists:
                widget.destroy()

    selectBScreen = Toplevel(bookWindow)
    selectBScreen.title("Select Book")
    selectBScreen.geometry("300x300")

    pattern = r'[^A-Za-z0-9]+'
    print(booksArr)
    books = []
    bookIdList = []
    for i in range(0, len(booksArr)):
        book = re.sub(pattern, ' ', str(booksArr[i][1]))
        bookIdList.append(booksArr[i][0])
        books.append(book)
    scrollBar = Scrollbar(selectBScreen, bg="grey")
    print(bookIdList)

    scrollBar.pack(side=RIGHT, fill=BOTH)
    bookList = Listbox(selectBScreen, selectmode=BROWSE, yscrollcommand=scrollBar.set)
    scrollBar.config(command=bookList.yview)
    bookList.pack(fill=BOTH, pady=10, padx=10)

    for i in range(0, len(books)):
        bookList.insert(i, books[i])

    def selectedBook():
        while True:
            if bookList.curselection() == ():
                break
            pattern = r'[^A-Za-z0-9]+'
            choice = re.sub(pattern, ' ', str(bookList.curselection()))
            choice = bookIdList[int(choice)]
            print(choice)
            if choice == ():
                messagebox.showwarning("showwarning", "Please select a book")
                break
            cursor.execute('SELECT * FROM books WHERE id = ?', (choice,))
            activity = cursor.fetchall()

            bookName.delete(0, "end")
            bookName.insert(0, activity[0][1])
            bookChapter.delete(0, "end")
            bookChapter.insert(0, activity[0][2])

            bookSummary.delete(1.0, "end")
            if activity[0][3] != "":
                bookSummary.insert(1.0, activity[0][3])
            bookVocabulary.delete(1.0, "end")
            if activity[0][4] != "":
                bookVocabulary.insert(1.0, activity[0][4])

            global currentSel
            currentSel = activity
            butSave.config(command=partial(updateBook, currentSel))
            butAddVoc.config(command=addVocab)
            selectBScreen.destroy()
            break

    butOk = Button(selectBScreen, text="Select", command=selectedBook)
    butOk.pack()

    def removeBook():
        while True:
            if bookList.curselection() == ():
                break
            pattern = r'[^A-Za-z0-9]+'
            choice = re.sub(pattern, '', str(bookList.curselection()))
            choice = bookIdList[int(choice)]
            print(choice)
            if choice == ():
                messagebox.showwarning("showwarning", "Please select a book")
                break
            print(choice)
            cursor.execute('SELECT book FROM Books WHERE id = ?', (choice,))
            book = str(cursor.fetchall())
            print(book)
            pattern = r'[^A-Za-z0-9]+'
            # Remove special characters from the string
            bookS = re.sub(pattern, ' ', book)

            if messagebox.askyesno("Deleting Entry", f"Are you sure you want to delete book: {bookS}"):
                sql = "DELETE FROM Books WHERE id = ?"

                cursor.execute(sql, (choice,))
                db.commit()

                bookList.delete(choice)
                selectBScreen.destroy()
                bookName.delete(0, "end")
                bookChapter.delete(0, "end")
                bookSummary.delete(1.0, "end")
                bookVocabulary.delete(1.0, "end")
                butSave.config(command=notify)
            break

    butDeleteBook = Button(selectBScreen, text="Delete Book", command=removeBook)
    butDeleteBook.pack()

bookWindow = Toplevel(window)
bookWindow.title("Your Books")
bookWindow.geometry("700x750")
top = Frame(bookWindow)
top.pack()

middle = Frame(bookWindow, width=500, height=100)
middle.pack()

bottom = Frame(bookWindow, width=500, height=100)
bottom.pack()

addBook = Button(bookWindow, text="Add new book", command=addBook)
addBook.pack(in_=top, side=TOP, pady=5)

selectBook = Button(bookWindow, text="Select book", command=selectBook)
selectBook.pack(in_=top, side=TOP, pady=5)

lblName = Label(bookWindow, text="Name: ")
lblName.pack(in_=top, side=LEFT, padx=5, pady=5)

bookName = Entry(bookWindow)
bookName.pack(in_=top, side=LEFT)

lblChapter = Label(bookWindow, text="Chapters: ")
lblChapter.pack(in_=top, side=LEFT, padx=5, pady=5)

bookChapter = Entry(bookWindow)
bookChapter.pack(in_=top, side=LEFT)

lblSummary = Label(middle, text="Summary: ")
lblSummary.pack(in_=middle)

bookSummary = Text(bookWindow, wrap=WORD, height=20)
bookSummary.pack(in_=middle, pady=5, padx=10, expand=TRUE, fill=BOTH)

lblVocabulary = Label(bookWindow, text="Vocabulary: ")
lblVocabulary.pack(in_=bottom, side=TOP)

def notify():
    messagebox.showwarning("Select book", "Please select or add a book first")
    bookName.delete(0, "end")
    bookChapter.delete(0, "end")
    bookSummary.delete(1.0, "end")
    bookVocabulary.delete(1.0, "end")

butAddVoc = Button(bookWindow, text="Add to Vocabulary", command=notify)
butAddVoc.pack(in_=bottom, padx=10, pady=5, side=TOP)

bookVocabulary = Text(bookWindow, wrap=WORD, height=10)
bookVocabulary.pack(in_=bottom, expand=TRUE, fill=BOTH, pady=5, padx=10)

def updateBook(currentSel):

    while True:
        id = currentSel[0][0]
        book = bookName.get()
        chapter = bookChapter.get()
        summaryB = bookSummary.get("1.0", 'end-1c')

        vocabulary = bookVocabulary.get("1.0", 'end-1c')
        if book == "":
            messagebox.showwarning("showwarning", "Please enter a valid book name")
            break
        if chapter == "" or int(chapter) < 1:
            messagebox.showwarning("showwarning", "Please enter a valid chapter")
            break
        if summaryB == "":
            messagebox.showwarning("showwarning", "Please enter summary for the chapter")
            break
        bookSummary.delete(1.0, 'end')
        for i in range(1, int(chapter) + 1):
            if f"Chapter {i}:" not in summaryB:
                summaryB = f"{summaryB}\nChapter {i}:\n\n================\n"

        bookSummary.insert(1.0, summaryB)
        sql = "UPDATE Books SET book =?, chapter =?, summary = ?, vocabulary = ? WHERE id = ?"

        cursor.execute(sql, (book, chapter, summaryB, vocabulary, id,))
        db.commit()
        messagebox.showinfo("Success", f"Book: {book} was successfully updated!")
        break

butSave = Button(bookWindow, text="Save", command=notify)
butSave.pack(padx=10, pady=5, side=TOP)

def addVocab():
    for widget in bookWindow.winfo_children():
        if ".!toplevel.!toplevel" in str(widget):
            exists = True
            if exists:
                widget.destroy()

    addVocabScreen = Toplevel(bookWindow)
    addVocabScreen.title("Add a word to your vocabulary")
    addVocabScreen.geometry("300x300")

    lblWord = Label(addVocabScreen, text="Add a word to your vocabulary:")
    lblWord.pack(padx=10, pady=5, side=TOP)

    entWord = Entry(addVocabScreen)
    entWord.pack(padx=10, pady=5, side=TOP)

    def addWord():
        enteredWord = entWord.get()
        print(enteredWord)
        if enteredWord == "":
            messagebox.showinfo("No match", "Please enter a word into the text field")
            return

            if meaning == "":
                messagebox.showinfo("No match", "Definition for entered word can not be found")

            bookVocabulary.insert(1.0, f"{enteredWord} - {meaning}\n")
            entWord.delete(0, 'end')


    butAdd = Button(addVocabScreen, text="Add Word", command=addWord)
    butAdd.pack(padx=10, pady=5, side=TOP)

    def desVoc():
        addVocabScreen.destroy()

    butDone = Button(addVocabScreen, text="Back", command=desVoc)
    butDone.pack(padx=10, pady=5, side=TOP)

def vocabScreen():
    for widget in bookWindow.winfo_children():
        if ".!toplevel.!toplevel" in str(widget):
            exists = True
            if exists:
                widget.destroy()
    vocScreen = Toplevel(bookWindow)
    vocScreen.title("List of words in vocabulary")
    vocScreen.geometry("500x500")

    cursor.execute('SELECT vocabulary FROM books')
    vocabularyArr = cursor.fetchall()

    vocabTxt = Text(vocScreen, wrap=WORD, height=20)
    vocabTxt.pack(pady=5, padx=10, expand=TRUE, fill=BOTH)

    vocabTxt.delete(1.0, "end")

    for i in range(0, len(vocabularyArr)):
        strWord = str(vocabularyArr[i][0])

        vocabTxt.insert(1.0, f"{strWord}")

butBook = Button(bookWindow, text="Your Vocabulary", font=("Helvetica", 14), command=vocabScreen)
butBook.pack(side=TOP)

def doneCom():
    option = messagebox.askyesno("Quit",
                                 "Are you sure you want to return to the main screen? \n \n Unsaved changes will be lost?")
    if option:
        bookWindow.destroy()

butDone = Button(bookWindow, text="Back", font=("Helvetica", 14), command=doneCom)
butDone.pack(side=TOP, padx=10, pady=10)

bookWindow.protocol("WM_DELETE_WINDOW", partial(on_closing, bookWindow))

butDiary = Button(topframe, text="Diary", font=("Arial", 10), command=diaryScreen)
butDiary.pack()
 '''

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
