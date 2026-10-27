from collections import Counter


def first_uniq_char(s: str) -> int:
    counts = Counter(s)
    for index, char in enumerate(s):
        if counts[char] == 1:
            return index
    return -1


if __name__ == "__main__":
    print(first_uniq_char("leopard"))      # 0
    print(first_uniq_char("loveleopard"))  # 2
    print(first_uniq_char("aabb"))         # -1
