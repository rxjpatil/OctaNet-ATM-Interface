class CardHolder():
    def __init__(self, cardnumber, pin, firstname, lastname, balance):
        self.cardnumber = cardnumber
        self.pin = pin
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance

#Getter Methods
    def get_cardnumber(self):
        return self.cardnumber
    def get_pin(self):
        return self.pin
    def get_firstname(self):
        return self.firstname
    def get_lastname(self):
        return self.lastname
    def get_balance(self):
        return self.balance
    
#Setter Methods
    def set_cardnumber(self, newVal):
        self.cardnumber = newVal
    def set_pin(self, newVal):
        self.pin = newVal
    def set_firstname(self, newVal):
        self.firstname = newVal
    def set_lastname(self, newVal):
        self.lastname = newVal
    def set_balance(self, newVal):
        self.balance = newVal

    def print_out(self):
        print("Card #: ",self.cardnumber)
        print("PIN #: ",self.pin)
        print("First Name #: ",self.firstname)
        print("Last Nmae #: ",self.lastname)
        print("Balance #: ",self.balance)