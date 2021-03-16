import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

# reading data and separating into features and labels
dataset = pd.read_csv(r"D:/Usman/Data Science/The Sparks Foundation/"
                      r"Task 6/Iris.csv")
print(dataset.head())
x = dataset.drop('Species', axis=1)
y = dataset["Species"]

# training the model
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
decision_tree = DecisionTreeClassifier()
decision_tree.fit(x_train, y_train)

# making predictions and evaluating the model
y_predict = decision_tree.predict(x_test)
print(confusion_matrix(y_test, y_predict))
print(classification_report(y_test, y_predict))

# converting df to np array
y_train = np.array(y_train)
x_train = np.array(x_train)
y_predict = np.array(y_predict)
x_test = np.array(x_test)

# plotting train and test set

plt.figure(figsize=(16, 8))

plt.scatter(x_train[y_train == "Iris-setosa", 0],
            x_train[y_train == "Iris-setosa", 1], c="lightgreen", marker="o",
            label="Iris-Setosa")
plt.scatter(x_train[y_train == "Iris-versicolor", 0],
            x_train[y_train == "Iris-versicolor", 1], c="lightblue", marker="s",
            label="Iris-Versicolor")
plt.scatter(x_train[y_train == "Iris-virginica", 0],
            x_train[y_train == "Iris-virginica", 1], c="yellow", marker="v",
            label="Iris-Virginica")

plt.scatter(x_test[y_predict == "Iris-setosa", 0],
            x_test[y_predict == "Iris-setosa", 1], c="green", marker="o",
            label="Predicted Iris-Setosa")
plt.scatter(x_test[y_predict == "Iris-versicolor", 0],
            x_test[y_predict == "Iris-versicolor", 1], c="blue", marker="s",
            label="Predicted Iris-Versicolor")
plt.scatter(x_test[y_predict == "Iris-virginica", 0],
            x_test[y_predict == "Iris-virginica", 1], c="orange", marker="v",
            label="Predicted Iris-Virginica")

plt.xlabel("Sepal Length cm")
plt.ylabel("Sepal Width cm")
plt.legend()
plt.title("Training set clusters")
plt.show()
