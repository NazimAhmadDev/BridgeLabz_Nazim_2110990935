from collections import deque, Counter

def frequency_sort(nums):
    freq = Counter(nums)

    sorted_nums = sorted(nums, key=lambda x: (freq[x] ,-x))
    
    return sorted_nums
  #queue = deque(sorted_nums)
  
  #return list(queue)

nums = [2,3,1,3,2]
print(frequency_sort(nums))