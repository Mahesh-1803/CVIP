import random
import string

lower_len = int(input("Enter No.of lowercase characters :"))
upper_len = int(input("Enter No.of uppercase characters :"))
digit_len = int(input("Enter No.of Digits :"))
symbol_len = int(input("Enter No.of symbols :"))
total_len  = (lower_len + upper_len + digit_len + symbol_len)
print("Length of the password you entered : ",total_len)

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digit = string.digits
symbol = string.punctuation

str = random.choices(lower,k=lower_len)+ random.choices(upper,k=upper_len) + random.choices(digit,k=digit_len) + random.choices(symbol,k=symbol_len)


random.shuffle(str)
password = " ".join(str)


print("The Generated Password is : ",password)

