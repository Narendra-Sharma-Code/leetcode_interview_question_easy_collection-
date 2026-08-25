nums = [1, 2, 3, 3]
hash_set = set()
for n in nums:
    if n in hash_set:
        print("True")
    hash_set.add(n)
# print("False")