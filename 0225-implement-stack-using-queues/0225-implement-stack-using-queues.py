class MyStack(object):

    def __init__(self):
        self.q = None
                

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q = deque([x, self.q])
        

    def pop(self):
        """
        :rtype: int
        """
        top = self.q.popleft()
        self.q = self.q.popleft()
        return top
        

    def top(self):
        """
        :rtype: int
        """
        return self.q[0]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.q


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()