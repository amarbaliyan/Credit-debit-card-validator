from tkinter import *
from wsgiref.validate import validator
root = Tk()
root.geometry("400x200")
def validater():
    card_numbers=entry.get()
    pi=int(card_numbers)
    ans=0
    card_number=[]
    while(pi>0):
        rem=pi%10
        card_number.append(rem)
        pi=pi//10
    
# Remove the last digit from the card number
    check_digit = card_number.pop(0)

    processed_digits = []

    for index, digit in enumerate(card_number):
        if index % 2 == 0:
            doubled_digit = int(digit) * 2

            # Subtract 9 from any results that are greater than 9       
            if doubled_digit > 9:
                doubled_digit = doubled_digit - 9

            processed_digits.append(doubled_digit)
        else:
            processed_digits.append(int(digit))

    total = int(check_digit) + sum(processed_digits)

    # Verify that the sum of the digits is divisible by 10
    if total % 10 == 0:
        name="valid!!!"
        entryvalue.set(name)
    else:
        name="Invalid!!!"
        entryvalue.set(name)
ok=Label(root, text="Type your card-number", font=('Arial',10))
ok.grid(row=3,column=1)
entryvalue = StringVar()
entry= Entry(root, textvariable="")
entry.grid(row=3, column=2)
button = Button(root, text="validate", command=validater)
button.grid(row=5, column=2)
label= Label(root, text="", textvariable=entryvalue , font= ('Helvetica 14 bold',20), foreground= "red3")
label.grid(row=8, column=2)
root.mainloop()

# card_number = list(input("Please enter a card number: ").strip())
