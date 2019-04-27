import csv
import os
import matplotlib.pyplot as plt
from ACF import get_correlogram

package_dir = os.path.dirname(os.path.abspath(__file__))
thefile = os.path.join(package_dir,'data/univariate.csv')

Y_axis_time_series_data = []
X_axis_time = []

with open (thefile) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        Y_axis_time_series_data.append(float(row["sales"]))
        line_count += 1


print(Y_axis_time_series_data)


def get_correlogram_integration():
	number_of_lags = 20
	Y_axis_ACF = get_correlogram(Y_axis_time_series_data, number_of_lags)
	for i in range(1, len(Y_axis_time_series_data) + 1):
		X_axis_time.append(i)
	X_axis_lag = []
	for i in range(1, number_of_lags + 1):
		X_axis_lag.append(i)
	plt.step(X_axis_lag, Y_axis_ACF)
	plt.show()


get_correlogram_integration()