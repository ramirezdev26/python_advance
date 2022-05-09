def is_palindrome(string: str) -> bool:
        string = string.replace(" ", "").lower()
        return string == string[::-1]
 
 
def is_odd(integer: int) -> bool:
    return integer % 2 != 0     





def run():
    print(is_odd("a"))
    



    
if __name__ ==  '__main__':
    run()        