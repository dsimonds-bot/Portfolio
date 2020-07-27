# Over 24 Hour Converter

# datetime strptime works well parsing dates and hours on the standard 24 hour clock
# However, for time aggregations (like time on page within google analytics) these may exhibit a gross value over 23 hours.

# As such, the following function uses floor and mod functions to parse a user provided string and delimiter and convert it to datetime timedelta 
  # Arguments:
    # x = time string in Hour Minute Second format. Can use any user defined delimiter
    # d = delimiter, in string format
    
# ================================================================================================================================================ #

def time_convert(x, d):

    # Package Import
    import datetime as datetime
    from datetime import timedelta
    import math
    
    # Checking if the hour is over 23
    if int(x.split(d)[0]) > 23:
    
    # If over 23, initiate following code
        return timedelta(
            days = math.floor(int(x.split(d)[0])/24),    # Taking floor of total hours / 24 to get number of days
            hours = int(x.split(d)[0])%24,               # Taking mod of total hours against 24 to get hours argument
            minutes = int(x.split(d)[1]),                # Extracting minutes
            seconds = int(x.split(d)[2])                 # Extracting seconds
        )
        
    # If not over 23, initiate following code
    else:
        return timedelta(
            days = 0,                                      # We know day is zero due to the if > 23 statement
            hours = int(x.split(d)[0])%24,               # Same mod function in earlier block
            minutes = int(x.split(d)[1]),                # Same minutes extraction
            seconds = int(x.split(d)[2])                 # Same seconds extraction
        )
        
 
# Try it!
# a = '23:14:15'
# b = '32:16:01'
