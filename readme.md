About the project
This study area includes 4 Wilderness Areas located in the Roosevelt National Forest of Northern Colorado. These area represent forests with minimal human-caused disturbances, so that existing forest cover types are more a result of ecological process rather than forest management practices.

Each observation is 30m x 30m forest cover type determined from US Forest Service (USFS) Region 2 Resource Information System (RIS) data. Independent variables were derived from the data originally obtained from US Geological Survey (USGS) and USFS data.

 There are seven possible forest cover types:

1. Spruce/Fir
2. Lodgepole Pine
3. Ponderosa Pine
4. Cottonwood/Willow
5. Aspen
6. Douglas-fir
7. Krummholz

What needs to be done
We have been given a total of 54 attributes/features, these attributes contain Binary and Quantative attributes, and we need to predict which Forest Cover-Type is it from the given features.

Project Objectives:
Develop one or more classifiers for this multi-class classification problem.
Use TensorFlow with Keras to build your classifier(s).
Use your knowledge of hyperparameter tuning to improve the performance of your model(s).
Test and analyze performance.


loading the data: 
Our data is in the .csv format and we load it with pandas: I use dataset as the variable.

To standardize the numerical features we use ColumnTransformer

Train test split used:
I have used 60% data for training and 40% for testing the data


All the hidden layers are activated by 'relu' or retifier function, and output layer by softmax.

The dataset was efficiently preprocessed and trained using a simple neural network architecture. The tuning process yielded strong performance, indicating that even basic models can achieve high accuracy with well-prepared features. 