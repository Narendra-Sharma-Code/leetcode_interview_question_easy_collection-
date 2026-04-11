nums = [2,7,11,15]
target = 9
# j = 0
# for num in nums:
#     if num or num+j  == target:
#         i = nums.index(num)
#         print(i)
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            print(i,j)











# inputs = [7,1,5,3,6,4]
# for i in range(len(inputs)-1):
#     print(i+1,inputs[i+1])
