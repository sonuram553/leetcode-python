class Solution:
  def countAndSay(self, n: int) -> str:
    value = "1"

    for x in range(n - 1):
      value = self.conversion(value)

    return value

  def conversion(self, num) -> str:
    counts = [[num[0], 1]]
    j = 0

    # Count digit repetition
    for i in range(1, len(num)):
      if (num[i - 1] == num[i]):
        counts[j][1] += 1
      else:
        j += 1
        counts.append([num[i], 1])

    # Create string - count plus digit
    countAndDigit = ""
    for [digit, count] in counts:
      countAndDigit += str(count) + digit

    return countAndDigit
