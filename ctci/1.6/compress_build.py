def compress_build(inp):
    if len(inp) == 0:
        return inp
    result = []
    inp = list(inp)
    count = 1
    for i in range(1, len(inp)):
        if inp[i] != inp[i - 1]:
            result.append(inp[i - 1])
            result.append(str(count))
            count = 1
        else:
            count += 1
    result.append(inp[-1])
    result.append(str(count))
    if len(result) >= len(inp):
        return ''.join(inp)
    else:
        return ''.join(result)

def main():
    print(compress_build("aaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccccdddddddddddddddddddddddddddddddddddddddeffffffffffffffffffffffffffffffffg"))
main()

