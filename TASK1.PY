def obchislyty_X(a, b):
  
  if a > b:
    X = a * b + 1
  elif a == b:
    X = 25
  else:
    X = (a - 5) / b
  return X

# Введення даних користувачем
a = float(input("Введіть додатне число a: "))
b = float(input("Введіть додатне число b: "))

# Перевірка на додатність
if a <= 0 or b <= 0:
  print("Числа a та b повинні бути додатними.")
else:
  # Обчислення та виведення результату
  result = obchislyty_X(a, b)
  print("Значення X =", result)
