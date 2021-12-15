import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import random

'''
Note: All features in house can be accessed either by going through self.features or by typing House.<feature>. The 
first is implemented for ease of use for Train.pred() and the rest are for questions 2-4 to make them easier.
'''


class House:
    def __init__(self, lis):
        self.features = lis
        self.featurelength = len(lis) - 2
        self.predPrice = 0  # predicted price, will be calculated through Train.pred()

        # all variables the model needs without all the features
        self.totalBsmtSF = lis[8]
        self.grLivAr = lis[12]
        self.fullBath = lis[14]
        self.bedroomAbvGr = lis[16]
        self.price = lis[26]


class Train:
    def __init__(self, alpha):
        self.trainingData = []
        self.meanPrice = 0
        self.maxPrice = 0
        self.minPrice = 0
        self.length = 0
        self.stdDev = 0
        self.W = []
        self.MSE = 0
        self.X = np.zeros((25, 818), dtype=float)
        self.deltaMSE = []
        self.alpha = alpha

    def setTrainingData(self, filename):

        with open(filename) as f:  # opening csv
            for i, line in enumerate(f.readlines()):
                if i != 0:  # skipping first line

                    temp = line.split(',')
                    temp = [float(k) for k in temp]  # changing all string taken from filename into float

                    self.trainingData.append(House(temp))  # adding house to trainingData

                    self.X[:, i - 1] = temp[1:len(temp) - 1]  # adding temp to list of all X

        self.length = len(self.trainingData)
        self.W = [random.random() for i in range(len(temp) - 2)]  # randomly initializing W

    def questionTwo(self):
        mean = 0
        max, min = self.trainingData[0].price, self.trainingData[0].price  # setting initial value for max, min

        for house in self.trainingData:  # finding mean, max, and min in for loop

            mean += house.price

            if house.price > max:
                max = house.price
            if house.price < min:
                min = house.price

        mean = mean / self.length  # dividing mean by amount of indexes added to mean

        self.meanPrice = mean  # setting meanPrice to mean

        self.maxPrice = max
        self.minPrice = min

        self.findStdDev()

    def findStdDev(self):  # finding standard deviation
        sum = 0

        for house in self.trainingData:
            sum += (house.price - self.meanPrice) ** 2

        self.stdDev = np.sqrt(sum / self.length)

    def questionThree(self):
        prices = [house.price for house in self.trainingData]

        # plotting histogram and adding title, axis labels

        plt.hist(prices, bins=[0.1 * i * self.maxPrice for i in range(10)], edgecolor='black')

        plt.title("Project 3 Question 3: Plotting Histogram of\nSales Prices of Training Set", fontsize=22)
        plt.ylabel("Number of houses", fontsize=18)
        plt.xlabel("Price Index (x$100,000)", fontsize=18)

        plt.show()

    def questionFour(self):
        # correlation between Garage Living Area and Bedroom Above Garage
        grLivAr = [house.grLivAr for house in self.trainingData]
        bedAbvGr = [house.bedroomAbvGr for house in self.trainingData]

        # correlation between Total Basement and Full Bathroom
        totBsmtSF = [house.totalBsmtSF for house in self.trainingData]
        fullBath = [house.fullBath for house in self.trainingData]

        scatter = np.transpose(np.array([grLivAr, bedAbvGr, totBsmtSF, fullBath]))

        # plotting scatter plots

        # creating data frame for scatter plot using pandas
        df = pd.DataFrame(scatter, columns=["GrAr(ft^2)", "# BedAbvGr", "BsmtAr (ft^2)", "# full bath"])

        # creating data plot
        sm = scatter_matrix(df, alpha=1, figsize=(6, 6))

        for ax in sm.ravel():  # changing axis label size
            ax.set_xlabel(ax.get_xlabel(), fontsize=18)
            ax.set_ylabel(ax.get_ylabel(), fontsize=18)

        plt.show()

    def pred(self):
        for house in self.trainingData:
            house.predPrice = 0  # setting to 0 every time so not accidentally added to last total

            for i in range(house.featurelength):
                # creating predPrice based on current weights and feature vals
                house.predPrice += self.W[i] * house.features[i + 1]

    def loss(self):  # finding MSE of model
        sum = 0

        for house in self.trainingData:
            sum += (house.predPrice - house.price) ** 2

        self.MSE = sum / self.length

    def gradient(self):  # finding deltaMSE
        lis = [0 for j in range(self.length)]  # initializing list for house predicted price vs actual

        for i, house in enumerate(self.trainingData):  # YPred-Y
            lis[i] += house.predPrice - house.price

        self.deltaMSE = np.multiply(np.dot(self.X, lis), (2 / self.length))  # getting deltaMSE

    def update(self):  # updating W

        self.W = [self.W[i] - self.alpha * self.deltaMSE[i] for i in range(len(self.W))]


if __name__ == '__main__':  # for all questions to make easier for user and creator
    proj3 = Train(0.2)
    proj3.setTrainingData("train.csv")

    proj3.questionTwo()

    print("\n-------- question 2 -------- ")
    print(f"Length of training set: {proj3.length}")
    print(f"Mean price for house: {proj3.meanPrice}")
    print(f"Max price of house in training set: {proj3.maxPrice} \n"
          f"Min price of house in training set: {proj3.minPrice}")
    print(f"Standard deviation of training set price: {proj3.stdDev}")

    print("\n-------- question 3 -------- ")
    # proj3.questionThree()

    print("\n-------- question 4 -------- ")
    proj3.questionFour()

    print("\n-------- question 5 -------- ")
    proj3.pred()

    print("\n-------- question 6 -------- ")
    proj3.loss()
    print(f"MSE of initial W: {proj3.MSE}")

    print("\n-------- question 7 -------- ")
    proj3.gradient()

    print("\n-------- question 8 -------- ")
    proj3.update()

    print("\n-------- question 11 -------- ")

    minus11 = Train(10 ** -8)
    minus11.setTrainingData("train.csv")
    w = minus11.W
    minus11lis = []
    for i in range(500):
        minus11.pred()
        minus11.loss()
        minus11.gradient()
        minus11.update()
        minus11lis.append(minus11.MSE)
    print(f"MSE (alpha = 10^-8): {minus11.MSE}")

    minus12 = Train(10 ** -9)
    minus12.setTrainingData("train.csv")
    minus12.W = w
    minus12lis = []
    for j in range(500):
        minus12.pred()
        minus12.loss()
        minus12.gradient()
        minus12.update()
        minus12lis.append(minus12.MSE)
    print(f"MSE (alpha = 10^-9): {minus12.MSE}")

    x = [i + 1 for i in range(500)]
    plt.plot(x, minus11lis, x, minus12lis)
    plt.legend(["alpha = 10^-8", "alpha=10^-9"])
    plt.title("ECE241 Project 3: Seeing the amount of time it takes \ndifferent alpha values to converge", fontsize=24)
    plt.ylabel("MSE", fontsize=18)
    plt.xlabel("Number of iterations", fontsize=18)
    plt.show()

    print("\n-------- question 13 -------- ")
    test = Train(10 ** -8)
    test.setTrainingData("test.csv")
    test.W = minus11.W
    test.pred()
    test.loss()
    print(f"MSE of test data (alpha = 10^-8): {test.MSE}")
