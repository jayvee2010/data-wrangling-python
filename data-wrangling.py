import pandas as pd
import numpy as np
df1=pd.DataFrame({'A': [1, 2, 3,np.nan], 'B': [4, 5, 6,np.nan], 'C': [7, 8, 9,np.nan]}) 
print(df1)
print(df1.isna())
print(df1.isna().sum())
print(df1.dropna())
print(df1.fillna(value='DEFAULT'))
print(df1.fillna(df1.mean()))

data={
    "roll_no":[1,2,3,4],
    "name":['Alice','Bob','Charlie','David'],
    "marks":[85,90,95,80],
    "age":[20,"-",22,21],
    "department":['CS','IT','CS','IT'],
    "admission_date":['2020-01-15','2020-02-20','2020-03-10','2020-04-05']
}
df=pd.DataFrame(data)
print(df)
#save as csv file
df.to_csv('students.csv', index=False)

df = pd.read_csv("students.csv")
print("original data:")
print(df)
df.replace('-', np.nan, inplace=True)

df['age'] = pd.to_numeric(df['age'], errors='coerce')
df['marks'] = pd.to_numeric(df['marks'], errors='coerce')

print("\n missing values:")
print(df.isnull().sum())
df['age'].fillna(df['age'].mean(), inplace=True)
df['marks'].fillna(df['marks'].median(), inplace=True)

print(df.isnull().sum())
df["department"] = df["department"].str.upper()
df["admission_date"] = pd.to_datetime(df["admission_date"], errors='coerce')
print(df)

print("\n cleaned data :")
print(df)

#save cleaned dataset
df.to_csv('students_cleaned.csv', index=False)
print("\n cleaned data saved to students_cleaned.csv")



df=pd.read_csv('/Users/jiyu/Downloads/Cars93.csv')
print(df.head())

df['Luggage.room']=df['Luggage.room'].fillna(value=df['Luggage.room'].mean())
df['Rear.seat.room']=df['Rear.seat.room'].fillna(value=df['Rear.seat.room'].mean())
df['AirBags']=df['AirBags'].fillna(value=df['AirBags'].mode().values[0])

df.to_csv('Cars93_cleaned.csv', index=False)

