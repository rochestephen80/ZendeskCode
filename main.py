import json
import requests
import pandas as pd
import subprocess
from subprocess import check_output
reqList = []
assignList = []
subList = []
descList = []
TagList = []
finalList = []








class JsonList:
    try:
        data = subprocess.call(["curl", "-v", "-H", "X-Auth-User: rochestephen80@gmail.com", "-H", "X-Auth-Key: Devilmaycry1","https://rochestephen80.zendesk.com/api/v2/imports/tickets/create_many.json"], shell=False)
        dataf = pd.read_json(data)
        with open('ticket.json')as f:
            for i in dataf['tickets']:
                reqList.append(i['requester_id'])
                assignList.append(i['assignee_id'])
                subList.append(i['subject'])
                descList.append(i['description'])
                TagList.append(i['tags'])
            f.close()
    except:
        print("unable to access api switching to local copy of tickets")
        with open('ticket.json')as f:

            data1=pd.read_json(f)
            #print(data1) #testing print
            for i in data1['tickets']:
                reqList.append(i['requester_id'])
                assignList.append(i['assignee_id'])
                subList.append(i['subject'])
                descList.append(i['description'])
                TagList.append(i['tags'])
            f.close()
    def listJson():
            for i in range(len(reqList)):
                finalList.append([reqList[i],assignList[i],subList[i],descList[i],TagList[i]])


    def selectTicket():
        tickno=int(input("Please input your ticket number:"))
        while tickno> len(finalList):
            print("invalid please reenter a VALID ticket number")
            tickno = int(input())

        for i in range(len(finalList[tickno-1])):
            print(finalList[tickno-1][i])


    def selectSpecific():
        tickno= int(input("Please input your ticket number:"))
        while tickno> len(finalList):
            print("invalid please reenter a VALID ticket number")
            tickno = int(input())
        selection=int(input("Please select which peice of information would you like\n1. requester ID\n2. Assignee ID\n3. Subject \n4. description\n5. Tags"))
        while selection> len(finalList[tickno-1]):
            print("invalid please reenter a VALID selection number")
            selection = int(input())
        print(finalList[tickno-1][selection-1])

    def pageTickets():
        base=0
        end=25
        for i in range(int(len(finalList)/25)):
            print([finalList[base:end]])
            print("\n\n")
            base+=25
            end+= 25


Jl1= JsonList
Jl1.listJson()
print("Please choose the option you would like to use\n1. Select your ticket\n2. Display to catalog of tickets\n3. Select the specific detail you would like to see\n0. to quit")
option = int(input())
while option != 0:
    if option == 1:
        Jl1.selectTicket()
        print(
            "Please choose the option you would like to use\n1. Select your ticket\n2. Display to catalog of tickets\n3. Select the specific detail you would like to see\n0. to quit")
        option = int(input())
    elif option == 2:
        Jl1.pageTickets()
        print(
            "Please choose the option you would like to use\n1. Select your ticket\n2. Display to catalog of tickets\n3. Select the specific detail you would like to see\n0. to quit")
        option = int(input())
    elif option == 3:
        Jl1.selectSpecific()
        print("Please choose the option you would like to use\n1. Select your ticket\n2. Display to catalog of tickets\n3. Select the specific detail you would like to see\n0. to quit")
        option = int(input())
    else:
        print("Invalid option selected. Try again!")
        option = int(input())

