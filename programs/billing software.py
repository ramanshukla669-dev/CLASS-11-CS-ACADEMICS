# Billing software for shops
while True:
    print("Welcome to billing software! ")
    print("Paymemt methods are cash, UPI, net banking,card")

    name= input('Enter the name of customer: ')
    address= input('Enter the address of customer: ')
    payment= input('Enter the mode of payment: ').lower()
    x= int(input("Enter how much item the user taken: "))
    sum= 0
    for i in range(x):
        x= float(input("Price of element: "))
        sum+=x
    GST= (18/100)*sum
    if payment=="card":
        discount= (5/100)*sum
    elif payment=="netbanking":
        discount= (10/100)*sum
    elif payment=="cash":
        discount= (7/100)*sum
    
    print("Does costumer want a carrybag?")
    print("if yes type y else type n")
    a= input("Enter the response: ")
    if a== "y":
        total_price= (sum+GST+15)- discount
    else:
        total_price= (sum+GST) - discount
    print("---------------------------------------------------------------Invoice-------------------------------------------------------------------")
    print("Name of the customer is:",name)
    print("Address of customer is:",address)
    print("Mode of payment is:",payment)
    if payment=="card":
       print("You got",5, "% discount") 
    elif payment=="netbanking":
       print("You got",10, "% discount") 
    elif payment=="cash":
       print("You got",7, "% discount") 
    print("Discount is ₹", discount)
    print("Total without GST is ₹:",sum)
    print("GST is ₹:",GST)
    print("Total price is ₹",total_price)

    str =input("Press Enter KEY to enter another entry and 0 key to exit ")
    if str=="0":
        break
