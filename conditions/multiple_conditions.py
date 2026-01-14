# Множественные условия с elif
print("=== Множественные условия ===")

# Определение времени суток - ночь
hour = 22
print(f"Время: {hour}:00")

if hour >= 6 and hour < 12:
    print("🌅 Утро - время завтракать!")
elif hour >= 12 and hour < 18:
    print("☀️ День - время обедать!")
elif hour >= 18 and hour < 22:
    print("🌆 Вечер - время ужинать!")
elif hour >= 22 or hour < 6:
    print("🌙 Ночь - время спать!")
else:
    print("❓ Неизвестное время")

# Определение сезона - лето
month = 13
print(f"Месяц: {month}")

if month in [12, 1, 2]:
    print("❄️ Зима - время для лыж и коньков!")
elif month in [3, 4, 5]:
    print("🌸 Весна - время цветения!")
elif month in [6, 7, 8]:
    print("☀️ Лето - время отпусков!")
elif month in [9, 10, 11]:
    print("🍂 Осень - время сбора урожая!")
else:
    print("❓ Неизвестный месяц")