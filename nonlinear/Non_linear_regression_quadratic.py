import matplotlib.pyplot as plt
import numpy as np

Y = [7.5,44.31,60.8,148.97,225.5,262.64,289.06,451.53,439.62,698.88] 
X = [1,2,3,4,5,6,7,8,9,10] 

# plt.scatter(X,Y)
# plt.show()

def list_powered(list, exponent):
    return [(element ** exponent) for element in list]

def lists_multiplied(list1, list2):
    return [a*b for a,b in zip(list1,list2)]

X_squared = list_powered(X, 2)
print(X_squared)

X_cubed = list_powered(X, 3)
print(X_cubed)

X_to_the_power_4 = list_powered(X, 4)
print(X_to_the_power_4)

XY = lists_multiplied(X, Y)
print(XY)

X_squared_Y = lists_multiplied(X_squared, Y)
print(X_squared_Y)

#Summation of (y = m1 x_squared + m2 x + nc)
# sum(Y) = m1 sum(X_squared) + m2 sum(X) + c len(X) 
first_equation_parameters = [sum(X_squared), sum(X), len(X)]
first_equation_value = sum(Y)

#Summation of (xy = m1 x_cubed + m2 x_squared + cx)
#sum(XY) = m1 sum(X_cubed) + m2 sum(X_squared) + c sum(X)
second_equation_parameters = [sum(X_cubed), sum(X_squared), sum(X)]
second_equation_value = sum(XY)

#Summation of (x_squared_y = m1 x_to_the_power_4 + m2 x_cubed + c x_squared)
#sum(X_squared_Y) = m1 sum(X_to_the_power_4) + m2 sum(X_cubed) + c sum(X_squared)
third_equation_parameters = [sum(X_to_the_power_4), sum(X_cubed), sum(X_squared)]
third_equation_value = sum(X_squared_Y)

parameters = np.array([first_equation_parameters, second_equation_parameters, third_equation_parameters])
values = np.array([first_equation_value, second_equation_value, third_equation_value])
solved_parameters = np.linalg.solve(parameters, values)
print(solved_parameters)

x = np.array(range(10))
Y_hat = solved_parameters[0] * x ** 2 + solved_parameters[1] * x + solved_parameters[2]
# plt.plot(x, Y_hat)
# plt.show()
