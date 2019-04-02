# -*- coding:utf-8 -*-
class Solution:
    # def minNumberInRotateArray(self, rotateArray):
    #     # write code here
    #     # 迭代
    #     if not rotateArray:
    #         return 0
    #     front = 0
    #     rear = len(rotateArray) - 1
    #     minVal = rotateArray[0]
    #
    #     if rotateArray[front] < rotateArray[rear]:
    #         return rotateArray[front]
    #     else:
    #         while (rear - front) > 1:
    #             mid = (front + rear) // 2
    #             if rotateArray[mid] >= rotateArray[front]:
    #                 front = mid
    #             elif rotateArray[mid] <= rotateArray[rear]:
    #                 rear = mid
    #             elif rotateArray[front] == rotateArray[rear] == rotateArray[mid]:
    #                 for i in range(1, len(rotateArray)):
    #                     if rotateArray[i] < minVal:
    #                         minVal = rotateArray[i]
    #                         rear = i
    #         minVal = rotateArray[rear]
    #         return minVal

    def minNumberInRotateArray(self, rotateArray):
        # write code here
        # 递归
        if not rotateArray:
            return 0
        front = 0
        rear = len(rotateArray) - 1
        minVal = rotateArray[0]

        if rotateArray[front] < rotateArray[rear]:
            return rotateArray[front]
        minVal = self.binary_search(rotateArray, minVal, front, rear)
        return minVal

    def binary_search(self, array, key, low, high):
        print(array, key, low, high)
        mid = (low + high) // 2
        if mid == low:
            return array[low] if array[low] < array[high] else array[high]
        print(mid)
        if array[mid] > array[low]:
            print('s1')
            return self.binary_search(array, key, mid, high)
        elif array[mid] < array[high]:
            print('s2')
            return self.binary_search(array, key, low, mid)
        elif array[mid] == array[low] == array[high]:
            print('s3')
            for i in range(low, high + 1):
                if array[i] < key:
                    key = array[i]
            return key


if __name__ == '__main__':
    test = Solution()
    array = [i for i in range(4890,100000)] + [i for i in range(4890)]
    print(test.minNumberInRotateArray(array))
