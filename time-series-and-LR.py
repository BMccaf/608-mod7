In [1]: %matplotlib
Using matplotlib backend: Qt5Agg

In [2]: import csv

In [3]: c = lambda f: 5 / 9 * (f - 32)

In [4]: temps = [(f, c(f)) for f in range(0, 101, 10)]
   ...:
   ...:

In [5]:

In [5]:

In [5]: import pandas as pd

In [6]: temps_df = pd.DataFrame(temps, columns=['Fahrenheit', 'Celcius'])

In [7]: axes = temps_df.plot(x='Fahrenheit', y='Celcius', style='.-')

In [8]: nyc = pd.read_csv("C:\\Users\\Ben\\Documents\\examples\\ch10\\ave_hi_nyc_jan_1895-2018.csv")

In [9]: nyc.head()
Out[9]:
     Date  Value  Anomaly
0  189501   34.2     -3.2
1  189601   34.7     -2.7
2  189701   35.5     -1.9
3  189801   39.6      2.2
4  189901   36.4     -1.0

In [10]: nyc.tail()
Out[10]:
       Date  Value  Anomaly
119  201401   35.5     -1.9
120  201501   36.1     -1.3
121  201601   40.8      3.4
122  201701   42.8      5.4
123  201801   38.7      1.3

In [11]: nyc.columns = ['Date', 'Temperature', 'Anomaly']

In [12]: nyc.head(3)
Out[12]:
     Date  Temperature  Anomaly
0  189501         34.2     -3.2
1  189601         34.7     -2.7
2  189701         35.5     -1.9

In [13]: nyc.Date.dtype
Out[13]: dtype('int64')

In [14]: nyc.Date = nyc.Date.floordiv(100)

In [15]: nyc.head(3)
Out[15]:
   Date  Temperature  Anomaly
0  1895         34.2     -3.2
1  1896         34.7     -2.7
2  1897         35.5     -1.9

In [16]: pd.set_option('precision', 2)

In [17]: nyc.Temperature.describe()
Out[17]:
count    124.00
mean      37.60
std        4.54
min       26.10
25%       34.58
50%       37.60
75%       40.60
max       47.60
Name: Temperature, dtype: float64

In [18]: from scipy import stats

In [19]: linear_regression = stats.linregress(x=nyc.Date, y=nyc.Temperature)

In [20]: linear_regression.slope
Out[20]: 0.014771361132966163

In [21]: linear_regression.intercept
Out[21]: 8.694993233674289

In [22]: linear_regression.slope * 2019 + linear_regression.intercept
Out[22]: 38.51837136113297

In [23]: linear_regression.slope * 2021 + linear_regression.intercept
Out[23]: 38.54791408339891

In [24]: linear_regression.slope * 1890 + linear_regression.intercept
Out[24]: 36.612865774980335

In [25]: import seaborn as sns

In [26]: sns.set_style('whitegrid')

In [27]: axes = sns.regplot(x=nyc.Date, y=nyc.Temperature)

In [28]: axes.set_ylim(10, 70)
Out[28]: (10.0, 70.0)

In [29]:
