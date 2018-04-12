# myquity

Machine learning for equity trading!

## The Model

**myquity** uses good old LSTMs to predict share prices (or at least, attempts to do so). A neural network with a single LSTM layer and multiple hidden LSTM layers were used, despite both yielding reasonably high accuracies, just for some clarity.

The iPython Notebooks in this repository contain predictions for the company **TCS** that trades on India's **National Stock Exchange** or **NSE**. However, the model was also trained and used to predict the share prices of **Hindustan Petroleum** and **Coral Laboratories Ltd**. Their symbols are :

    NSE:TCS
    NSE:HINDPETRO
    BSE:CORALAB


The single LSTM layer contains 4 units or cells while the deep neural net has 4 LSTM layers, followed by a dense layer with a single cell to make a single prediction into the future. The 4 LSTM layers have 10, 10, 5, and 5 units respectively.

## The Data

The data was obtained from [AlphaVantage](https://www.alphavantage.co), a free API service that anybody can query once they sign up on their website and receive a free API key.

Data from as far back as available on AlphaVantage was used, upto (and including) 23-03-2018, i.e, 23rd March 2018, to make train the model and make predictions.

Missing data was replaced with average of the 2 data points on either side of the missing data point. Erroneous data, if any, was left as is in the hopes that the neural network would be robust enough and manage this by itself.

## TRAINING!

The model was trained with all of the data available upto, and including, 28th March 2018.

## What predictions?

Once the model was trained, 365 data points were used to make 365 predictions into the future.

## Graphs!!

What's the best way to look at share prices? Graphs of course!

Making predictions as described earlier, here are some of the graphs obtained :

### Single Layer LSTM

|Symbol|Graph|
|:-:|:-:|
| NSE:TCS | ![NSE:TCS](https://github.com/avinashshenoy97/myquity/blob/master/plots/Single%20LSTM/NSE:TCS.png) |
| NSE:HINDPETRO|![NSE:HINDPETRO](https://github.com/avinashshenoy97/myquity/blob/master/plots/Single%20LSTM/NSE:HINDPETRO.png) |
| BSE:CORALAB | ![BSE:CORALAB](https://github.com/avinashshenoy97/myquity/blob/master/plots/Single%20LSTM/BSE:CORALAB.png) |


### Deep LSTM

|Symbol|Graph|
|:-:|:-:|
| NSE:TCS | ![NSE:TCS](https://github.com/avinashshenoy97/myquity/blob/master/plots/Deep%20LSTM/NSE:TCS.png) |
| NSE:HINDPETRO|![NSE:HINDPETRO](https://github.com/avinashshenoy97/myquity/blob/master/plots/Deep%20LSTM/NSE:HINDPETRO.png) |
| BSE:CORALAB | ![BSE:CORALAB](https://github.com/avinashshenoy97/myquity/blob/master/plots/Deep%20LSTM/BSE:CORALAB.png) |

### So far so good, right?

Both models seem to have successfully predicted future values of each of the comapny's share prices. Notice that the legend only describes the colour of the `Original` values' plot. All the other colours represent the predictions.

## Into the FUTURE!

The last data point in the data used is `23rd March 2018`. Using a year's data upto this date, we try to predict the next year's values.

More graphs!

#### Single Layer LSTM

|Symbol|Graph|
|:-:|:-:|
| NSE:TCS | ![NSE:TCS](https://github.com/avinashshenoy97/myquity/blob/master/plots/Single%20LSTM/Future/nextNSE:TCS.png) |
| NSE:HINDPETRO|![NSE:HINDPETRO](https://github.com/avinashshenoy97/myquity/blob/master/plots/Single%20LSTM/Future/nextNSE:HINDPETRO.png) |
| BSE:CORALAB | ![BSE:CORALAB](https://github.com/avinashshenoy97/myquity/blob/master/plots/Single%20LSTM/Future/nextBSE:CORALAB.png) |

#### Deep LSTM

|Symbol|Graph|
|:-:|:-:|
| NSE:TCS | ![NSE:TCS](https://github.com/avinashshenoy97/myquity/blob/master/plots/Deep%20LSTM/Future/nextNSE:TCS.png) |
| NSE:HINDPETRO|![NSE:HINDPETRO](https://github.com/avinashshenoy97/myquity/blob/master/plots/Deep%20LSTM/Future/nextNSE:HINDPETRO.png) |
| BSE:CORALAB | ![BSE:CORALAB](https://github.com/avinashshenoy97/myquity/blob/master/plots/Deep%20LSTM/Future/nextBSE:CORALAB.png) |


### The Predictions!

#### Single Layer LSTM

| Symbol | Days into the Future | Predicted Price in ₹ |
| :----: | :----: | :-------------: |
| NSE:TCS | 30 | 2132 |
|  | 120 | 2441 |
|  | 365 | 1246 |
| | | |
| NSE:HINDPETRO | 30 | 294 |
| | 120 | 344 |
| | 365 | 322 |
| | | |
| BSE:CORALAB | 30 | 587 |
| | 120 | 721 |
| | 365 | -278 |

#### Deep LSTM

| Symbol | Days into the Future | Predicted Price in ₹ |
| :----: | :----: | :-------------: |
| NSE:TCS | 30 | 2132 |
|  | 120 | 2441 |
|  | 365 | 125 |
| | | |
| NSE:HINDPETRO | 30 | 294 |
| | 120 | 344 |
| | 365 | 29 |
| | | |
| BSE:CORALAB | 30 | 587 |
| | 120 | 721 |
| | 365 | 7.8 |

### Now what?

The day these predictions were made, and committed, is 12th April 2018. On 23rd April 2018, we will know how accurate the 30-day away predictions are/were!

### Primary Contributor
| | |
| :-: | :-: |
| <img src="https://github.com/avinashshenoy97.png" width="48"> | [Avinash Shenoy](https://github.com/avinashshenoy97) | 

### License

[MIT License](https://github.com/avinashshenoy97/myquity/blob/master/LICENSE)

Copyright (c) 2018 Avinash Shenoy