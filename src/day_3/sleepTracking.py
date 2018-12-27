import pandas as pd
from enum import Enum

def guard_checkin(df:pd.DataFrame, guard_no: int, date: str)->pd.DataFrame:
    """
    Takes in an existing DF, guard's ID, and date of checkin to track sleep/
    wake. Adds a row for each minute of the guard's checkin

    Args:
        df:pd.DataFrame The dataFrame the rows will be appended to
        guard_no: int The id number of the guard being tracked
        date: str The date the guard was on duty
    
    Returns:
        The DataFrame with the guard check in data
    """
    mins = [int(min) for min in range(0,60)]
    nsertables = []
    for min in mins:
        nsertables.append({"Guard": guard_no, "Date": date, "Minute":min, "Wake":True})
    return df.append(nsertables, ignore_index=True)

def update_guard_sleep(df: pd.DataFrame, date: str, start_sleep: int, end_sleep: int)->pd.DataFrame:
    """
    Takes in a dataframe to be modified, using the date of the event logged, a 
    start time and end time, sets the 'Wake' parameter between the start and 
    end to False

    Args:
        df: pd.DataFrame The Dataframe that will have the 'Wake' column modified in
        date: str The date of the incident sleep
        start_sleep: int The beginning minute the guard slept
        end_sleep: int The ending minute the guard slept
    Returns:
        The updated DataFrame
    """
    df_updates = []
    for min in range(start_sleep, end_sleep):
        df_updates.append({'Date':date, 'Minute': min, 'Wake':False})
    #df[df['Date'==date, 'Guard'==guard_no, 'Minute'>=start_sleep, 'Minute'<=end_sleep], 'Wake'] = False
    df.update(df_updates, overwrite=True)


class LogType(Enum):
    """
    There are 3 types of log messages - this will help keep track of them
    """
    start_shift = "begins shift"
    falls_asleep = "falls asleep"
    wakes_up = "wakes up"

def get_log_type(log_line: str)->LogType:
    """
    Takes in a raw log and detects which LogType the log belongs to
    """
    if LogType.start_shift.value in log_line:
        return LogType.start_shift
    elif LogType.falls_asleep.value in log_line:
        return LogType.falls_asleep
    elif LogType.wakes_up.value in log_line:
        return LogType.wakes_up

def get_date_time(log_line:str)->(str,int):
    """
    From a log line this will pull out the date and time the log was captured. 
    Time is represented as the minute integer after midnight.

    Args:
        log_line: str The line of the log being interpreted
    Returns: 
        A tuple, first term indicating month-day second term indicating the 
        minute the event occurred
    """
    #[1518-06-08 00:49]
    date_time = log_line.split("[1518-")[1]
    date_time_split = date_time.split(' ')
    date_only = date_time_split[0]
    minute_only = date_time_split[1].split(':')[1][0:2]
    return (date_only, int(minute_only))

def get_guard_no(log_line:str)->int:
    """
    From a log line this will pull out the integer ID of a guard

    Args:
        log_line: str The line of the log being interpreted
    Returns: 
        Integer of the guard's ID
    """
    return int(log_line.split('#')[1].split(' ')[0])