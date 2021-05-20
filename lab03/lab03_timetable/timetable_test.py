from timetable import timetable
from datetime import date, time, datetime
import datetime

def test_for_timetable():
    assert(timetable([date(2019,9,27)], [time(14,10)]) == [datetime.datetime(2019, 9, 27, 14, 10)])
    assert(timetable([date(2019,9,27), date(2019,9,30)], [time(14,10), time(10,30)]) == [datetime.datetime(2019, 9, 27, 10, 30), datetime.datetime(2019, 9, 27, 14, 10), datetime.datetime(2019, 9, 30, 10, 30), datetime.datetime(2019, 9, 30, 14, 10)])
    