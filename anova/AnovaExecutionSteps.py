## Following steps needs to be followed by integration team.

#### This class describes how to use Functions Defined in Anova_Functions.py File

from Anova_Functions_Main import *

## There are 2 Main methods in Anova_Function.Py file:
## 1. To calculate F-Statistic Values- Method Name: calculate_f_statistic()
## 2. To Compare Models and Output Best Models- Method Name: compare_and_choose_best_model()

#### CASE 1: IF ONLY ANOVA F-Statistic VALUES ARE REQUIRED

## Step-1: Create the Required Inputs
x_arr = [1,2,3,4,5,6,7,8,9,10]
y_arr = [7.5,44.31,60.8,148.97,225.5,262.64,289.06,451.53,439.62,698.88]
alpha_value = 0.05

# Create Input Regression Model Object with required coefficient array
model = RegressionModel()
model.coeff_arr = [5.4, 9.6, 1.79]

## INPUT FORMAT FOR COEFF_ARR
# if equation is: y = 5x + 4, then degree = 1, coeff_arr = [5, 4]
# if equation is: y = 5x^2 + 3x + 4, then degree = 2, coeff_arr = [5, 3, 4]
# if equation is: y = 5x^2 + 4, it should be considered as: y=5x^2 + 0.x + 4, then degree = 2, coeff_arr = [5, 0, 4]
# Note: All coefficients irrespective of being 0 should be provided in proper order like shown in last example

# Step-2: Create an Object of Anova Class and call the calculate_f_statistic() method with input values
anova = Anova()
response = anova.calculate_f_statistic(x_arr, y_arr, model, alpha_value)

# To see or access output f-statistic values, just access fields via reponse object as given below
print("SSE: ", response.sse)
print("SSR: ", response.ssr)
print("MSE: ", response.mse)
print("MSR: ", response.msr)
print("F: ", response.f)
print("P: ", response.p)
print("Is Result Significant: ", response.isSignificant)


print("-------------------------------------------------------------------------------------------")


#### CASE 2: TO COMPARE MODELS

## Step-1: Create the Required Inputs as done in previous case as well
x_arr = [1,2,3,4,5,6,7,8,9,10]
y_arr = [7.5,44.31,60.8,148.97,225.5,262.64,289.06,451.53,439.62,698.88]
alpha_value = 0.05

# Create Input Regression Model Objects which needs to be compared, with required values and create array of models
model_1 = RegressionModel()
model_1.coeff_arr = [69.09, -117.14]

model_2 = RegressionModel()
model_2.coeff_arr = [5.4, 9.6, 1.79]

models_arr = []
models_arr.append(model_1)
models_arr.append(model_2)

# Step-2: Create an Object of Anova Class and call the compare and compare_and_choose_best_model() method with input values
anova = Anova()
best_model_arr_index = anova.compare_and_choose_best_model(x_arr, y_arr, models_arr, alpha_value)
print("best model in given array is model at index: ", best_model_arr_index)