#4

time = input ("Please input your time as a(H:M:S) : ")


hour , minute , second = time.split(":")

second = int(hour)*3600 + int (minute)*60 + int(second)


print ("Your time to (second) is : " , second , "ثانیه")