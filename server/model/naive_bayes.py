import category_encoders as ce, matplotlib.pyplot as plt, seaborn as sns, pandas as pd, warnings, pickle
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


list_cols = ['Academics', 'Looks_Fitness', 'Social_life', 'Xtra_curricular', 'Athletics', 'Career', 'Finance', 'Relationship', 'Cultural_Shock', 'Emotional_bullied', 'Physical_bullied', 'Verbal_bullied', 'Social_bullied', 'Cyber_bullied', 'International', 'Miss_home', 'Family_friends', 'Food', 'Sensory', 'Miss_social', 'Native_language', 'Courses', 'Loan', 'Stressed_commute']
ce_ohe = ce.OneHotEncoder(cols=list_cols)
df = ce_ohe.fit_transform(dataset)

# Split data into separate training and test set
X = df.drop(['Bullied', 'Stressed', 'Stress_rating'], axis=1)
y = df['Stress_rating']

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7,test_size = 0.3, random_state=100)

# Extracting variables and storing student IDs
df_train = X_train
studentID = []
for i in X_test["Student ID"]:
    studentID.append(i)

X_test = X_test.drop(['Student ID'], axis=1)
X_train = X_train.drop(['Student ID'], axis=1)

cols = X_train.columns

# Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform (X_test)

X_train = pd.DataFrame(X_train)
X_test = pd.DataFrame(X_test)

X_train.columns = cols
X_test.columns = cols

# Model training
# gnb = GaussianNB()
gnb = KNeighborsClassifier(n_neighbors = 13)

# fit the model
gnb.fit(X_train.values, y_train)

# Predict the results
y_pred= gnb.predict(X_test)
#gnb_pred=gnb.predict_proba(X_test)

# Check accuracy score
print('Model accuracy score: {0:0.4f}'. format(accuracy_score(y_test, y_pred)))

# print('Train Model accuracy score: {0:0.4f}'. format(gnb.score(X_train, y_train)))
# print('Test Model accuracy score: {0:0.4f}'. format(gnb.score(X_test, y_test)))

# Confusion Matrix
# cm = confusion_matrix(y_test, y_pred)

conf_mat = confusion_matrix(y_test, y_pred, normalize="true")
sns.heatmap(conf_mat.T, annot=True, fmt=".0%", cmap="cividis")#, xticklabels=y_train.column, yticklabels=X_train.columns)
plt.xlabel("True label")
plt.ylabel("Predicted label")
plt.show()

print('Confusion matrix\n\n', conf_mat)
# print('\nTrue Negative(TN) = ', cm[0,0] + cm[])
# print('\nFalse Positives(FP) = ', cm[0,1])
# print('\nFalse Negative(FN) = ', cm[1,0])
# print('\nTrue Positive(TP) = ', cm[1,1])


# Print the predicted values
df = pd.DataFrame(y_pred)

# for index, row in df.iterrows():
#     print("Student ID - " +str(studentID[index])+" - " + str(row[0]))

print("\n Rating wise Student numbers: \n", y_test.value_counts())

pickle.dump(gnb, open("./static/model.pkl","wb"))



