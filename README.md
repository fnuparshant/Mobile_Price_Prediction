# Hackathon Project 

## Problem Statement 
Using the Mobile Price Classification dataset in [Kaggle](https://www.kaggle.com/iabhishekofficial/mobile-price-classification?select=train.csv), we would like to predict the price range of the mobile phones that Bob, the storeowner has in his inventory.

[![maxresdefault.jpg](https://i.postimg.cc/vB9WKfwG/maxresdefault.jpg)](https://postimg.cc/zbzbbLfQ)

## Dataset

Kaggle link: [Mobile Price Classification](https://www.kaggle.com/iabhishekofficial/mobile-price-classification?select=train.csv)
* Download link: [Dataset](https://www.kaggle.com/iabhishekofficial/mobile-price-classification/download)

## Data Dictionary

|Feature|Type|Variable|Description|
|---|---|---|---|
|**battery_power**|*int*|Predictor|Total energy a battery can store in one time measured in mAh|
|**blue**|*int*|Predictor|Has bluetooth or not|
|**clock_speed**|*float*|Predictor|speed at which microprocessor executes instructions|
|**dual_sim**|*int*|Predictor|Has dual sim support or not|
|**fc**|*int*|Predictor|Front Camera mega pixels|
|**four_g**|*int*|Predictor|Has 4G or not|
|**int_memory**|*int*|Predictor|Internal Memory in Gigabytes|
|**m_dep**|*float*|Predictor|Mobile Depth in cm|
|**mobile_wt**|*int*|Predictor|Weight of mobile phone|
|**n_cores**|*int*|Predictor|Number of cores of processor|
|**pc**|*int*|Predictor|Primary Camera mega pixels|
|**px_height**|*int*|Predictor|Pixel Resolution Height|
|**px_width**|*int*|Predictor|Pixel Resolution Width|
|**ram**|*int*|Predictor|Random Access Memory in Mega Bytes|
|**sc_h**|*int*|Predictor|Screen Height of mobile in cm|
|**sc_w**|*int*|Predictor|Screen Width of mobile in cm|
|**talk_time**|*int*|Predictor|longest time that a single battery charge will last when you are|
|**three_g**|*int*|Predictor|Has 3G or not|
|**touch_screen**|*int*|Predictor|Has touch screen or not|
|**wifi**|*int*|Predictor|Has wifi or not|
|**price_range**|*int*|Target|value of 0(low cost), 1(medium cost), 2(high cost) and 3(very high cost)|

## Data Cleaning
* Complete dataset with no null values
* Outliers
    * px_height - contained a 0 height

## EDA
* Boxplots
    * ram / price_range
    * battery_power / price_range
    * px_height / price_range
    * px_width / price_range


* Heatmap - Showed very little correlation between the predictor variables and the price_range. Because battery_power, px_height, px_width, and ram had highest correlation values of 0.2, 0.15, 0.16 and 0.92 respectively, we decided to include these in our model.


## Modeling
1. Logistic Regression with ram as sole feature
2. Logistic Regression with ram, battery_power as features
3. Logistic Regression with ram, battery_power, px_height as features
4. Logistic Regression with ram, battery_power, px_height and px_weight as features
5. Logistic Regression (Model 4) with scaled predictor variables
6. Support Vector Classifier with ram, battery_power, px_height and px_weight
7. Random Forest with ram, battery_power, px_height and px_weight
8. KNN with ram, battery_power, px_height and px_weight
9. AdaBoost with ram, battery_power, px_height and px_weight

## Analysis

The results of our models are summarized below.

|Model Type|CV Score (Test Data)|Description|
|---|---|---|
|0|0.25|Null model|
|1|0.77|Logistic Regression with ram as sole feature|
|2|0.8060|Logistic Regression with ram, battery_power as features|
|3|0.8780|Logistic Regression with ram, battery_power, px_height as features|
|**4**|**0.968**|**Logistic Regression with ram, battery_power, px_height and px_weight as features**|
|5|0.952|Logistic Regression (Model 4) with scaled predictor variables|
|6|0.9280|Support Vector Classifier with ram, battery_power, px_height and px_weight|
|7|0.882|Random Forest with ram, battery_power, px_height and px_weight|
|8|0.840|KNN with ram, battery_power, px_height and px_weight|
|9|0.718|AdaBoost with ram, battery_power, px_height and px_weight|


We determined that our logistic regression model using the 4 most correlated features of battery_power, px_height, px_weight and ram gave us the best model. 

Therefore, we used this model to create a streamlit app to allow for inputting sample parameters to estimate the mobile phone price range.

## Conclusion

In conclusion, we determined that the logistic regression model featuring ram, battery_power, px_height and px_weight as parameters returned the best model. When we scaled the variables, the logistic regression model became less overfit. Also, when we used the support vector classifier model, the overfitting decreased further, although still above 0.9.


