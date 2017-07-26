def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n % base]

def main():
    print(toStr(567, 10))
    print(toStr(567, 2))
main()
