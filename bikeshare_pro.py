import time
import pandas as pd
import numpy as np
import datetime

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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = str(input('Enter city to analyze: ')).lower()
    while city not in CITY_DATA.keys():
        print('Invalid city! Try one of {chicago, new york city, washington}')
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    month = str(input('Enter month name to analyze: ')).lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = str(input('Enter day of week to analyze: ')).lower()

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

    # TO DO: display the most common month
    month_num = df['month'].mode()[0]
    datetime_object = datetime.datetime.strptime(str(month_num), "%m")
    month_name = datetime_object.strftime("%B")
    print('Most common month of travel is:', month_name)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day of week of travel is:', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most common day of week of travel is:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used start station:', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Most commonly used end station:', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    combo = df.groupby(['Start Station', 'End Station'])['Unnamed: 0'].count()
    print('Most frequent combination of start station and end station trip:',combo.idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel duration:',df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Total travel duration:',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types:\n',df['User Type'].value_counts())

    # TO DO: Display counts of gender
    try:
        print('Counts of gender:\n',df['Gender'].value_counts())
    except KeyError:
        print('No gender data available for this city!')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common = int(df['Birth Year'].mode()[0])

        print('Earliest birth year is {}, most recent birth year is {}, most common birth year is {}.'.format(earliest, recent, common))
    except KeyError:
        print('No birth year data available for this city!')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """ Display raw data per user request. """
    start_loc = 0
    while True:
        rawdata = input('\nWould you like to see 5 rows of the raw data? Enter yes or no.\n')
        if rawdata.lower() != 'yes':
            break

        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        print('-'*40)


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
