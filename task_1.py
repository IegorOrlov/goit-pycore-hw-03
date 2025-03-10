import datetime as da
from datetime import datetime as dada


def get_days_from_today(date: str) -> int:
    try:
        datetime = dada.strptime(date, "%Y-%m-%d")
    except ValueError:
        print(f"The data {date} does not match format 'YYYY-mm-dd'")
        return None
    today = dada.today()
    delta = today - datetime
    return delta.days


date_str = input("Inpit date in folloeing format 'YYYY-mm-dd'")
print(f"The difference with current date is: {get_days_from_today(date_str)}")
