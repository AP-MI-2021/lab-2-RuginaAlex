def get_base_2(n):
    r=0
    p=1
    nr=0
    while n!=0:
        r=n%2
        n=n//2
        nr=nr+r*p
        p=p*10
    print (nr)


def test_get_base_2():
    assert get_base_2(730)== 1011011010
    assert get_base_2(251)== 11111011


def oglindit(n):
    '''
    Functie pentru a afla oglinditul unui numar.
    '''

    ogl=0
    while n!=0:
        ogl=ogl*10+n%10
        n=n//10
    return ogl


def is_antipalindrome(n):
    c1=0
    c2=0
    invers=oglindit(n)
    while n!=0:
        c1=n%10
        c2=invers%10
        n=n//10
        invers=invers//10
        if c1==c2:
            return False


    return True

def test_is_antipalindrome():
    assert test_is_antipalindrome(2783) == True
    assert test_is_antipalindrome(2773) == False

def main():

    while True:
        print('1. Transformare numar in baza 2 .')
        print('2. Este antipalindrom?')
        optiune=input('Alege optiunea:')
        if optiune == '1':
            n=int(input('Dati un numar'))
            get_base_2(n)
        elif optiune == '2':
            n =int(input('Dati un numar'))
            print(is_antipalindrome(n))
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida.')



main()