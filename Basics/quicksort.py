#! /usr/bin/env python

"""
    This class implements the sorting algorithm QuickSort
"""

class QuickSort():
    def __init__(self, nums:list) -> None:
        self.__nums = nums
        self.__sort()
    
    def __sort(self) -> None:
        self.__divide(self.__nums, 0, len(self.__nums) - 1)
    
    def __divide(self, nums:list, start:int, end:int) -> None:
        if end - start > 0:
            pivot, left, right = self.__nums[start], start, end
            while left <= right:
                while  self.__nums[left] < pivot:
                    left += 1
                while self.__nums[right] > pivot:
                    right -= 1
                if left <= right:
                    self.__nums[left], self.__nums[right] = self.__nums[right], self.__nums[left]
                    left += 1
                    right -= 1
            self.__divide(self.__nums, start, right)
            self.__divide(self.__nums, left, end)
    
    @property
    def result(self) -> list:
        return self.__nums
