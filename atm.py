import datetime
from fpdf import FPDF

upin = int(input("Enter your pin"))
f= open("D:\\Study\\Python\\pin.txt","r")
fpin=int(f.read())
f.close()

if(upin == fpin):
    f=open("D:\\Study\\Python\\balance.txt","r")
    bal=int(f.read())
    f.close()
    print("Your Balance is Rs",bal)
    n = int(input("1.Withdraw 2.Deposit 3.Change Pin 4.Show Statement 5.Convert to PDF"))
    if(n==1):
        amt=int(input("Enter amount to be withdrawn"))
        bal=bal-amt
        print("Withdraw successful!")

        f=open("D:\\Study\\Python\\balance.txt","w")
        f.write(str(bal))
        f.close()

        s ="Withdraw of Rs "+str(amt)+" on date " + str(datetime.datetime.now()) + "\n"
        f=open("D:\\Study\\Python\\log.txt","a")
        f.write(s)
        f.close()

    elif(n==2):
        amt=int(input("Enter amount to be Deposited"))
        bal=bal+amt
        print("Deposit successful")

        f=open("D:\\Study\\Python\\balance.txt","w")
        f.write(str(bal))
        f.close()

        s = "Deposit of Rs "+ str(amt)+" on date " +str(datetime.datetime.now())+"\n"
        f=open("D:\\Study\\Python\\log.txt","a")
        f.write(s)
        f.close()

    elif(n==3):
        pin=int(input("Enter the new pin"))

        f=open("D:\\Study\\Python\\pin.txt","w")
        f.write(str(pin))
        f.close()

        s="Pin changed on date "+str(datetime.datetime.now())+"\n"
        f=open("D:\\Study\\Python\\log.txt","a")
        f.write(s)
        f.close()


    elif(n==4):
        f=open("D:\\Study\\Python\\log.txt","r")
        log = f.read()
        print(log)
        f.close()

    elif(n==5):
        f=open("D:\\Study\\Python\\log.txt","r")
        log=f.read()
        f.close()

        pdf=FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=10)
        pdf.cell(10,100,txt=log,ln=1,align='C')
        pdf.output("D:\\Study\\Python\\log.pdf")

    else:
        print("Invalid Choice")
else:
    print("Invalid pin")
