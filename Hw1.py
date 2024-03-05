from datetime import datetime
def get_days_from_today(date):
    try:
        input_data = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return None

    data_today = datetime.today()
    result = data_today - input_data
    return result.days

print(get_days_from_today("2010-10-09"))
print(get_days_from_today('2010/10/09'))