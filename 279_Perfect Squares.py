class Solution:
    def numSquares(self, n: int) -> int:
        #like coin change
        #nums[i]  // =0, if i=0
        #         // = 1, if i=1
        #         // Min(nums[i-aj])+1, if i > aj

        #Table 
        #i: 0 - n
        #nums[i]: Should be count

        #At first we have to find all the possible numbers
        numlis = list()
        nums = list()
        key = 1
        while(key):
            if key * key <= n:
                numlis.append(key*key)
                key += 1
            else:
                break
        for i in range(0,n+1):
            if i==0:
                nums.append(0)
            elif i==1:
                nums.append(1)
            else:
                minnum = 100000
                for j in range(0,len(numlis)):
                    if i >= numlis[j]:
                        tempnum = nums[i-numlis[j]] + 1
                        if minnum > tempnum:
                            minnum = tempnum
                nums.append(minnum)
        
        return nums[-1]
