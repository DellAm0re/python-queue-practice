from collections import deque


def moves_to_stamp(stamp: str, target: str) -> list[int]:
    m, n = len(stamp), len(target)
    windows = []
    depends_on = [[] for _ in range(n)]
    ready = deque()
    erased = [False] * n
    result = []

    # Для кожного положення штампа запам'ятовуємо символи,
    # які поки що не збігаються з target.
    for start in range(n - m + 1):
        missing = 0
        for j in range(m):
            pos = start + j
            if target[pos] != stamp[j]:
                missing += 1
                depends_on[pos].append(start)
        windows.append(missing)
        if missing == 0:
            result.append(start)
            for pos in range(start, start + m):
                if not erased[pos]:
                    erased[pos] = True
                    ready.append(pos)

    # Стирання символу дозволяє використовувати нові вікна.
    while ready:
        pos = ready.popleft()
        for start in depends_on[pos]:
            windows[start] -= 1
            if windows[start] == 0:
                result.append(start)
                for p in range(start, start + m):
                    if not erased[p]:
                        erased[p] = True
                        ready.append(p)

    if not all(erased) or len(result) > 10 * n:
        return []
    return result[::-1]


if __name__ == "__main__":
    print(moves_to_stamp("abc", "ababc"))
    print(moves_to_stamp("abca", "aabcaca"))
