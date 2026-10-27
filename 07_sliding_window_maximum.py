from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    positions = deque()
    result = []

    for i, value in enumerate(nums):
        # Індекси за межами поточного вікна більше не потрібні.
        while positions and positions[0] <= i - k:
            positions.popleft()

        # Менші значення позаду поточного вже не стануть максимумом.
        while positions and nums[positions[-1]] <= value:
            positions.pop()

        positions.append(i)
        if i >= k - 1:
            result.append(nums[positions[0]])

    return result


if __name__ == "__main__":
    print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
    # [3, 3, 5, 5, 6, 7]
    print(max_sliding_window([1], 1))  # [1]
