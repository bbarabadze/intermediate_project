import random

real_number = random.randint(1, 100)

while True:
    try:
         guess_number = int(input("შეიყვანეთ რიცხვი 1-დან 100-მდე: "))
         if guess_number == real_number:
              print(f"გილოცავთ, თქვენ გამოიცანით რიცხვი {real_number}")
              break
         elif guess_number > real_number:
               print("თქვენი რიცხვი მაღალია გამოსცნობ რიცხვზე")
               continue
         elif guess_number < real_number:
               print("თქვენი რიცხვი ნაკლებია გამოსცნობ რიცხვზე")
               continue

         
    except ValueError:
        print("შეცდომა, გთხოვთ შეიყვანოთ მთელი რიცხვი 0-დან 100-მდე.")
