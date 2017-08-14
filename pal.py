def pal(s):
    first, last = 0, len(s) - 1
    while last - first > 1:
        while s[first] == ' ':
            first += 1
        while s[last] == ' ':
            last -= 1
        