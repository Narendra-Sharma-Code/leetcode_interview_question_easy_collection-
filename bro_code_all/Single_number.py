nums = [2,2,1,1,3,4,4,3,5,5,9]
# seen = set()
# single = None
# for num in nums:
#     if num in seen:
#         num += 1
#     else:
#         single = num
# print(single)

# num1 = nums
# seen = set()
# result = None

# for i in range(len(nums)):
#     if nums[i] in num1:
#         result = nums[i]
        
# print(result)   

result = 0
for num in nums:
    result ^= num

print(result)