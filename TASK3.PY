def create_pattern(n):
  
  for i in range(n, 0, -1):
    row = ""
    for j in range(5, i - 1, -1):
      row += str(j)
    print(row)

# Введення числа N
n = int(input("Введіть число N (1 < N < 9): "))

# Перевірка введеного числа
if 1 < n < 9:
  create_pattern(n)
else:
  print("Некоректне значення N. Введіть число від 2 до 8.")
