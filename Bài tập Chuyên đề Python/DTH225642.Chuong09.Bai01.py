from __future__ import print_function
import numpy as np
from sklearn import datasets, linear_model



def main():

    heights = np.array([[147,150,153,158,163,165,168,170,173,175,178,180,183]]).T

    weights = np.array([49,50,51,54,58,59,60,62,63,64,66,67,68])

    one = np.ones((heights.shape[0], 1))

    Xbar = np.concatenate((one, heights), axis=1)

    A = np.dot(Xbar.T, Xbar)
    b = np.dot(Xbar.T, weights)
    w = np.dot(np.linalg.pinv(A), b)

    regr = linear_model.LinearRegression()

    regr.fit(heights, weights)

    print("scikit-lean's solution:w_1=", regr.coef_[0], "w_0=", regr.intercept_)
    print("our solution : w_1 = ", w[1], "w_0=", w[0])
    yourHeight = int(input("Input your height:"))
    yourWeight = regr.coef_[0] * yourHeight+regr.intercept_
    print("Your height is ", yourHeight, ", I predict your weight is", yourWeight, "kg")
if __name__ == "__main__":
    main()