age = int(input("Enter Age of Participant"))
if age>0 and age<=5:
    print("Your ticket price is FREE")
elif age >5 and age<=12:
    print("Your ticket price is 500kshs ")
elif age > 12 and age <=17:
    print("Your ticket price is 1000kshs ")
elif age >17 and age <=130 :
    print("You ticket price is 1500kshs ")

else:
    print("wrong input")