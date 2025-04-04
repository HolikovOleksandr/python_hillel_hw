seconds = int(input("Введіть кількість секунд: "))

days, remainder = divmod(seconds, 86400)
hours, remainder = divmod(remainder, 3600)
minutes, seconds = divmod(remainder, 60)

day_word = "день" if days == 1 else "дні" if 2 <= days <= 4 else "днів"
formatted_time = f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

print(formatted_time)
