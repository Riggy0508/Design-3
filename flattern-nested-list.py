# TC: O(N)  Size of the list 
# SC: O(1)

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        
        def flattern(nl):
            temp=[]
            for i in nl:
                if i.isInteger():
                    temp.append(i.getInteger())
                else:
                    temp.extend(flattern(i.getList()))
            return temp
        self.n=deque(flattern(nestedList))

    def next(self) -> int:
        return self.n.popleft()
    
    def hasNext(self) -> bool:
         return self.n

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())