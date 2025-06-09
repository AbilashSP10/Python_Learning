class Bank_Details:

    Acc_Nam = input("Enter Your Name: ")
    Acc_Num = int(input("Enter Your Account Number: "))
    Acc_Bal = int(input("Enter Your Account Balance: "))
    Acc_Wit = int(input("Enter the Amount You want to withdraw: "))

    Acc_Bal_Now = Acc_Bal - Acc_Wit


obj = Bank_Details()

print(f"Your Current Account Balance is: {obj.Acc_Bal_Now}")

