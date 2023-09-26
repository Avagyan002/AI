import numpy as np


class FruitOrVegetable:
    COLOR = ['red', 'green', 'yellow', 'orange', 'violet', 'brown']
    TESTE = ['sweet', 'spicy', 'bitter', 'sour', 'tasteless']
    VIEW = ['round', 'long', 'oval', 'other']
    RESULT = ['fruit', 'vegetable']

    def __init__(self, row, colum, y, k, *args):
        self.colum = colum
        self.row = row
        self.parents_row = int(self.row - (self.row * 0.2))
        self.Y = y
        self.k = k
        self.X = np.column_stack(args)

    def __repr__(self):
        return f"{self.X}"

    def distance_between_points(self):
        distance_array = []
        for i in range(self.parents_row, self.row):
            distance_list = []
            for j in range(0, self.parents_row):
                diff = 0
                for k in range(0, self.colum):
                    diff += (self.X[i, k] - self.X[j, k]) ** 2
                distance_list.append((np.sqrt(diff), j))
            distance_array.append(distance_list)
        return distance_array

    def array_sorting(self):
        distance = self.distance_between_points()
        for i in range(len(distance)):
            distance[i].sort()
        return distance

    def getting_intermediate_y(self):
        sorted_distance = self.array_sorting()
        real_y_array = []
        for i in sorted_distance:
            temporal_array = []
            for j in range(self.k):
                temporal_array.append(i[j][1])
            real_y_array.append(temporal_array)
        return real_y_array

    def getting_appropriate_y(self):
        real_y = self.getting_intermediate_y()
        appropriate_y = []
        for i in real_y:
            temporal_array = []
            for j in i:
                temporal_array.append(self.Y[j])
            appropriate_y.append(temporal_array)
        return appropriate_y

    def getting_real_y(self):
        appropriate_y = self.getting_appropriate_y()
        real_y = []
        for i in range(len(appropriate_y)):
            real_y.append(max(appropriate_y[i], key=appropriate_y[i].count))
        return real_y

    def getting_epsilon(self):
        real_y = self.getting_real_y()
        Y = self.Y[self.parents_row:]
        diff = 0
        for i in range(len(real_y)):
            diff += (Y[i] - real_y[i]) ** 2
        return np.sqrt((1/(self.row * 0.2)) * diff)


row = 10
colum = 3
y = np.array([0, 1, 1, 0, 1, 0, 0, 0, 1, 1])
k = 3
x1 = np.array([5, 3, 0, 1, 1, 4, 5, 3, 2, 0])
x2 = np.array([0, 2, 3, 4, 1, 2, 3, 2, 1, 0])
x3 = np.array([0, 1, 3, 2, 0, 2, 1, 3, 2, 0])

X = FruitOrVegetable(row, colum, y, k, x1, x2, x3)
print("Our_Matrix = ", X.X)
print("Distance_between_points", X.distance_between_points())
print("Sorted_Array", X.array_sorting())
print("Intermediate_y = ", X.getting_intermediate_y())
print("Appropriate_y = ", X.getting_appropriate_y())
print("Real_Y = ", X.getting_real_y())
print("Epsilon = ", X.getting_epsilon())
