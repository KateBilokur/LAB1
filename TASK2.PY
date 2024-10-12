def find_multiples_of_three(start, end):
  
  multiples = []
  for num in range(start, end + 1):
    if num % 3 == 0:
      multiples.append(num)
  return multiples, len(multiples)

# Встановлюємо діапазон
start_range = 30
end_range = 60

# Знаходимо числа, кратні 3, та їх кількість
result, count = find_multiples_of_three(start_range, end_range)

# Виводимо результат
print("Числа, кратні 3, в діапазоні від", start_range, "до", end_range, ":")
print(result)
print("Кількість таких чисел:", count)
