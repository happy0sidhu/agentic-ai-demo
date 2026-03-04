from datetime import datetime


def get_current_time():
    """
    Returns the current system time.
    """

    now = datetime.now()

    return now.strftime("%Y-%m-%d %H:%M:%S")