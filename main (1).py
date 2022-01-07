# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

plants = 0
price = 0
years = 5
repitions = 0
yyield = 0
profit = 0
finalprice = 0
capital = 0
profitratio = 0
remainder = 0
newremainder = 0
days = 0
payout = 0

file = open("testfile.txt", "w")


#Flash
file.write("---------------------- Min -----------------------" + "\n")
file.write("---------------------- Flash -----------------------" + "\n")
plants = 40
price = 50

capital = plants * price

repitions = 208/365
yyield = 68
profitratio = yyield/price



profit = (capital * profitratio)

time = repitions * 365
payout += 1

file.write("Payout number: " + str(payout) + "\n")
file.write("Profit is: " + str(profit) + " after days: " + str(time) + "\n")

remainder = newremainder

plants = profit/price

newremainder = (profit % price) / price

if (newremainder + remainder < 1):
    plants = plants - newremainder
    newremainder = newremainder + remainder
else:
    plants = plants + 1
    newremainder = (newremainder + remainder) - 1

    plants = int(plants)


file.write("New plants bought is: " + str(plants) + "\n")
days = time
file.write("" + "\n")

while(days < 1800):

    capital = profit
    profit = (capital * profitratio)
    days = days + time
    payout += 1
    file.write("Payout number: " + str(payout) + "\n")
    file.write("Profit is: " + str(profit) + " after days: " + str(days) + "\n")
    remainder = newremainder

    plants = profit / price

    newremainder = (profit % price) / price

    if (newremainder + remainder < 1):
        plants = plants - newremainder
        newremainder = newremainder + remainder
    else:
        plants = plants + 1
        newremainder = (newremainder + remainder) - 1

        plants = int(plants)

    file.write("New plants bought is: " + str(plants) + "\n")
    file.write("" + "\n")
file.write("------------------------------------------------------" + "\n")

#Mist
file.write("---------------- Mist -------------------" + "\n")
plants = 1
price = 2000
days = 0
payout = 1

capital = plants * price

repitions = 0.25
yyield = 300

profit = yyield * plants

time = int(repitions * 365)

days = days + time


file.write("Payout number: " + str(payout) + "\n")
file.write("New plants bought is: " + str(plants) + "\n")
file.write("Profit is: " + str(profit) + " after days: " + str(days) + "\n")
file.write("" + "\n")


while(days < 1800):

    days = days + time
    payout += 1

    if int(profit/2000) > plants - 1:
        plants += int(profit/2000) - (plants-1)
        profit = profit + yyield * plants
    else:
        profit = profit + (yyield * plants)
    file.write("Payout number: " + str(payout) + "\n")
    file.write("New plants bought is: " + str(plants) + "\n")
    file.write("Profit is: " + str(profit) + " after days: " + str(days) + "\n")
    file.write("" + "\n")
file.write("------------------------------------------------------" + "\n")

#Kush
file.write("---------------- Kush -------------------" + "\n")
plants = 1
price = 2000
days = 0
payout = 1

capital = plants * price

repitions = 0.3333333
yyield = 500

profit = yyield * plants

time = int(repitions * 365)

days = days + time


file.write("Payout number: " + str(payout) + "\n")
file.write("New plants bought is: " + str(plants) + "\n")
file.write("Profit is: " + str(profit) + " after days: " + str(days) + "\n")
file.write("" + "\n")

while(days < 1800):

    days = days + time
    payout += 1

    if int(profit/2000) > plants - 1:
        plants += int(profit/2000) - (plants-1)
        profit = profit + yyield * plants
    else:
        profit = profit + (yyield * plants)
    file.write("Payout number: " + str(payout) + "\n")
    file.write("New plants bought is: " + str(plants) + "\n")
    file.write("Profit is: " + str(profit) + " after days: " + str(days) + "\n")
    file.write("" + "\n")
file.write("------------------------------------------------------" + "\n")

#Haze
file.write("----------------------- Haze ----------------------" + "\n")
plants = 1
price = 2000
days = 0
payout = 1

capital = plants * price

repitions = 0.5
yyield = 900

profit = yyield * plants

time = int(repitions * 365)

days = days + time

file.write("Payout number: " + str(payout) + "\n")
file.write("New plants bought is: " + str(plants) + "\n")
file.write("Profit is: " + str(profit) + " after days: " + str(days) + "\n")
file.write("" + "\n")

while(days < 1800):

    days = days + time

    payout += 1
    if int(profit/2000) > plants - 1:
        plants += int(profit/2000) - (plants-1)
        profit = profit + yyield * plants
    else:
        profit = profit + (yyield * plants)
    file.write("Payout number: " + str(payout) + "\n")
    file.write("New plants bought is: " + str(plants) + "\n")
    file.write("Profit is: " + str(profit) + " after days: " + str(days) + "\n")
    file.write("Year" + str(days/365) + "\n")
    file.write("" + "\n")
