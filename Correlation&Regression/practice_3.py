import math as mt
import statistics as stat

def calculate_mean(alist, blist):
    return stat.mean(alist), stat.mean(blist)
    
def calculate_slope(alist, blist, amean, bmean):
    a_dev = [x - amean for x in alist]
    b_dev = [y - bmean for y in blist]
    dev_prod = [round(m*n,2) for m,n in zip(a_dev, b_dev)]
    sum_dev_prod = sum(dev_prod)
    b_dev_sq_sum = sum([k*k for k in a_dev])
    value = sum_dev_prod/b_dev_sq_sum
    return value
    
def calculate_intercept(slope, amean, bmean):
    return bmean-(slope*amean)
    
    
def main():

    phy_list = [15,12,8,8,7,7,7,6,5,3]
    his_list = [10,25,17,11,13,17,20,13,9,15]
    phy_mean, his_mean = calculate_mean(phy_list, his_list)
    beta_slope = calculate_slope(phy_list, his_list, phy_mean, his_mean)
    beta_intercept = calculate_intercept(beta_slope, phy_mean, his_mean)
    his_pred_score = beta_intercept+(beta_slope*10)
    print(round(his_pred_score, 1))
    
if __name__ == "__main__":
    main()
    
