def URLify(input, length):
  input = list(input)
  spaceCount = 0
  for i in range(length):
    if input[i] == ' ':
      spaceCount += 1
  newLen = length + (2 * spaceCount)
  result = newLen * [' ']
  for j in range(length - 1, -1, -1):
    if input[j] == ' ':
      result[newLen - 1] = '0'
      result[newLen - 2] = '2'
      result[newLen - 3] = '%'
      newLen -= 3
    else:
      result[newLen - 1] = input[j]
      newLen -= 1
  return ''.join(result)

def main():
  s = "Hello World  "
  trueLen = 11
  print(URLify(s, trueLen))
main()