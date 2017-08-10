class Interval:

    def __init__(self, s = 0, e = 0):
        self.start = s
        self.end = e

def insert_interval(arr, newInterval):
    result = []
    if len(arr) == 0:
        result.append(newInterval)
        return result
    else:
        for interval in arr:
            if interval.end < newInterval.start:
                result.append(interval)
            elif interval.start > newInterval.end:
                result.append(newInterval)
                newInterval = interval
            elif interval.end >= newInterval.start or interval.start <= newInterval.end:
                newInterval = Interval(min(interval.start, newInterval.start), max(newInterval.end, interval.end))
        result.append(newInterval)
        return result

def main():
    arr = []
    arr = insert_interval(arr, Interval(1, 2))
    arr = insert_interval(arr, Interval(3, 5))
    arr = insert_interval(arr, Interval(6, 7))
    arr = insert_interval(arr, Interval(8, 10))
    arr = insert_interval(arr, Interval(12, 16))
    arr = insert_interval(arr, Interval(4, 9))
    print("[")
    for interval in arr:
        print("[" + str(interval.start) + ",", str(interval.end) + "]")
    print("]")
main()