with open('file.txt', 'r', encoding='utf-8')  as f:  # открываем файл на чтение
    lines = f.readlines()  # читаем все строки файла в список

lines_sorted = sorted(lines, key=lambda x: x.split()[1])  # сортируем список строк по второму элементу (фамилии)

for line in lines_sorted:
    print(line.strip())  # выводим каждую строку без лишних пробелов и переносов