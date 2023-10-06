class LinearSearch:
    def __init__(self, data):
        self.data = data

    def search(self, target):
        for index, value in enumerate(self.data):
            if value == target:
                return index
        return -1

data = [5, 2, 9, 1, 5, 6]
target = 9

search_algorithm = LinearSearch(data)
result = search_algorithm.search(target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found.")
