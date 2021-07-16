class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 0
        # followerList: Map<userID: int, Set(followeeID)>
        self.followerList = collections.defaultdict(set)
        # userList: Map<userID: int, List[Tuple(time: int, tweetID: int)]>
        self.userList = collections.defaultdict(list)


    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.userList[userId].append((self.time, tweetId))
        self.time += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId not in self.userList:
            return []
        else:
            minHeap = BinaryHeap()
            # 先从自己的tweetList里面，选出10 most recent tweet
            self.userList[userId].sort(key=lambda x: x[0], reverse=True)  # self.time跟踪的是tweet进队的顺序，数字越小就越旧, 所以我们要recerse order，把数字大的放前面
            for tweet in self.userList[userId]:
                if minHeap.size() < 10:
                    minHeap.push(tweet)
                else:
                    oldest = minHeap.peak_top()
                    oldest_time_stamp = oldest[0]
                    tweet_time_stamp = tweet[0]
                    if tweet_time_stamp > oldest_time_stamp:    # if this tweet is ealier than the oldest one in the minHeap, replace it
                        minHeap.pop()
                        minHeap.push(tweet)

            # 然后再把自己的follower's tweet遍历一遍, 如果有时间比目前10里的最后一个还要早的，那就swap掉，然后在10个 most recent tweets 里从新排一次序
            for followeeId in self.followerList[userId]:
                for tweet in self.userList[followeeId]:
                    if minHeap.size() < 10:
                        minHeap.push(tweet)
                    else:
                        oldest = minHeap.peak_top()
                        oldest_time_stamp = oldest[0]
                        tweet_time_stamp = tweet[0]
                        if tweet_time_stamp > oldest_time_stamp:    # if this tweet is ealier than the oldest one in the minHeap, replace it
                            minHeap.pop()
                            minHeap.push(tweet)
            # Prepare the answer for return
            ans = []
            while minHeap.size() > 0:
                ans.insert(0, minHeap.pop()[1])

        return ans 


    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.userList:
            self.userList[followerId] = []
        self.followerList[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            if followeeId in self.followerList[followerId]:
                self.followerList[followerId].discard(followeeId)
        
# Good Reference: 1) https://leetcode-cn.com/problems/design-twitter/solution/dui-you-xian-dui-lie-by-hw_wt-tb9g/

class BinaryHeap():
    def __init__(self):
        self.minHeap = []   # start index with 0
    
    def leftChild(self, i):
        return 2*i+1

    def rightChild(self, i):
        return 2*i + 2
    
    def parent(self, i):
        return (i-1)//2

    def swap(self, id1, id2):
        self.minHeap[id1], self.minHeap[id2] = self.minHeap[id2], self.minHeap[id1]

    def size(self):
        return len(self.minHeap)
    
    def peak_top(self):
        return self.minHeap[0]

    # Just append it to the end, and perform a heapifyUp
    def push(self, node):
        self.minHeap.append(node)
        i = len(self.minHeap)-1
        # Heapify Up: 把新来的放到最后，然后不停的向上调整
        while i>0:
            fa = self.parent(i)
            if self.minHeap[i][0] < self.minHeap[fa][0]:
                self.swap(i, fa)
                i = fa
            else:
                break
    
    # Extract the first one and return as the answer, and replace the first spot with the last one, and perform heapify Down
    def pop(self):
        if len(self.minHeap)==0:
            return 
        ans = self.minHeap[0]
        self.minHeap[0] = self.minHeap[-1]
        self.minHeap.pop()
        # Heapify Donw
        j = 0
        flagDone = False
        while flagDone!= True:
            smallest = j
            L = self.leftChild(smallest)
            R = self.rightChild(smallest)
            if L < len(self.minHeap) and self.minHeap[L][0] < self.minHeap[smallest][0]:
                smallest = L
            if R < len(self.minHeap) and self.minHeap[R][0] < self.minHeap[smallest][0]:
                smallest = R
            if smallest != j:
                self.swap(j, smallest)
                j = smallest
            else:
                flagDone = True 
        return ans


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)