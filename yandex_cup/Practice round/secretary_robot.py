
def optimal_clicks(string):
    answer = len(string)
    string = string.replace(' ', '')
    low, big = 0, answer * 2 + 2
    for symb in string:
        if symb > 'Z':
            low, big = min(low, big + 2), big + 1
        else:
            big, low  = min(big, low + 2), low + 1
    answer += min(low, big)
    return answer

if __name__ == '__main__':
    print(optimal_clicks(input()))
