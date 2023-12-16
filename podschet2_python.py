text = input('Введите строчку')
a = input('Что нужно найти?')
count_symbol = 0
symbol = text.find(f"{a}")
while symbol != -1:
    count_symbol += 1
    symbol = text.find(f"{a}", symbol + 1)
print(f'Символов {a} в строчке {count_symbol}')
search = text.find(f'{a}')
if search != -1:
    print(f"Ближайший к началу строки символ {a} найден на позиции {search + 1}.")
else:
    print(f"Символов {a} нет в этой строке.")