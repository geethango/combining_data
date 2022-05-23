import pandas as pd
import os

team_list = os.listdir(r"C:\Users\geeth\Desktop\espn")
#print(team_list)
df2=pd.DataFrame()
df3=pd.DataFrame()
df5=pd.DataFrame()

t=[]


for team_name in team_list:
    #print(team_name)
    path=(r"C:\Users\geeth\Desktop\espn")
    path=os.path.join(path,team_name)
    l=os.listdir(path)
    #print(path)
    #if(l[1]=='skating'):
    for i in l:
     if(i == 'skating'):
        #print(team_name)
        #print(i)
        #df1=pd.read_csv(path+'/skating/2001-02 Regular Season.csv')
        df1=pd.read_csv(r'C:/Users/geeth/Desktop/espn/'+team_name+'/Goaltending/2019-20 Regular Season.csv')
        
        #df1 = df1.iloc[:-1 , :]
        df4=df1.mean(numeric_only=True)
        df3.append(df1.loc[j]
        # df=pd.read_csv(r'C:/Users/geeth/Desktop/espn/'+team_name+'/Goaltending/2019-20 Regular Season.csv')
        # #print(df)
        # #df=df.drop([5])
        
        # df2=df.mean(numeric_only=True)
        # df3 = pd.DataFrame(df3.append(df2, 
        #           ignore_index = True))
       
        # print(df2)
        #df3.append(df2,ignore_index=True)
        #print(df.mean(numeric_only=True))
#df3['names']=team_list 
df5['Visitor']=team_list      
#df3.to_csv('C:/Users/geeth/Desktop/new/2019-20avgGoaltending.csv')       
df5.to_csv('C:/Users/geeth/Desktop/new/2019-20avgGoaltending.csv')       