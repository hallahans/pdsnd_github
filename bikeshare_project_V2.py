import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = {'january','february','march', 'april' 'may' 'june'}

DAY_DATA = {'sunday' 'monday' 'tuesday' 'wednesday' 'thursday' 'friday' 'saturday'}

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
    city = []
    while city not in ['chicago', 'new york city', 'washington']:
        city = str(input("Which city would you like to explore? \n 'Chicago', 'New York City' or 'Washington'? ")).lower()
        if city.islower == 'chicago':
            return 'chicago.csv'
        elif city.islower == 'new york city':
            return 'new_york_city.csv'
        elif city.islower == 'washington':
            return 'washington'
        else:
            print("Please enter 'Chicago', 'New York City' or 'Washington' as city input! ")


    # TO DO: get user input for month (all, january, february, ... , june)
    month =[]
    while month not in ['all', 'january','february','march', 'april', 'may', 'june']:
        month = str(input("Which month would you like to explore? Type either 'all' or the respective month from 'January' to 'June'. ")).lower()
        if month not in ['all', 'january','february','march', 'april', 'may' ,'june']:
            print('This did not work. Please try again. \n ')




    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day =[]
    while day not in ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
        day = str(input("Which day of the week would you like to explore? Type either 'all' or the respective day. ")).lower()
        if day not in ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
               print('This did not work. Try again. \n ')

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

    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    index = df['month'].mode()[0]
    most_com_month = months[index - 1]
    #print (index)
    #print (most_com_month)
    print('The most common month is {}.'.format(most_com_month))


    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    most_com_dow = df['day_of_week'].mode()[0]
    print('The most common day is {}.'.format(most_com_dow))
    #print(most_common_month)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common start hour is: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_com_start = df['Start Station'].mode()[0]
    print ('The most common start station is: ', most_com_start)

    # TO DO: display most commonly used end station
    most_com_end = df['End Station'].mode()[0]
    print ('The most common end station is: ', most_com_end)

    # TO DO: display most frequent combination of start station and end station trip

    #Creating a 'journey' column that concatenates 'start_station' with
    # 'end_station' for the use popular_trip() function
    df['journey'] = df['Start Station'] + ' to ' + df['End Station']

    most_com_trip = df['journey'].mode()[0]
    print ('The most common trip is: ', most_com_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    start_time = time.time()

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    minute, second = divmod(total_travel_time, 60)
    hour, minute = divmod(minute, 60)
    print('The total trip duration is {} hours, {} minutes and {}'
          ' seconds.'.format(hour, minute, second))

    # TO DO: display mean travel time
    average_duration = df['Trip Duration'].mean()
    m, s = divmod(average_duration, 60)
    if m > 60:
        h, m = divmod(m, 60)
        print('The average trip duration is {} hours, {} minutes and {}'
              ' seconds.'.format(h, m, s))
    else:
        print('The average trip duration is {} minutes and {} seconds.'.format(m, s))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The user type distribution is: \n', user_types)


    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        gender = df['Gender'].value_counts()
        print('The gender distribution is: \n',gender)
    else:
        print("Gender column does not exist for this city! ")

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        earliest_year = int(df['Birth Year'].min())
        print ('The earliest birth year is: ', earliest_year)
        latest_year = int(df['Birth Year'].max())
        print ('The most recent birth year is: ', latest_year)
        most_com_year = int(df['Birth Year'].mode()[0])
        print ('The most common birth year is: ', most_com_year)
    else:
            print("Birth year column does not exist for this city! ")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def showdata(df):
    """Function asking user if they would like to see some data"""
    def is_valid(show):
        if show.lower() in ['yes', 'no']:
            return True
        else:
            return False
    head = 0
    tail = 5
    valid_input = False
    while valid_input == False:
        show = input('\nWould you like to see some data? '
                        'Enter\'yes\' or \'no\'.\n')
        valid_input = is_valid(show)
        if valid_input == True:
            break
        else:
            print("Sorry, something went wrong. Please type 'yes' or 'no'.")
    if show.lower() == 'yes':
        print(df.iloc[head:tail])
        show_more = ''
        while show_more.lower() != 'no':
            valid_input_2 = False
            while valid_input_2 == False:
                show_more = input('\nWould you like to see more data? Type \'yes\' or \'no\'.\n')
                valid_input_2 = is_valid(show_more)
                if valid_input_2 == True:
                    break
                else:
                    print("Sorry, something went wrong. Please type 'yes' or 'no'.")
            if show_more.lower() == 'yes':
                head += 5
                tail += 5
                print(df.iloc[head:tail])
            elif show_more.lower() == 'no':
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        showdata(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
