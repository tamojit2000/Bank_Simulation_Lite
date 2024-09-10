import os
import random
import datetime
import time

C_F=0
B_F=0
B_P=0
L_F=0


Customer=[]
Loan=[]

def display():
    global C_F,B_F,B_P,L_F
    B_P=B_F-C_F
    print('='*20)
    print('C_F',C_F)
    #print(Customer)
    print('B_F',B_F)
    print('B_P',B_P)
    print('L_F',L_F)
    #print(Loan)




def generate_customer():
    global C_F,B_F,B_P,L_F
    if random.randint(1,200)%3==0:
        #ADD
        d={
            'Acc':str(datetime.datetime.now()),
            'Bal':random.randint(1,200000)
        }
        Customer.append(d)
        C_F+=d['Bal']
        B_F+=d['Bal']

    elif random.randint(1,200)%11==0:
        #DELETE
        if len(Customer)>0:
            tmp=random.randint(0,len(Customer)-1)
            obj=Customer[tmp]
            C_F-=obj['Bal']
            del Customer[tmp]
            B_F-=obj['Bal']

def give_interest():
    global C_F
    if random.randint(1,100)%25==0:
        #print(Customer)
        for i in range(len(Customer)):
            obj=Customer[i]
            obj['Bal']=obj['Bal']+int(obj['Bal']*0.03)
            C_F+=int(obj['Bal']*0.03)
        #print(Customer)


def generate_loan():
    global C_F,B_F,B_P,L_F

    if random.randint(1,200)%13==0:
        #ADD
        if B_F>0:
            d={
                'Acc':str(datetime.datetime.now()),
                'Amt':random.randint(1,int(B_F*0.2))
            }

            Loan.append(d)
            L_F+=d['Amt']
            B_F-=d['Amt']

    elif random.randint(1,200)%13==0:
        #DELETE
        if len(Loan)>0:
            tmp=random.randint(0,len(Loan)-1)
            obj=Loan[tmp]
            L_F-=obj['Amt']
            del Loan[tmp]
            B_F+=obj['Amt']+int(obj['Amt']*1.15)


def run():
    generate_customer()
    generate_loan()
    give_interest()

    B_P=B_F-C_F
    return C_F,B_F,B_P,L_F

def formalize(x):
    negative=False
    if x<0:
        negative=True
        x=abs(x)
    #1093736,11,11,111
    #l=list(str(x).zfill(20))
    l=list(str(x))
    #print(l)
    l.insert(-3,',')
    l.insert(-6,',')
    l.insert(-9,',')
    y=''.join(l)
    y=y.lstrip(',')
    y=y.lstrip('0')
    y=y.lstrip(',')
    y=y.lstrip('0')
    if negative:
        y='-'+y
    return y





if __name__=='__main__':
    print()
    #print(formalize(12898477))
    exit()
    for i in range(500):
        generate_customer()
        generate_loan()
        give_interest()
        display()
        #time.sleep(2)
