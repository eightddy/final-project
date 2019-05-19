from keras.models import model_from_json
import pandas as pd
from csv import writer
from sklearn.preprocessing import StandardScaler


# load json and create model
json_file = open('save/model-ann-ms.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

# load weights into new model
loaded_model.load_weights("save/model-ann-ms.h5")
print("Loaded model from disk")

# evaluate loaded model on test data
loaded_model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

# Predicting the Test set results
dataset_test = pd.read_csv('test/test.csv')
X_test = dataset_test.iloc[:, 0:1573].values
X_test = StandardScaler().fit_transform(X_test)

ynew = loaded_model.predict(X_test, batch_size=10, verbose=1)

print ynew 

f_csv = open('result_ann.csv', 'w')
csv_w = writer(f_csv)
csv_w.writerows([["Prediction1","Prediction2","Prediction3","Prediction4","Prediction5","Prediction6","Prediction7","Prediction8","Prediction9"]])

for i in ynew:
    csv_w.writerows([i])
f_csv.close()