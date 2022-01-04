if __name__ == '__main__':
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    read_ptr, write_ptr = 0, 0
    while read_ptr < len(chars):
        ch = chars[read_ptr]
        count = 0
        while read_ptr < len(chars) and chars[read_ptr] == ch:
            read_ptr += 1
            count += 1
        chars[write_ptr] = ch
        write_ptr += 1
        if count > 1:
            for dig in str(count):
                chars[write_ptr] = dig
                write_ptr += 1
    chars = chars[:write_ptr]
    print(chars)
