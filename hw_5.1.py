import keyword

name = input("Введіть ім'я змінної: ")


is_valid = (
    name not in keyword.kwlist and               
    not name[0].isdigit() and                    
    name.islower() and                           
    all(c.islower() or c.isdigit() or c == '_' for c in name) and 
    name.count('_') <= 1                         
)

print(is_valid)
