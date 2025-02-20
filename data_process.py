import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plot
import re

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


# Load dataset
input_data = pd.read_csv('data/new_data.csv')

# save the new data to a csv file



# Print out number of missing values in each column
print(input_data.isnull().sum())
print(input_data.shape)
print(input_data.info())
# Fill in missing values with NaN


# Print data dimensions to see how impactful the missing values are

# Duplicate the data set



# Figure out sex based on regular expression that searches name for Mr, Mrs. or Miss.

# Drop Cabin and Embarked columns due to many missing entries. Fare data likely embeds cabin info because higher price gets you nicer cabin.

# Drop Name and Ticket columns because they are not likely to be useful in predicting survival

# Figure out Fare based on pclass and embarked 

# Figure out cabin based on Fare? Also, parch?





