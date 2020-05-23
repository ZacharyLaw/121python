"""
Filename: pos.py
Author: Law Hong Chun Zachary
Date: 10/5/2020

Description: This program features as a supermarket POS system by input inventory records and output a receipt
"""
import csv
import pandas as pd
import msvcrt
from datetime import datetime
from os import system, name 
import sys


class pos:
    def memeberlogin():
        while True:
            _ = system('cls') 
            staffid=input('Enter membership id: ')
            staffpw=input('Enter membership password: ')
            if not role.query('Staff_ID==@staffid and Pw==@staffpw').empty:return 'Member '+staffid
            else:print('Error: Wrong membership id or membership password')
    def stafflogin():
        while True:
            _ = system('cls') 
            memberid=input('Enter staff id: ')
            memberpw=input('Enter staff password: ')
            if not role.query('Staff_ID==@memberid and Pw==@memberpw').empty:return 'Staff '+memberid
            else:print('Error: Wrong staff id or staff password')
            
    def shoppingcart(role):
        cart=[]#shopping cart item
        cred=[]#shopping cart price
        tab=cursor=0
        swap={1:0,0:1}
        number_of_items=len(inventory['Name'])
        _ = system('cls') 
        print('        121 Supermarket POS\nInventory:')
        for row in range(number_of_items):
            if row==cursor:print('%-20s    $%3s'%('<'+inventory.loc[row,'Name']+'>',inventory.loc[row,'Price']))
            else:print('%-20s    $%3s'%(' '+inventory.loc[row,'Name']+' ',inventory.loc[row,'Price']))
        print('\n\n↑ ↓ W S Select Item        Space Bar To Select \nTab Switch to Shopping Cart        Esc To Logout')
        while True:
            choice=msvcrt.getch()
            if choice==b'\xe0':choice=msvcrt.getch()
            _ = system('cls') 
            if choice in [b'H',b'w',b'W'] and cursor!=0:cursor-=1#^
            elif choice in [b'P',b's',b'S'] and cursor!=len(cart)-1 and tab:cursor+=1#V
            elif choice in [b'P',b's',b'S'] and cursor!=number_of_items-1 and not tab:cursor+=1#V
            elif choice==b'\t' and cart:
                tab=swap[tab]
                if not tab and cursor>number_of_items-1:cursor=number_of_items-1
                elif tab and cursor>len(cart)-1:cursor=len(cart)-1
            elif choice==b' ' and not tab:
                cart.append(inventory.loc[cursor,'Name'])
                cred.append(int(inventory.loc[cursor,'Price']))
            elif choice==b' ' and tab:
                cart.pop(cursor)
                cred.pop(cursor)
                if not cart:tab=swap[tab]
            elif choice == b'\r' and len(cart)!=0:
                print('         121 Supermarket\n  83 Tat Chee Ave, Kowloon Tong\n   New Territories, Hong Kong\nCasher: '+role+'    '+str(datetime.now().strftime('%y/%m/%d %H:%M')))
                for x in range(len(cart)):print('   %-20s %5d'%(cart[x],cred[x]))
                print('   Total:                 $'+str(sum(cred))+'\n      Have a nice day!\n\n\nEsc Enter To return')
                while True:
                    choice=msvcrt.getch()
                    if choice in [b'\r',b'\x1b']:
                        cart=[]
                        cred=[]
                        _ = system('cls') 
                        break
            elif choice ==b'q' or choice == b"\x1b":break    
            print('        121 Supermarket POS\nInventory:')
            for row in range(number_of_items):
                if row==cursor and not tab:print('%-20s    $%3s'%('<'+inventory.loc[row,'Name']+'>',inventory.loc[row,'Price']))
                else:print('%-20s    $%3s'%(' '+inventory.loc[row,'Name']+' ',inventory.loc[row,'Price']))
            if not cart:print('\n\n↑ ↓ W S Select Item        Space Bar To Select  \nTab Switch to Shopping Cart        Esc To Exit')
            else:
                print('\n\n%-17sTotal: $%3d'%('Shopping Cart:',sum(cred)))
                for row in range(len(cart)):
                    if row==cursor and tab:print('%-20s    $%3s'%('<'+cart[row]+'>',cred[row]))
                    else:print('%-20s    $%3s'%(' '+cart[row]+' ',cred[row]))
                print('\n\n↑ ↓ W S Select Item        Space Bar To Unselect\nTab Switch to Shopping Cart        Esc To Exit       Enter To Check Out')
try:inventory= pd.read_csv(sys.argv[1])
except IndexError:
    try:inventory= pd.read_csv('inventory.csv')
    except:
        print('Error: Inventory File not found')
        sys.exit()
try:role= pd.read_csv(sys.argv[2])
except IndexError:
    try:role=pd.read_csv('role.csv')
    except:
        print('Error: Role File not found')
        sys.exit()
while True:
    _ = system('cls') 
    print('Enter role:\n1 or any key    Guest\n2.              Supermarket Memebership\n3.              Staff\n\nEsc To Exit')
    choice=msvcrt.getch()
    if choice==b'1':role='Guest' 
    elif choice==b'2':role=pos.memeberlogin()
    elif choice==b'3':role=pos.stafflogin()
    elif choice ==b'q' or choice == b"\x1b":break
    else:role='Guest'
    pos.shoppingcart(role)
