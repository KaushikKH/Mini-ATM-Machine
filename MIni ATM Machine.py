print("welcome to ATM ")
restart = ('Y')
chances = 3
balance = 100

while chances >= 0:
    pin = int(input("Enter the password"))
    if pin == 1234:
        print("welcome")
        while restart not in ('n' , 'No' , 'N' , 'NO') :
            print('please press 1 to know your balance amount\n')
            print('please press 2 to make a withdrawl\n')
            print('please press 3 to pay in\n')
            print('please press 4 to return card\n')
            option = int (input("which option would you choose?"))
            if option == 1:
                print("your balance is",balance,'\n')
                restart = input ('would you like to go back')
                if restart in ('n' , 'No' , 'N' , 'NO'):
                    print ('Thank you')
                    break
            elif option == 2:
                withdrawl = float(input('how much are you withdrawing?\n Rs 10/Rs 20/Rs 30/Rs 40/Rs 50'))
                if withdrawl in [10,20,30,40,50]:
                    balance = balance - withdrawl
                    print ('your current balance is', balance , '\n')
                    restart = input('would you like to go back')
                    if restart in ('n', 'No', 'N', 'NO'):
                        print ('thank you')
                        break
                    elif withdrawl != [10,20,30,40,50]:
                        print('invalid amount,please try again\n')
                        restart = ('y')
                elif withdrawl == 1:
                    print('please enter the desired amount\n')
            elif option == 3:
                pay_in = float(input('please enter desired amount to be added'))
                balance = balance + pay_in
                print('your current balance is', balance,'\n')
                restart = input('would you like to go back')
                if restart in ('n', 'No', 'N', 'NO'):
                    print ('thank you')
                    break
            elif option == 4:
                print ('please wait for the card to be returned\n ')
                print ('Thank you for your service')
                break
        else:
            print('please enter a correct number\n')
            restart = ('y')
    elif pin != 1234:
        print('incorrect password!\n')
        chances = chances - 1
        if chances == 0:
            print('no more tries\n')
            break
