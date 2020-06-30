import datetime

TODAY = datetime.date.today()
YESTERDAY = TODAY - datetime.timedelta(days=1)
TOMORROW = TODAY + datetime.timedelta(days=1)
NEXT_WEEK = TODAY + datetime.timedelta(weeks=1)
