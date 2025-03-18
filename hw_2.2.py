positive_five_digit_number = int(input("Plese, enter a positive 5-digit number: "))

first_digit = positive_five_digit_number // 10000
second_digit = (positive_five_digit_number // 1000) % 10
third_digit = (positive_five_digit_number // 100) % 10
fourth_digit = (positive_five_digit_number // 10) % 10
fifth_digit = positive_five_digit_number % 10

reversed_positive_five_digit_number = fifth_digit * 10000 + fourth_digit * 1000 + third_digit * 100 + second_digit * 10 + first_digit
print(reversed_positive_five_digit_number)