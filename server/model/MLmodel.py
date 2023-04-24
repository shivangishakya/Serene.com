import category_encoders as ce, matplotlib.pyplot as plt, seaborn as sns, pandas as pd, warnings, pickle, numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier

warnings.simplefilter(action="ignore", category=FutureWarning)
sns.set(color_codes=True)

dataset = pd.read_csv("./static/dataset.csv")
# print("Shape of Data:", dataset.shape)

# Dataset Information
# print(dataset.info())

# Prepare the Data
X = dataset.drop(['Student ID', 'Stress_rating'], axis=1)
y = dataset['Stress_rating']

# Split data into separate training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7,test_size = 0.3, random_state=100)

# Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model training
knn = KNeighborsClassifier(n_neighbors = 13).fit(X_train, y_train)

# Predict the results
y_pred= knn.predict(X_test)

# Check accuracy score
print('Model accuracy score: {0:0.4f}'. format(accuracy_score(y_test, y_pred)))

# Test for the value of K with the lowest error rate.
# Uncomment when changes in the data to generate new value of K
# error_rate = []
# for i in range(1,50):
#     knn1 = KNeighborsClassifier(n_neighbors=i)
#     knn1.fit(X_train,y_train)
#     pred_i = knn1.predict(X_test)
#     error_rate.append(np.mean(pred_i != y_test))
# print("Minimum error:-",min(error_rate),"at K =",error_rate.index(min(error_rate))+1)

# Confusion Matrix
conf_mat = confusion_matrix(y_test, y_pred, normalize="true")
# sns.heatmap(conf_mat.T, annot=True, fmt=".0%", cmap="cividis")#, xticklabels=y_train.column, yticklabels=X_train.columns)
# plt.xlabel("True label")
# plt.ylabel("Predicted label")
# plt.show()

# Print the predicted values
df = pd.DataFrame(y_pred)

print("\n Rating wise Student numbers: \n", y_test.value_counts())

with open('./static/model.pkl', 'wb') as f:
    pickle.dump(knn, f)



