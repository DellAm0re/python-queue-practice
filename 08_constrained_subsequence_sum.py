from collections import deque


def constrained_subset_sum(nums: list[int], k: int) -> int:
    best_ending = [0] * len(nums)
    positions = deque()
    answer = nums[0]

    for i, value in enumerate(nums):
        # Залишаємо лише попередні індекси на відстані не більшій k.
        while positions and positions[0] < i - k:
            positions.popleft()

        best_previous = max(0, best_ending[positions[0]]) if positions else 0
        best_ending[i] = value + best_previous
        answer = max(answer, best_ending[i])

        # У деку підтримуються спадні значення best_ending.
        while positions and best_ending[positions[-1]] <= best_ending[i]:
            positions.pop()
        positions.append(i)

    return answer


if __name__ == "__main__":
    print(constrained_subset_sum([10, 2, -10, 5, 20], 2)) # 37
    print(constrained_subset_sum([-1, -2, -3], 1))       # -1
    print(constrained_subset_sum([10, -2, -10, -5, 20], 2)) # 23
