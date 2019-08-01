class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        start = [0 for i in range(n+1)]
        end = [0 for i in range(n+1)]
        for booking in bookings:
            start[booking[0]]+=booking[2]
            end[booking[1]]+=booking[2]
        answer = [0 for i in range(n+1)]
        answer[1] = start[1]
        for i in range(2,len(start)):
            # answer[i-1]可以认为是前一时刻的人数，start[i]是i时刻上来多少人，end[i-1]是i-1时刻下来多少人
            answer[i] = answer[i-1]+start[i]-end[i-1]
        return answer[1:]

def test_function():
    solution = Solution()
    bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    answer = solution.corpFlightBookings(bookings,5)
    print(answer)

if __name__ == '__main__':
    test_function()