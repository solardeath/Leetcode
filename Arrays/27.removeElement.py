"""
27. Remove Element
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""
nums = [3,2,2,3]
val = 3

nums2 = [0,1,2,2,3,0,4,2]
val2 = 2

def removeElement(nums, val):
    j=0
    for i in range(len(nums)):
        if nums[i]!=val:
            nums[j]=nums[i]
            j+=1
    print(j)

removeElement(nums, val)
removeElement(nums2, val2)


#Strategy: 2 pointers: curr number and place where replacements should occur, check i with val,assign and increment j if not same