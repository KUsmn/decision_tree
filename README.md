# 🌿 Decision Tree Classifier: Iris Dataset

This project demonstrates a **from-scratch implementation** of a
Decision Tree classifier to predict **Iris flower species** using
petal and sepal dimensions. It’s designed as a learning resource
to understand how decision trees work under the hood.  

## 📦 Project Structure

```
📁 Decision_Tree_Algorithm.ipynb   – Walkthrough with visualizations  
📁 decision_tree.py                – Clean script version for reuse  
📁 README.md                       – Project overview and instructions  
```

---

## 🔧 Installation

You’ll need Python 3 and the following libraries:

```bash
pip install numpy pandas matplotlib scikit-learn
```

Alternatively, run the notebook in [Google Colab](https://colab.research.google.com/)
to avoid local setup.

---

## 🚀 Getting Started

### 🧪 Run the Notebook

For learning and exploration:

```bash
jupyter notebook Decision_Tree_Algorithm.ipynb
```

You'll see a step-by-step breakdown of:
- How the data is loaded and preprocessed
- How splits are calculated (Gini index)
- How the decision tree is built and used for prediction
- Visual analysis of the decision boundaries

---

### ⚙️ Run the Script

For quick classification using the same logic:

```bash
python decision_tree.py
```

The script:
- Loads the Iris dataset
- Trains the model
- Prints accuracy and predictions

You can adapt it to any other dataset with minor tweaks.

---

## 🧠 Why This Project?

Instead of relying on black-box classifiers like
`sklearn.DecisionTreeClassifier`, this project
**builds the tree from scratch**:

- Split selection via Gini Index  
- Recursive tree building  
- Manual prediction function  
- Clear structure for visualization and debugging  

This approach gives deep insight into how tree-based models
learn from data and make decisions.

---

## 🌼 Dataset Info

We use the famous [Iris dataset](https://archive.ics.uci.edu/ml/datasets/iris),
which contains 150 flower samples from three species:

- *Iris Setosa*
- *Iris Versicolor*
- *Iris Virginica*

Each sample includes 4 features:
- Sepal length  
- Sepal width  
- Petal length  
- Petal width  

---

## 📊 Example Output

```
Model accuracy: 96.7%

Confusion Matrix:
[[19  0  0]
 [ 0 17  1]
 [ 0  1 17]]
```

You can also visualize the decision boundaries using `matplotlib`
in the notebook.

---

## 🔁 Customize for Your Dataset

To use a different dataset:
- Replace the CSV/file loading section  
- Adjust feature and label selection  
- Tune depth or stopping conditions if needed  
- Update plots and labels to fit your domain  

The implementation is modular and easy to adapt.

---

## 🧑‍💻 Author

Built by [Your Name](https://github.com/yourusername)

I created this project to sharpen my ML fundamentals,
practice algorithmic thinking, and provide a clean
starting point for others learning machine learning.

---

## 🔖 Tags

#MachineLearning `#DecisionTree` `#IrisDataset` `#Python` `#FromScratch`  
`#DataScience` `#JupyterNotebook` `#Educational`
