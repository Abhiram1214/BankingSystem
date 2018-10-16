print("Banking application")

class Banking:
    BankName = "CITI"
    Location = "Nizampet, Hyderabad"    
    
    def __init__(self):
        self.Balance = 2000
        self.AccountNumber = 13254
        self.AccountName = "Abhiram"
        self.AmountTransferable = 200
        self.AmountReceivable = 500
        
    def BankInfo(self):
        print("Name of the bank" + Banking.BankName)
        print("Branch Location" + Banking.Location)
        
    def AccountInfo(self):
        print("Account Holder: " + self.AccountName)
        print("Account Number: " + str(self.AccountNumber))
        print("Balance: " + str(self.Balance))
        
    def SendMoney(self):
        self.Balance = self.Balance - self.AmountTransferable
        print("Remaining Balance: " + str(self.Balance))
        
    def ReceiveMoney(self):
        self.Balance = self.Balance + self.AmountReceivable
        print("Updated Balance: " + str(self.Balance))
        
    
Bank = Banking()

while True:
    result = input("Enter (B) BankInfo, (A) AccountInfo, (S) Send Money, (R) Received Money")
    if result == 'B' or result == 'b':
        Bank.BankInfo()
    elif result == 'A' or result == 'a':
        Bank.AccountInfo()
    elif result == 'S' or result == 's':
        Bank.SendMoney()
    elif result == 'R' or result == 'r':
        Bank.ReceiveMoney()
    else:
        print("Entered wromg input")
        break

        
print("Bye")
        
        
        
            