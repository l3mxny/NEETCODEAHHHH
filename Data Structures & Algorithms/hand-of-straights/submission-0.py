class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hashmap = {}
        for i in range(len(hand)):
            hashmap[hand[i]] = hashmap.get(hand[i],0) + 1
        
        vals = sorted(hashmap.keys())
        for val in vals:
            while hashmap[val] > 0:
                for i in range(0, groupSize):
                    card = val + i 
                    if card not in hashmap or hashmap[card] == 0:
                        return False
                    hashmap[card] -= 1
        return True
