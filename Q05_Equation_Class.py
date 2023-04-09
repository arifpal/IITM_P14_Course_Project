import math

class DistanceCalculator:

    def calculate_distance(self, x1, y1, x2, y2):
        try:
            distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            return distance
        except TypeError:
            print("Invalid input! Please enter valid integer or float values for x and y coordinates.")

dc = DistanceCalculator()

# example usage
print(dc.calculate_distance(1, 2, 3, 4))
print(dc.calculate_distance(1, 'a', 3, 4))
