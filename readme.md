# Project Description

This is my first small project in data analysis and visualisation using the Python programming language.
The project is part of the "Introductory Machine Learning in Python" track offered by the online education
platform JetBrains Academy. This project is listed in the "hard" category.

## First stage
Imagine you are a data scientist and you're currently working with the data for local hospitals. You have several files with information about patients from different districts. Sometimes, the data is split into many datasets or may contain empty or invalid values. The first step is to preprocess the data before the analysis: merge the files into one, delete empty or incorrect rows, fill the missing values, and so on.

In this stage, you will deal with datasets that contain information about patients from three hospitals: a general, a prenatal, and a sports one. You need to upload the data from the hidden test directory of the project for further processing.

### Objectives
In this stage, your program should:

1. After all the libraries imports write the following line of code:
pd.set_option('display.max_columns', 8)
It sets the number of columns, which pandas lets to display in the terminal. Unfortunately, this number differs occasionally and causes problems in the tests, so we need to fix the number.
2. Read 3 CSV files containing the datasets 
3. Print the first 20 rows of each data frame. Use the following order: general, prenatal, sports

## Second Stage

Hooray, you have the datasets! However, they are somewhat difficult to work with. They are divided into three parts, and the column names are different: HOSPITAL and Sex in the prenatal, Hospital and Male/female in the sports facility. We cannot study our data in full and perform statistical calculations. It also stands in the way of good visualization.
In this stage, we will change the column names and merge our datasets into one. To combine the columns, use the concat function and the ignore_index = True parameter. After merging, a side Unnamed: 0 column will appear. This column contains the indexes of the tables. This column is not needed for the practical purposes of this project, so we will delete it in this stage.

### Objectives
In addition to the previous stage objectives
1. Change the column names. All column names in the sports and prenatal tables must match the column names in the general table
2. Merge the data frames into one. Use the ignore_index = True parameter and the following order: general, prenatal, sports
3. Delete the Unnamed: 0 column (first column)
4. Print random 20 rows of the resulting data frame. For the reproducible output set random_state=30


## Third Stage

Some cells in our table have NaN as values: the patient gender is not defined in the prenatal hospital, and the test columns are empty in all three tables. We still cannot commit to the analysis as the statistics are not going to be objective. We have to correct the table for further study.

Let's take a closer look at the gender column. It's a big mess: there we have female, male, man, woman. You need to correct the data in this column. The values should be either f or m. Replace the empty gender column values for prenatal patients with f (we can assume that the prenatal treats only women).

The bmi, diagnosis, blood_test, ecg, ultrasound, mri, xray, children, months columns also need to be corrected. Replace the NaN values of the columns above with zeros.

### Objectives
Steps 1-5 are the same as in the previous stage. The third stage additionally requires:
1. Delete all the empty rows
2. Correct all the gender column values to f and m respectively
3. Replace the NaN values in the gender column of the prenatal hospital with f
4. Replace the NaN values in the bmi, diagnosis, blood_test, ecg, ultrasound, mri, xray, children, months columns with zeros
5. Print shape of the resulting data frame
6. Print random 20 rows of the resulting data frame. For the reproducible output set random_state=30


## Fourth Stage

You have cleared your dataset of empty rows and values. Some values have also been corrected, and now we can start a comprehensive study of our data. In this stage, we will find the main statistical characteristics of our data, consider data distributions, and so on.

Answer the following questions and output the answers in the specified format.

Which hospital has the highest number of patients?

What share of the patients in the general hospital suffers from stomach-related issues? 
Round the result to the third decimal place.

What share of the patients in the sports hospital suffers from dislocation-related issues? 
Round the result to the third decimal place.

What is the difference in the median ages of the patients in the general and sports hospitals?

After data processing at the previous stages, the blood_test column has three values: 
t= a blood test was taken, f= a blood test wasn't taken, and 0= there is no information. 
In which hospital the blood test was taken the most often (there is the biggest number of t in 
the blood_test column among all the hospitals)? How many blood tests were taken?

### Objectives
This stage additionally requires:
1. Answer the 1-5 questions using the pandas library methods. 
2. Output the answers on the separate lines in the format given in the Example section.

### Fifth Stage

Graphics are arguably the most accessible way to represent the data and its structure. 
Sometimes, it can help to find the main data patterns and deviations. 
We will use data visualization methods to conclude our dataset.

In the last stage, you need to create data visualization to answer the following questions:

What is the most common age of a patient among all hospitals? 
Plot a histogram and choose one of the following age ranges: 0-15, 15-35, 35-55, 55-70, or 70-80

What is the most common diagnosis among patients in all hospitals? 
Create a pie chart

Build a violin plot of height distribution by hospitals. 
Try to answer the questions. What is the main reason for the gap in values? 

Why there are two peaks, which correspond to the relatively small and big values? 
No special form is required to answer this question
