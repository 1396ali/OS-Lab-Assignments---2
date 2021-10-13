#5

second = int(input("Please input your time as a second : " ))

hour = int (second/3600)
second = second % 3600
minute = int (second/60)
second = second % 60

print ("Your time to (H,M,S) is : " , hour , ":" , minute , ":" , second)