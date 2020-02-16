def groupusm6(start, nums, target):
    if len(nums)<=start:
        return target==0
    if nums[start]==6:
        return groupusm6(start+1, nums, target-6)
    return groupusm6(start+1,nums, target-nums[start]) or groupusm6(start+1,nums,target)
def groupnoadj(start,nums,target):
    if start>=len(nums):
        return target==0
    return groupnoadj(start+2,nums,target-nums[start]) or groupnoadj(start+1,nums,target)
def groupsum5(start,nums,target):
    if start>=len(nums):
        return target==0
    if nums[start]%5==0:
        if start<=len(nums) and nums[start+1]==1:
            return groupsum5(start+2,nums,target-nums[start])
        return groupsum5(start + 1, nums, target - nums[start])
    return groupsum5(start+1,nums,target-nums[start]) or groupsum5(start+1,nums,target)
def groupsumclump(start,nums, target):
    if start>=len(nums):
        return target==0
    i=start
    suma=0

    while i<len(nums) and nums[start]==nums[i]:
        suma+=nums[i]
        i+=1


    return groupsumclump(i,nums,target-suma) or groupsumclump(i,nums,target)
def splitarray(start,nums,array1,array2):

    if start>=len(nums):
        return array1==array2

    return splitarray(start+1,nums,array1+nums[start],array2) or splitarray(start+1,nums,array1,array2+nums[start])



