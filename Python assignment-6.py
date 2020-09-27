#import the libraries
import pandas as pd
import numpy as np

#Load the data
Data = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],
                   'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
                   'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                   'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )','12. Air France', '"Swiss Air"']})

Data

#1)Some values in the the FlightNumber column are missing. These numbers are meant to increase by 10 with each row so 10055 and 10075 need to be put in place. Fill in these missing numbers and make the column an integer column (instead of a float column).

Data.isna().sum()
Data.fillna(Data.median(), inplace=True)

#2)The FromTo column would be better as two separate columns! Split each string on the underscore delimiter to give a new temporary DataFrame with the correct values. Assign the correct column names to this temporary DataFrame.

df_temp= Data.From_To.str.split('_', expand=True)
df_temp.columns = ['From', 'To']
print("Output")
df_temp

#3) Notice how the capitalisation of the city names is all mixed up in this temporary DataFrame. Standardise the strings so that only the first letter is uppercase (e.g. "londON" should become "London".)

df_temp.From = df_temp.From.str.title()
df_temp.To = df_temp.To.str.title()
print("Output")
df_temp

#4) Delete the From_To column from df and attach the temporary DataFrame from the previous questions.

Data = Data.drop("From_To", axis=1).join(df_temp)
print("Output")
Data

#5) In the RecentDelays column, the values have been entered into the DataFrame as a list. We would like each first value in its own column, each second value in its own column, and so on. If there isn't an Nth value, the value should be NaN.
#Expand the Series of lists into a DataFrame named delays, rename the columns delay_1, delay_2, etc. and replace the unwanted RecentDelays column in df with delays


df_delays=pd.DataFrame(Data["RecentDelays"].values.tolist())
df_delays.columns = ['delay_{}'.format(n) for n in range(1, len(df_delays.columns)+1)]
df_delays

Data=Data.drop("RecentDelays" , axis=1).join(df_delays)
print("Output")
Data




