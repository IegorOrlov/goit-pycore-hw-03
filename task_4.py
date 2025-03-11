import datetime as da
import re
from datetime import datetime as dada


def get_congratilation_date(birthday: str, year: int) -> dada.date:
    congratilation_date_str = re.sub(r"\d{4}", str(year), birthday)
    congratilation_date = dada.strptime(congratilation_date_str, "%Y.%m.%d").date()
    if congratilation_date.isoweekday() == 6:
        congratilation_date = congratilation_date + da.timedelta(days=2)
    elif congratilation_date.isoweekday() == 7:
        congratilation_date = congratilation_date + da.timedelta(days=1)
    return congratilation_date


def get_upcoming_birthdays(users: list[dict[str, str]]) -> list[dict[str, str]]:
    result = []
    today = dada.today().date()
    for user in users:
        congratulation_date = get_congratilation_date(user["birthday"], today.year)
        delta = congratulation_date - today
        print("delta:", delta.days)
        if delta.days < 0:
            congratulation_date = get_congratilation_date(
                user["birthday"], today.year + 1
            )

        if (delta.days < 7) and (delta.days >= 0):
            result.append(
                {
                    "name": user["name"],
                    "congratulation_date": dada.strftime(
                        congratulation_date, "%Y.%m.%d"
                    ),
                }
            )
    return result


users = [
    {"name": "John Doe", "birthday": "1985.03.11"},
    {"name": "Jane Smith", "birthday": "1990.03.15"},
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
