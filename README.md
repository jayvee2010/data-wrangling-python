 # Lab Experiment Journal: Data Cleaning & Preprocessing with Pandas                           
                                                                                                
  ---                                                                                           
                                                                                                
  ## Experiment Details

  | Field | Value |
  |----------|-----------|
  | **Experiment Title** | Data Cleaning and Missing Value Handling using Pandas |
  | **Date** | 2026-03-18 |                                                                     
  | **Programming Language** | Python 3.x |
  | **Libraries Used** | pandas, numpy |                                                        
                                                                                                
  ---
                                                                                                
  ## 1. Objective 

  To understand and implement various data cleaning techniques including:                       
  - Identifying missing values in datasets
  - Handling missing values using different strategies (dropping, filling with default values,  
  mean/median/mode imputation)                                                                  
  - Data type conversion and standardization
  - Exporting cleaned datasets to CSV format                                                    
                  
  ---                                                                                           
                  
  ## 2. Prerequisites

  - Python 3.x installed
  - Required libraries:

  ```python
  import pandas as pd
  import numpy as np                                                                            
  
  ---                                                                                           
  3. Experiment Sections
                        
  3.1 Basic Missing Value Detection (DataFrame with NaN)
                                                                                                
  Purpose: Create a sample DataFrame with missing values and explore detection methods.         
                                                                                                
  Code Snippet:                                                                                 
                  
  df1 = pd.DataFrame({'A': [1, 2, 3, np.nan],                                                   
                       'B': [4, 5, 6, np.nan],
                       'C': [7, 8, 9, np.nan]})                                                 
                                                                                                
  Operations Performed:                                                                         
                                                                                                
  ┌─────────────────────┬─────────────────────────────┬─────────────────────────────────────┐
  │      Operation      │          Function           │             Description             │
  ├─────────────────────┼─────────────────────────────┼─────────────────────────────────────┤
  │ Display DataFrame   │ print(df1)                  │ Shows original data with NaN values │
  ├─────────────────────┼─────────────────────────────┼─────────────────────────────────────┤
  │ Detect NaN values   │ df1.isna()                  │ Returns boolean mask of missing     │   
  │                     │                             │ values                              │   
  ├─────────────────────┼─────────────────────────────┼─────────────────────────────────────┤   
  │ Count NaN per       │ df1.isna().sum()            │ Counts missing values in each       │   
  │ column              │                             │ column                              │
  ├─────────────────────┼─────────────────────────────┼─────────────────────────────────────┤   
  │ Drop rows with NaN  │ df1.dropna()                │ Removes rows containing any NaN     │
  │                     │                             │ values                              │   
  ├─────────────────────┼─────────────────────────────┼─────────────────────────────────────┤
  │ Fill with default   │ df1.fillna(value='DEFAULT') │ Replaces NaN with 'DEFAULT' string  │   
  ├─────────────────────┼─────────────────────────────┼─────────────────────────────────────┤
  │ Fill with mean      │ df1.fillna(df1.mean())      │ Replaces NaN with column mean       │
  │                     │                             │ values                              │   
  └─────────────────────┴─────────────────────────────┴─────────────────────────────────────┘
                                                                                                
  Observations:   
  - isna() returns a boolean DataFrame where True indicates missing values
  - dropna() removes entire rows even if only one value is missing                              
  - Mean imputation works only on numeric columns
                                                                                                
  ---             
  3.2 Student Dataset Cleaning                                                                  
                              
  Purpose: Create, clean, and export a student dataset with various data quality issues.
                                                                                                
  Original Data Structure:                                                                      
                                                                                                
  data = {                                                                                      
      "roll_no": [1, 2, 3, 4],                                                                  
      "name": ['Alice', 'Bob', 'Charlie', 'David'],                                             
      "marks": [85, 90, 95, 80],                                                                
      "age": [20, "-", 22, 21],                                                                 
      "department": ['CS', 'IT', 'CS', 'IT'],                                                   
      "admission_date": ['2020-01-15', '2020-02-20', '2020-03-10', '2020-04-05']                
  }                                                                                             
                                                                                                
  Data Cleaning Steps:                                                                          
                  
  ┌──────┬───────────────┬─────────────────────────────────────────────┬───────────────────┐    
  │ Step │   Operation   │                    Code                     │      Purpose      │ 
  ├──────┼───────────────┼─────────────────────────────────────────────┼───────────────────┤    
  │ 1    │ Replace       │ df.replace('-', np.nan, inplace=True)       │ Convert '-' to    │ 
  │      │ placeholder   │                                             │ proper NaN        │ 
  ├──────┼───────────────┼─────────────────────────────────────────────┼───────────────────┤ 
  │      │ Convert to    │                                             │ Handle            │ 
  │ 2    │ numeric       │ pd.to_numeric(df['age'], errors='coerce')   │ non-numeric       │    
  │      │               │                                             │ values            │ 
  ├──────┼───────────────┼─────────────────────────────────────────────┼───────────────────┤    
  │ 3    │ Fill age with │ df['age'].fillna(df['age'].mean(),          │ Impute missing    │    
  │      │  mean         │ inplace=True)                               │ age values        │ 
  ├──────┼───────────────┼─────────────────────────────────────────────┼───────────────────┤    
  │ 4    │ Fill marks    │ df['marks'].fillna(df['marks'].median(),    │ Impute missing    │    
  │      │ with median   │ inplace=True)                               │ marks             │ 
  ├──────┼───────────────┼─────────────────────────────────────────────┼───────────────────┤    
  │      │ Standardize   │                                             │ Convert           │ 
  │ 5    │ text          │ df["department"].str.upper()                │ department to     │    
  │      │               │                                             │ uppercase         │ 
  ├──────┼───────────────┼─────────────────────────────────────────────┼───────────────────┤    
  │      │               │                                             │ Parse date        │
  │ 6    │ Convert dates │ pd.to_datetime(df["admission_date"])        │ strings to        │    
  │      │               │                                             │ datetime objects  │
  └──────┴───────────────┴─────────────────────────────────────────────┴───────────────────┘    
                  
  Output Files:
  - students.csv - Raw dataset
  - students_cleaned.csv - Cleaned dataset

  Before vs After Cleaning:                                                                     
  
  ┌─────────────────┬──────────────────────────┬──────────────────────────┐                     
  │     Aspect      │          Before          │          After           │
  ├─────────────────┼──────────────────────────┼──────────────────────────┤
  │ Age data type   │ Mixed (int + string '-') │ Float (numeric)          │
  ├─────────────────┼──────────────────────────┼──────────────────────────┤
  │ Missing values  │ Present (marked as '-')  │ Imputed with mean        │
  ├─────────────────┼──────────────────────────┼──────────────────────────┤
  │ Department case │ Mixed case               │ Uppercase (standardized) │
  ├─────────────────┼──────────────────────────┼──────────────────────────┤
  │ Date format     │ String                   │ datetime64               │
  └─────────────────┴──────────────────────────┴──────────────────────────┘                     
  
  ---                                                                                           
  3.3 Cars93 Dataset Cleaning
                                                                                                
  Purpose: Clean a real-world automotive dataset by handling missing values.
                                                                                                
  Dataset: Cars93.csv (downloaded from external source)                                         
  
  Operations Performed:                                                                         
                  
  ┌────────────────┬────────────────────────┬──────────────────────────────────────────────┐    
  │     Column     │ Missing Value Strategy │                     Code                     │
  ├────────────────┼────────────────────────┼──────────────────────────────────────────────┤
  │ Luggage.room   │ Mean imputation        │ fillna(value=df['Luggage.room'].mean())      │
  ├────────────────┼────────────────────────┼──────────────────────────────────────────────┤
  │ Rear.seat.room │ Mean imputation        │ fillna(value=df['Rear.seat.room'].mean())    │    
  ├────────────────┼────────────────────────┼──────────────────────────────────────────────┤
  │ AirBags        │ Mode imputation        │ fillna(value=df['AirBags'].mode().values[0]) │    
  └────────────────┴────────────────────────┴──────────────────────────────────────────────┘

  Rationale for Strategy Selection:
  - Mean imputation for numeric columns (Luggage.room, Rear.seat.room) - Preserves average
  values                                                                                        
  - Mode imputation for categorical column (AirBags) - Uses most frequent category
                                                                                                
  Output File: Cars93_cleaned.csv

  ---
  4. Key Learnings

  4.1 Missing Value Detection Methods

  ┌─────────────────┬───────────────────┬────────────────────────────────┐
  │     Method      │      Returns      │            Use Case            │
  ├─────────────────┼───────────────────┼────────────────────────────────┤
  │ df.isna()       │ Boolean DataFrame │ Identify missing values        │
  ├─────────────────┼───────────────────┼────────────────────────────────┤
  │ df.isna().sum() │ Series of counts  │ Quick overview of missing data │
  ├─────────────────┼───────────────────┼────────────────────────────────┤
  │ df.isnull()     │ Same as isna()    │ Alternative syntax             │
  └─────────────────┴───────────────────┴────────────────────────────────┘

  4.2 Missing Value Handling Strategies

  ┌──────────────────┬────────────────────────┬─────────────────────────────────────────────┐
  │     Strategy     │         Method         │                 When to Use                 │
  ├──────────────────┼────────────────────────┼─────────────────────────────────────────────┤
  │ Dropping         │ df.dropna()            │ When missing data is minimal and rows are   │
  │                  │                        │ expendable                                  │
  ├──────────────────┼────────────────────────┼─────────────────────────────────────────────┤   
  │ Fill with        │ df.fillna(value)       │ When a default value makes sense            │
  │ constant         │                        │                                             │   
  ├──────────────────┼────────────────────────┼─────────────────────────────────────────────┤
  │ Mean imputation  │ df.fillna(df.mean())   │ For numeric data with normal distribution   │
  ├──────────────────┼────────────────────────┼─────────────────────────────────────────────┤   
  │ Median           │ df.fillna(df.median()) │ For numeric data with outliers              │
  │ imputation       │                        │                                             │   
  ├──────────────────┼────────────────────────┼─────────────────────────────────────────────┤
  │ Mode imputation  │ df.fillna(df.mode())   │ For categorical data                        │
  └──────────────────┴────────────────────────┴─────────────────────────────────────────────┘   
  
  4.3 Best Practices                                                                            
                  
  1. Always inspect data types before cleaning using df.dtypes                                  
  2. Convert placeholders (like '-', 'N/A', 'NULL') to proper NaN values first
  3. Use errors='coerce' when converting to numeric to handle invalid entries gracefully        
  4. Save cleaned data to a new file to preserve the original dataset                           
  5. Standardize text data (uppercase, lowercase) for consistency                               
                                                                                                
  ---                                                                                           
  5. Output Files Generated                                                                     
                                                                                                
  ┌──────────────────────┬─────────────────────────┬───────────────────────────┐
  │       Filename       │       Description       │         Location          │                
  ├──────────────────────┼─────────────────────────┼───────────────────────────┤
  │ students.csv         │ Raw student dataset     │ Current working directory │                
  ├──────────────────────┼─────────────────────────┼───────────────────────────┤
  │ students_cleaned.csv │ Cleaned student dataset │ Current working directory │                
  ├──────────────────────┼─────────────────────────┼───────────────────────────┤                
  │ Cars93_cleaned.csv   │ Cleaned Cars93 dataset  │ Current working directory │                
  └──────────────────────┴─────────────────────────┴───────────────────────────┘                
                  
  ---                                                                                           
  6. Conclusion   
                                                                                                
  This experiment successfully demonstrated:
  - Multiple techniques for identifying missing values in pandas DataFrames                     
  - Various imputation strategies (mean, median, mode) for handling missing data                
  - Data type conversion and standardization                                                    
  - Real-world application on automotive dataset                                                
                                                                                                
  The choice of imputation method depends on:                                                   
  - Data type (numeric vs categorical)                                                          
  - Data distribution (presence of outliers)
  - Domain knowledge and business requirements

  ---
  7. References
                                                                                                
  - Pandas Documentation: https://pandas.pydata.org/docs/
  - NumPy Documentation: https://numpy.org/doc/                                                 
  - Working with Missing Data:
  https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html
