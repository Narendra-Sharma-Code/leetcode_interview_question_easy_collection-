nums1 = [1,2,2,1]
nums2 = [2,2]

nums2 = [4,4,4,9,9,9,8]
nums1 = [9,4,9,8,4,]

seen = []
# for num in nums1:
#     if num in nums2:
#         seen.append(num)

# if len(nums1) <= len(nums2):
#     for num in nums1:
#         if num in nums2:
#             seen.append(num)
            
# if len(nums2) < len(nums1):
#     for num in nums2:
#         if num in nums1:
#             seen.append(num)

freq ={}
for num in nums1:
    freq[num] = freq.get(num,0) +1
seen =[]

for i ,num in enumerate(nums2):
    if num in freq and freq[num] > 0:
        seen.append(num)
        freq[num] -=1

print(seen)   
    

