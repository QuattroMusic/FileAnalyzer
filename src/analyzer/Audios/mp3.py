from ._audio_utils import get_duration

rowsData = {
    "type": "MP3",
    "extension": ".mp3",
    "file_count": 0,
    "min_duration": "",
    "max_duration": "",
}
durations = []


def should_analyze(ext):
    return ext in [".mp3"]


def analyze(path):
    rowsData["file_count"] += 1
    durations.append(get_duration(path))

    rowsData["min_duration"] = min(durations)
    rowsData["max_duration"] = max(durations)


def get_data():
    return rowsData
