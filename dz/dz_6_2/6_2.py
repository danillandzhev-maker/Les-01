seconds = int(input("Введи количество секунд: "))

days, seconds = divmod(seconds, 24 * 60 * 60)
hours, seconds = divmod(seconds, 60 * 60)
minutes, seconds = divmod(seconds, 60)

if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif days % 10 in (2, 3, 4) and days % 100 not in (12, 13, 14):
    day_word = "дня"
else:
    day_word = "днів"

hours = str(hours).zfill(2)
minutes = str(minutes).zfill(2)
seconds = str(seconds).zfill(2)

print(f"{days} {day_word}, {hours}:{minutes}:{seconds}")