import math
import numpy as np
import matplotlib.pyplot as plt


#Task_1
my_list = [92, 94, 88, 91, 87]
test_1 = np.array(my_list)
#Task_2
test_2 = np.genfromtxt('test_2.csv', delimiter=',')
#Task_3
test_3 = np.array([87, 85, 72, 90, 92])
test_3_fixed = test_3 + 2
#Task_4
total_grade = (test_1 + test_2 + test_3_fixed) / 3
#так же можно использовать // для целочисленного деления но в задании это не указано
print('задание 4 ',total_grade)
#Task_5
coin_toss = np.array(['1', '0', '0', '1', '0'])
coin_toss_again = np.array([coin_toss, ['0', '0', '1', '1', '1']])
#Task_6
jeremy_test_2 = test_2[3]
manual_adwoa_test_1 = test_1[1:3]
#Task_7
student_scores = np.array([[92, 94, 88, 91, 87],
                           [79, 100, 86, 93, 91],
                           [87, 85, 72, 90, 92]])
tanya_test_3 = student_scores[2, 0]
cody_test_scores = student_scores[:, 4]
#Task_8
array_temperature = np.genfromtxt('temperature_data.csv', delimiter=',')
print('Проверка в задании 8', array_temperature)
temperature_fixed = array_temperature + 3
monday_temperas = temperature_fixed[0, :]
thursday_friday_morning = temperature_fixed[3:5, 1]
print('чт-пт', thursday_friday_morning)
a = temperature_fixed
temperature_extremes = sorted(a[(a < 50) | (a > 60)])


#Task_9
def archimed_spiral():
    n = np.array([n for n in range(0, 97)])
    fi = (n * math.pi) / 12
    x = fi * np.cos(fi)
    y = fi * np.sin(fi)
    x_y_plot = plt.plot(x, y)
    plt.show()

def pascal_snail():
    n = np.array([n for n in range(0, 25)])
    fi = (n * math.pi) / 12
    x = 2 * np.cos(fi) ** 2 + np.cos(fi)
    y = 2 * np.cos(fi) * np.sin(fi) + np.sin(fi)
    x_y_plot = plt.plot(x, y)
    plt.show()

def distance(lat_1, lon_1, lat_2, lon_2):
    r = 6371
    mas = np.array([lat_1, lon_1, lat_2, lon_2])
    lat_1, lon_1, lat_2, lon_2 = np.radians(mas)
    formula = 2 * r * np.arcsin(np.sqrt(np.sin((lat_2 - lat_1) / 2) ** 2 + np.cos(lat_1) * np.cos(lat_2) * np.sin((lon_2 - lon_1) / 2) ** 2))
    return np.round(formula, 1)

print(distance(57.37, 39.51, 57.46, 40.55))