 # Lab Experiment Journal: Data Cleaning & Preprocessing with Pandas
    2
    3 ---
    4
    5 ## Experiment Details
    6
    7 | **Field** | **Value** |
    8 |----------|-----------|
    9 | **Experiment Title** | Data Cleaning and Missing Value Handling using Pandas |
   10 | **Date** | 2026-03-18 |
   11 | **Programming Language** | Python 3.x |
   12 | **Libraries Used** | pandas, numpy |
   13
   14 ---
   15
   16 ## 1. Objective
   17
   18 To understand and implement various data cleaning techniques including:
   19 - Identifying missing values in datasets
   20 - Handling missing values using different strategies (dropping, filling with default va
      lues, mean/median/mode imputation)
   21 - Data type conversion and standardization
   22 - Exporting cleaned datasets to CSV format
   23
   24 ---
   25
   26 ## 2. Prerequisites
   27
   28 - Python 3.x installed
   29 - Required libraries:
   30   ```python
   31   import pandas as pd
   32   import numpy as np
   33   ```
   34
   35 ---
   36
   37 ## 3. Experiment Sections
   38
   39 ### 3.1 Basic Missing Value Detection (DataFrame with NaN)
   40
   41 **Purpose:** Create a sample DataFrame with missing values and explore detection method
      s.
   42
   43 **Code Snippet:**
   44 ```python
   45 df1 = pd.DataFrame({'A': [1, 2, 3, np.nan],
   46                      'B': [4, 5, 6, np.nan],
   47                      'C': [7, 8, 9, np.nan]})
   48 ```
   49
   50 **Operations Performed:**
   51
   52 | Operation | Function | Description |
   53 |-----------|----------|-------------|
   54 | Display DataFrame | `print(df1)` | Shows original data with NaN values |
   55 | Detect NaN values | `df1.isna()` | Returns boolean mask of missing values |
   56 | Count NaN per column | `df1.isna().sum()` | Counts missing values in each column |
   57 | Drop rows with NaN | `df1.dropna()` | Removes rows containing any NaN values |
   58 | Fill with default | `df1.fillna(value='DEFAULT')` | Replaces NaN with 'DEFAULT' strin
      g |
   59 | Fill with mean | `df1.fillna(df1.mean())` | Replaces NaN with column mean values |
   60
   61 **Observations:**
   62 - `isna()` returns a boolean DataFrame where `True` indicates missing values
   63 - `dropna()` removes entire rows even if only one value is missing
   64 - Mean imputation works only on numeric columns
   65
   66 ---
   67
   68 ### 3.2 Student Dataset Cleaning
   69
   70 **Purpose:** Create, clean, and export a student dataset with various data quality issu
      es.
   71
   72 **Original Data Structure:**
   73 ```python
   74 data = {
   75     "roll_no": [1, 2, 3, 4],
   76     "name": ['Alice', 'Bob', 'Charlie', 'David'],
   77     "marks": [85, 90, 95, 80],
   78     "age": [20, "-", 22, 21],          # Contains non-numeric placeholder
   79     "department": ['CS', 'IT', 'CS', 'IT'],
   80     "admission_date": ['2020-01-15', '2020-02-20', '2020-03-10', '2020-04-05']
   81 }
   82 ```
   83
   84 **Data Cleaning Steps:**
   85
   86 | Step | Operation | Code | Purpose |
   87 |------|-----------|------|---------|
   88 | 1 | Replace placeholder | `df.replace('-', np.nan, inplace=True)` | Convert '-' to pr
      oper NaN |
   89 | 2 | Convert to numeric | `pd.to_numeric(df['age'], errors='coerce')` | Handle non-num
      eric values |
   90 | 3 | Fill age with mean | `df['age'].fillna(df['age'].mean(), inplace=True)` | Impute
      missing age values |
   91 | 4 | Fill marks with median | `df['marks'].fillna(df['marks'].median(), inplace=True)`
       | Impute missing marks |
   92 | 5 | Standardize text | `df["department"].str.upper()` | Convert department to upperca
      se |
   93 | 6 | Convert dates | `pd.to_datetime(df["admission_date"])` | Parse date strings to da
      tetime objects |
   94
   95 **Output Files:**
   96 - `students.csv` - Raw dataset
   97 - `students_cleaned.csv` - Cleaned dataset
   98
   99 **Before vs After Cleaning:**
  100
  101 | Aspect | Before | After |
  102 |--------|--------|-------|
  103 | Age data type | Mixed (int + string '-') | Float (numeric) |
  104 | Missing values | Present (marked as '-') | Imputed with mean |
  105 | Department case | Mixed case | Uppercase (standardized) |
  106 | Date format | String | datetime64 |
  107
  108 ---
  109
  110 ### 3.3 Cars93 Dataset Cleaning
  111
  112 **Purpose:** Clean a real-world automotive dataset by handling missing values.
  113
  114 **Dataset:** Cars93.csv (downloaded from external source)
  115
  116 **Operations Performed:**
  117
  118 | Column | Missing Value Strategy | Code |
  119 |--------|----------------------|------|
  120 | Luggage.room | Mean imputation | `fillna(value=df['Luggage.room'].mean())` |
  121 | Rear.seat.room | Mean imputation | `fillna(value=df['Rear.seat.room'].mean())` |
  122 | AirBags | Mode imputation | `fillna(value=df['AirBags'].mode().values[0])` |
  123
  124 **Rationale for Strategy Selection:**
  125 - **Mean imputation** for numeric columns (Luggage.room, Rear.seat.room) - Preserves av
      erage values
  126 - **Mode imputation** for categorical column (AirBags) - Uses most frequent category
  127
  128 **Output File:** `Cars93_cleaned.csv`
  129
  130 ---
  131
  132 ## 4. Key Learnings
  133
  134 ### 4.1 Missing Value Detection Methods
  135
  136 | Method | Returns | Use Case |
  137 |--------|---------|----------|
  138 | `df.isna()` | Boolean DataFrame | Identify missing values |
  139 | `df.isna().sum()` | Series of counts | Quick overview of missing data |
  140 | `df.isnull()` | Same as isna() | Alternative syntax |
  141
  142 ### 4.2 Missing Value Handling Strategies
  143
  144 | Strategy | Method | When to Use |
  145 |----------|--------|-------------|
  146 | Dropping | `df.dropna()` | When missing data is minimal and rows are expendable |
  147 | Fill with constant | `df.fillna(value)` | When a default value makes sense |
  148 | Mean imputation | `df.fillna(df.mean())` | For numeric data with normal distribution
      |
  149 | Median imputation | `df.fillna(df.median())` | For numeric data with outliers |
  150 | Mode imputation | `df.fillna(df.mode())` | For categorical data |
  151
  152 ### 4.3 Best Practices
  153
  154 1. **Always inspect data types** before cleaning using `df.dtypes`
  155 2. **Convert placeholders** (like '-', 'N/A', 'NULL') to proper `NaN` values first
  156 3. **Use `errors='coerce'`** when converting to numeric to handle invalid entries grace
      fully
  157 4. **Save cleaned data** to a new file to preserve the original dataset
  158 5. **Standardize text data** (uppercase, lowercase) for consistency
  159
  160 ---
  161
  162 ## 5. Execution Flowchart
  163
  164 ```
  165 ┌─────────────────────────────────────────────────────────────┐
  166 │                    EXPERIMENT WORKFLOW                      │
  167 ├─────────────────────────────────────────────────────────────┤
  168 │                                                             │
  169 │  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐  │
  170 │  │ Section 3.1  │    │ Section 3.2  │    │ Section 3.3  │  │
  171 │  │   (Basic)    │    │  (Students)  │    │  (Cars93)    │  │
  172 │  └──────┬───────┘    └──────┬───────┘    └──────┬───────┘  │
  173 │         │                   │                   │          │
  174 │         ▼                   ▼                   ▼          │
  175 │  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐  │
  176 │  │ Create DF    │    │ Create DF    │    │ Load CSV     │  │
  177 │  │ with NaN     │    │ Save to CSV  │    │ from file    │  │
  178 │  └──────┬───────┘    └──────┬───────┘    └──────┬───────┘  │
  179 │         │                   │                   │          │
  180 │         ▼                   ▼                   ▼          │
  181 │  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐  │
  182 │  │ isna(),      │    │ Replace '-'  │    │ Fill numeric │  │
  183 │  │ dropna(),    │    │ with NaN     │    │ with mean    │  │
  184 │  │ fillna()     │    │              │    │              │  │
  185 │  └──────┬───────┘    └──────┬───────┘    └──────┬───────┘  │
  186 │         │                   │                   │          │
  187 │         ▼                   ▼                   ▼          │
  188 │  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐  │
  189 │  │ Print output │    │ Convert types│    │ Fill category│  │
  190 │  │              │    │ Impute values│    │ with mode    │  │
  191 │  └──────────────┘    └──────┬───────┘    └──────┬───────┘  │
  192 │                             │                   │          │
  193 │                             ▼                   ▼          │
  194 │                      ┌──────────────┐    ┌──────────────┐  │
  195 │                      │ Save cleaned │    │ Save cleaned │  │
  196 │                      │ CSV file     │    │ CSV file     │  │
  197 │                      └──────────────┘    └──────────────┘  │
  198 │                                                             │
  199 └─────────────────────────────────────────────────────────────┘
  200 ```
  201
  202 ---
  203
  204 ## 6. Output Files Generated
  205
  206 | Filename | Description | Location |
  207 |----------|-------------|----------|
  208 | `students.csv` | Raw student dataset | `/Users/jiyu/` |
  209 | `students_cleaned.csv` | Cleaned student dataset | `/Users/jiyu/` |
  210 | `Cars93_cleaned.csv` | Cleaned Cars93 dataset | `/Users/jiyu/` |
  211
  212 ---
  213
  214 ## 7. Conclusion
  215
  216 This experiment successfully demonstrated:
  217 - Multiple techniques for identifying missing values in pandas DataFrames
  218 - Various imputation strategies (mean, median, mode) for handling missing data
  219 - Data type conversion and standardization
  220 - Real-world application on automotive dataset
  221
  222 The choice of imputation method depends on:
  223 - Data type (numeric vs categorical)
  224 - Data distribution (presence of outliers)
  225 - Domain knowledge and business requirements
  226
  227 ---
  228
  229 ## 8. References
  230
  231 - Pandas Documentation: https://pandas.pydata.org/docs/
  232 - NumPy Documentation: https://numpy.org/doc/
  233 - Working with Missing Data: https://pandas.pydata.org/pandas-docs/stable/user_guide/mi
      ssing_data.html
  234
