class BankAccount: 
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print((f"Se ha depositado {amount}. Saldo actual {self.balance}"))    
        else:
            print("Cuenta inactiva")    
    
    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Se a retirador {amount}. Saldo actual {self.balance}")  
    
    def deactivate(self):
        self.is_active = False
        print(f"La cuenta se ha desativado")      
    
    def activate(sefl):
        sefl.is_active = True
        print(f"La cuenta se ha activado")

# Creacion de Objetos
cuenta1 = BankAccount("Ana", 500)
cuenta2 = BankAccount("Luis", 1000)

# Llamada a metodos
cuenta1.deposit(500)
cuenta2.withdraw(100)
cuenta1.deactivate()
cuenta1.deposit(200)
cuenta1.activate()
cuenta1.deposit(200)