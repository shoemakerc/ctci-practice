def n_gram(s, n):
  arr = s.split(" ")
  if n > len(arr):
    return None
  result = []
  for i in range(len(arr) - n + 1):
    result.append(arr[i])
    for j in range(i + 1, i + n):
      result[i] += " " + arr[j]
  return result

def main():
  s = "The quick brown fox jumped over the lazy dog"
  print("Digrams:", n_gram(s, 2))
  print("Trigrams:", n_gram(s, 3))
  print("4-grams:", n_gram(s, 4))
  print("5-grams:", n_gram(s, 5))
  print("6-grams:", n_gram(s, 6))
  print("7-grams:", n_gram(s, 7))
  t = "A G C T T C G A"
  print("Trigrams:", n_gram(t, 3))
  #print("Digrams", n_gram(["The", "quick", "brown", "dog", "jumped", "over"], 2))
  #print("Trigrams", n_gram(["The", "quick", "brown", "dog", "jumped", "over"], 3))
  #print("4-grams", n_gram(["The", "quick", "brown", "dog", "jumped", "over"], 4))
  #print("5-grams", n_gram(["The", "quick", "brown", "dog", "jumped", "over"], 5))
main()