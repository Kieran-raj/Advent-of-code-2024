def is_only_increasing_or_decreasing(row):
    is_decreasing = False
    is_increasing = False
    for i in range(len(row)-1):
        if i+1 >= len(row):
            continue

        if row[i+1] == row[i]:
            return False

        if row[i+1] < row[i]:
            is_decreasing = True
        else:
            is_increasing = True
        
    if is_decreasing != is_increasing:
        return True
    else:
        return False


def is_safe_deltas(row):
    safe_deltas = [1, 2, 3]
    is_safe = False
    for i in range(len(row)-1):
        if abs(row[i+1] - row[i]) in safe_deltas:
            is_safe = True
        else:
            is_safe = False
            return False
    return is_safe


def remove_step(row, idx=0):
    row_copy = row.copy()
    row_copy.pop(idx)
    return row_copy

def test_step_removal(row, idx=0): 
    row_copy = remove_step(row, idx)
    checks = {
                "safe_deltas": is_safe_deltas(row_copy),
                "is_increasing_or_decreasing": is_only_increasing_or_decreasing(row_copy)
            }

    return all(status for status in checks.values())


if __name__=="__main__":
    parsed_rows = []
    errored_rows = []
    count = 0
    with open("data.txt", "r") as f:
        for row in f.readlines():
            parsed_rows.append([int(r) for r in row.strip().split(" ")])
    
    for row in parsed_rows:
        checks = {
                    "safe_deltas": is_safe_deltas(row),
                    "is_increasing_or_decreasing": is_only_increasing_or_decreasing(row)
                }
        
        row_status = all(status for status in checks.values())
        if row_status:
            count += 1
        else:
            errored_rows.append(row)

    print(f"Count before extra checks - {count}")
    errored_rows.append([1, 1, 1, 1, 1, 1])
    if errored_rows:
        for row in errored_rows:
            row_copy = row.copy()
            step_index = 0
            while step_index < len(row_copy):
                is_now_successful = test_step_removal(row_copy, step_index)
                if is_now_successful:
                    count += 1
                    break

                step_index += 1
                row_copy = row.copy()
    
    print(f"Count after extra checks - {count}")

