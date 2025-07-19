# 🌿 Decision Tree Classifier: Iris Dataset

This project applies a **Decision Tree classifier using scikit-learn**
to classify **Iris flower species** based on sepal and petal features.
It includes model training, evaluation, and a colorful 2D plot
visualizing predictions against actual training samples.

---

## 📦 Project Structure

```
📁 decision_tree.py                – Script for loading data, training model,
                                    evaluating, and visualizing results  
📁 README.md                       – Project overview and instructions  
```

---

## 🔧 Installation

Ensure Python 3 is installed along with the required packages:

```bash
pip install numpy pandas matplotlib scikit-learn
```

---

## 🚀 Getting Started

### ⚙️ Run the Script

1. Update the dataset path in `decision_tree.py`:
   ```python
   dataset = pd.read_csv("path/to/Iris.csv")
   ```
2. Then run the script:
   ```bash
   python decision_tree.py
   ```

---

## 🧠 What This Script Does

- Loads the Iris dataset from a local CSV file
- Splits the data into training and testing sets
- Trains a Decision Tree Classifier (`sklearn.tree.DecisionTreeClassifier`)
- Evaluates performance using a confusion matrix and classification report
- Plots training and predicted test samples using sepal length and width

---

## 🌼 Dataset Info

The [Iris dataset](https://archive.ics.uci.edu/ml/datasets/iris)
contains 150 samples from three classes:
- *Iris Setosa*
- *Iris Versicolor*
- *Iris Virginica*

Each sample includes:
- Sepal length (cm)
- Sepal width (cm)
- Petal length (cm)
- Petal width (cm)

---

## 📊 Sample Output

```
Confusion Matrix:
[[10  0  0]
 [ 0 11  1]
 [ 0  1  7]]

Classification Report:
                 precision    recall  f1-score   support

    Iris-setosa       1.00      1.00      1.00        10
Iris-versicolor       0.92      0.92      0.92        12
 Iris-virginica       0.88      0.88      0.88         8

      accuracy                           0.93        30
     macro avg       0.93      0.93      0.93        30
  weighted avg       0.93      0.93      0.93        30
```

---

## 📈 Visualization

A 2D scatter plot is generated to show how:
- Training data points cluster by species  
- Test data points are classified by the model  

X-axis: Sepal Length  
Y-axis: Sepal Width  

Each species and predicted point has a distinct color and shape.

---

## 🔖 Tags

`#MachineLearning` `#DecisionTree` `#IrisDataset` `#Python`  
`#ScikitLearn` `#Visualization` `#DataScience`
