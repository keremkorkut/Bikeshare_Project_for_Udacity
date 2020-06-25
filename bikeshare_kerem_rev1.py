import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!,with together')
    
    print('My name is Kerem Korkut:)')

        # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    check_input = 1

    while check_input==1:

          city = input('Would you like to see data for chicago, new york city, or washington?')

          if  city.lower() not in ("chicago","new york city","washington") :

            print ('Valid options are chicago, new york city, or washington')

            continue

          else :
              check_input=0

              break

             # get user input for month (all, january, february, ... , june)

    check_input = 1

    while check_input==1 :

          month = input('Which month? all, january, february, march, april, may, june?')

          if  month.lower() not in ("all","january","february","march","april","may","june") :

            print ('Valid options are all,january, february, march, april, may, june')

            continue

          else :
             check_input=0

             break

                 # get user input for day of week (all, monday, tuesday, ... sunday)

    check_input = 1

    while check_input==1  :

          day = input('Which day? all,monday,tuesday,wednesday,thursday,friday,saturday,sunday?')

          if  day.lower() not in ("all","monday","tuesday","wednesday","thursday","friday","saturday","sunday") :

            print ('Valid options are all,monday,tuesday,wednesday,thursday,friday,saturday,sunday')

            continue

          else :
             check_input=0

             break

    print('-'*40)

    return city, month, day

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

    # load data file into a dataframe

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.dayofweek

    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':

        months = ['january', 'february', 'march', 'april', 'may', 'june']

        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':

        days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

        day = days.index(day)

        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')

    start_time = time.time()

    # display the most common month

    most_common_month = df['month'].value_counts().idxmax()

    print("The most common month is :", most_common_month)

    # display the most common day of week

    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()

    print("The most common day of week is :", most_common_day_of_week)

    # display the most common start hour

    most_common_start_hour = df['hour'].value_counts().idxmax()

    print("The most common start hour is :", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    most_common_start_station = df['Start Station'].value_counts().idxmax()

    print("The most commonly used start station :", most_common_start_station)


    # display most commonly used end station

    most_common_end_station = df['End Station'].value_counts().idxmax()

    print("The most commonly used end station :", most_common_end_station)

    # display most frequent combination of start station and end station trip

    most_common_start_end_station = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).nlargest(n=1)

    print("The most commonly used start station and end station : {}, {}"\
            .format(most_common_start_end_station[0], most_common_start_end_station[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    total_travel = df['Trip Duration'].sum()

    print("Total travel time :", total_travel)

    # display mean travel time

    mean_travel = df['Trip Duration'].mean()

    print("Mean travel time :", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_counts = df['User Type'].value_counts()

    print("Counts of user types:", user_counts )

    # Display counts of gender

    if 'Gender' in df.columns:

        gender_counts = df['Gender'].value_counts()

        print("Counts of gender:", gender_counts)

    if 'Birth Year' in df.columns:

        # Display earliest, most recent, and most common year of birth

        birth_year = df['Birth Year']

        # the most earliest birth year
        earliest_year = birth_year.min()
        print("The most earliest birth year:", earliest_year)

        # the most recent birth year
        most_recent = birth_year.max()
        print("The most recent birth year:", most_recent)

        # the most common birth year
        most_common_year = birth_year.value_counts().idxmax()
        print("The most common birth year:", most_common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)

def display_data(df):

    index=0

    user_input='y'

    while user_input in ['yes','y','yep','yea'] and index+5 < df.shape[0]:
        user_input = input('would you like to display 5 rows of raw data? ').lower()
        print(df.iloc[index:index+5])
        index += 5

def main():

     while True:

        city, month, day = get_filters()

        df = load_data(city, month, day)

        time_stats(df)

        station_stats(df)

        trip_duration_stats(df)

        user_stats(df)

        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')

        if restart.lower() != 'yes':

            break

if __name__ == "__main__":
	main()
