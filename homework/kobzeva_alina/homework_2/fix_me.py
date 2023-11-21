import random
from typing import List


def binarysearch(arr: List[int], lb: int, ub: int, target: int) -> int:
    """A Binary Search Example which has O(log n) time complexity."""
    if lb <= ub:
        mid: int = lb + (ub - lb) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binarySearch(arr, mid + 1, ub, target)
        else:
            return binarySearch(arr, lb, mid - 1, target)
    else:
        return -1


if __name__ == '__main__':
    rand_num_li: List[int] = sorted([random.randint(1, 50) for _ in range(10)])
    target: int = random.randint(1, 50)
    print(
        "List: {}\nTarget: {}\nIndex: {}".format(
            rand_num_li, target, binarySearch(rand_num_li, 0, len(rand_num_li) - 1, target)
        )
    )
