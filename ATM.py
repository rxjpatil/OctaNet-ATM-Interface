from Card_Holder_for_ATM import CardHolder

def print_menu():
    #for printing options to the user
    print("Please choose from one of the following options.")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance")
    print("4. Quit")

def deposit(CardHolder):
    try:
        deposit = float(input("How much ₹₹ would you like to deposit: "))
        CardHolder.set_balance(CardHolder.get_balance() + deposit)
        print("Thank you for your ₹₹. Your new balance is: ", str(CardHolder.get_balance()))
    except:
        print("Invalid input")

def withdraw(CardHolder):
    try:
        withdraw = float(input("How much ₹₹ would you like to withdraw: "))
        #Check if the user has enough money
        if(CardHolder.get_balance() < withdraw):
            print("Insufficient balance")
        else:
            CardHolder.set_balance(CardHolder.get_balance() - withdraw)
            print("You're good to go! Thank you")
    except:
        print("Invalid input")

def check_balance(CardHolder):
    print("Your current balance is: ",CardHolder.get_balance())

if __name__ == "__main__":
    current_user = CardHolder("","","","","")

    #list of card holders
    list_of_cardholders = []
    list_of_cardholders.append(CardHolder("9511892111",6969,"Raj","Patil",95000.69))
    list_of_cardholders.append(CardHolder("7414942111",7417,"Gitu","Shivsena",59000.78))
    list_of_cardholders.append(CardHolder("7972992111",7972,"Sushil","Date",86100.64))
    list_of_cardholders.append(CardHolder("9096465111",9096,"Abhijeet","Walke",75000.79))                
    list_of_cardholders.append(CardHolder("7218872933",6969,"Abhisheck","Dotted",45000.15))
    
    #prompt user for debit card number
    DebitCardNumber = ""
    while True:
        try:
            DebitCardNumber = input("Please insert your Debit Card: ")
            #check against repo
            DebitMatch = [holder for holder in list_of_cardholders if holder.cardnumber == DebitCardNumber]
            if(len(DebitMatch) > 0):
                current_user = DebitMatch[0]
                break
            else:
                print("Card number not recognized. Please try again")
        except:
            print("Card number not recognized.Please try again.")
    
    #prompt for PIN
    while True:
        try:
            userpin = int(input("Enter your password: ").strip())
            if(current_user.get_pin() == userpin):
                break
            else:
                print("Invalid PIN. Please try again.")
        except:
            print("Invalid PIN. Please try again.")
    
    #print options
    print("Welcome",current_user.get_firstname(),"!")
    option = 0
    while (option != 4):
        print_menu()
        try:
            option = int(input())
        except:
            print("Invalid input. Please try again.")

        if(option == 1):
            deposit(current_user)
        elif(option == 2):
            withdraw(current_user)
        elif(option == 3):
            check_balance(current_user)
        elif(option == 4):
            break
        else:
            option = 0
    print("Thank you!")

        






