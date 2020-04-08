# Declaring the variables

paymentAmt = 0.00

flag = 0

 

# Take the payment input from the user and validate the payment amount

while flag == 0:

    paymentAmt = float(input("Please Enter Amount (XX.XX): "))

    if isinstance(paymentAmt, float)==True:

        print("Payment is Valid !!")   

        flag += 1

    else:

        print("Please enter a valid payment amount")

 

# Reset the flag           

flag = 0

 

# Take the payment input from the user and validate the payment amount

while flag == 0:

    cardNumber = input ("Please Enter Card Number (XXXXXXXXXXXXXXXX): ")

    if len(str(cardNumber))==16 and (str(cardNumber).isdigit()):

        print("Card Number is Valid !!")

        flag += 1

    else:

        print("Please enter a valid Card Number")

           

# Reset the flag 

flag = 0

 

# validate if payment amount is greater than £30 and request for pin if it is greater

if paymentAmt>30:

    while flag == 0:

        pinNumber = input("Enter Your 4 Digit Pin Number: ")

        if len(str(pinNumber))==4 and str(pinNumber).isdigit()==True:

            print("Pin is Valid !!")    # Display Pin Valid

            flag += 1

        else:

            print("Please enter the correct Pin")

 

# Display Payment successful

print("Processing your payment ...")

print("Your Payment is successful")