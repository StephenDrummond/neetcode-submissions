class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list) # userid : [tweetId]. Pop least after size > 10
        self.following = defaultdict(list) # userid : [userId]. use swap with last to keep O(1) removal
        self.timer = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timer, tweetId))
        self.timer += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        feedIds = [userId]   
        feedIds += self.following[userId]

        timeline = []
        for fid in feedIds:
            for t in self.tweets[fid]:
                timeline.append(t)
        timeline.sort(reverse=True)
        
        return [x[1] for x in timeline[0:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or followeeId in self.following[followerId]:
            return
        self.following[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or followeeId not in self.following[followerId]:
            return
        self.following[followerId].remove(followeeId)
