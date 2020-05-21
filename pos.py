import csv
import pandas as pd
import msvcrt
from datetime import datetime
from os import system, name 
import sys
try:inventory= pd.read_csv('inventory.csv')
except FileNotFoundError:
    print('Error: Inventory File not found')
    sys.exit()
cart=[]
cred=[]
cursor=0
tab=0
swap={1:0,0:1}
number_of_items=len(inventory['Name'])
_ = system('cls') 
print('        121 Supermarket POS\nInventory:')
for row in range(number_of_items):
    if row==cursor:print('%-20s    $%3s'%('<'+inventory.loc[row,'Name']+'>',inventory.loc[row,'Price']))
    else:print('%-20s    $%3s'%(' '+inventory.loc[row,'Name']+' ',inventory.loc[row,'Price']))
print('\n\n↑ ↓ Select Item        Space Bar To Select         Tab Switch to Shopping Cart        Esc To Exit')
while True:
    choice=msvcrt.getch()
    _ = system('cls') 
    if choice==b'H' and cursor!=0:cursor-=1#^
    elif choice==b'P' and cursor!=len(cart)-1 and tab:cursor+=1#V
    elif choice==b'P' and cursor!=number_of_items-1 and not tab:cursor+=1#V
    elif choice==b'\t' and len(cart)>0:
        tab=swap[tab]
        if not tab and cursor>number_of_items:cursor=number_of_items
        elif tab and cursor>len(cart):cursor=len(cart)
    elif choice==b' ' and not tab:
        cart.append(inventory.loc[cursor,'Name'])
        cred.append(int(inventory.loc[cursor,'Price']))
    elif choice==b' ' and tab:
        cart.pop(cursor)
        cred.pop(cursor)
        if len(cart)==0:tab=swap[tab]
    elif choice == b'\r' and len(cart)!=0:
        print('         121 Supermarket\n  83 Tat Chee Ave, Kowloon Tong\n   New Territories, Hong Kong\nCasher: Self    '+str(datetime.now().strftime('%y/%m/%d %H:%M')))
        for x in range(len(cart)):print('   %-20s %5d'%(cart[x],cred[x]))
        print('   Total:                 $'+str(sum(cred))+'\n      Have a nice day!\n')
        break
    elif choice ==b'q' or choice == b"\x1b":break
    print('        121 Supermarket POS\nInventory:')
    for row in range(number_of_items):
        if row==cursor and not tab:print('%-20s    $%3s'%('<'+inventory.loc[row,'Name']+'>',inventory.loc[row,'Price']))
        else:print('%-20s    $%3s'%(' '+inventory.loc[row,'Name']+' ',inventory.loc[row,'Price']))
    if len(cart)==0:print('\n\n↑ ↓ Select Item        Space Bar To Select          Tab Switch to Shopping Cart        Esc To Exit')
    else:
        print('\n\n%-17sTotal: $%3d'%('Shopping Cart:',sum(cred)))
        for row in range(len(cart)):
            if row==cursor and tab:print('%-20s    $%3s'%('<'+cart[row]+'>',cred[row]))
            else:print('%-20s    $%3s'%(' '+cart[row]+' ',cred[row]))
        print('\n\n↑ ↓ Select Item        Space Bar To Unselect        Tab Switch to Shopping Cart        Esc To Exit       Enter To Check Out')
