def check_palindrome(arr):
    arr1= arr[::-1]
    if arr== arr1:
        return True
    return False

string= 'aaaa'
res= check_palindrome(string)
print(res)