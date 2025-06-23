# first approach to merge two sorted arrays

def mergeSortedArray(nums1, m, nums2, n):
    nums1copy = nums1[:m]
    p1 = 0
    p2 = 0
    for i in range(m+n):
        if p2 >= n or (p1 < m and nums1copy[p1] <= nums2[p2]):
            nums1[i] = nums1copy[p1]
            p1 += 1
        else:
            nums1[i] = nums2[p2]
            p2 += 1

    return nums1

print(mergeSortedArray([1,2,3,0,0,0], 3, [2,5,6], 3))

# second approach to merge two sorted arrays

def mergeSortedArrays(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    for i in range(m+n-1, -1, -1):
        if p2 < 0:
            break  # nothing to merge from nums2 anymore

        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[i] = nums1[p1]
            p1 -= 1
        else:
            nums1[i] = nums2[p2]
            p2 -= 1

    return nums1

print(mergeSortedArrays([1,2,3,0,0,0], 3, [2,5,6], 3))

