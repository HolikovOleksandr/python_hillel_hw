import string

input_str =input("Enter two letters separated by a hyphen (e.g., a-z): ")

start, end = input_str.split('-')

all_letters = string.ascii_lowercase + string.ascii_uppercase

start_index = all_letters.index(start)
end_index = all_letters.index(end)

print(all_letters[start_index:end_index + 1])
