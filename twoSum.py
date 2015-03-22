class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        length = len(num)
        seq = []
        for i in range(length):
            seq.append((num[i], i+1))
        seq = sorted(seq)
        for i in range(length):
            value = target - seq[i][0]
            index2 = self.binarySearch(seq, i+1, length-1, value)
            if index2 is not None:
                index1 = seq[i][1]
                return sorted((index1, index2))
            else:
                continue


    def rBinarySearch(self,num,l,r,value):
        m = (l + r) / 2
        if l > r:
            return None
        if value == num[m][0]:
            return num[m][1]
        if l == r:
            return None
        if value < num[m][0]:
            return self.binarySearch(num, l, m-1, value)
        else:
            return self.binarySearch(num, m+1, r, value)

    def binarySearch(self, num, l, r, value):
        m = (l + r)
        while l < r:

num = [-1,-2,-3,-4,-5]
target = -8
solution = Solution()
print solution.twoSum(num, target)

