#Creater info
print("Creator Information:")
print("                                                                        ")
print("Name:Aditya Anand \
      Class: XI B\
      Roll number: 11212")
print("                                                                        ")      
print("These Are the folowing set of Operations you can use :)")   
print("+ for ADDITION, ","- for SUBSTRACTION, "," * for MULTIPLICATION, ","/ for DIVISION, ","n for Power value")
print("                                                                        ")      
no=int(input("Enter the number of Inputs with which you want to do the operation: "))

#max no is 2 and min no is 5       
if no==2:
       number_1=float(input("Enter The 1st Number:"))
       number_2=float(input("Enter The 2nd Number:"))
elif no==3:
        number_1=float(input("Enter The 1st Number:"))
        
        number_2=float(input("Enter The 2nd Number:"))
        number_3=float(input("Enter The 3rd Number:"))
elif no==4:
        number_1=float(input("Enter The 1st Number:"))
        number_2=float(input("Enter The 2nd Number:"))
        number_3=float(input("Enter The 3rd Number:"))
        number_4=float(input("Enter The 4th Number:"))
elif no==5:
        number_1=float(input("Enter The 1st Number:"))
        number_2=float(input("Enter The 2nd Number:"))
        number_3=float(input("Enter The 3rd Number:"))
        number_4=float(input("Enter The 4th Number:"))
        number_5=float(input("Enter The 5th Number:"))
else:
        print("Minimun number with which operation can be done is 2 & Maximum number with which operation can be done is 5")
"+ - ADDITION"
"- - SUBSTRACTION"
"* - MULTIPLICATION"
"/ - DIVISION"
"n-to the power"
user_input = input("Enter the Function to be used:")
if user_input == "+" and no==2:
        number_3=0
        number_4=0
        number_5=0
if user_input == "+" and no==3:
        number_4=0
        number_5=0
if user_input == "+" and no==4:
        number_5=0
if user_input == "-" and no==2:
        number_3=0
        number_4=0
        number_5=0
if user_input == "-" and no==3:
        number_4=0
        number_5=0
if user_input == "-" and no==4:
        number_5=0
if user_input == "*" and no==2:
        number_3=1
        number_4=1
        number_5=1
if user_input == "*" and no==3:
        number_4=1
        number_5=1
if user_input == "*" and no==4:
        number_5=1
if user_input == "/" and no==2:
        number_3=1
        number_4=1
        number_5=1
if user_input == "/" and no==3:
        number_4=1
        number_5=1
if user_input == "/" and no==4:
        number_5=1
if user_input == "+":
    output = number_2 + number_1+ number_3+ number_4+ number_5
    print(output)
elif user_input == "-":
    output = number_2 - number_1-number_3- number_4- number_5
    print(output)
elif user_input == "*":
    output = number_2 * number_1* number_3* number_4* number_5
    print(output)
elif user_input == "/":
    output = number_1 / number_2/ number_3/ number_4/ number_5
    print(output)
elif user_input == "n":
    output = number_2 ** number_1
    print(output)
else:
    print ("!*!*! Invalid Entry !*!*!")


