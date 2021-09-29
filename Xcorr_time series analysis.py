import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv

#read data from directory
data= pd.read_csv (r'file.csv')


# identify which variable is leading and which is lagging
x= np.array(data['lead'],dtype=np.float32)### for leading variable
y= np.array(data['lagged'],dtype=np.float32)#### for lagging variable 


# Plot graph
fig = plt.figure()
ax= fig.add_subplot(211)
 
# cross correlation using
ax.xcorr(x, y, usevlines=True,
          maxlags=14, normed=True,
          lw=2)## max lags defult is 10
files=  ax.xcorr(x, y, usevlines=True,
         maxlags=14, normed=True,
        lw=2)                   
print (files)### out put file is printed arrays of lags and cross corelation values in a line


# Modification on out put of matplotlib.pyplot.xcorr
header = ['lags','Cross','info']### new coulumn headers for output file
with open('in.csv','w') as f: ### writing temporary output
        writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    # write the data
    writer.writerow(files)
df= pd.read_csv (r'in.csv')
df2 = pd.DataFrame(df['lags'].str.split().values.tolist())
cols= [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
df2.drop(df2.columns[cols],axis=1,inplace=True)### droping unwanted lags(negative lags )
df2=df2.T ### tranposing arrayl list
df2.columns=['Cross_Corr']
Lags= ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14']### keeping wanted lags
df2['lags'] =Lags
print(df2)
columns_titles = ["lags","Cross_Corr"] ### adding desired columns
df2=df2.reindex(columns=columns_titles)
df2=df2.sort_values(by='Cross_Corr',ascending=False)
df2.to_csv('Salmo_anorexia.csv', index=False) ### Saving desired output


# adding grid to the graph
ax1.grid(True)
ax1.axhline(0, color='blue', lw=1)


plt.title('title')### Add title and axis names
plt.xlabel('Lags')### Add x axis lable
plt.ylabel('Cross-Correlation')### Add y axis lable

# show final plotted graph
plt.savefig('Save.png')
plt.show()



