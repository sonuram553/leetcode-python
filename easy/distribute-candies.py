class Solution:
  def distributeCandies(self, candyType: list[int]) -> int:
    map = {}
    candyTypeCount = 0

    for candy in candyType:
      if (not candy in map.keys()):
        candyTypeCount += 1
        map[candy] = 1

        if (candyTypeCount == len(candyType) // 2):
          return candyTypeCount

    return candyTypeCount
