# -------------------- Imports -------------------- #
from common import *


# -------------------- Globals and Data -------------------- #

train_x, train_y = data_with_look_back(train_data)
test_x, test_y = data_with_look_back(test_data)

train_x = np.reshape(train_x, (train_x.shape[0], 1, train_x.shape[1]))
test_x = np.reshape(test_x, (test_x.shape[0], 1, test_x.shape[1]))

if verbosity == False :
    verbose = 0
elif verbosity == 1 :
    verbose = 2
elif verbosity == 2 :
    verbose = 1


# -------------------- Model -------------------- #
model = Sequential()
model.add(LSTM(10, input_shape=(1, look_back), return_sequences=True))
model.add(LSTM(5, input_shape=(1, look_back), return_sequences=True))
model.add(LSTM(5, input_shape=(1, look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(train_x, train_y, epochs=100, batch_size=30, verbose=verbose)

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