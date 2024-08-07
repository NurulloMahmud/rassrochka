import re
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def is_valid_phone_number(phone_number):
    # Define a regex pattern for a valid phone number format
    pattern = re.compile(r'^\+?1?\d{9,15}$')
    
    # Match the input phone number with the pattern
    if pattern.match(phone_number):
        return True
    else:
        return False
    
def is_valid_email(email):
    # Define a regex pattern for a valid email format
    pattern = re.compile(
        r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    )
    
    # Match the input email with the pattern
    return bool(pattern.match(email))

def get_next_month_same_day(date_str, months: int):
    # Parse the input date string into a datetime object
    date = datetime.strptime(date_str, "%Y-%m-%d")
    
    # Add one month using relativedelta
    next_month_date = date + relativedelta(months=months)
    
    return next_month_date

def get_next_week_same_day(date_str, weeks: int):
    # Parse the input date string into a datetime object
    date = datetime.strptime(date_str, "%Y-%m-%d")
    
    # Add one week using timedelta
    next_week_date = date + timedelta(weeks=weeks)
    
    return next_week_date

def get_next_day(date_str, days: int):
    # Parse the input date string into a datetime object
    date = datetime.strptime(date_str, "%Y-%m-%d")
    
    # Add one day using timedelta
    next_day_date = date + timedelta(days=days)
    
    return next_day_date