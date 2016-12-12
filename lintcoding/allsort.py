# -*- coding: utf-8 -*-


###最近一段时间学习了python，发现python真是个强大，强大到和Matlab相媲美。为了熟悉python，将之前的各种排序算法用python实现了一下。
# 、
# 常用的时间复杂度为O(n^2)的排序算法有冒泡排序，插入排序和选择排序，时间复杂度为O(nlog2(n))的算法有快速排序，归并排序和堆排序，
# 、
# 这里、的快速排序的初始比较值partition是随机给定的，在用python进行编写时能更清楚的理解整个排序算法的过程。

import random

def BubbleSort(num):
    n = len(num)
    for i in range(0, n):
        for j in range(i, n):
            if num[i] >= num[j]:
                num[i], num[j] = num[j], num[i]
    return num


def SelectSort(num):
    for i in range(0, len(num)):
        mindex = i
        for j in range(i, len(num)):
            if num[mindex] > num[j]:
                mindex = j
        num[mindex], num[i] = num[i], num[mindex]
    return num


def InsertSort(num):
    for i in range(1, len(num)):
        j = i - 1
        tmp = num[i]
        while j > 0 and tmp < num[j]:
            num[j + 1] = num[j]
            j -= 1
        num[j] = tmp
    return num


def MergerSort(num):
    if len(num) <= 1:
        return num
    left = MergerSort(num[:len(num) / 2])
    right = MergerSort(num[len(num) / 2:])
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
    if len(left) > 0:
        result.extend(MergerSort(left))
    else:
        result.extend(MergerSort(right))
    return result


def QuickSort(num):
    if len(num) <= 1:
        return num
    greater = []
    less = []
    p = num.pop(random.randint(0, len(num) - 1))
    for item in num:
        if item < p:
            less.append(item)
        else:
            greater.append(item)
    return QuickSort(less) + [p] + QuickSort(greater)


############################################################
def InsertIntoHeap(x, heap):
    if len(heap) == 0:
        heap = [x]
        return heap
    heap.append(x)
    pos = len(heap)
    while True:
        if pos == 1:
            return heap
        father = pos / 2
        if heap[father - 1] < heap[pos - 1]:
            heap[father - 1], heap[pos - 1] = heap[pos - 1], heap[father - 1]
            pos = father
        else:
            return heap


def CreateHeap(x):
    b = []
    for i in x:
        InsertIntoHeap(i, b)
    return b


def HandHeap(a):
    if a == None or type(a) != list:
        return
    if a == [] or len(a) == 1:
        return a
    pos = 0
    while True:
        if 2 * (pos + 1) > len(a):
            return a
        if 2 * (pos + 1) == len(a):
            if a[pos] < a[2 * pos + 1]:
                a[pos], a[2 * pos + 1] = a[2 * pos + 1], a[pos]
            return a
        if 2 * (pos + 1) + 1 <= len(a):
            if a[pos] < a[2 * pos + 1] and a[2 * pos + 1] >= a[2 * pos + 2]:
                a[pos], a[2 * pos + 1] = a[2 * pos + 1], a[pos]
                pos = 2 * pos + 1
            elif a[pos] < a[2 * pos + 2] and a[2 * pos + 1] < a[2 * pos + 2]:
                a[pos], a[2 * pos + 2] = a[2 * pos + 2], a[pos]
                pos = 2 * pos + 2
            else:
                return a


def HeapSort(num):
    if num == None or type(num) != list:
        return
    b = CreateHeap(num)
    a = []
    while b:
        a.append(b[0])
        b[0] = b[len(b) - 1]
        b.pop()
        b = HandHeap(b)
    return a
