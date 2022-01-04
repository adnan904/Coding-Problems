# Implementation of Knutt-Moris-Pratt String Matching
# Given a Text and a pattern, returns all indices where the pattern exists in the text
# If n is the length of the text, has a TC = O(n) as it traverses the text only once

def calc_lps(pattern: str) -> list:
    '''
    :param pattern:
    :return: a list containing max count for how many characters are repeating in the pattern upto an index
    '''
    n = len(pattern)
    lps = [0]*n
    max_reps = 0
    i = 1
    while i < n:
        if pattern[i] == pattern[max_reps]:
            max_reps += 1
            lps[i] = max_reps
            i += 1
        else:
            if max_reps != 0:
                max_reps = lps[max_reps-1]
            else:
                lps[i] = 0
                i += 1
    return lps


if __name__ == '__main__':
    pattern = "ABABCABAB"
    text = "ABABDABACDABABCABAB"
    lps = calc_lps(pattern)
    len_text = len(text)
    len_pattern = len(pattern)

    # checking if pattern exists in the text and printing all indices where it is found (if found)
    i = j = 0
    while i < len_text:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len_pattern:
                print(f"Pattern found in text at index {i - j}")
                j = lps[j-1]
        else:
            if i < len_text:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
