from datetime import date
import sys

def get_minutes_since_birth(birth_date):
    today = date.today()
    delta = today - birth_date
    return delta.days * 24 * 60

def number_to_words(n):
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion"]
    
    if n < 10:
        return ones[n]
    elif 10 < n < 20:
        return teens[n - 11]
    elif n < 100:
        return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")
    elif n < 1000:
        return ones[n // 100] + " hundred" + (" " + number_to_words(n % 100) if n % 100 != 0 else "")
    else:
        for i, word in enumerate(thousands):
            if n < 1000 ** (i + 1):
                return number_to_words(n // (1000 ** i)) + " " + word + (" " + number_to_words(n % (1000 ** i)) if n % (1000 ** i) != 0 else "")

def main():
    birth_date_str = input("Date of Birth (YYYY-MM-DD): ")
    try:
        birth_date = date.fromisoformat(birth_date_str)
    except ValueError:
        sys.exit("Invalid date format. Use YYYY-MM-DD.")
    
    minutes_lived = get_minutes_since_birth(birth_date)
    words = number_to_words(minutes_lived)
    print(f"{words} minutes")

if __name__ == "__main__":
    main()
