# Artificial Neural Network

# Installing Theano
# pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

# Installing Tensorflow
# pip install tensorflow

# Installing Keras
# pip install --upgrade keras

# Part 1 - Now let's make the ANN!

# Importing the Keras libraries and packages
import sys
import keras
from keras.models import Sequential
from keras.layers import Dense

# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(units = 64, kernel_initializer = 'uniform', activation = 'relu', input_dim = 1573))

# Adding the second hidden layer
classifier.add(Dense(units = 64, kernel_initializer = 'uniform', activation = 'relu'))

# Adding the output layer
classifier.add(Dense(units = 9, kernel_initializer = 'uniform', activation = 'softmax'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

print (classifier.summary())

print ("===========================================================================================")

#sys.exit()

# Part 2 - Data Preprocessing

# Importing the libraries
import matplotlib.pyplot as plt
import itertools
import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('train/train.csv')
X = dataset.iloc[:, 0:1573].values
print "X: ", X.shape, X
y = dataset.iloc[:, 1573:1574].values
print "y: ", y.shape, y

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
enc = OneHotEncoder()
enc.fit(y)
y = enc.transform(y)
print "y: ", y.shape, y

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 101, test_size=0.3)


print "X_train: ", X_train.shape, X_train
print "X_test: ", X_test.shape, X_test
print "y_train: ", y_train.shape, y_train
print "y_test: ", y_test.shape, y_test
# sys.exit()
# Fitting the ANN to the Training set
history = classifier.fit(X_train, y_train, batch_size = 10, epochs = 30)
# Part 3 - Making predictions and evaluating the model
print("Val Score: ", classifier.evaluate(X_test, y_test))

plt.plot(history.history['acc'])
#plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# sys.exit()


# Making the Confusion Matrix
y_pred = classifier.predict(X_test)
y_pred = enc.inverse_transform(y_pred)
print y_pred.shape, y_pred, y_test.shape, y_test

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(enc.inverse_transform(y_test), y_pred)
print cm

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1, keepdims = True)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

#class_names = ["1. Ramnit", "2. Lollipop", "3. Kelihos_ver3", "4. Vundo", "5. Simda", "6. Tracur", "7. Kelihos_ver1", "8. Obfuscator.ACY", "9. Gatak"]
class_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
plt.figure()
plot_confusion_matrix(cm, classes=class_names,title='Confusion matrix, without normalization')

plt.figure()
plot_confusion_matrix(cm, classes=class_names, normalize=True, title='Normalized confusion matrix')
plt.show()

# sys.exit()

# Predicting the Test set results
dataset_test = pd.read_csv('test/test.csv')
X_test = dataset_test.iloc[:, 0:1573].values
X_test = StandardScaler().fit_transform(X_test)
# X_test = X_test.reshape((X_test.shape[0], 1573, 1))

ynew = classifier.predict(X_test, batch_size=10, verbose=1)
#ynew = enc.inverse_transform(ynew)
print ynew 

from csv import writer

f_csv = open('result_ann.csv', 'w')
csv_w = writer(f_csv)
csv_w.writerows([["Prediction1","Prediction2","Prediction3","Prediction4","Prediction5","Prediction6","Prediction7","Prediction8","Prediction9"]])

for i in ynew:
    csv_w.writerows([i])