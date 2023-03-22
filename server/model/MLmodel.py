import category_encoders as ce, matplotlib.pyplot as plt, seaborn as sns, pandas as pd, warnings, pickle, numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier

warnings.simplefilter(action="ignore", category=FutureWarning)
sns.set(color_codes=True)

dataset = pd.read_csv("./static/dataset.csv")
print("Shape of Data:", dataset.shape)

# Dataset Information
print(dataset.info())

# fig, ax = plt.subplots(nrows=1, ncols=3, sharey=True, figsize=(14,5))
# ax1 = sns.barplot(x="Academics", y="Stress_rating", hue="International", data=dataset, palette="winter", linewidth=0.0, errwidth=0, ax=ax[0])
# for i in ax1.containers:
#     ax1.bar_label(i,)

dataset.loc[(dataset["Academics"] == 1) | (dataset["Looks_Fitness"] == 1) | (dataset["Social_life"] == 1) | (dataset["Xtra_curricular"] == 1) | (dataset["Athletics"] == 1) | (dataset["Career"] == 1) | (dataset["Finance"] == 1) | (dataset["Relationship"] == 1) | (dataset["Cultural_Shock"] == 1), 'Stressed'] = 1
dataset.loc[(dataset["Academics"] == 0) & (dataset["Looks_Fitness"] == 0) & (dataset["Social_life"] == 0) & (dataset["Xtra_curricular"] == 0) & (dataset["Athletics"] == 0) & (dataset["Career"] == 0) & (dataset["Finance"] == 0) & (dataset["Relationship"] == 0) & (dataset["Cultural_Shock"] == 0), 'Stressed'] = 0
# ax2 = sns.barplot(x="Stressed", y="Stress_rating", hue="International", data=dataset, palette="winter", linewidth=0.0, errwidth=0, ax=ax[1])
# for i in ax2.containers:
#     ax2.bar_label(i,)

dataset.loc[(dataset["Emotional_bullied"] == 1) | (dataset["Physical_bullied"] == 1) | (dataset["Verbal_bullied"] == 1) | (dataset["Social_bullied"] == 1) | (dataset["Cyber_bullied"] == 1), 'Bullied'] = 1
dataset.loc[(dataset["Emotional_bullied"] == 0) & (dataset["Physical_bullied"] == 0) & (dataset["Verbal_bullied"] == 0) & (dataset["Social_bullied"] == 0) & (dataset["Cyber_bullied"] == 0), 'Bullied'] = 0
# ax3 = sns.barplot(x="Bullied", y="Stress_rating", hue="International", data=dataset, palette="winter", linewidth=0.0, errwidth=0, ax=ax[2])
# for i in ax3.containers:
#     ax3.bar_label(i,)

# plt.tight_layout()
# plt.show()

# Prepare the Data
X = dataset.drop(['Student ID','Bullied', 'Stressed', 'Stress_rating'], axis=1)
y = dataset['Stress_rating']

# Feature Scaling
X = StandardScaler().fit(X).transform(X)

# Split data into separate training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7,test_size = 0.3, random_state=100)

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

pickle.dump(knn, open("./static/model.pkl","wb"))



