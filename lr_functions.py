import numpy as np
import pandas as pd
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import operator
import math
import csv
import collections
import sys

CorrelationCoeff = collections.namedtuple('CorrelationCoeff', ['corr', 'isSignificant'])

def round_float(floatValue) :
	return round(floatValue, 2)
def sum_of_columns( dataSet, columnName) :
	return sum(dataSet[columnName])

def mean_of_column( dataSet, columnName) :
	return round_float(sum(dataSet[columnName])/len(dataSet))

def sum_of_x_minus_x_bar( dataSet, columnName) :
	mean = round_float(mean_of_column(dataSet, columnName))
	tempCol = dataSet[columnName]- mean
	return round_float(sum(tempCol))

def sum_of_squares( dataSet, columnName) :
	return round_float(sum(dataSet[columnName]**2))

def sum_of_muliplication_of_cols( dataSet, columnName1, columnName2) :
	return round_float(sum(dataSet[columnName1]*dataSet[columnName2]))

def standard_deviation(dataSet, columnName) :
	return round_float(math.sqrt(sum((dataSet[columnName]- mean_of_column(dataSet, columnName))**2)/(len(dataSet)-1)))


def covariance(dataSet, featureColumn, actualValueColumn) :
	x_min_xbar = dataSet[featureColumn]- mean_of_column(dataSet, featureColumn)
	y_min_ybar = dataSet[actualValueColumn]- mean_of_column(dataSet, actualValueColumn)
	cov_numerator = x_min_xbar * y_min_ybar
	cor_num = sum(cov_numerator)/(len(dataSet)-1)
	return round_float(cor_num)

def find_corr_coeff(dataSet, featureColumn, actualValueColumn) :
	cor_num = covariance(dataSet, featureColumn, actualValueColumn)
	standard_deviationOfFeatureColumn = standard_deviation(dataSet, featureColumn)
	standard_deviationOfValueColumn = standard_deviation(dataSet, actualValueColumn)
	cor_r = round_float((cor_num)/(standard_deviationOfFeatureColumn*standard_deviationOfValueColumn))
	return CorrelationCoeff(cor_r, (abs(cor_r) > (1.96/math.sqrt(len(dataSet)))))

def check_correlation_coeff(inputFile , valueColumn, *featureColumns ) :
	data = pd.read_csv(inputFile)
	print("--------------------------Correlation Coefficient ---------------------- ")
	for feature in featureColumns:
			corr_value = find_corr_coeff(data, feature, valueColumn)
			significant_stmt = "It is significant" if corr_value.isSignificant else "It is not significant"
			print ("Correlation Coefficient of feature column %s with value column %s is %s. %s." % (feature, valueColumn, corr_value.corr, significant_stmt))

# def find_parameters(inputFile, featureColumn, actualValueColumn) :
# 	# y = mx + c
# 	data = pd.read_csv(inputFile)
# 	r1c1 = sum_of_squares(data, featureColumn)
# 	r1c2 = sum_of_columns(data,featureColumn)
# 	r2c1 = sum_of_columns(data, featureColumn)
# 	r2c2 = len(data)
# 	A = np.array([[r1c1, r1c2],[r2c1, r2c2]])

# 	b1 = sum_of_muliplication_of_cols(data, featureColumn,actualValueColumn)
# 	b2 =  sum_of_columns(data, actualValueColumn)
# 	B = np.array([b1, b2]) 
	
# 	return np.linalg.solve(A, B)


def find_parameters_for_multivariate(inputFile, actualValueColumn, *featureColumn ) :
	# y = mx + c
	features = list(featureColumn)
	features.append("c")
	dataset = pd.read_csv(inputFile)
	data = dataset
	data["c"] = 1

	matrix = []
	i =0
	y_matrix = []
	while i < len(features) :
		row1 = []
		j=0
		while j < len(features) :
			row1.append(sum_of_muliplication_of_cols(data, features[i], features[j]))
			j+=1
		y_matrix.append(sum_of_muliplication_of_cols(data, features[i],actualValueColumn))
		matrix.append(row1)
		i+=1
	A = np.array(matrix)
	print("------------------------------------------------------------------------")
	print("Matrix for solving equations")
	print("A = \n", A)
	B = np.array(y_matrix) 
	print("B =", B)
	print("------------------------------------------------------------------------")
	params = np.linalg.solve(A, B)
	roundedParams = np.asarray([round_float(param) for param in params])
	build_anova_table(inputFile, params,actualValueColumn, *featureColumn)
	return roundedParams


def estimate_value(params, *featureValue) :
	parameters = params[:-1]
	output = (parameters.dot(featureValue)) + params[-1]
	return output

def build_anova_table(inputFile, params, targetColumn, *featureNames) :
	features = list(featureNames)
	features.append("c")
	dataSet = pd.read_csv(inputFile)
	dataSet["estimate_value"] = params[len(params)-1]
	i = 0
	while i < len(featureNames) :
		dataSet["estimate_value"] = dataSet["estimate_value"] + params[i] * dataSet[featureNames[i]]
		i = i+1
	dataSet["squaredError"] = (dataSet["estimate_value"] - dataSet[targetColumn])**2
	dataSet["squaredErrorRegression"] = (dataSet["estimate_value"] - mean_of_column(dataSet,targetColumn))**2
	SSE = sum(dataSet["squaredError"])
	SSR = sum(dataSet["squaredErrorRegression"])
	MSR = SSR / (len(params) -1)
	MSE = SSE / (len(dataSet) -len(params))
	F = MSR/MSE
	anovastats = pd.DataFrame(columns=('source', 'df', 'SS','MS','F'))
	anovastats["source"] = ["regression", "error" ," total"]
	anovastats["df"] = [len(params) -1, (len(dataSet) -len(params)), (len(dataSet) -1)]
	anovastats["SS"] = [SSR, SSE, SSE+SSR]
	anovastats["MS"] = [MSR, MSE, float('nan')]
	anovastats["F"] = [F, float('nan'),float('nan')]
	print("---------------------------Anova stats----------------------------------")
	print(anovastats)
	print("------------------------------------------------------------------------")

def main(inputFile, targetColumn, *featuresAndValue):
	features =[elem.split('=', 1)[0] for elem in featuresAndValue]
	values =[float(elem.split('=', 1)[1]) for elem in featuresAndValue]
	check_correlation_coeff(inputFile,targetColumn, *features)
	params = find_parameters_for_multivariate(inputFile,targetColumn,*features,)
	SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
	strval =""
	i = 0
	while i < len(params) -1 :
		strval = strval + str(params[i]) + "("+features[i]+")" + (" + " if params[i+1] >= 0 else " ")
		#strval = strval + str(params[i]) + "x" + str(i+1).translate(SUB) + "+ "
		i += 1
	strval  = strval + str(params[i])
	output = estimate_value(params, *values)
	print("Equation : ", strval )
	print("Output : ", output )

if __name__ == "__main__" :
	#main(sys.argv[1],sys.argv[2],sys.argv[3:])
	main("test/data/multivariate-date.csv","Salary","Education=16","Experience=5","Hours per week=50")
	


