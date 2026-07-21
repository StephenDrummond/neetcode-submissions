class Twitter:

    def __init__(self):
        self.users = set()
        self.tweets = {} # userid : min heap. Pop least after size > 10
        self.following = {} # userid : userid. use swap with last to keep O(1) removal
        self.timer = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        heapq.heappush(self.tweets[userId], (self.timer, tweetId))
        self.timer += 1
        if len(self.tweets[userId]) > 10:
            heapq.heappop(self.tweets[userId])


    def getNewsFeed(self, userId: int) -> List[int]:
        feedIds = [userId]
        if userId in self.following:
            feedIds += self.following[userId]

        timeline = []
        for fid in feedIds:
            if fid in self.tweets:
                for t in self.tweets[fid]:
                    timeline.append(t)
        timeline.sort(reverse=True)
        
        return [x[1] for x in timeline[0:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = []
        if followerId == followeeId or followeeId in self.following[followerId]:
            return
        self.following[followerId].append(followeeId)
        print(self.following)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or followeeId not in self.following[followerId]:
            return
        self.following[followerId].remove(followeeId)
        print(self.following)
