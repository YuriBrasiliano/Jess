import datetime


class SystemInfo:
    def __init__(self):
        pass

    def get_time():
        now = datetime.datetime.now()
        return now

    def get_date():
        hoje = datetime.date.today()
        return 'Its {0:%d} of {0:%B} of {0:%y}.'.format(hoje, "day", "month", "year")