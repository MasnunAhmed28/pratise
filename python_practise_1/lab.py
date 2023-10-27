import heapq

def merge_sorted_lists(sorted_lists):
    merged_list = []
    heap = []  
    for i, lst in enumerate(sorted_lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    while heap:
        val, list_index, element_index = heapq.heappop(heap)
        merged_list.append(val)
        
      
        next_element_index = element_index + 1
        if next_element_index < len(sorted_lists[list_index]):
            heapq.heappush(heap, (sorted_lists[list_index][next_element_index], list_index, next_element_index))

    return merged_list




merged_list = merge_sorted_lists(sorted_lists)
print("output", merged_list)
