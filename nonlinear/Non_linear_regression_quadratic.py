import matplotlib.pyplot as plt
import numpy as np

def list_powered(list, exponent):
    return [(element ** exponent) for element in list]

def lists_multiplied(list1, list2):
    return [a*b for a,b in zip(list1,list2)]

def fit_non_regression_quadratic_equation(X, Y):
    X_squared = list_powered(X, 2)
    X_cubed = list_powered(X, 3)
    X_to_the_power_4 = list_powered(X, 4)
    XY = lists_multiplied(X, Y)
    X_squared_Y = lists_multiplied(X_squared, Y)
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
    return solved_parameters

def get_non_linear_quadratic_estimated_values_of_y(solved_parameters, X):
    x = np.array(X)
    return get_non_linear_quadratic_estimated_value_of_y(solved_parameters, x)

def get_non_linear_quadratic_estimated_value_of_y(solved_parameters, x):
    return solved_parameters[0] * x ** 2 + solved_parameters[1] * x + solved_parameters[2]    

def fit_non_regression_quadratic_equation_test():
    Y = [7.5,44.31,60.8,148.97,225.5,262.64,289.06,451.53,439.62,698.88] 
    X = [1,2,3,4,5,6,7,8,9,10] 
    solved_parameters = fit_non_regression_quadratic_equation(X, Y)
    Y_hat = get_non_linear_quadratic_estimated_values_of_y(solved_parameters, X)
    plt.scatter(X, Y)
    plt.plot(X, Y_hat)
    plt.show()
    print("y = m1 x^2 + m2 x + c")
    print('y = {0} x^2 + {1} x + {2}'.format(solved_parameters[0], solved_parameters[1], solved_parameters[2]))
    print(get_non_linear_quadratic_estimated_value_of_y(solved_parameters, 5))

# fit_non_regression_quadratic_equation_test()