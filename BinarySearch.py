things = [4, 7, 34, 98, 100, 101, 200]

def binary(structure, value):
    mid_idx = len(structure) // 2
    mid_val = structure[mid_idx]

    right = structure[mid_idx + 1:]
    left = structure[:mid_idx]
    # if it equals the middle
    if value == mid_val:
        return mid_idx
    # right side
    if value > mid_val:
        result = binary(right, value)
        return result + mid_idx + 1
    # left side
    if value < mid_val:
        result = binary(left, value)
        return result
    





print(binary(things, 7))
print(binary(things, 200))
