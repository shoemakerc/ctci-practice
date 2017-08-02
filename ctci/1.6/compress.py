def compress(inp):
    if len(inp) == 0:
        return inp
    result = ""
    count = 1
    for i in range(1, len(inp)):
        if inp[i] != inp[i - 1]:
            result += inp[i - 1] + str(count)
            count = 1
        else:
            count += 1
    result += inp[-1] + str(count)
    if len(result) >= len(inp):
        return "compression failed: " + inp
    else:
        return result

def main():
    print(compress("aaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccccdddddddddddddddddddddddddddddddddddddddeffffffffffffffffffffffffffffffffg"))
main()

