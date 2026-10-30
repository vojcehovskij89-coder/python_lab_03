# def greet(name):
#     print("Здравствуйте,", name)


# greet(input("Введите ваше имя: "))


# def square(number):
#     return number ** 2

# print(square(int(input("Введите число: "))))

# def max_of_two(a, b):
#     if a > b:
#         return a
#     else:
#         return b

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))

# print(max_of_two(a, b))


# def calculate_rectangle(width, height):
#     return width * height

# def calculate_perimeter(width, height):
#     return 2 * (width + height)

# def describe_rectangle(width, height, unit="см"):
#     s = calculate_rectangle(width, height)
#     p = calculate_perimeter(width, height)
    
#     print(f"Прямоугольник: {width} {unit} на {height} {unit}")
#     print(f"Площадь: {s} {unit}")
#     print(f"Периметр: {p} {unit}")

# width = int(input("Введите первую сторону: "))
# height = int(input("Введите боковую сторону: "))


# describe_rectangle(width, height)

# value = 10
# def example():
#     value = 20
#     score = 100
#     print(value)
    
# example()
# print(value)
# print(score)

# number = [11, 15, 34, 13, 57, 346, 96, 80, 53, 49, 85, 14, 19]
# number.append(33)
# number.pop(4)
# print(number[0])    
# print(number)
# print(len(number))  

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers[:3])
# print(numbers[-3:])
# print(numbers[2:7])
# print(numbers[::2])
# print(numbers[::-1])


# measurements = (10, 11, 12, 13, 14, 15, 16,17, 18)
# x, y = measurements[0:2]
# measurements = list(measurements)
# measurements[1] = 40
# measurements = tuple(measurements)


# print(x)
# print(y)
# print(measurements)
# # print(measurements[0])
# # print(measurements[-1])
# # print(measurements[2:6])


# spisok = [10, 12, 15, 164, 153, 78, 696]
# spisok_sort = sorted(spisok)
# print(len(spisok))
# print(sum(spisok))
# print(min(spisok))
# print(max(spisok))
# print(sum(spisok)/len(spisok))
# print(spisok_sort)
# spisok.sort()
# print(spisok)

# numbers = [1, 2, 3, 4, 5, ]

# def calculate_sum(numbers):
#     summa = 0
#     for i in numbers:
#         summa += i
#     return summa
# def find_min(numbers):
#     minimum = numbers[0]
#     for i in numbers:
#         if minimum > i:
#             minimum = i
#         return minimum

# def find_max(numbers):
#     maximum = numbers[0]
#     for i in numbers:
#         if maximum < i:
#             maximum = i
#     return maximum

# print('Сумма', calculate_sum(numbers), sum(numbers))
# print('Мин число', find_min(numbers), min(numbers))
# print('Макс число', find_max(numbers), max(numbers))


# numbers = [1, 2, 3, 4, 5]

# def find_element(numbers, target):
#     for i in range(len(numbers)):
#         if numbers[i] == target:
#             return i
#     return -1
# print(find_element(numbers, 2))
# print(find_element(numbers, 42))  

# numbers = [1, 2, 3, 4, 5]
# def analyze(numbers):
#     output = (min(numbers), max(numbers), sum(numbers) / len(numbers))
#     return output

# numb1, numb2, avg = analyze(numbers)
# print(numb1, numb2, avg)

# numbers = [-10, 3, -2, 8, -5]

# num_sort = sorted(numbers)
# print(num_sort)

# num_sort2 = sorted(numbers, key=lambda x: abs(x))
# print(num_sort2)

measurements = [12, 7, 25, 3, 18, 9, 30, 14, 21, 6]


def calculate_average(measurements):
    total = 0
    for value in measurements:
        total += value
    return total / len(measurements)


def find_minimum(measurements):
    minimum = measurements[0]
    for value in measurements:
        if value < minimum:
            minimum = value
    return minimum


def find_maximum(measurements):
    maximum = measurements[0]
    for value in measurements:
        if value > maximum:
            maximum = value
    return maximum


def count_above_average(measurements):
    average = calculate_average(measurements)
    count = 0
    for value in measurements:
        if value > average:
            count += 1
    return count


def find_value(measurements, target):
    for i in range(len(measurements)):
        if measurements[i] == target:
            return i
    return -1


def analyze_measurements(measurements):
    return find_minimum(measurements), find_maximum(measurements), calculate_average(measurements)


minimum, maximum, average = analyze_measurements(measurements)

print("Количество измерений:", len(measurements))
print("Минимум:", minimum)
print("Максимум:", maximum)
print("Среднее:", average)
print("Значений выше среднего:", count_above_average(measurements))

target = float(input("Введите значение для поиска: "))
index = find_value(measurements, target)
if index == -1:
    print("Значение не найдено")
else:
    print("Значение найдено, индекс:", index)
    