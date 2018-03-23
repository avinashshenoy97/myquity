# -------------------- Imports -------------------- #
import keras, pandas as pd, sys, numpy as np, math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error


# -------------------- Globals -------------------- #
input_file = '../data/NSE:HINDPETRO.csv'
dataset = None
look_back = 30

if len(sys.argv) > 1:
    if sys.argv[1] == '-vv':
        verbosity = 2
    elif sys.argv[1] == '-v':
        verbosity = 1
else:
    verbosity = False


# -------------------- Data -------------------- #
def data_with_look_back(dataset):
    '''Returns x with look_back samples at time t and y with the sample at t+1 '''

    if len(dataset) < look_back:
        raise Exception("Dataset not large enough for given look back!")

    x, y = list(), list()
    for i in range(len(dataset) - look_back):
        x.append(dataset[i:look_back+i])
        y.append(dataset[look_back+i])
    
    return np.array(x), np.array(y)


# Get data
df = pd.read_csv(input_file, usecols=['timestamp', 'close'])
dataset = df['close'].astype('float32')
dataset = dataset[::-1]

if verbosity:
    print("Most recent data point at :", df['timestamp'][0], ":", dataset[len(dataset) - 1])
    print("Oldest data point at :", df['timestamp'][len(df['timestamp']) - 1], ":", dataset[0])

for i in range(len(dataset)):       # replace missing values with mean of prev and next
    if dataset[i] == 0:
        dataset[i] = np.mean([dataset[i-1], dataset[i+1]])

dataset = dataset.reshape((-1, 1))

# Normalize data
scaler = MinMaxScaler(feature_range=(0, 1))
dataset = scaler.fit_transform(dataset)

# Train and test
l = len(dataset) * 60 // 100
train_data = dataset[:l]
test_data = dataset[l:]

if verbosity:
    print("Length of training set =", len(train_data))
    print("Length of test data =", len(test_data))


train_x, train_y = data_with_look_back(train_data)
test_x, test_y = data_with_look_back(test_data)

train_x = np.reshape(train_x, (train_x.shape[0], 1, train_x.shape[1]))
test_x = np.reshape(test_x, (test_x.shape[0], 1, test_x.shape[1]))


# -------------------- Model -------------------- #
model = Sequential()
model.add(LSTM(4, input_shape=(1, look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(train_x, train_y, epochs=100, batch_size=30, verbose=2)

trainPredict = model.predict(train_x)
testPredict = model.predict(test_x)

# invert predictions
trainPredict = scaler.inverse_transform(trainPredict)
train_y = scaler.inverse_transform(train_y)
testPredict = scaler.inverse_transform(testPredict)
test_y = scaler.inverse_transform(test_y)

# calculate average error
trainScore = np.mean([math.fabs(x - y) for x, y in zip(train_y, trainPredict)])
print('Average Error in Training set predictions: %.2f ' % (trainScore))
testScore = np.mean([math.fabs(x - y) for x, y in zip(test_y, testPredict)])
print('Average Error in Test set predictions: %.2f ' % (testScore))

print('\n')

# calculate RMSE
trainScore = math.sqrt(np.mean([math.fabs(x - y)**2 for x, y in zip(train_y, trainPredict)]))
print('Average RMSE in Training set predictions: %.2f ' % (trainScore))
testScore = math.sqrt(np.mean([math.fabs(x - y)**2 for x, y in zip(test_y, testPredict)]))
print('Average RMSE in Test set predictions: %.2f ' % (testScore))