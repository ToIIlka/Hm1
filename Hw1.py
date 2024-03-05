from datetime import datetime
def get_days_from_today(date):
    try:
        input_data = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return None

    date_today = datetime.today()
    result = date_today - input_data
    return result.days

print(get_days_from_today("2010-10-09"))
print(get_days_from_today('2010/10/09'))