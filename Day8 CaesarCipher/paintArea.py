import math


def paint_calc(height, width, cover):
    return math.ceil((height * width) / cover)


test_h = int(input("Height of wall (m): "))
test_w = int(input("Width of wall (m): "))
coverage = 5
result = paint_calc(height=test_h, width=test_w, cover=coverage)
result = str(int(result))
print(f"You'll need {result} cans of paint.")
