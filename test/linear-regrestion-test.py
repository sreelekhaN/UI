# add source to path
import sys
sys.path.insert(0, '../')


from lr_functions import main

if __name__ == "__main__" :
	main("data/multivariate-date.csv","Salary","Education=16","Experience=5","Hours per week=50")