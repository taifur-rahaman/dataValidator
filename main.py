import checker

print("Data Validator\n\n")

while True:
    choice = input("1. Even or Odd Checker\n2. Vowel or Consonant Checker\n3. Leap Year Checker\n4. Palindrome Checker\n5. Prime Number Checker\n0. Exit\n\nEnter your Choice: ")
    
    if choice == '1':
        checker.even_odd_checker()
    elif choice == "2":
        checker.vowel_consonant_checker()
    elif choice == "3":
        checker.leap_year_checker()
    elif choice == "4":
        checker.palindrome_checker()
    elif choice == "5":
        checker.prime_number_checker()
    elif choice == "0":
        print("Exiting the program.\nGoodbye!")
        break
    else:
        print("Invalid Choice! Please try again.\n")