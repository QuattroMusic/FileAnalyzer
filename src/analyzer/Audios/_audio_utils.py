import audioread

#TODO: Upgrade execution speed

def duration_detector(length):
    hours = length // 3600  # calculate in hours
    length %= 3600
    mins = length // 60  # calculate in minutes
    length %= 60
    seconds = length  # calculate in seconds

    return int(hours), int(mins), round(seconds,2)

def get_duration(path):
    with audioread.audio_open(path) as f:
        hours, mins, seconds = duration_detector(f.duration)

    return f"{hours}:{mins}:{seconds}"