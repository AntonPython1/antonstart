language = int(input('Введите 1 чтобы выбрать русский  Enter 2 to select english '))
if language == 2:
    text = input('Enter line or text')
    a = input('Symbol that programm need to find')
    count_symbol = 0
    symbol = text.find(f"{a}")
    count = len(a)
    if count == 1:
        count = 'Letter'
    elif count > 1:
        count = 'Word'
    while symbol != -1:
        count_symbol += 1
        symbol = text.find(f"{a}", symbol + 1)
    print(f'Line contains {count} "{a}"  {count_symbol} time(s)')
    search = text.find(f'{a}')
    if search != -1:
        print(f' {count} "{a}" closest to the beginning of the line was found at position {search + 1}.')
    else:
        print(f'There are no {count} "{a}" in this line.')
    variant = int(input(f"Enter 1 if you want to replace {a}, enter 0 if you don't want"))
    if variant == 1:
        new = input(f'Enter {count} which needs to be replacedь {a}')
        newtext = text.replace(a , new)
        print('Text after editing:')
        print(newtext)
    if variant == 0:
        print('Thanks for using the program!')
if language == 1:
    text = input('Введите строку или текст')
    a = input('Введите символ который нужно найти')
    count_symbol = 0
    symbol = text.find(f"{a}")
    count = len(a)
    if count == 1:
        count = 'Буква'
        g = 'Ближайшая'
        
    elif count > 1:
        count = 'Слово'
        g = 'Ближайшее'
    while symbol != -1:
        count_symbol += 1
        symbol = text.find(f"{a}", symbol + 1)
    print(f'В текст {count} "{a}"  {count_symbol} раз(а)')
    search = text.find(f'{a}')
    if search != -1:
        print(f'{g} {count} "{a}" находиться на позиции {search + 1}.')
    else:
        print(f' {count} "{a}" не присутствует в этой строке');
    variant = int(input(f'Введите 1 если хотите заменить {a}, если не хотите введите 0'))
    if variant == 1:
        new = input(f'Введите {count} на которое нужно заменить {a}')
        newtext = text.replace(a , new)
        print('Текст после редактирования:')
        print(newtext)
    if variant == 0:
        print('Спасибо за использавание программы!')
    