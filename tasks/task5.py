#triangle

def draw_triangle(height):
    for i in range(1, height + 1):
        spaces = " " * (height - i)  # Пробелы перед звездочками
        stars = "*" * (2 * i - 1)   # Звездочки
        print(spaces + stars)

height = int(input("enter the height of triangle: "))

# Рисуем треугольник
draw_triangle(height)