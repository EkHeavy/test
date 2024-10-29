Test = ["1. Лимон", "2. Яблоко", "3. Груша", "4. Инжир"]

for i in range(4):
    fruit_user = input("Введите фрукт: ")
    if fruit_user == "Лимон":
        print("Кислый фрукт")
    else:
        print("Сладкий фрукт")