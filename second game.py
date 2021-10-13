#3

import random

user_score = 0
computer1_score = 0
computer2_score = 0

print ( "1 : پالام ")
print ( "2 : پولوم ")
print ( "3 : پیلیش ")

for i in range(5):
    print ("\n Round " , i+1 )


    print ("User turn: ")
    user = int(input("Please choice 1,2,3 :\n"))

    if user == 1 :
        user_choice = "پالام"

    elif user == 2 :
        user_choice = "پولوم"

    elif user == 3 :
        user_choice = "پیلیش"



    print ("Computer1 turn : ")
    computer1 = random.randint(1,3)
    print(computer1)


    if computer1 == 1 :
        computer1_choice = "پالام"

    elif computer1 == 2 :
        computer1_choice = "پولوم"

    elif computer1 == 3 :
        computer1_choice = "پیلیش"



    print ("Computer2 turn : ")
    computer2 = random.randint(1,3)
    print(computer2)


    if computer2 == 1 :
        computer2_choice = "پالام"

    elif computer2 == 2 :
        computer2_choice = "پولوم"

    elif computer2 == 3 :
        computer2_choice = "پیلیش"

    print ("User choice is :" , user_choice , "&" , "Computer1 choice is : " , computer1_choice , "&" , "Computer2 choice is : " , computer2_choice)



    if user_choice == computer1_choice == computer2_choice:
        print(" Tie ")
##
    elif user_choice == "پالام" and computer1_choice == "پولوم" and computer2_choice == "پولوم" :
        print("User win")
        user_score += 1

    elif user_choice == "پالام" and computer1_choice == "پیلیش" and computer2_choice == "پیلیش" :
        print("User win")
        user_score += 1    

    
    elif user_choice == "پولوم" and computer1_choice == "پالام" and computer2_choice == "پالام" :
        print("User win")
        user_score += 1

    elif user_choice == "پولوم" and computer1_choice == "پیلیش" and computer2_choice == "پیلیش" :
        print("User win")
        user_score += 1


    elif user_choice == "پیلیش" and computer1_choice == "پالام" and computer2_choice == "پالام" :
        print("User win")
        user_score += 1    
   
    elif user_choice == "پیلیش" and computer1_choice == "پولوم" and computer2_choice == "پولوم" :
        print("User win")
        user_score += 1

#
    elif computer1_choice == "پالام" and computer2_choice == "پولوم" and user_choice == "پولوم" :
        print("Computer1 win")
        computer1_score += 1

    elif computer1_choice == "پالام" and computer2_choice == "پیلیش" and user_choice == "پیلیش" :
        print("Computer1 win")
        computer1_score += 1
    
    elif computer1_choice == "پولوم" and computer2_choice == "پالام" and user_choice == "پالام" :
        print("Computer1 win")
        computer1_score += 1
        
    elif computer1_choice == "پولوم" and computer2_choice == "پیلیش" and user_choice == "پیلیش" :
        print("Computer1 win")
        computer1_score += 1
    
    elif computer1_choice == "پیلیش" and computer2_choice == "پالام" and user_choice == "پالام" :
        print("Computer1 win")
        computer1_score += 1
        
    elif computer1_choice == "پیلیش" and computer2_choice == "پولوم" and user_choice == "پولوم" :
        print("Computer1 win")
        computer1_score += 1
    
    
#
    elif computer2_choice == "پالام" and computer1_choice == "پولوم" and user_choice == "پولوم" :
        print("Computer2 win")
        computer2_score += 1
    
    elif computer2_choice == "پالام" and computer1_choice == "پیلیش" and user_choice == "پیلیش" :
        print("Computer2 win")
        computer2_score += 1
    
    elif computer2_choice == "پولوم" and computer1_choice == "پالام" and user_choice == "پالام" :
        print("Computer2 win")
        computer2_score += 1
    
    elif computer2_choice == "پولوم" and computer1_choice == "پیلیش" and user_choice == "پیلیش" :
        print("Computer2 win")
        computer2_score += 1

    elif computer2_choice == "پیلیش" and computer1_choice == "پالام" and user_choice == "پالام" :
        print("Computer2 win")
        computer2_score += 1
    
    elif computer2_choice == "پیلیش" and computer1_choice == "پولوم" and user_choice == "پولوم" :
        print("Computer2 win")
        computer2_score += 1


#
    elif user_choice == "پالام" and computer1_choice == "پولوم" and computer2_choice == "پیلیش" :
        print("No one scored")
    elif user_choice == "پالام" and computer1_choice == "پیلیش" and computer2_choice == "پولوم" :
        print("No one scored")
        

    elif computer1_choice == "پالام" and computer2_choice == "پولوم" and user_choice == "پیلیش" :
        print("No one scored")
    elif computer1_choice == "پالام" and computer2_choice == "پیلیش" and user_choice == "پولوم" :
        print("No one scored")


    elif computer2_choice == "پالام" and computer1_choice == "پولوم" and user_choice == "پیلیش" :
        print("No one scored")
    elif computer2_choice == "پالام" and computer1_choice == "پیلیش" and user_choice == "پولوم" :
        print("No one scored")



    print ( "User score is : " , user_score , "&" , "Computer1 score is : " , computer1_score , "&" , "Computer2 score is : " , computer2_score)

print ( "Finally score : user VS computer1 VS computer2 " , user_score , "&" , computer1_score , "&" , computer2_score)

if user_score==computer1_score==computer2_score:
    print(" No one wins ")

elif user_score>computer1_score and user_score>computer2_score:
    print("USER is winner")

elif computer1_score>user_score and computer1_score>computer2_score:
    print("COMPUTER1 is winner")

elif computer2_score>user_score and computer2_score>computer1_score:
    print("COMPUTER2 is winner")