file.write("---------------------- Max -----------------------" + "\n")
file.write("---------------------- Flash -----------------------" + "\n")
plants = 40
price = 50

capital = plants * price

repitions = 208/365
yyield = 83
profitratio = yyield/price



profit = (capital * profitratio)

time = repitions * 365
payout += 1

file.write("Payout number: " + str(payout) + "\n")
file.write("Profit is: " + str(profit) + " after days: " + str(time) + "\n")

remainder = newremainder

plants = profit/price

newremainder = (profit % price) / price

if (newremainder + remainder < 1):
    plants = plants - newremainder
    newremainder = newremainder + remainder
else:
    plants = plants + 1
    newremainder = (newremainder + remainder) - 1

    plants = int(plants)


file.write("New plants bought is: " + str(plants) + "\n")
days = time
file.write("" + "\n")

while(days < 1800):

    capital = profit
    profit = (capital * profitratio)
    days = days + time
    payout += 1
    file.write("Payout number: " + str(payout) + "\n")
    file.write("Profit is: " + str(profit) + " after days: " + str(days) + "\n")
    remainder = newremainder

    plants = profit / price

    newremainder = (profit % price) / price

    if (newremainder + remainder < 1):
        plants = plants - newremainder
        newremainder = newremainder + remainder
    else:
        plants = plants + 1
        newremainder = (newremainder + remainder) - 1

        plants = int(plants)

    file.write("New plants bought is: " + str(plants) + "\n")
    file.write("" + "\n")
file.write("------------------------------------------------------" + "\n")

#Mist
file.write("---------------- Mist -------------------" + "\n")
plants = 1
price = 2000
days = 0
payout = 1

capital = plants * price

repitions = 0.25
yyield = 400

profit = yyield * plants

time = int(repitions * 365)

days = days + time


file.write("Payout number: " + str(payout) + "\n")
file.write("New plants bought is: " + str(plants) + "\n")
file.write("Profit is: " + str(profit) + " after days: " + str(days) + "\n")
file.write("" + "\n")


while(days < 1800):

    days = days + time
    payout += 1

    if int(profit/2000) > plants - 1:
        plants += int(profit/2000) - (plants-1)
        profit = profit + yyield * plants
    else:
        profit = profit + (yyield * plants)
    file.write("Payout number: " + str(payout) + "\n")
    file.write("New plants bought is: " + str(plants) + "\n")
    file.write("Profit is: " + str(profit) + " after days: " + str(days) + "\n")
    file.write("" + "\n")
file.write("------------------------------------------------------" + "\n")

#Kush
file.write("---------------- Kush -------------------" + "\n")
plants = 1
price = 2000
days = 0
payout = 1

capital = plants * price

repitions = 0.3333333
yyield = 750

profit = yyield * plants

time = int(repitions * 365)

days = days + time


file.write("Payout number: " + str(payout) + "\n")
file.write("New plants bought is: " + str(plants) + "\n")
file.write("Profit is: " + str(profit) + " after days: " + str(days) + "\n")
file.write("" + "\n")

while(days < 1800):

    days = days + time
    payout += 1

    if int(profit/2000) > plants - 1:
        plants += int(profit/2000) - (plants-1)
        profit = profit + yyield * plants
    else:
        profit = profit + (yyield * plants)
    file.write("Payout number: " + str(payout) + "\n")
    file.write("New plants bought is: " + str(plants) + "\n")
    file.write("Profit is: " + str(profit) + " after days: " + str(days) + "\n")
    file.write("" + "\n")
file.write("------------------------------------------------------" + "\n")

#Haze
file.write("----------------------- Haze ----------------------" + "\n")
plants = 1
price = 2000
days = 0
payout = 1

capital = plants * price

repitions = 0.5
yyield = 1200

profit = yyield * plants

time = int(repitions * 365)

days = days + time

file.write("Payout number: " + str(payout) + "\n")
file.write("New plants bought is: " + str(plants) + "\n")
file.write("Profit is: " + str(profit) + " after days: " + str(days) + "\n")
file.write("" + "\n")

while(days < 1800):

    days = days + time

    payout += 1
    if int(profit/2000) > plants - 1:
        plants += int(profit/2000) - (plants-1)
        profit = profit + yyield * plants
    else:
        profit = profit + (yyield * plants)
    file.write("Payout number: " + str(payout) + "\n")
    file.write("New plants bought is: " + str(plants) + "\n")
    file.write("Profit is: " + str(profit) + " after days: " + str(days) + "\n")
    file.write("Year" + str(days/365) + "\n")
    file.write("" + "\n")


file.close()







