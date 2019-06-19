class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.Stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.Stack.append(x)


    def pop(self):
        """
        :rtype: None
        """
        del self.Stack[-1]

    def top(self):
        """
        :rtype: int
        """
        try:
            return self.Stack[-1]
        except Exception:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.Stack)

def test_fucntion():
    stack =MinStack()
    stack.push(-1)
    stack.pop()
    stack.push(2)
    stack.push(3)
    print(stack.top())
    print(stack.getMin())

if __name__ == '__main__':
    test_fucntion()