import math

def length(x1, y1, x2, y2):
    return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)

a = 360
b = 270
fi_rad = [] # Хранятся значения углов (в радианах) для каждого количества игроков
fi_grad = [] # Хранятся значения углов (в градусах) для каждого количества игроков
count_of_points = [] # Количество точек для каждого значения угла
x = [] # Хранятся значения х для каждого угла
y = [] # Хранятся значения y для каждого угла
result_points = [] # Хранятся результирующие значения точек для центров фигур

length = 5

for i in range(length):
    count_of_points.append((i + 4) * 2)
    fi_grad.append(360 / (i + 4))
    fi_rad.append(fi_grad[i] / 180 * math.pi)

# print(count_of_points)
print('Углы в градусах: ', fi_grad)
# print(fi_rad)

for i in range(length):
    temp_x = []
    temp_y = []
    points1 = []
    for j in range(count_of_points[i] + 1):
        angle = (-math.pi / 2) + (j + 1) * (fi_rad[i] / 2)
        print('angle_grad = ', angle / math.pi * 180)
        print('x = ', a * math.cos(angle))
        print('y = ', b * math.sin(angle))
        temp_x.append(a * math.cos(angle))
        temp_y.append(b * math.sin(angle))
        if((j != 0) and (j % 2 == 0)):
            point1_x = temp_x[j - 1] / 3
            point1_y = temp_y[j - 1] / 3

            # point2_x = ((2 / 3) * (temp_x[j - 2]) + (2 / 3) * (temp_x[j])) / 3
            # point2_y = ((2 / 3) * (temp_y[j - 2]) + (2 / 3) * (temp_y[j])) / 3

            # point2_x = (temp_x[j - 2] - temp_x[j]) / 3 + temp_x[j]
            # point2_y = (temp_y[j - 2] - temp_y[j]) / 3 + temp_y[j]

            point2_x = ((2 / 3) * temp_x[j - 2] - (2 / 3) * temp_x[j]) / 3 + (2 / 3) * temp_x[j]
            point2_y = ((2 / 3) * temp_y[j - 2] - (2 / 3) * temp_y[j]) / 3 + (2 / 3) * temp_y[j]

            # point3_x = ((2 / 3) * (temp_x[j - 2]) + (2 / 3) * (temp_x[j])) * 2 / 3
            # point3_y = ((2 / 3) * (temp_y[j - 2]) + (2 / 3) * (temp_y[j])) * 2 / 3

            # point3_x = (temp_x[j - 2] - temp_x[j]) * 2 / 3 + temp_x[j]
            # point3_y = (temp_y[j - 2] - temp_y[j]) * 2 / 3 + temp_y[j]

            point3_x = ((2 / 3) * temp_x[j - 2] - (2 / 3) * temp_x[j]) * 2 / 3 + (2 / 3) * temp_x[j]
            point3_y = ((2 / 3) * temp_y[j - 2] - (2 / 3) * temp_y[j]) * 2 / 3 + (2 / 3) * temp_y[j]

            points1.append([(point1_x, point1_y), (point2_x, point2_y), (point3_x, point3_y)])

    print()
    result_points.append(points1)
    x.append(temp_x)
    y.append(temp_y)

# print(result_points)

for i in range(len(result_points)):
    print('Для угла в ' + str(fi_grad[i]) + ' градусов точки будут следующие:')
    for j in range(len(result_points[i])):
        print('Точка ' + str(j) + ': ', str(result_points[i][j]))