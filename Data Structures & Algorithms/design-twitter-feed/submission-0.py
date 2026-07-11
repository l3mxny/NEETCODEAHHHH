class Twitter:

    def __init__(self):
        self.count = 0 
        self.tweets = {}
        self.follows = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = list([])
        self.tweets[userId].append((self.count, tweetId))
        self.count += 1
    
    def getNewsFeed(self, userId: int) -> List[int]:
        #holds userid and everyone they follow
        friends = set()
        friends.add(userId)
        if userId in self.follows:
            for i in self.follows[userId]:
                friends.add(i)
        heap = []
        for f in friends:
            if f in self.tweets:
                for count, tweetId in self.tweets[f]:
                    heapq.heappush(heap,(-count,tweetId))
        res = []
        while heap and len(res) < 10:
            #unpack
            ct,tID =  heapq.heappop(heap)
            res.append(tID)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = (set())
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        #break the connection
        if followerId in self.follows:
            self.follows[followerId].discard(followeeId)

        
