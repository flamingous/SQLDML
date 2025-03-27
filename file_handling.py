import numpy as np

#load data, handling missing values
data = np.genfromtxt("loans.csv", delimiter=",", skip_header=1, usecols=8)
# print(data)

#remove missing values
loan_amounts = data[~np.isnan(data)]
print(loan_amounts)

#compute basic statistics
mean_loan = np.mean(loan_amounts)
print(mean_loan)

#calculate median
median_loan = np.median(loan_amounts)
print(median_loan)

#calculate standard deviation
std_loan = np.std(loan_amounts)
print(std_loan)