import matplotlib.pyplot as plt
from Plot import initial_plot
from LinearRegression import LinearRegression
import pandas as pd

if __name__ == "__main__":
    initial_plot()

    linreg = LinearRegression(learning_rate=0.01, epochs=10000)
    df = pd.read_csv("data.txt", sep=",")
    X_train = df.iloc[:, 0]
    X_train = X_train.to_numpy().reshape(96, 1)
    y_train = df.iloc[:, 1]
    y_train = y_train.to_numpy().reshape(96, 1)
    y_predicted = linreg.fit(X_train, y_train)
    print("theta_1: ", linreg.theta_1)
    print("theta_0: ", linreg.theta_0)
    X_test = [3.5000, 7.0000]
    predictions = linreg.predict(X_test[0])
    print("predictions for 3.5000: ", predictions)

    predictions = linreg.predict(X_test[1])
    print("predictions for 7.0000: ", predictions)

    plt.figure(0)
    plt.plot(X_train, y_predicted, c="blue", linewidth=0.5, label="Linear Regression")
    plt.legend(loc="lower right")
    plt.savefig('final_plot.png')
