print('Welcome to my Germain Prime Finder')
print('A Germain Prime is a Prime number whose value doubled plus one is still a Prime Number')
print('This Program Finds all Germain Primes between 2 Values. Type in a Starting Value then an Ending Value')

ending = 0

while ending != -1:

    x = int(input('Type Start Value (Type -1 to Exit): '))
    ending = x
    if ending == -1:
        break
    y = int(input('Input Y Value: '))

    i = x
    j = 1
    k = 1
    count = 0
    if i<=1:
        i=2

    while i>j and i<y:
        j += 1
        if i%j==0:
            if i == j:
                # print(f'{i} is Prime')
                num1 = i
                a = (2*i)+1
                k += 1
                while a>k:
                    k += 1
                    if a%k==0:
                        if a == k:
                            print(f'{i} is a Germain Prime Number')
                            count += 1
                    else:
                            k += 1
                k=1
                i += 1
                j = 1
            else:
                i += 1
                j = 1

    if count > 0:
        print(f'There are a total of: {count} Germain Prime Values')
    elif count == 0:
        if x>y:
            print('X Value MUST be Larger Than Y Value')
        elif x<0 and y<0:
            print('There are no Negative Germain Prime Values')
        else:
            print('There are no Germain Prime Values')
