def rearrangedString(s):
    # Write your code here
    s = [c for c in s if c.isalnum()]
    dict = {}
    for c in s:
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1
    a = [(key, val) for key, val in dict.items()]
    a.sort(key=lambda x: x[1], reverse=True)
    prev_count = -1
    temp_list = []
    result = []
    block_count = 0
    for (char, count) in a:
        if count < prev_count:
            if block_count % 2 == 0:
                result.append(str(prev_count) + ''.join(sorted(temp_list)))
            else:
                result.append(str(prev_count) +
                              ''.join(sorted(temp_list, reverse=True)))
            temp_list = []
            block_count += 1
        temp_list.append(char)
        prev_count = count
    if block_count % 2 == 0:
        result.append(str(prev_count) + ''.join(sorted(temp_list)))
    else:
        result.append(str(prev_count) +
                      ''.join(sorted(temp_list, reverse=True)))
    return ','.join(result)


if __name__ == '__main__':
    s = input()

    result = rearrangedString(s)

    print(result)
