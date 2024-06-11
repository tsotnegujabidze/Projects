def calculate_area(width, length):
    area = width * length
    return area

width = float(input('Enter the width> '))
length = float(input('Enter the length> '))

area = calculate_area(width, length)
print(area)