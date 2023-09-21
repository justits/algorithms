import pandas as pd


def count_sessions_on_day(df: pd.DataFrame, day: str) -> int:
    """
    Count the number of sessions that started on a specific day.
    Args:
        df (pd.DataFrame): DataFrame containing user activity logs.
        day (str): Date in 'YYYY-MM-DD' format.
    Returns:
        int: Number of sessions.
    """
    df.sort_values(['user', 'date'], inplace=True)

    # Creating a column with a time difference between user events
    df['time_diff'] = df.groupby('user')['date'].diff()

    df['session_start'] = (df['time_diff'] >= pd.Timedelta(minutes=30))

    # Filter only sessions that started on a given day
    sessions_started_on_day = df[
        df['session_start'] & (df['date'].dt.date == pd.to_datetime(day).date())]

    # Counting the number of sessions
    session_count = sessions_started_on_day['session_start'].sum()
    return session_count


def max_uploaded_pictures_day(df: pd.DataFrame) -> (str, int):
    """
    Find the day with the maximum number of unique users who uploaded pictures.
    Args:
        df (pd.DataFrame): DataFrame containing user activity logs.
    Returns:
        str: Date in 'YYYY-MM-DD' format.
        int: Maximum number of users who uploaded pictures.
   """
    # Filtering events with type 3 and the 'picture' parameter
    image_upload_events = df[(df['event_type'] == 3) & (df['parameter'] == 'picture')]

    # Grouping by days and counting unique users
    daily_unique_users = image_upload_events.groupby(image_upload_events['date'].dt.date)['user'].nunique()

    # Finding the day with the maximum number of unique users
    max_users_day = daily_unique_users.idxmax()
    max_users_count = daily_unique_users[max_users_day]

    return max_users_day, max_users_count


def max_event_interval(df: pd.DataFrame) -> str:
    """
    Find the start time of the interval with the maximum number of events.
    Args:
        df (pd.DataFrame): DataFrame containing user activity logs.
    Returns:
        str: Start time of the interval in 'YYYY-MM-DD hh:mm:ss' format.
    """
    event_count = df \
        .groupby(pd.Grouper(key='date', freq='1S')) \
        .size() \
        .rolling(10 * 60, min_periods=1, closed='left') \
        .sum() \
        .reset_index(name='event_count') \
        .sort_values(['event_count', 'date'], ascending=False)

    # Find the start time of the interval with the maximum number of events
    max_interval = event_count.iloc[0]
    start_time_of_max_event_interval = max_interval['date'] - pd.Timedelta(minutes=10)

    return start_time_of_max_event_interval


if __name__ == "__main__":
    FILE_PATH = 'data/log.csv'

    # Load data
    logs = pd.read_csv(FILE_PATH)
    logs['date'] = pd.to_datetime(logs['date'], format='%Y-%m-%d_%H:%M:%S')

    # First task
    sessions_count = count_sessions_on_day(logs, '2020-04-11')
    print(f"Number of sessions that started on 2020-04-11: {sessions_count}")

    # Second task
    max_upload_day, max_users_count = max_uploaded_pictures_day(logs)
    print(
        f"Day with the maximum number of users who uploaded pictures: {max_upload_day}, Users count: {max_users_count}")

    # Third task
    max_event_interval = max_event_interval(logs)
    print(f"Start time of the interval with the maximum number of events: {max_event_interval}")
