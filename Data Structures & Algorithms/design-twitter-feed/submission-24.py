class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.tweets[userId], (self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        timeline = []
        following = list(self.following[userId])
        following.append(userId)
        for f in following:
            for tweet in self.tweets[f]:
                heapq.heappush(timeline, tweet)
        return [heapq.heappop(timeline)[1] for _ in range(min(10, len(timeline)))]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
