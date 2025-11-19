def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        return ValueError
    return tuple((min(nums), max(nums)))


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return tuple(sorted(set(nums)))


def flatten(mat: list[list | tuple]) -> list:
    array = []
    for element in mat:
        if not isinstance(element, (list, tuple)):
            return TypeError
        array.extend(element)
    return array


print(
    min_max([3, -1, 5, 5, 0]),
    min_max([42]),
    min_max([-5, -2, -9]),
    min_max([]),
    min_max([1.5, 2, 2.0, -3.1]),
)  # Тест-кейсы min_max

print(
    unique_sorted([3, 1, 2, 1, 3]),
    unique_sorted([]),
    unique_sorted([-1, -1, 0, 2, 2]),
    unique_sorted([1.0, 1, 2.5, 2.5, 0]),
)  # Тест-кейсы unique_sorted

print(
    flatten([[1, 2], [3, 4]]),
    flatten([[1, 2], (3, 4, 5)]),
    flatten([[1], [], [2, 3]]),
    flatten([[1, 2], "ab"]),
)  # Тест-кейс flatten
