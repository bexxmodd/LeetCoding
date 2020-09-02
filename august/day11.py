class Solution:

    def hIndex(self, citations):        
        citations.sort()
        n = len(citations)
        for i in range(n):
            print(i)
            if citations[i] >= (n-i):
                print(citations[i])
                return n-i
        return 0
        
        


sss = [11, 15, 15, 22, 3, 5, 0, 22]
obj = Solution()
print(obj.hIndex(sss))