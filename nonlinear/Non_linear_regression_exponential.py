import math
import numpy as np
import matplotlib.pyplot as plt

def list_powered(list, exponent):
    return [(element ** exponent) for element in list]

def lists_multiplied(list1, list2):
    return [a*b for a,b in zip(list1,list2)]

def list_log(list):
    return [math.log(element, 10) for element in list]

def fit_linear_equation(X, Y):
    X_squared = list_powered(X, 2)
    XY = lists_multiplied(X, Y)
    #Summation of (y = m x + nc)
    # sum(Y) = m sum(X) + c len(X) 
    first_equation_parameters = [sum(X), len(X)]
    first_equation_value = sum(Y)

    #Summation of (xy = m x_squared + c x)
    #sum(XY) = m sum(X_squared) + c sum(X)
    second_equation_parameters = [sum(X_squared), sum(X)]
    second_equation_value = sum(XY)
    
    parameters = np.array([first_equation_parameters, second_equation_parameters])
    values = np.array([first_equation_value, second_equation_value])
    solved_parameters = np.linalg.solve(parameters, values)
    return solved_parameters

def get_non_linear_exponential_estimated_value_of_y(a, b, x):
    return a * (b ** x)    

def get_non_linear_exponential_estimated_values_of_y(a, b, X):
    x = np.array(X)
    return get_non_linear_exponential_estimated_value_of_y(a,b,x)

def fit_non_regression_exponential_equation(X, Y):
    log_Y = list_log(Y)
    transformed_Y = log_Y
    solved_parameters = fit_linear_equation(X, transformed_Y)
    b = math.pow(10, solved_parameters[0])
    a = math.pow(10, solved_parameters[1])
    return a, b
    
def fit_non_regression_exponential_equation_test():
    Y = [7.5,44.31,60.8,148.97,225.5,262.64,289.06,451.53,439.62,698.88]
    X = [1,2,3,4,5,6,7,8,9,10] 
    a, b = fit_non_regression_exponential_equation(X, Y)
    Y_hat = get_non_linear_exponential_estimated_values_of_y(a, b, X)
    plt.scatter(X, Y)
    plt.plot(X, Y_hat)
    plt.show()
    print('a.b^x')
    print('y = {0} * {1} ^x '.format(a,b))
    print(get_non_linear_exponential_estimated_value_of_y(a, b , 5.5))

# fit_non_regression_exponential_equation_test()

