# -*- coding: utf-8 -*-
"""develop

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jBOvWzWMvcQLj5Hdouj8LkgWPj-IG_ro
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

weather_data=pd.read_csv(r"/content/weather_forecast.csv")

weather_data.head()

weather_data.describe()

weather_data.info()

weather_data[ 'datetime_utc' ] = pd.to_datetime(weather_data[ 'datetime_utc' ])


weather_data.set_index('datetime_utc', inplace= True)
weather_data

weather_data =weather_data.resample('D').mean()

weather_data

weather_data=weather_data[[' _tempm' ]]


type(weather_data[[' _tempm' ]])

weather_data.isnull().any()

weather_data.reset_index(inplace=True)

weather_data[' _tempm' ].fillna(weather_data[' _tempm' ].mean(), inplace=True)

weather_data.rename(columns={ 'datetime_utc':'ds',' _tempm' : 'y'},inplace=True)

weather_data.head()

plt.figure(figsize=(12,8))
plt.plot(weather_data.set_index(["ds"]))

weather_data['year']=pd.DatetimeIndex(weather_data['ds']).year
weather_data['month']=pd.DatetimeIndex(weather_data['ds']).month
weather_data['day']=pd.DatetimeIndex(weather_data['ds']).day

weather_data

weather_data.drop('ds', axis=1, inplace=True)

weather_data

weather_data.corr()

import seaborn as sns
plt.figure(figsize=(8,6))
sns.heatmap(weather_data.corr(), annot=True)

x=weather_data.iloc[:,1:4].values
y=weather_data.iloc[:,0:1].values


x

y


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
mlr=LinearRegression()
mlr.fit(x_train,y_train)

mlr_pred_test=mlr.predict(x_test)
mlr_pred_train=mlr.predict(x_train)

from sklearn.tree import DecisionTreeRegressor
dtr=DecisionTreeRegressor()
dtr.fit(x_train,y_train)

dtr_pred_test=dtr.predict(x_test)
dtr_pred_train=mlr.predict(x_train)

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 100, random_state = 0)
regressor.fit(x_train, y_train)

rfr_pred_test=regressor.predict(x_test)
rfr_pred_train=regressor.predict(x_train)

from xgboost import XGBRegressor
xgb = XGBRegressor(n_estimators=1000)
xgb.fit(x_train, y_train, verbose=False)


xgb_pred_test=xgb.predict(x_test)
xgb_pred_train=xgb.predict(x_train)

from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error

mlr_train_mae = mean_absolute_error(y_train,mlr_pred_train)
print("MLR Train data MAE: ", mlr_train_mae)
mlr_test_mae = mean_absolute_error(y_test,mlr_pred_test)
print("MLR Test data MAE: ",mlr_test_mae)
dtr_train_mae = mean_absolute_error(y_train,dtr_pred_train)
print("DTR Train data MAE: " , dtr_train_mae)
dtr_test_mae = mean_absolute_error(y_test,dtr_pred_test)
print("DTR Test data MAE: ",dtr_test_mae)
rfr_train_mae = mean_absolute_error(y_train,rfr_pred_train)
print("RFR Train data MAE: " , rfr_train_mae)
rfr_test_mae = mean_absolute_error(y_test,rfr_pred_test)
print("RFR Test data MAE: ",rfr_test_mae)
xgb_train_mae = mean_absolute_error(y_train,xgb_pred_train)
print("XGB Train data MAE: ",xgb_train_mae)
xgb_test_mae = mean_absolute_error(y_test,xgb_pred_test)
print("XGB Test data MAE: ",xgb_test_mae)


from sklearn.metrics import mean_squared_error

mlr_train_mse = mean_squared_error(y_train,mlr_pred_train)
print("MLR Train data MSE: ", mlr_train_mse)
mlr_test_mse = mean_squared_error(y_test,mlr_pred_test)
print("MLR Test data MSE: ", mlr_test_mse)
dtr_train_mse = mean_squared_error(y_train,dtr_pred_train)
print("DTR Train data MSE: ", dtr_train_mse)
dtr_test_mse = mean_squared_error(y_test,dtr_pred_test)
print("DTR Test data MSE: ", dtr_test_mse)
rfr_train_mse = mean_squared_error(y_train,rfr_pred_train)
print("RFR Train data MSE: ", rfr_train_mse)
rfr_test_mse = mean_squared_error(y_test,rfr_pred_test)
print("RFR Test data MSE: ", rfr_test_mse)
xgb_train_mse = mean_squared_error(y_train,xgb_pred_train)
print("XGB Train dat MSE: ", xgb_train_mse)
xgb_test_mse = mean_squared_error(y_test,xgb_pred_test)
print("XGB Test data MSE: ", mlr_test_mse)

import math

def rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())

mlr_train_rmse = math.sqrt(mean_squared_error(y_train,mlr_pred_train))
print("MLR Train data RMSE: ", mlr_train_rmse)
mlr_test_rmse = math.sqrt(mean_squared_error(y_test,mlr_pred_test))
print("MLR Test data RMSER: ", mlr_test_rmse)
dtr_train_rmse = math.sqrt(mean_squared_error(y_train,dtr_pred_train))
print("DTR Train data RMSE: ", dtr_train_rmse)
dtr_test_rmse = math.sqrt(mean_squared_error(y_test,dtr_pred_test))
print("DTR Test data RMSE: ", dtr_test_rmse)
rfr_train_rmse = math.sqrt(mean_squared_error(y_train,rfr_pred_train))
print("RFR Train data RMSE: ", rfr_train_rmse)
rfr_test_rmse = math.sqrt(mean_squared_error(y_test,rfr_pred_test))
print("RFR Test data RMSE: ", rfr_test_rmse)
xgb_train_rmse = math.sqrt(mean_squared_error(y_train,xgb_pred_train))
print("XGB Train RMSE: ", xgb_train_rmse)
xgb_test_rmse = math.sqrt(mean_squared_error(y_test,xgb_pred_test))
print("XGB Test data RMSE: ", xgb_test_rmse)

from sklearn.metrics import r2_score
import numpy

mlr_train_acc = r2_score(y_train,mlr_pred_train)
print("MLR Train data R2 Score: ", mlr_train_acc)

mlr_test_acc = r2_score(y_test,mlr_pred_test)
print("MLR Test data R2 Score: ", mlr_test_acc)

dtr_train_acc = r2_score(y_train,dtr_pred_train)
print("DTR Train data R2 Score: ",dtr_train_acc)

dtr_test_acc = r2_score(y_test,dtr_pred_test)
print("DTR Test data R2 Score: ", dtr_test_acc)

rfr_train_acc = r2_score(y_train,rfr_pred_train)
print("RFR Train data R2 Score: ", rfr_train_acc)

rfr_test_acc = r2_score(y_test,rfr_pred_test)
print("RFR Test data R2 Score: ", rfr_test_acc)

xgb_train_acc = r2_score(y_train,xgb_pred_train)
print("XGB Train data R2 Score: ",xgb_train_acc)

xgb_test_acc = r2_score(y_test,xgb_pred_test)
print("XGB Test data R2 Score: ", xgb_test_acc)




d={'Train RMSE': [mlr_train_rmse,dtr_train_rmse,rfr_train_rmse,xgb_train_rmse],
   'Test RMSE': [mlr_test_rmse,dtr_test_rmse,rfr_test_rmse,xgb_test_rmse],
   
    'Train MSE': [mlr_train_mse,dtr_train_mse,rfr_train_mse,xgb_train_mse],
    'Test MSE': [mlr_test_mse,dtr_test_mse,rfr_test_mse,xgb_test_mse],
   
    'Train MAE': [mlr_train_mae,dtr_train_mae,rfr_train_mae,xgb_train_mae],
     'Test MAE': [mlr_test_mae,dtr_test_mae,rfr_test_mae,xgb_test_mae],
     
     'Train R2 score': [mlr_train_acc,dtr_train_acc,rfr_train_acc,xgb_train_acc],
      'Test R2 score': [mlr_test_acc,dtr_test_acc,rfr_test_acc,xgb_test_acc]}
df = pd.DataFrame(data=d, index=["MLR","DTR","RFR","XGB"])    
df
   

y_p= regressor.predict([[2005,1,23]])
y_p

import pickle
pickle.dump(regressor,open('weather_ml.pkl','wb'))