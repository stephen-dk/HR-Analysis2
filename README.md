# HR Analysis 📊

![pydata2](https://github.com/stephen-dk/HR-Analysis2/assets/144712896/38c71452-aeb3-4d4d-960a-60b02dfae736)
--

## Introduction

This is a detailed record that aims to provide a transparent account of the analytical process employed in my HR data analytics project. The objective of this project is not only to showcase my ability to work with  python to extract and prepare data for use, but also to answer crucial questions from a large or complex datasets.


## Data Sorce

HR data: The dataset used in this analysis is a ".xlsx" file,containing detailed information about each employee in the company.

***Disclaimer*** : *This dataset does not represent any company, but just a dummy dataset to demonstrate my capabilities*


## Problem Statement

1. What is the total salary progression over time(Year) for each department.
2. total number of employees by employment type per department.
3. what is the gender breakdown of employees in the company for each department.
4. top 3 highest paid enployees per department.


##  Tools Used
- Python 

|Library|Function|
|-------|--------|
|Pandas |Provides a functional framework for handelin larg datasets.|
|Matplotlib|For data visualization.|
|Datetime|for working with datetime datatypes.|


## Data Preparation

The following tasks were performed in the preparation phase.

- data loading and inspection.
- Deleting redundant columns.
- Renaming the columns.
- Dropping duplicates.
- Cleaning and formatting individual columns.
- Handling NaN values in the dataset

*Dirty dataset* ☹️

![py_dirty](https://github.com/stephen-dk/HR-Analysis2/assets/144712896/6ac76010-4562-4f26-b4ac-99e27d3b408e)
--

*Clean dataset* 😃

![py_clean](https://github.com/stephen-dk/HR-Analysis2/assets/144712896/1dcac6fb-c6a4-4b18-a9d9-f77893f6ce52)
--

## How It Works
This project takes an input from the user and outpt the required result

```python
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
```


## Data Visualization

![python2](https://github.com/stephen-dk/HR-Analysis2/assets/144712896/5a2d9b4f-4e86-471b-95e4-289c11f785f1)
--


## Result And Conclution 

- Total money spent on employee salary was highest in 2020 and lowest in 2018.
- The sales department has 12 permanent,2 fixed term and 2 tempotary employees.
- 44% of total employees in sales are male and 56% are female.
- The top 3 highest paid employees in sales are Freda Legan, Antonetta Coggeshall and Roselle Wandrach.
