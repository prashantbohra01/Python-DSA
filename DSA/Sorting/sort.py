nums = [3,1,2,4]

for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        if nums[i]%2!=0:
            nums[i], nums[j] = nums[j], nums[i]
            
print(nums)