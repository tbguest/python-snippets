import datetime


"""
Nice method for retrieving (hours, mins) or (mins, secs) from a posix timestamp difference or timedelta object.
"""

some_posix_offset = 9845943

# returns (hours, minutes)
hours_mins = divmod(
    some_posix_offset / 60, 60
)

# returns (minutes, seconds)
mins_secs = divmod(
    some_posix_offset, 60
)

# or using a datetime object
time0 = datetime.datetime(1950, 1, 1, 0, 0, 0)
time1 = datetime.datetime.now()
difference = time1 - time0
minutes_in_day = 24 * 60

hours_since_epoch = divmod(
    difference.days * minutes_in_day + difference.seconds / 60, 60
)