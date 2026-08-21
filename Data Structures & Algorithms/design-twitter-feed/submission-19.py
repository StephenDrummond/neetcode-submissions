class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.tweets[userId], (self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        timeline = []
        following = list(self.following[userId])
        following.append(userId)
        for f in following:
            for tweet in self.tweets[f]:
                heapq.heappush(timeline, tweet)
                if len(timeline) > 10:
                    heapq.heappop(timeline)
        timeline.sort(reverse=True)
        return [t[1] for t in timeline]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            return
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.following[followerId]:
            return
        self.following[followerId].remove(followeeId)
