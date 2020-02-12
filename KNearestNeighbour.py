import numpy as np

# Load the data
iris = load_iris()
X = iris.data [:, (1,3)]
y = iris.target

# Function to calculates the euclidean 
# distance between two data ponts
def euclidean_distance(point1,point2):
    distance = 0;
    for x in range(len(point1)):
        distance += np.square(point1[x]-point2[x]);
    return np.sqrt(distance);

# Split the data for testing and training
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.3, random_state=100)

def kNNPoint(data,testPoint,k):
    distances=[];
    index =[];
    for i in range(len(X_train)):
        dist = euclidean_distance(testPoint,data[i]);
        distances.append((dist,i)); 
    distances.sort();
    for j in range(k):
        index.append(distances[j][1])
    classVoting =[0,0,0];
    for x in range(k):
        response = y_train[index[x]];
        setVals = set(y_train);
        for x in setVals:
            if response == x:
                classVoting[x] +=1;
    sortedVotes = sorted(range(len(classVoting)), key=lambda i: classVoting[i])[-1:];
    return (sortedVotes[0]);

def kNN(train_data,test_data,k):
    sol = [];
    for x in range(len(test_data)):
        sol.append(kNNPoint(train_data,test_data[x],k));
    return (sol);

# Predict the outcome
print kNN(X_train,X_test,3)

# Correct answers
print y_test

#Determine if the prediction is inconsistent with acutal outcomes
print sol - y_test