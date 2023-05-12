def min_str(str1, str2):
    if str1 == '':
        return str2
    if len(str1) < len(str2):
        return str1
    elif len(str1) == len(str2):
        return min(str1, str2)
    else:
        return str2


def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-1 - i]:
            return False
    return True


if __name__ == '__main__':
    string = input()
    ans = ''
    for i in range(len(string) - 1):
        s = string[i:i + 2]
        if is_palindrome(s):
            ans = min_str(ans, s)
            if ans == 'aa':
                break
        if len(ans) != 2:
            s = string[i:i + 3]
            if is_palindrome(s):
                ans = min_str(ans, s)
    if ans == '':
        print(-1)
    else:
        print(ans)
