import pandas as pd # pyright: ignore[reportMissingModuleSource]
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import InputLayer # type ignore
from tensorflow.keras.optimizers import Adam # type: ignore
from tensorflow.keras.layers import Dense, Dropout # type: ignore
from tensorflow.keras import layers # type: ignore
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping # type: ignore
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix

dataset = pd.read_csv('cover_data.csv') 

#To view the ten first rows of our data
dataset.head(10)

dataset.columns

#view data columns and types
dataset.info()

# Define feature columns and target variable
features = dataset.iloc[:, :-1]
labels = dataset.iloc[:, -1] - 1 

print(features.describe())

training_features=features.columns

#Split data into train and test sets:
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.4, random_state=42)
features_val, features_test, labels_val, labels_test = train_test_split(features, labels, test_size=0.5, random_state=42)

 #check the shape of features_train and features_test
features_train.shape, features_test.shape

 #check data types in features_train
features_train.dtypes

#scale the numeric training and test feature values
scaler = StandardScaler()
features_train = scaler.fit_transform(features_train)
features_val = scaler.transform(features_val)
features_test = scaler.transform(features_test)

# Build the model
#create model instance with input, hidden and output lay
model = Sequential()
#The following code initializes an input layer for a DataFrame my_data that has 54 columns:
input = layers.InputLayer(input_shape=(features_train.shape[1],)) 
model.add(input)
model.add(Dense(128, input_dim=features_train.shape[1], activation='relu'))
model.add(Dropout(0.2))  # Dropout regularization
model.add(Dense(64, activation='relu'))
model.add(tf.keras.layers.Dense(100, activation = 'relu'))
model.add(Dropout(0.2))
model.add(Dropout(0.2))
model.add(Dense(32, activation='relu'))
model.add(Dense(7, activation='softmax'))

#We’ll start by introducing the Adam optimizer
model.compile(optimizer=Adam(learning_rate=0.001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Define the early stopping callback
early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

history = model.fit(features_train, labels_train, epochs=50, batch_size=500, validation_data=(features_val, labels_val), 
                    callbacks=[early_stopping])

model.save('covtype_classification_model.h5')

# Evaluate the model on the test set and Generate a classification report ###
labels_pred = np.argmax(loaded_model.predict(features_test), axis=1)
print("Classification Report:\n", classification_report(labels_test, labels_pred))
print("Confusion Matrix:\n", confusion_matrix(labels_test, labels_pred))


plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='train')
plt.plot(history.history['val_accuracy'], label='validation')
plt.title('lrate=' + str(learning_rate))
plt.legend(loc="upper right")
plt.xlabel("# of epochs")
plt.ylabel("accuracy")
plt.legend()


plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='train loss')
plt.plot(history.history['val_loss'], label='val loss')
plt.title('model loss')
plt.xlabel("# of epochs")
plt.ylabel("loss")
plt.legend()
