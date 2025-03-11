def check_num(nums, target):
    mapped_obj = {}
    for i, num in enumerate(nums):
        res = target-num
        if res in mapped_obj:
            return [mapped_obj[res], i]
        mapped_obj[num] = i
    return -1

nums = [2, 3, 4, 5, 1, 0, 9]
target = 11

res = check_num(nums, target)
print(res)