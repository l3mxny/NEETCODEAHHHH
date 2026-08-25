class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        maxA = 0 
        maxB = 0 
        maxC = 0 
        for i in range(len(triplets)):
            triplet = triplets[i]
            a = triplet[0]
            b = triplet[1]
            c = triplet[2]

            if a > target[0] or b > target[1] or c > target[2]:
                continue

            maxA = max(maxA, a)
            maxB = max(maxB, b)
            maxC = max(maxC, c)

        return maxA == target[0] and maxB == target[1] and maxC == target[2]
        