'''
Input: nums = [1,1,2,2,3,4]
Output: true
Explanation: One of the possible ways to split nums is nums1 = [1,2,3] and nums2 = [1,2,4]. 

Input: nums = [1,1,1,1]
Output: false
Explanation: The only possible way to split nums is nums1 = [1,1] and nums2 = [1,1]. Both nums1 and nums2 do not contain distinct elements. Therefore, we return false.
'''


from typing import List

class Solution:
    def count_freq(self, nums):
        d = {}
        for num in nums:
            if num in d.keys():
                d[num] += 1
            else:
                d[num] = 1
        return d

    def isPossibleToSplit(self, nums: List[int]) -> bool:
        n = len(nums)
        if n%2 == 1:
            return False
        nums1 = []
        nums2 = []
        nums3 = []
        # c1 = 0
        # c2 = 0
        # nums.sort()

        d = self.count_freq(nums)
        c1 = 0

        for k, v in d.items():
            if v==3:
                return False
                    
            elif v==2:
                nums1.append(k)
                nums2.append(k)
            elif v==1:
                if c1%2==0:
                    nums1.append(k)
                    # c1 = 0
                else:
                    nums2.append(k)

                c1 += 1


        # for i in range(n):

        #     if not nums[i] in nums1:
        #         nums1.add(nums[i])
        #     elif not nums[i] in nums2:
        #         nums2.add(nums[i])
        #     else:
        #         nums3.append(nums[i])
        
        print("nums => ", sorted(nums))
        print("nums1 => ", sorted(list(nums1)))
        print("nums2 => ", sorted(list(nums2)))


        if len(nums1) == n//2 and len(nums2)==n//2:
            return True
        else:
            return False


if __name__ == "__main__":
    
    nums = [1,1,2,2,3,4]
    nums = [1,1,1,1]
    nums = [1, 1]
    nums = [1,2, 3, 1]



    nums = [2,10,2,7,8,9,7,6,6,9]
    nums = [8,9,8,5,9,3,3,1,2,1]
    print(Solution().isPossibleToSplit(nums=nums))
