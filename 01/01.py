with open("data.txt", "r") as f:
    left_list = []
    right_list = []
    for line in f.readlines():
        edited_line = line.strip().replace("   ", ",").split(",")
        left_list.append(int(edited_line[0]))
        right_list.append(int(edited_line[1]))

    ordered_left = sorted(left_list)
    ordered_right = sorted(right_list)
    
    print(ordered_left)
    print(ordered_right)

    total_sum = 0
    
    # part one
    #for idx, val in enumerate(ordered_left):
    #    distance = ordered_left[idx] - ordered_right[idx]
    #    if distance < 0:
    #        distance *= -1

    #    total_sum += distance
    
    for i in ordered_left:
        appearance_count = ordered_right.count(i)
        total = i * appearance_count
        total_sum += total

    print(total_sum)


