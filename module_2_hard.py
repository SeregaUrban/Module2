def ancient_cipher(n):
    if n < 3 :
        print('Введеное число не может быть использованно ')
    else:
        result = []
        for i in range(1,n):
            for j in range(i+1,n):
                if n%(i+j)==0:
                    result.append(i)
                    result.append(j)
    return print(n,'-',*result)
ancient_cipher(6)