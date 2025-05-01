# Given the test scores of 10 students in Physics and History, compute the slope of the regression line obtained by treating Physics as the independent variable. The result should be rounded to three decimal places.

# The scores to use:

# Physics Scores  15  12  8   8   7   7   7   6   5   3
# History Scores  10  25  17  11  13  17  20  13  9   15
# Slope of a regression line

# Where:

 # is the slope of the regression line,
 # and  are the data points,
 # and  are the means of the -values and -values, respectively,
 # is the number of data points.
# Output Format

# In the text box, enter the floating point/decimal value required. Do not leave any leading or trailing spaces. Your answer may look like: 0.255

# This is NOT the actual answer - just the format in which you should provide your answer.

# Enter your code here. Read input from STDIN. Print output to STDOUT# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics as stat
import math as np

def multiply(a, b):
    return [x*y for x,y in zip(a,b)]
    
def square(a):
    #print("Value: ", a)
    return [x ** 2 for x in a]
    
phy_score_x = [15,12,8,8,7,7,7,6,5,3]
history_score_y = [10,25,17,11,13,17,20,13,9,15]

x_mean =  stat.mean(phy_score_x)
y_mean = stat.mean(history_score_y)

xi_xbar = [x - x_mean for x in phy_score_x]
yi_ybar = [y - y_mean for y in history_score_y]
  
numerator = sum(multiply(xi_xbar, yi_ybar))
denominator = sum(square(xi_xbar))

coefficient = numerator/denominator
print(round(coefficient,3))

    
