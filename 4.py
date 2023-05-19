def sum_digits(num):
# функция для вычисления суммы цифр данного числа
  return sum(int(digit) for digit in str(num))

n = int(input("Введите число n: "))
for i in range(10**(n-1), 10**n):
    if sum_digits(i) == n:
        print(i)