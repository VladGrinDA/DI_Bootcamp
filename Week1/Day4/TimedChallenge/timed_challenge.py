def count_occurences(string, tgt_char):
    cnt = 0
    for char in string:
        if char == tgt_char:
            cnt += 1
    return cnt

print(count_occurences('Programming is cool!', 'o'))