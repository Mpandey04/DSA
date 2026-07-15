nums = [1,2,3,4,5,6,7,8,9]

def ReverseOfList(nums, left, right):
    if left >= right:
        return

    nums[left], nums[right] = nums[right], nums[left]
    ReverseOfList(nums, left+1, right-1)

ReverseOfList(nums, 0, len(nums)-1)
print(nums)