from typing import List
import random

def binary_search(arr: List[int], low: int, high: int, target: int) -> int:
    """Выполняет бинарный поиск в упорядоченном списке."""
    if low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            return binary_search(arr, mid + 1, high, target)
        return binary_search(arr, low, mid - 1, target)
    return -1

if __name__ == '__main__':
    rand_num_list: List[int] = sorted([random.randint(1, 50) for _ in range(10)])
    target: int = random.randint(1, 50)
    print(f"Список: {rand_num_list}\nЦель: {target}\nИндекс: "
          f"{binary_search(rand_num_list, 0, len(rand_num_list) - 1, target)}")
