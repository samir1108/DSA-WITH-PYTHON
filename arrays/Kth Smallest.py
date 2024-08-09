import heapq

def find_kth_minimum(nums, k):
    if k > len(nums):
        raise ValueError("k is larger than the number of elements in the array")
    
    # Build a max-heap with the first k elements
    max_heap = [-num for num in nums[:k]]  # Use negative values to simulate max-heap
    heapq.heapify(max_heap)
    
    # Process the remaining elements
    for num in nums[k:]:
        if num < -max_heap[0]:  # Compare with the largest element in the heap
            heapq.heappushpop(max_heap, -num)
    
    return -max_heap[0]  # The root of the max-heap (negated) is the k-th minimum

# Example usage
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(f"The {k}-th minimum element is {find_kth_minimum(nums, k)}")
