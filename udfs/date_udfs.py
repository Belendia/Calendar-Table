import holidays
from datetime import date
from .ethiopian_date import EthiopianDateConverter

eth_holidays = holidays.ET()
#return the suffix of the ordinal day number. e.g., the "st" in "31st day of March"
#only works for two-digit or smaller integers
#only uses the whole number portion of any number passed (won't account for decimals)
def ordinalSuffix(number):

    #truncate any decimals, and use only last 2 digits of resutling integer
    number = number // 1 % 100

    if ( (number % 10 == 1) & (number // 10 != 1) ):
        suffix = 'st'
    elif ( (number % 10 == 2) & (number // 10 != 1) ):
        suffix = 'nd'
    elif ( (number % 10 == 3) & (number // 10 != 1) ):
        suffix = 'rd'
    else:
        suffix = 'th'

    return suffix

#used to find fields based on dow value
def mapDayOfWeekToOrdinalFieldName(dow_number):
    if   dow_number == 0: return 'mon'
    elif dow_number == 1: return 'tue'
    elif dow_number == 2: return 'wed'
    elif dow_number == 3: return 'thu'
    elif dow_number == 4: return 'fri'
    elif dow_number == 5: return 'sat'
    elif dow_number == 6: return 'sun'

#Function to convert Gregorian dates to Ethiopian dates
def convert_to_ethiopian(date):
     # Create an instance of EthiopianDateConverter
    converter = EthiopianDateConverter()
    # Convert the Gregorian date to Ethiopian date
    eth_date = converter.to_ethiopian(date.year, date.month, date.day)
    return "{:04d}-{:02d}-{:02d}".format(*eth_date)


# It extracts the year from an ethiopian date from stringIt retrieves the year, month, or day from an Ethiopian date represented as a string
def extract_year(date_string):
    try:
        # Split the string using '-' as the separator and extract the second element
        year = date_string.split('-')[0]
        return int(year)
    except (IndexError, ValueError):
        # Handle exceptions, return None if extraction fails
        return None

# It extracts the month from an ethiopian date from stringIt retrieves the year, month, or day from an Ethiopian date represented as a string
def extract_month(date_string):
    try:
        # Split the string using '-' as the separator and extract the second element
        month = date_string.split('-')[1]
        return int(month)
    except (IndexError, ValueError):
        # Handle exceptions, return None if extraction fails
        return None

# It extracts the day from an ethiopian date from stringIt retrieves the year, month, or day from an Ethiopian date represented as a string
def extract_day(date_string):
    try:
        # Split the string using '-' as the separator and extract the second element
        day = date_string.split('-')[2]
        return int(day)
    except (IndexError, ValueError):
        # Handle exceptions, return None if extraction fails
        return None

def check_eth_holiday(dt):
    result = date(dt.year, dt.month, dt.day) in eth_holidays
    return 1 if result else 0

def get_eth_holiday_label(date):
    return eth_holidays.get(date.strftime('%Y-%m-%d'))