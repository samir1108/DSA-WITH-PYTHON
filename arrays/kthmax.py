import heapq

def find_kth_maximum(nums, k):
    if k > len(nums):
        raise ValueError("k is larger than the number of elements in the array")
    
    # Build a min-heap with the first k elements
    min_heap = nums[:k]
    heapq.heapify(min_heap)
    
    # Process the remaining elements
    for num in nums[k:]:
        if num > min_heap[0]:  # Compare with the smallest element in the heap
            heapq.heappushpop(min_heap, num)
    
    return min_heap[0]  # The root of the min-heap is the k-th maximum

# Example usage
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(f"The {k}-th maximum element is {find_kth_maximum(nums, k)}")
