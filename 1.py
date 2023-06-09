import pandas as pd
students = pd.DataFrame({
'Фамилия': ['Иванов', 'Петров', 'Сидоров', 'Смирнов', 'Кузнецов', 'Васильев', 'Попов', 'Морозов'],
'Имя': ['Иван', 'Петр', 'Алексей', 'Николай', 'Дмитрий', 'Андрей', 'Михаил', 'Владислав'],
'Год рождения': [1998, 1997, 1998, 1999, 1997, 1999, 1998, 1997],
'Группа': ['БИ1', 'БИ2', 'БИ1', 'БИ2', 'БИ1', 'БИ2', 'БИ1', 'БИ2'],
'Оценка за экзамен': [9, 8, 10, 6, 8, 9, 7, 10]
})
print(students[(students['Оценка за экзамен'] >= 8) & (students['Группа'] == 'БИ1')]['Фамилия'])