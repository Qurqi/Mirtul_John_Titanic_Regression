import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import re
import statistics


        ####                                 
 #    ##    ##                       
#!#  # ^   ^  #                                      
 #   # 0   0  #                                      
  #   #  ~   #                                           
   ##  ##  ##                                        
     ##      ##                                  
      ##    ## #                             
       #    #   #                                            
       ######    #                               
       ##  ##                        
       ##  ##                                
    ##/#    #\##                                     


  # Takes dataframe as its argument and cleans data
  # returns cleaned data set as a dataframe
def clean_data(input_data):

  # Print out number of missing values in each column
  #print(input_data.isnull().sum())
  #print(input_data.shape)
  #print(input_data.info())

  # There are a lot of missing cabin values, so we will drop the column. We may come back and try to make inferences later.
  input_data = input_data.drop('Cabin', axis=1)

  #Drop other unneccessary information
  input_data = input_data.drop(['Name', 'Ticket', 'PassengerId'], axis=1)

  # We can infer the age values by modelling the distribution of the age values and sampling randomly from it
  #age_plot = input_data['Age'].hist(bins=50)
  #plot.show()

  # Model age with a standard normal. Plot reveals that normal is not a bad estimation
  # We could get more granular and fill in the age values by looking at parents/children, siblings/spouses, and fare, but we will keep it simple for now
  mean_age = input_data['Age'].mean()
  std_age = input_data['Age'].std()

  # Sample randomly from a standard normal distribution with corresponding mean and std. Sample size: num missing entries
  age_dist = abs(np.random.normal(mean_age, std_age, input_data['Age'].isnull().sum()))

  # Round all entries to the nearest integer 
  # Chose 'round' rather than 'floor' or 'ceil' because we retain more information from the normal distribution by rounding relative to the situation, instead of absolutely
  age_dist = [round(x) for x in age_dist]

  # Replace the missing values with the random age values
  input_data.loc[input_data['Age'].isnull(), 'Age'] = age_dist

  # Check Pclass for corresponding missing fare value
  #print(input_data[input_data['Fare'].isnull()])

  # Pclass is 3
  # Fill in missing fare value with the mean fare value of Pclass 3
  mean_fare = input_data.groupby('Pclass')['Fare'].mean()
  input_data.loc[input_data['Fare'].isnull(), 'Fare'] = mean_fare[3]

  # Fill missing Embarked Values
  # There is a correlation between price of far, Pclass and Embarked location

  # Check Pclass and Fare value to determine missing Embarked values
  #print(input_data[input_data['Embarked'].isnull()])

  # Pclass is 1 and fare is 80.0 for both missing values
  # What emabrked location has a mean fare closest to 80.0 for Pclass 1?
  mean_fare = input_data.groupby(['Pclass', 'Embarked'])['Fare'].mean()
  #print(mean_fare)
  # Embarked location C has a mean fare of 72.0 for Pclass 1. This is closer that Q's mean fare of 90.0
  # Fill in missing Embarked values with C
  input_data.loc[input_data['Embarked'].isnull(), 'Embarked'] = 'C'

  # Check for missing values
  #print(input_data.isnull().sum())

  # Convert string data into numbers
  # lets use 1 for female and 2 for male in sex, and 1 for C, 2 for Q, and 3 for S in Embarked
  input_data.replace('female', 1, inplace=True)
  input_data.replace('male', 2, inplace=True)
  input_data.replace('C', 1, inplace=True)
  input_data.replace('Q', 2, inplace=True)
  input_data.replace('S', 3, inplace=True)

  # return newly processed data
  return input_data












