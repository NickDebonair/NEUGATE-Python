numbers = [1, 1]
count = 0
for i in numbers:
    next_elem = numbers[count] + numbers[count+1]
    if next_elem > 1000:
        break
    numbers.append(next_elem)
    count += 1
print(numbers)

count2 = 0
for i in numbers:
    ratios_elem = numbers[count2] / numbers[count2+1]
    