

def even_odd_checker():
    try:
        num = int(input("Enter an Integer: "))
        if num % 2 == 0:
            print(f"{num} is Even.\n")
        else:
            print(f"{num} is Odd.\n")
    except ValueError:
        print("Invalid input! Please enter a valid integer.\n")

def vowel_consonant_checker():
    char = input("Enter a single alphabet character: ").lower()
    if len(char) != 1 or not char.isalpha():
        print("Invalid input! Please enter a single alphabet character.\n")
    elif char in 'aeiou':
        print(f"{char} is a Vowel.\n")
    else:
        print(f"{char} is a Consonant.\n")

def leap_year_checker():
    try:
        year = int(input("Enter a Year: "))
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year} is a leap year.\n")
        else:
            print(f"{year} is not a leap year.\n")
    except ValueError:
        print("Invalid input! Please enter a valid year.\n")

def palindrome_checker():
    text = input("Enter a string: ").lower()
    if text == text[::-1]:
        print(f"{text} is a Palindrome.\n")
    else:
        print(f"{text} is not a Palindrome.\n")

def prime_number_checker():
    try:
        num = int(input("Enter an Integer greater than 1: "))
        if num <= 1:
            print("Number must be greater than 1.\n")
            return
        for i in range(2, int(num * 0.5) + 1):
            if num % i == 0:
                print(f"{num} is not a Prime Number.\n")
                return
        print(f"{num} is a Prime Number.\n")
    except ValueError:
        print("Invalid Input! Please Enter a valid Integer.\n")
