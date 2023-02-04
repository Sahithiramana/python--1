def max_area_container(arr):
    max_area=0
    left=0
    right=len(arr)-1
    while left<right:
        cur_area=min(arr[left],arr[right])*(right-left)
        max_area=max(max_area,cur_area)
        if arr[left]<arr[right]:
            left+=1
        else:
            right-=1
    return max_area
arr=[7,3]
print(max_area_container(arr))
