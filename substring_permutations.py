from collections import defaultdict

"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.
https://leetcode.com/problems/permutation-in-string/

Solution: A substring of s2(of the same length as s1) will be a permutation of s1, if and all if they have the exact same 
characters of same counts. We maintain a sliding window within s2 of the same length as s1. We count the occurences of each
character in both the s1 and the substring of s2. If the count is same for each character in s1 then True else False.
"""


def permute(data, i, length, results):
    if i == length - 1:
        results.append(''.join(data))
    else:
        for j in range(i, length):
            # swap
            data[i], data[j] = data[j], data[i]
            permute(data, i + 1, length, results)
            data[i], data[j] = data[j], data[i]


def counts_dict(s):
    counts = defaultdict(int)
    for char in s:
        counts[char] += 1
    return counts


def counts_compare(s1, s2):
    same = True
    for key in s1.keys():
        if s1[key] != s2[key]:
            same = False
            break
    if same:
        return True
    else:
        return False


if __name__ == '__main__':
    # s1 = "mart"
    # s2 = "karma"
    s1 = "trinitrophenylmethylnitramine"
    s2 = "dinitrophenylhydrazinetrinitrophenylmethylnitramine"
    if len(s1) > len(s2):
        print("False")
        exit()
    s1_counts = counts_dict(s1)
    s2_counts = counts_dict(s2[0:len(s1)])
    result = counts_compare(s1_counts, s2_counts)
    if result:
        print("True")
        exit()
    for i in range(1, len(s2) - len(s1) + 1):
        s2_counts[s2[i - 1]] -= 1
        s2_counts[s2[i + len(s1) - 1]] += 1
        result = counts_compare(s1_counts, s2_counts)
        if result:
            print("True")
            exit()
    print("False")
