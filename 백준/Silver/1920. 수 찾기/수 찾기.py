def search(arr, target, high, low):
    mid = (high + low) // 2
    if high < low: return 0
    
    if arr[mid] == target: return 1
    elif arr[mid] < target: return search(arr, target, high, mid + 1)
    elif arr[mid] > target: return search(arr, target, mid - 1, low)


n = int(input())
nums = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))
nums.sort()

for target in targets:
    print(search(nums, target, len(nums) - 1, 0))