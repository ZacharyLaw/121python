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
y=0
tab=0
swap={1:0,0:1}
number_of_items=len(inventory['Name'])
_ = system('cls') 
print('Inventory:')
for row in range(number_of_items):
    if row==y:print('%-10s    $%3s'%('<'+inventory.loc[row,'Name']+'>',inventory.loc[row,'Price']))
    else:print('%-10s    $%3s'%(' '+inventory.loc[row,'Name']+' ',inventory.loc[row,'Price']))
print('\n\n↑ ↓ Select Item        Space Bar To Select         Tab Switch to Shopping Cart        Esc To Exit')
while True:
    choice=msvcrt.getch()
    _ = system('cls') 
    if choice==b'H' and y!=0:y-=1#^
    elif choice==b'P' and y!=number_of_items-1:y+=1#V
    elif choice==b'\t':tab=swap[tab]
    elif choice==b' ':
        cart.append(inventory.loc[y,'Name'])
        cred.append(int(inventory.loc[y,'Price']))
    elif choice == b'\r' and len(cart)!=0:
        print('         121 Supermarket\n  83 Tat Chee Ave, Kowloon Tong\n   New Territories, Hong Kong\nCasher: Self    '+str(datetime.now().strftime('%Y/%m/%d %H:%M')))
        for x in range(len(cart)):print('   %-20s %5d'%(cart[x],cred[x]))
        print('   Total:                 $'+str(sum(cred)))
        break
    elif choice ==b'q' or choice == b"\x1b":break
    print('Inventory:')
    for row in range(number_of_items):
        if row==y and tab==0:print('%-20s    $%3s'%('<'+inventory.loc[row,'Name']+'>',inventory.loc[row,'Price']))
        else:print('%-20s    $%3s'%(' '+inventory.loc[row,'Name']+' ',inventory.loc[row,'Price']))
    if len(cart)==0:print('\n\n↑ ↓ Select Item        Space Bar To Select          Tab Switch to Shopping Cart        Esc To Exit')
    else:
        print('\n\n%-18sTotal:$%3d'%('Shopping Cart:',sum(cred)))
        for row in range(len(cart)):
            if row==y and tab==1:print('%-20s    $%3s'%('<'+cart[row]+'>',cred[row]))
            else:print('%-20s    $%3s'%(' '+cart[row]+' ',cred[row]))
        print('\n\n↑ ↓ Select Item        Space Bar To Unselect        Tab Switch to Shopping Cart        Esc To Exit       Enter To Check Out')
