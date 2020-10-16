def ispalindrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return ispalindrome(string[1:-1])


if __name__ == '__main__':
    print('потоп:', ispalindrome('потоп'))
    print('поп:', ispalindrome('поп'))
    print('топот:', ispalindrome('топот'))
    print('короб:', ispalindrome('короб'))
    print('777:', ispalindrome('777'))
