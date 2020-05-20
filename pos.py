import csv
import pandas as pd
import msvcrt
from datetime import datetime
from os import system, name 
cart=[]
cred=[]
inventory= pd.read_csv('inventory.csv')#, index_col=0
_ = system('cls') 
print('Enter number for item:\n'+inventory[['Index','Name']].to_string(index=False,header=False))
dict={b'1':0,b'2':1,b'3':2,b'4':3,b'5':4,b'6':5,b'7':6,b'8':7,b'9':8}
while True:
    choice=msvcrt.getch()
    _ = system('cls') 
    if choice in [b'1',b'2',b'3',b'4',b'5',b'6',b'7',b'8',b'9']:
        cart.append(inventory.loc[dict[choice],'Name'])
        cred.append(int(inventory.loc[dict[choice],'Price']))
        print('Enter number for item:\n'+inventory[['Index','Name']].to_string(index=False,header=False))    
        print('Shopping cart: '+str(cart).strip('[]').replace("'",""))
        print('Price: '+str(sum(cred)))
    elif choice == b'\r':
        print('              121 Supermarket\n      83 Tat Chee Ave, Kowloon Tong\n        New Territories, Hong Kong\nCasher: Self    '+str(datetime.now()))
        for x in range(len(cart)):print('   %-30s %d'%(cart[x],cred[x]))
        print('   Total:                         $'+str(sum(cred)))
        break
    elif choice ==b'q':break
