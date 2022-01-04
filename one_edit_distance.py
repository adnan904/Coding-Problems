# Given two strings s1 and s2, check if one of them is 1 edit distance away from the other.
# Operations allowed are update a character, delete a character, add a character at an index
if __name__ == '__main__':
    s1 = "geeks"
    s2 = "gaekq"
    count = 0
    i = j = 0
    if abs(len(s1) - len(s2)) > 1:
        print("False")
        exit()
    while i < len(s1) and j < len(s2):
        if count > 1:
            break
        if s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            count += 1
            if len(s1) == len(s2):
                i += 1
                j += 1
            else:
                if len(s1) > len(s2):
                    i += 1
                else:
                    j += 1
    if count > 1:
        print("False")
    else:
        print("True")
