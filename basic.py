print("hello sir")

#NUMPY LIBBRARY

import numpy as np
my_lst1=[1,2,3,4,5]
arr=np.array(my_lst1)
print(arr)
print(type(arr))
print(arr.imag) 

#PANDAS LIBRARY

import pandas as pd
import numpy as np
df=pd.DataFrame(np.arange(0,20).reshape(5,4),index=["row1","row2","row3","row4","row5"],columns=["col1","col2","col3","col4"])

df.head()
print(df)
print(df.loc["row2","col4"])
print(df.loc["row5","col2"])
df.to_csv("testdata.csv")
print(type(df))
print(df.describe())
print(df.info())
print(df.dtypes)


#READING CSV AND JSON FILES


from io import StringIO
data=('apple,banana,mango\n'
      'x,y,z \n'
      '1,2,3 \n')
df=pd.read_csv(StringIO(data))
print(df)
df.to_csv("testdata2.csv")
 
#data='{"employee_name":"james","employee_email":"james@123gmail.com","title":"developer"}'
df=pd.read_json(data)
print(df)

df_excel=pd.read_excel("excel_sample.xlsx")
df_excel.head()
print(df_excel.head())
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,10)
y=np.arange(10,20)
plt.scatter(x,y)
plt.scatter(x,y,c='b',marker='*',linestyle='dashed')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("GRAPH PLOT")
plt.show(x,y)
plt.savefig("scatterplot.png") 

x=np.arange(0,20)
y=8*x-8
plt.title("LINE PLOT")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.plot(x,y)
plt.show()
plt.savefig("lineplot.png")

np.pi=3.14
x=np.arange(0,12*np.pi,0.1)
y=np.sin(x)
plt.xlabel("X-AXIS")
plt.ylabel("Y-AXIS")
plt.title("Sine WAVE")
plt.plot(x,y)
plt.show()
plt.savefig("sinewave.png")

x1=[4,6,8]
y1=[3,5,7]
x2=[4,3,5]
y2=[5,7,9]
plt.bar(x1,y1,color='b')
plt.bar(x2,y2,color='g')
plt.title("BAR GRAPH")
plt.xlabel("X-AXIS")
plt.ylabel("Y-AXIS")
plt.show()
plt.savefig("bargraph.png")

#SEABORN LIBRARY

from matplotlib.pyplot import savefig
from matplotlib.pyplot import savefig
import seaborn as sns
df=sns.load_dataset("tips")
df.head()
print(df.head())
#df.corr() its for coorrelation

sns.jointplot(x="tip",y="total_bill",data=df,kind="hex")
savefig("jointplot.png")
sns.jointplot(x="tip",y="total_bill",data=df,kind="reg")
savefig("regplot.png")
sns.pairplot(df,hue="sex")
savefig("pairplot.png")
#(distplot) 

# sns.distplot(df["tip"])
