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

number = [11, 15, 34, 13, 57, 346, 96, 80, 53, 49, 85, 14, 19]
number.append(33)
number.pop(4)
print(number[0])    
print(number)
print(len(number))  
