# Kadanes Algorithm

nums = [-2,1,-3,4,-1,2,1,-5,4]
cur_max = 0
over_max = nums[0]
for num in range(len(nums)):

    if cur_max >= 0:
        cur_max = cur_max + nums[num]
    else:
        cur_max = 0
    
    if cur_max > over_max:
        over_max = cur_max
print(over_max)




