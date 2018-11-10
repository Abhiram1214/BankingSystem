print("Banking application")

class Banking:
    UseBankName = "CITI"
    UserAccountName = "Abhiram"
    UserBalance = 10000
    UserAccountNumber = 13254
    UserBankLocation = "Nizampet, Hyderabad"   
    BankList = []
    
    def __init__(self, bankname, transactionfee):
        self.bankname = bankname
        self.transactionfee = transactionfee
       # self.AmountTransferable = 200
       # self.AmountReceivable = 500
        
    def BankInfo(self):
        print("Name of the bank" + self.bankname)
        #print("Branch Location" + Banking.Location)
        

    def SendMoney(self, send):
        Banking.UserBalance = Banking.UserBalance - send
        print("Remaining Balance: " + str(Banking.UserBalance))
        
    def ReceiveMoney(self, amtreceived):
        Banking.UserBalance = Banking.UserBalance + amtreceived
        print("Updated Balance: " + str(Banking.UserBalance))
        

 
#Banking.BankList.append(Banking('ICICI', 10))
    
    
bank = Banking('ICICI', 10)

#bank.BankInfo()
#Bank = Banking()

while True:
    result = input("Enter (B) BankInfo, (A) AccountInfo, (S) Send Money, (R) Received Money")
    if result == 'B' or result == 'b':
        bank.BankInfo()
    elif result == 'A' or result == 'a':
        bank.AccountInfo()
    elif result == 'S' or result == 's':
        send = int(input("Enter the amount you want to transfer "))
        bank.SendMoney(send)
    elif result == 'R' or result == 'r':
        receive = int(input("Enter the amount you want to receive "))
        bank.ReceiveMoney(receive)
    else:
        print("Entered wromg input")
        break

        
print("Bye")
        
        
        
            