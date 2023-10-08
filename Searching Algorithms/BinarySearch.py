class BinarySearch:
    def __init__(self, data):
        self.data = sorted(data)

    def search(self, target):
        left, right = 0, len(self.data) - 1

        while left <= right:
            mid = (left + right) // 2
            if self.data[mid] == target:
                return mid
            elif self.data[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

data = [5, 2, 9, 1, 5, 6]
target = 9

search_algorithm = BinarySearch(data)
result = search_algorithm.search(target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found.")
