def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar cadenas"
        return string * n
    return repeater

def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Nando"))
    repeat_10 = make_repeater_of(10)
    print(repeat_10("Hello"))
    
def make_division_by(n):
    def divisor(x):
        assert type(x) == int, "Solo puedes utilizar enteros"
        return x / n
    return divisor

def make():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))
    
    division_by_5 = make_division_by(5)
    print(division_by_5(100))
    
    division_by_18 = make_division_by(18)
    print(division_by_18(54))
    
    
    

    
if __name__ == '__main__':
    make()