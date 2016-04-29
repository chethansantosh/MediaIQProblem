import re
import logging
import operator
from collections import Counter

#Book object with id, price , name
class Book():
    def __init__(self, bid, price, name):
        self.bookId = bid
        self.price = price
        self.name = name

#Customer with id , list of books purchased
class Customer():
    def __init__(self, cid, bookslist):
        self.customerId = cid
        self.booksList = bookslist


def getInputs():
    filename = raw_input("Enter the file name having the books information")
    with open(filename) as f:
        booksList = f.read().splitlines()

    filename2 = raw_input("Enter the filename having the customers information")
    with open(filename2) as f:
        customerList = f.read().splitlines()
    bList, cList = processInputs(booksList, customerList)

    r = raw_input("Enter the value of r<Number greater than zero to generate report>")
    generateReport(bList, cList, r)



def processInputs(bList, cList):
    #Process the inputs into the list of book and customer objects
    booksObj = []
    customerObj = []
    for i in range(len(bList)):
        b = Book(bList[i].split(',')[0], bList[i].split(',')[1], bList[i].split(',')[2])
        booksObj.append(b)
    for i in range(len(cList)):
        c = Customer(cList[i].split(',')[0], cList[i].split(',')[1:])
        customerObj.append(c)
    return booksObj, customerObj


def generateReport(blist, clist, r):
    print("Please find the reports below ")


    print("top N frequent customers and the number of visits they made")
    listtemp = []
    dicttemp ={}
    for i in range(len(clist)):
        listtemp.append(clist[i].customerId)

    dicttemp = sorted(dict(Counter(listtemp)).items(), key=operator.itemgetter(1), reverse = True)
    print(dicttemp[0 :int(r)])

    dicttemp = {}
    for i in range(len(blist)):
        dicttemp[blist[i].bookId] = blist[i].price

    print("the top N highest transactions and the corresponding customerid")

    temp = []
    sum = 0
    for i in range(len(clist)):
        for j in range(len(clist[i].booksList)):
            sum = sum + int(dicttemp[clist[i].booksList[j]])
        temp.append((clist[i].customerId, sum))
        sum = 0
    print(temp[0:int(r)])

    temp1 =  []
    dicttemp = {}
    for i in range(len(clist)):
        temp1.extend(clist[i].booksList)

    print("the top N highest selling books and quantity sold")
    print(sorted(dict(Counter(temp1)).items(), key=operator.itemgetter(1), reverse=True)[:int(r)])
    print("the N least selling books and quantity sold (this includes books that did not sell at all as well)")
    print(sorted(dict(Counter(temp1)).items(), key=operator.itemgetter(1))[:int(r)])

    print("Customer %s eligiblity for discount 1:Eligible , 0:Not Eligible")
    d = raw_input("Enter the value above which if the purchase exceeds than discount is provided")
    c = raw_input("Enter the customer ID to check for discount eligibility")

    for i in range(len(temp)):
        if temp[i][0] == c:
            if int(temp[i][1]) > int(d):
                print("1")
            else:
                print("0")

#Run the program by taking the inputs
getInputs()
