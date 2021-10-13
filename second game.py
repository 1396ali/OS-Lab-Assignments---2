#3

import random

user_score = 0
computer1_score = 0
computer2_score = 0

print ( "1 : رو ")
print ( "2 : پشت ")


for i in range(5):
    print ("\n Round " , i+1 )


    print ("User turn: ")
    user = int(input("Please choice 1,2 :\n"))

    if user == 1 :
        user_choice = "رو"

    elif user == 2 :
        user_choice = "پشت"



    print ("Computer1 turn : ")
    computer1 = random.randint(1,2)
    print(computer1)


    if computer1 == 1 :
        computer1_choice = "رو"

    elif computer1 == 2 :
        computer1_choice = "پشت"



    print ("Computer2 turn : ")
    computer2 = random.randint(1,2)
    print(computer2)


    if computer2 == 1 :
        computer2_choice = "رو"

    elif computer2 == 2 :
        computer2_choice = "پشت"



    print ("User choice is :" , user_choice , "&" , "Computer1 choice is : " , computer1_choice , "&" , "Computer2 choice is : " , computer2_choice)




    if user_choice == computer1_choice == computer2_choice:
        print(" Tie ")
##
    elif user_choice == "رو" and computer1_choice == "پشت" and computer2_choice == "پشت" :
        print("User win")
        user_score += 1

    
    elif user_choice == "پشت" and computer1_choice == "رو" and computer2_choice == "رو" :
        print("User win")
        user_score += 1


#
    elif computer1_choice == "رو" and computer2_choice == "پشت" and user_choice == "پشت" :
        print("Computer1 win")
        computer1_score += 1

    
    elif computer1_choice == "پشت" and computer2_choice == "رو" and user_choice == "رو" :
        print("Computer1 win")
        computer1_score += 1
        

#
    elif computer2_choice == "رو" and computer1_choice == "پشت" and user_choice == "پشت" :
        print("Computer2 win")
        computer2_score += 1
    

    
    elif computer2_choice == "پشت" and computer1_choice == "رو" and user_choice == "رو" :
        print("Computer2 win")
        computer2_score += 1
    

    


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
