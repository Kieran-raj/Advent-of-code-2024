import re
import ast


is_dont = False

def find_mul_tuples(line):
    global is_dont
    #mul_regex = r"(mul\(\d{1,3},\s*\d{1,3}\))"
    mul_regex = r"(?:do\(\)|don't\(\)_?|mul\(\d{1,3},\s*\d{1,3}\))"
    matches = re.findall(mul_regex, line)

    tuples = []
    for idx, m in enumerate(matches):
        print(m)
        if m.startswith("don't"):
            is_dont = True
            continue

        if m.startswith("do"):
            is_dont = False
            continue

        if not is_dont:
            tuple_regex = r"\(\d{1,3},\d{1,3}\)"
            found_tuple = re.findall(tuple_regex, m)[0]
            tuples.append(ast.literal_eval(found_tuple))
    return tuples
    
        
        
if  __name__=="__main__":
    with open("data.txt", "r") as f:
        count = 0
        lines = [line.strip() for line in f.readlines()]
        
        for l in lines:
            tuples = find_mul_tuples(l)
            for t in tuples:
                count += int(t[0]) * int(t[1])

        print(count)
    
