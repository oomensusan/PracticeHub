# Enter your code here. Read input from STDIN. Print output to STDOUT
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
denominator = np.sqrt(sum(square(xi_xbar))*sum(square(yi_ybar)))

coefficient = numerator/denominator
print(coefficient)

    
