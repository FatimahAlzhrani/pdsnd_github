import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks the user to specify the city, month, and day to display the data analysis .
    """

    print('Hello! want to explore some US bikeshare data?! then Let\'s start ! ')

    
    # Filter by city: get user input for city (chicago, new york city, washington).
    
    city = input('\nWhich city would you like to filter by?\nNew York City \nChicago \nWashington\n').strip().lower()
    while city not in(CITY_DATA.keys()) :
            print ('invalid input. Please enter a valid value.')
            city = input('\nWhich city would you like to filter by?\nNew York City \nChicago \nWashington\n').strip().lower()
   

    # Filter by month: get user input for month (all, january, february, ... , june)

    months = ['january', 'february', 'march', 'april', 'may', 'june','all']
    month = input('Which month would you like to filter by?- January, February, March, April, May, June or all?\n ').strip().lower()
    while month not in months:
        print('invalid input. Please enter a valid value.')
        month = input('Which month would you like to filter by? - January, February, March, April, May, June or all? ').strip().lower()    
    

    # Filter by day: get user input for day of week (all, monday, tuesday, ... sunday)


    days= ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    day = input ("Do you want details specific to a particular day? If yes, type day name else type 'all'. \n").strip().lower()
    while day not in days:
        print('invalid input. Please enter a valid value.')
        day = input("Do you want details specific to a particular day? If yes, type day name else type 'all'.").strip().lower()

    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    """
   # load data file into a dataframe

    df = pd.read_csv(CITY_DATA[city])

   # convert the Start Time column to datetime

    df['Start Time'] = pd.to_datetime(df['Start Time'])

   # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

   # filter by month if applicable

    if month != 'all':
        # use the index of the months list to get the corresponding int

        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe

        df = df[df['month'] == month]


    # filter by day of week if applicable

    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = df['month'].mode()[0]
    print(f'The most common month is: {months[month-1]}')

    # display the most common day of week

    day = df['day_of_week'].mode()[0]
    print('The most common day of week is:'+ day)

    # display the most common start hour

    df['Start_hour'] = df['Start Time'].dt.hour
    common_hour = df['Start_hour'].mode()[0]
    print('Most Common Hour:', common_hour)

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)

    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    popular_start_station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:'+ popular_start_station)

    # display most commonly used end station

    popular_end_station = df['End Station'].mode()[0]
    print('Most popular end station is:' + popular_end_station)

    # display most frequent combination of start station and end station trip

    popular_trip = df['Start Station'] + ' to ' + df['End Station']
    print( 'Most popular trip is: from' + popular_trip.mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    Total_Time=60*60*24
    Total_Travel_Time = df['Trip Duration'].sum()
    print('Total travel time:', Total_Travel_Time/Total_Time, " Days")

    # display mean travel time

    Mean_Time=60
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time/Mean_Time, " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    print(df['User Type'].value_counts())
    print('\n\n')


    # Display counts of gender

    try:    
        gender_count = df['Gender'].value_counts().to_frame()
        print('Counts of each gender :\n' ,gender_count)
    except KeyError:
        print("\nGender Types:\nNo data available for this month.")

    # display earliest, most recent, and most common year of birth

    try:
        Earliest_Year = df['Birth Year'].min()
        print('\nEarliest Year:', Earliest_Year)
        Most_Recent_Year = df['Birth Year'].max()
        print('\nMost Recent Year:', Most_Recent_Year)
        Most_Common_Year = df['Birth Year'].value_counts().idxmax()
        print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
        print("\n\nSorry, No data available for this month.")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def display_raw_data(city):
    """
     The fuction takes the city name from get_filters fuction as input 
    and returns the raw data of that city by chunks of 5 rows.
    Args:
        (str) city - name of the city to return the raw data.
    Returns:

        city- raw data of that city by chunks of 5 rows.s
        display_raw - raw data of that city by chunks of 5 rows.

    """
    print('\nRaw data is available to check... \n')

    display_raw = input("Do you want to display raw data? Type Yes or No\n").strip().lower()
    
    while display_raw == 'yes':
          try:
          
             for raw in pd.read_csv(CITY_DATA[city], rawsize=5):
                print(raw) 
                
                # repeating the question

                display_raw = input("Do you want to have a look on more raw data? Type Yes or No\n").strip().lower()
                if display_raw != 'yes':
                    print('Thank You')
                    break

          except KeyboardInterrupt:
            clear()
            print('Thank you.')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)

      

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Thank You')
            break


if __name__ == "__main__":
	main()

