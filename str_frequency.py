def str_frequency(arr):
    freqDict = {}
    for i in range(len(arr)):
        if arr[i] in freqDict:
            freqDict[arr[i]] += 1
        else:
            freqDict[arr[i]] = 1
    return freqDict
def main():
    arr = ["hello", "hello", "hood"]
    print(str_frequency(arr))
main()