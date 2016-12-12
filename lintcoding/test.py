# -*- coding: utf-8 -*-

# k大

import random
def quickSorted(A):
    if len(A) <= 0:
        return []
    less = []
    greater = []

    p = A.pop(random.randint(0, len(A) - 1))
    for item in A:
        if item < p:
            less.append(item)
        else:
            greater.append(item)
    return quickSorted(greater) + [p] + quickSorted(less)

    # @param k & A a integer and an array
    # @return ans a integer


def kthLargestElement( k, A):
    a = quickSorted(A)
    print a
    return a[k]



def andset(nums1, nums2):
    ans = []
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)

    print nums1, nums2
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        while i < len(nums1) and j < len(nums2) and nums1[i] < nums2[j]:
            i += 1
        while i < len(nums1) and j < len(nums2) and nums1[i] > nums2[j]:
            j += 1
        while i < len(nums1) and j < len(nums2) and nums1[i] == nums2[j]:
            ans.append(nums1[i])
            i += 1
            j += 1

    # for num in nums1:
    #     if num in nums2:
    #         nums2.pop(nums2.index(num))
    #         ans.append(num)

    return ans



if __name__ == '__main__':
    a = [1, 2, 2, 1]
    b = [2, 2]

    a = [4, 7, 9, 7, 6, 7]
    b = [5, 0, 0, 6, 1, 6, 2, 2, 4]

    # a = [61, 24, 20, 58, 95, 53, 17, 32, 45, 85, 70, 20, 83, 62, 35, 89, 5, 95, 12, 86, 58, 77, 30, 64, 46, 13, 5, 92,
    #      67, 40, 20, 38, 31, 18, 89, 85, 7, 30, 67, 34, 62, 35, 47, 98, 3, 41, 53, 26, 66, 40, 54, 44, 57, 46, 70, 60,
    #      4, 63, 82, 42, 65, 59, 17, 98, 29, 72, 1, 96, 82, 66, 98, 6, 92, 31, 43, 81, 88, 60, 10, 55, 66, 82, 0, 79, 11,
    #      81]
    # b = [5, 25, 4, 39, 57, 49, 93, 79, 7, 8, 49, 89, 2, 7, 73, 88, 45, 15, 34, 92, 84, 38, 85, 34, 16, 6, 99, 0, 2, 36,
    #      68, 52, 73, 50, 77, 44, 61, 48]
    # print andset(a, b)

    print kthLargestElement(1,b)
