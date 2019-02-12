import time
import pandas as pd
import numpy as np

# dictonary for files
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
    cities = ('washington', 'chicago', 'new york city')
    while True:
        try:
            city = input("Would you like to see data for Chicago, New York City, or Washington? ").lower()
            if city in cities:
                break
            else:
                print('That\'s not a valid city. Please try again: ')
        except KeyError:
            print("That\'s not a valid city. Try again: ")

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ('january', 'february', 'march', 'april', 'may', 'june')
    while True:
         try:
            month = input("Which month - January, February, March, April, May, or June? ").lower()
            if month in months:
                break
            else:
                print("That\'s not a valid month. Try again: ")
         except:
            print("That\'s not a valid month. Try again: ")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all')
    while True:
          try:
             day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all? ").lower()
             if day in days:
                break
             else:
                print("That\'s not a valid day. Try again: ")
          except:
             print("That\'s not a valid day. Try again: ")

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
    df['day'] = df['Start Time'].dt.weekday_name


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
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('The most common month is: ', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day'].mode()[0]
    print('The most common day is: ', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    hour_format = (popular_hour, %I %p)
    print('The most common starting hour is: ', hour_format)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('The most popular Start Station is: ', popular_start)

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('The most popular End Station is: ', popular_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start End'] = df['Start Station'] + ' and ' + df['End Station']
    popular_start_end = df['Start End'].value_counts().idxmax()
    print('The most popular route is: ', popular_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_total = df['Trip Duration'].sum()
    print('The total travel time is: ', trip_total)

    # TO DO: display mean travel time
    trip_average = df['Trip Duration'].mean()
    print('The average travel time is: ', trip_average)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = pd.value_counts(df['User Type'])
    print("User Types: \n", user_types)

    # TO DO: Display counts of gender
    city, month, day = get_filters()

    if city != 'washington':
       gender_types = pd.value_counts(df['Gender'])
       print("Gender Types: \n", gender_types)
    else:
       print("No Gender data available for Washington.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        birth_min = int(df['Birth Year'].min())
        print('The earliest Birth Year is: ', birth_min)
        birth_max = int(df['Birth Year'].max())
        print('The most recent Birth Year is: ', birth_max)
        birth_mode = int(df['Birth Year'].mode())
        print('The most common Birth Year is: ', birth_mode)
    else:
        print("No Birth Year data available for Washington.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # ask if user wants to see raw data and restart program
        raw_data = input('\n Would you like to see 5 rows of raw data? y or n: ').lower()
        if raw_data != 'n':
            i = 0
            while True:
                print(df.iloc[i:i+5])
                i += 5
                more_rows = input('Would you like to see more data? y or n: ').lower()
                if more_rows != 'n':
                    break
        else:
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break


if __name__ == "__main__":
	main()
