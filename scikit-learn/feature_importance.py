import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

iris = load_iris()

X = iris["data"]
Y = iris["target"]
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=1)

rand_for = RandomForestClassifier(random_state=42, n_estimators=100)
rand_for.fit(x_train, y_train)

importances = rand_for.feature_importances_
std = np.std([tree.feature_importances_ for tree in rand_for.estimators_], axis=0)

forest_importances = pd.Series(importances, index=iris["feature_names"])
fig, ax = plt.subplots()
forest_importances.plot.bar(yerr=std, ax=ax)
ax.set_title("Feature importances using MDI")
ax.set_ylabel("Mean decrease in impurity")
fig.tight_layout()
plt.show()
