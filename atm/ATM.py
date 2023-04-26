from user import user
import random
import csv

list_of_users = []

#LOAD DATA FROM  (from file)
def load_data():
    with open("C:/Users/User/OneDrive/Desktop/task/data.csv","r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # for the first row which is column header
                pass
            else:

                print('User list --', ",".join(row))
                # data, one record per line
                list_of_users.append(user(row[0], row[1], row[2], row[3], row[4]))
            line_count += 1

load_data()


#SAVE DATA TO FILE
def store_data():

    with open('C:/Users/User/OneDrive/Desktop/new/data.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)

        # write header or column names
        writer.writerow(['firstname','lastname','money','idCode','password'])

        # write all records
        for account in list_of_users:
            writer.writerow([account.firstname, account.lastname, account.balance, account.cardNum, account.password])

#Print menu
def print_menu():
    print("\nPlease choose from the following options")
    print("1 Deposit")
    print("2 Withdraw")
    print("3 Show balance")
    print("4 Send money")
    print("5 Exit")

# Put money in account
def deposit(user):
    try:
        deposit = float(input("\nHow much money do you want to deposit? - "))
        user.balance = float(user.balance)
        user.set_balance(user.get_balance()+deposit)
        print("\nYour current balance - ", str(user.get_balance()))
    except:
        print("Invalid input.")

# Send money
def send_money(user):

    while True:

        Wheresend = ""
        try:
            if __name__ == "__main__":
                recivemoney_user = user("", "", "", "", "")
                Wheresend = input("To whom you would like to send money? Please enter ID code- ")

            # find to whom send
            sendMach = [senderr for senderr in list_of_users if str(senderr.cardNum) == str(Wheresend)]

            for senderr in list_of_users:
                if (len(sendMach) > 0):
                    recivemoney_user = sendMach[0]
                    recivemoney_user.print_id()

                    # check if there is enough
                    while True:
                        try:
                            sendd = float(input("\nHow much you would like to send - "))
                            if float(current_user.get_balance()) < sendd:
                                print("Not enough money.")

                            else:
                                current_user.balance = float(current_user.balance)
                                recivemoney_user.balance = float(recivemoney_user.balance)

                                current_user.set_balance(current_user.get_balance() - sendd)
                                recivemoney_user.set_balance(recivemoney_user.get_balance() + sendd)
                                print(f"You sent {sendd} to account: {Wheresend}")

                                return


                        except:
                            print("Wrong input try agen.")

                break
            print("Wrong account number try agen.")
            break

        except:
            print("There is no card holder with this ID.")


#Take money out of bank
def withdraw(user):

    try:
        withdraw = float(input("\nWhat amount do you want to withdraw : "))
        user.balance = float(user.balance)
#check if there is enough

        if(user.get_balance() < withdraw):
            print("Not enough money.")
        else:
            user.set_balance(user.get_balance()-withdraw)
            print(f"Your current balance is {user.get_balance()}")
    except:
        print("Invalid input.")

def check_balance(user):
    print("Your balance is - ",user.get_balance())

if __name__ == "__main__":
    current_user = user("","","","","")

#Registration

ipName = ""
ipLastName = ""
rndCardNum = random.randint(10000000,99999999)
rndCardPin = random.randint(1000,9999)

def reg(list_of_users, user):
    ipName = str(input("\nPlease enter name - "))
    ipLastName = str(input("\nPlease enter last name - "))
    newUser = user(ipName,ipLastName, 15, rndCardNum, rndCardPin)
    list_of_users.append(newUser)
    print(f"\nThank you for registration! {ipName} {ipLastName}\n You recive 15 $ for registration!! \n Your login code is - {rndCardNum} \n  Your pin - {rndCardPin}")


regOrLogin = input("\nDo you already have account? If yes press ENTER \nIf you want to register press - r : ")

if regOrLogin == "r":
    reg(list_of_users, user)
else:
    pass


# make sure data is right for login
debitCardNum = ""

while True:
    try:
        debitCardNum = input("\nPlease enter your login code : ")
        debitMach = [holder for holder in list_of_users if str(holder.cardNum) == str(debitCardNum)]

        for holder in list_of_users:
            if (len(debitMach)>0):
                current_user = debitMach[0]
                break

            else:
                print("Card is not recognized.")
                break

        if(len(debitMach)>0):
            break

    except:
        print("Wrong account number.")


# password

while True:
    try:
        userPin = (input("Enter pin - ").strip())
        if(str(current_user.get_password()) == userPin):
            break
        else:
            print("Wrong pin. Try again - ")

    except:
        print("Wrong pin. Try again - ")


#print menu

print("Welcome!", current_user.get_firstname(),current_user.get_lastname())
option= 0
while (True):
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
    elif (option == 4):
        send_money(user)
        pass
    elif(option == 5):
        break
    else:
        option = 0

print("Thank you! Have a nice day!")

store_data()