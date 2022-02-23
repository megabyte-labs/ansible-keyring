""" Arrow makes it easy to work with datetimes in Python """

import arrow

# Get current datetimes
now = arrow.now()
utc_now = arrow.utcnow()

# Parse from string
created_from_timestamp = arrow.get("2021-09-19", "YYYY-MM-DD")

# Change timezone
pacific = utc_now.to("US/Pacific")

# Format time
formatted_pacific = pacific.format('YYYY-MM-DD HH:mm:ss')

# Shift time
thirty_minutes_from_now = pacific.shift(minutes=30)

# Get datetime representation (python stl)
thirty_minutes_from_now_datetime = thirty_minutes_from_now.datetime
