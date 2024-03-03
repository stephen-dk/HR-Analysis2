#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.style as st


# In[2]:


data = pd.read_excel(r"C:\Users\user\Desktop\data-cleaning-in-excel.xlsx.xls")


# In[27]:


data.head(7)


# In[4]:


data.info()


# In[5]:


header =data.loc[2]


# In[6]:


data.columns=header


# In[7]:


data.head(3)


# In[8]:


data.reset_index(drop=True,inplace=True)


# In[9]:


data.rename(columns={2:'Num'},inplace=True)


# In[10]:


data.drop(index=[0,1,2],inplace=True)


# In[11]:


data=data.iloc[:,2:11]


# In[12]:


data.reset_index(drop=True,inplace=True)


# In[13]:


data.dtypes


# In[14]:


data=data[~data['Emp ID'].duplicated()]


# In[15]:


data['Emp ID'].isna().sum()


# In[16]:


data['Salary'].isna().sum()


# In[17]:


data['Salary'].fillna(0,inplace=True)


# In[18]:


data['Salary']=data['Salary'].astype('float')


# In[19]:


data['Start Date']=pd.to_datetime(data['Start Date'])


# In[20]:


data['Start Date']=data['Start Date'].dt.year


# In[21]:


data.sort_values('Start Date',inplace=True)


# In[22]:


data.reset_index(drop=True,inplace=True)


# In[23]:


data.head()


# In[24]:


dept = data['Department'].unique()


# In[25]:


dept


# In[26]:


while True:
    i= input("""DEPARTMENTS
                
                Research and Development
                Sales
                Human Resources
                Support
                Training
                Marketing
                Product Management
                Accounting
                Services
                Engineering
                Business Development
                Legal
                
                ^pick a department   :   """)
    tik=np.arange(40000,100000,10000)
    tik2=np.arange(10000,150000,10000)
    z=data.groupby(['Department','Start Date'])[['Emp ID','Gender','Department','Salary','Start Date']].\
    agg({'Emp ID':'count','Department':'unique','Salary':'mean','Start Date':'unique'})
    gen=data.loc[data['Department']==i]
    gen2=gen.groupby('Gender')[['Gender','Emp ID']].agg({'Gender':'unique','Emp ID':'count'})
    top3=gen[['Name','Salary']].sort_values(by='Salary',axis=0,ascending=False).head(3)
    et=gen.groupby('Employee type')[['Employee type','Emp ID']].agg({'Employee type':'unique','Emp ID':'count'}).\
    sort_values(by='Emp ID',axis=0,ascending=False)
    st.use('Solarize_Light2')
    
    if i in dept:
        fig,ax=plt.subplots(2,2,figsize=(14,10))
        ax[0,0].plot(z['Start Date'].loc[z['Department']==i],z['Salary'].loc[z['Department']==i],c='red')
        ax[0,0].set_title('Salary progression per year on averaga')
        ax[0,0].set_xlabel('Year')
        ax[0,0].set_ylabel('Salary')
        ax[0,0].set_yticks(tik,[f'${a}k' for a in tik])
        ax[0,0].set_xticks(z['Start Date'].loc[z['Department']==i].astype('int'))
         
        ax[0,1].pie(gen2['Emp ID'],labels=gen2['Gender'],autopct='%.2f%%',colors=['red','green'])
        ax[0,1].set_title('Male vs Female')
        
        ax[1,0].bar(top3['Name'],top3['Salary'],color=['darkgreen','green','lightgreen'])
        ax[1,0].set_title('Top 3 highest paid employees')
        ax[1,0].set_xlabel('Employee')
        ax[1,0].set_ylabel('Salary')
        ax[1,0].set_yticks(tik2,[f'${a}k' for a in tik2])
        
        ax[1,1].bar(et['Employee type'].astype('str'),et['Emp ID'],color=['darkred','red','red'])
        ax[1,1].set_title('Employee type breakdown')
        ax[1,1].set_xlabel('Employee count')
        ax[1,1].set_ylabel('Employee type')
        
        fig.suptitle(f'Analysis Of {i} Department')
        plt.savefig('python2.png',dpi=300) 
        plt.show()
    else:
        print('invalid input....try again')
        continue
    j = input('Type "yes" to continue and any other character to exit  :  ')
    if j == 'yes':
        continue
    else:
        break
    


# In[ ]:





# In[ ]:




