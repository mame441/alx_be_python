#Program to access the current date and time

#First import datetime module 

import datetime

#Import time delta explicetly
from datetime import timedelta

#Define a function that return current date and time

def display_current_datetime():
    current_date = datetime.datetime.now() #A variable to retrive current date and time
    print(f'Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}') # Print the formatted current date and time


#Define a function to calculate the future date and time

def calculate_future_date():
    #Prompt users to enter the number of days to be added
    number_of_days = int(input('Enter the number of days to add to the current date: '))
    
    #Calculate the future date
    future_date = datetime.datetime.now() + timedelta(days=number_of_days)
    
    #Print the  future date 

    print(f'Future date: {future_date.strftime("%Y-%m-%d")}')


display_current_datetime() #run the function that display the current date and time 


calculate_future_date()  #run the function that display the future date and time




