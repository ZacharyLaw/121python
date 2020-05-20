import csv
import pandas as pd
import msvcrt
cart=[]
cred=[]
inventory= pd.read_csv('inventory.csv')#, index_col=0
print('Enter number for item:\n'+inventory[['Index','Name']].to_string(index=False,header=False))
while True:
    choice=msvcrt.getch()
    if choice==b'1':
        cart.append(inventory.loc[1,'Name'])
        cred.append(int(inventory.loc[1,'Price']))
    print('Enter number for item:\n'+inventory[['Index','Name']].to_string(index=False,header=False))    
    print('Shopping cart: '+str(cart).strip('[]').replace("'",""))
    print('Price: '+str(sum(cred)))