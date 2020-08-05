#!/usr/bin/env python
# coding: utf-8

# Frist We Need to Imports all Lib We need

# In[1]:


import time
import pandas as pd
import numpy as np


# Second We want to Declare City Months and Day

# In[2]:


# for Citys 


'''
CITY_DATA = { 'chicago': "C:/Users/kholoud/Desktop/CLoud/chicago.csv",
              'new york city': "C:/Users/kholoud/Desktop/CLoud/new_york_city.csv",
              'washington': "C:/Users/kholoud/Desktop/CLoud/washington.csv "
            }

'''

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }




City = ['chicago', 'washington ','new york city']


# for Months 

Months = [ 'january', 'february', 'march', 'april', 'may', 'june','all']

# for Days 

Days = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']




# Now we Get  Data Info from User Like Month , city , Day 

# In[3]:



def get_filters():
    
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        
    """
    
    
    
    print ("                                 *********************************************                                   ")
    print ('                                  Hello! Let\'s explore some US bikeshare data!                                  ')
    print ("                                 *********************************************                                   ")

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
     
    City_Input = ''
    while City_Input not in CITY_DATA:
        print("Which City You Want to know the Data  ? ")
        print("chicago")
        print("new york city")
        print("washington")
        City_Input=input().lower()
        
        if City_Input in CITY_DATA:
            city = City_Input
            print ( ' So Cool Let s go to', city )
        else:
            
            print("You Enter city Not Avilable , Please Enter Name right ")
    #----------------------------------------------------------------------------------------------------------------------

    # TO DO: get user input for month (all, january, february, ... , june)
    Month_Input = ''
    while Month_Input not in Months:
        
            
        print("filter by Months ?")
        print( 'january')
        print('february')
        print('March')
        print('April')
        print('May')
        print('June')
        print(" or All to NO month ?")
        Month_Input = input().lower()
        if Month_Input in Months:
            #We were able to get the name of the month to analyze data.
            month = Month_Input
            if month =='all':
                print ( 'it is avilable for you More Analyze , wonderfull !! ', month )
            else :
                print('it is my Favorite Month , let s go Analyze -->', month )
        else:
            print("You Enter Month Not Avilable , Please Enter Name right  or All for No Month ")
   #----------------------------------------------------------------------------------------------------------------------

   # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_Input =''
    while day_Input not in Days:
        print("filter by Days ?")
        print( 'Sunday')
        print('Monday')
        print('Tuesday')
        print('Wednesday')
        print('Thursday')
        print('Friday')
        print('Saturday')
        print(" or All to NO Days ?")        
        day_Input = input().lower()
        if day_Input in Days:
            day = day_Input
            if day =='all':
                print ( 'it is avilable for you More Analyze , wonderfull !! ', day )
            else :
                print('it is my Favorite day , let s go Analyze -->', day )

        else:
             print("You Enter Days Not Avilable , Please Enter Name right  or All for No Days ")

    


    print('-'*40)
    return city ,month ,day


# In[4]:


#c,m ,d= get_filters()


# Now in Second Part i need to Filter Dataframe Use The info i get in previous Function 

# In[5]:


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    
    
    
    
    
    DataFrame = pd.read_csv(CITY_DATA[city])
    # need to convert Start Time to Date time to Able to get month and day
    DataFrame['Start Time'] = pd.to_datetime(DataFrame['Start Time'])
  
    # make a new column to Hours 

    DataFrame['hour'] = DataFrame['Start Time'].dt.hour
    
    # make a new column to Days 

    DataFrame['Day']  = DataFrame['Start Time'].dt.weekday_name
    
    DataFrame['Day'] = DataFrame['Day'].str.lower()
    # make a new column to Months 
    DataFrame['month'] = DataFrame['Start Time'].dt.month
    

    
    #-------------------------------------------------------------
    
    #filter by  Month 
    if month != 'all':
        month = Months.index(month)+1

        DataFrame = DataFrame.loc[DataFrame['month'] == month]
        


        
    #-----------------------------------------------------------------   
    if day != 'all':
        DataFrame = DataFrame.loc[DataFrame['Day'] == day]


    return DataFrame


# In[6]:


#df = load_data(c,m ,d)
#df


# In[7]:



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # to get most common i need to know mode for Month
    common_month = df['month'].mode()[0]
    print(common_month)
    print("The most common month  " , Months[common_month])


    # TO DO: display the most common day of week
    print(df['Day'])
    common_day = df['Day'].mode()[0]
    print("The most common Day  " ,  common_day)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print("The most common hour  " ,  common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[8]:


#time_stats(df)


# In[9]:



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    start_station = df['Start Station'].mode()[0]
    print("The most common start station  " , start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print("The most common end_station " , end_station)


    # TO DO: display most frequent combination of start station and end station trip
    combination = (df['Start Station'] +" <--AND--> " + df['End Station']).mode()[0]
    
    print("The most  combination of start station and end station: " + combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[10]:


#station_stats(df)


# In[11]:



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()
    print("The most total travel time " , travel_time)




    # TO DO: display mean travel time
    
    travel_time_mean= df['Trip Duration'].mean()
    print("The most total travel time " , travel_time_mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[12]:


#trip_duration_stats(df)


# In[13]:



def user_stats(df ,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_types = df['User Type'].value_counts()
    print("The count of user types  \n" ,user_types)

    # TO DO: Display counts of gender
    
    if city == 'chicago' or city == 'new york city':
        gender = df['Gender'].value_counts()
        print("The count of user gender " ,gender)


        # TO DO: Display earliest, most recent, and most common year of birth
        earliest = df['Birth Year'].min()
        most_recent= df['Birth Year'].max()
        most_common= df['Birth Year'].mode()[0]
        print('Earliest birth ', earliest)
        print('Most recent birth ', most_recent)
        print('Most common birth ', most_common) 


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[14]:


def display_Five_row(df):
    print(df.head())
    next_step = 0
    while True:
        print( "are you want see the next five row from Data frame ?")
        print("Choice Yes Or No ?")
        Choice = input().lower() 
        if Choice != 'yes':
            return
        next_step = next_step + 5
        print(df.iloc[next_step:next_step+5])
        


# In[15]:


#user_stats(df ,'washington' )


# In[16]:


def main():
    

    while True:
            city, month, day = get_filters()
            df = load_data(city, month, day)

            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df,city)

            while True:
                
                print( "are you want see the next five row from Data frame ?")
                print("Choice Yes Or No ?")
                Choice = input().lower() 
                if  Choice != 'yes':
                    break
                display_Five_row(df)
                break

            
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break


if __name__ == "__main__":
	main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




