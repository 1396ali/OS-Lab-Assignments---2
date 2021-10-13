#2

import random

user_score = 0
computer_score = 0

print ( "1 : سنگ ")
print ( "2 : کاغذ ")
print ( "3 : قیچی ")

for i in range(5):
    print ("\n Round " , i+1 )


    print ("User turn: ")
    user = int(input("Please choice 1,2,3 :\n"))

    if user == 1 :
        user_choice = "سنگ"

    elif user == 2 :
        user_choice = "کاغذ"

    elif user == 3 :
        user_choice = "قیچی"


    print ("Computer turn : ")
    computer = random.randint(1,3)
    print(computer)


    if computer == 1 :
        computer_choice = "سنگ"

    elif computer == 2 :
        computer_choice = "کاغذ"

    elif computer == 3 :
        computer_choice = "قیچی"

    print ("User choice is :" , user_choice , "&" , "Computer choice is : " , computer_choice)



    if user_choice == computer_choice:
        print(" Tie ")

    elif user_choice == "سنگ" and computer_choice == "قیچی" :
        print("User win")
        user_score += 1
    
    elif user_choice == "سنگ" and computer_choice == "کاغذ" :
        print("Computer win")
        computer_score += 1

    elif user_choice == "کاغذ" and computer_choice == "قیچی" :
        print("Computer win")
        computer_score += 1
        
    
    elif computer_choice == "سنگ" and  user_choice == "قیچی" :
        print("Computer win")
        computer_score += 1

    elif computer_choice == "سنگ" and  user_choice == "کاغذ" :
        print("User win")
        user_score += 1

    elif computer_choice == "کاغذ" and  user_choice == "قیچی" :
        print("User win")
        user_score += 1


    print ( "User score is : " , user_score , "&" , "Computer score is : " , computer_score)

print ( "Finally score : user VS computer " , user_score , "&" , computer_score )

if user_score==computer_score:
    print(" No one wins ")

elif user_score>computer_score:
    print("USER is winner")

elif computer_score>user_score:
    print("COMPUTER is winner")