#Car Salesman with Hidden Fees
name=input("Welcome to the Ford Dealership. My name is Tommy, what's your name?: ")
list_price=int(input("Great to meet you " + name +
                     ". Let's see then, just let me know the number on the windshield, and we'll get you a great deal: "))
#Random Values
bs_discount=list_price*.1
tax=list_price*.1
license_fee=list_price*.3
dealer_prep=1000
dest_charge=2435
print("Alright, so after our end-of-the-year discount, your total comes to", list_price - bs_discount, end="..."*5)
print("And after factoring in tax, license fee, dealer prep, and destination charge, we can let this car go for",
      list_price - bs_discount + tax + license_fee + dealer_prep + dest_charge, end=".\n")
