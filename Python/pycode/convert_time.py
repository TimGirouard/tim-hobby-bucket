def convert_to_minutes(num_hours):
    '''
    (int) ->int

    Convert a number of hours into an
    equivalent number of minutes.
    
    >>>convert_to_minutes(2)
    120
    >>>convert_to_minutes(3)
    180
    '''

    minutes = num_hours * 60
    return minutes

def convert_to_seconds(num_hours):
    '''
    (int) ->int

    Convert a number of hours into an
    equivalent number of seconds.
    
    >>>convert_to_seconds(2)
    7200
    >>>convert_to_seconds(3)
    10800
    '''

    minutes = convert_to_minutes(num_hours)
    seconds = minutes * 60
    return seconds

seconds = convert_to_seconds(2)
