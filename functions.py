# x = input('Число:')
# sis1 = int(input("В какой системе счисления:"))
# sis2 = int(input("В какую систему счисления:"))


def perevod(x,sis1,sis2):
    newnum = 0
    f = False
    x = x.upper()
    if x == "":
        return False, "Пустая строка"
    if sis1<2 or sis2<2:
        return False,"Основание системы счисления не может быть меньше 2"
    if sis1>36 or sis2>36:
        return False,"Система не поддерживается. Максимальное значение 36"
    s=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    for i in range(0,len(x)):
        if (x[i] >= 'A' and x[i] <= 'Z') or (x[i] >= '0' and x[i] <= '9'):
            if x[i] in s:
                a = s.index(x[i])
                if (a+10)>=sis1:
                    f = True
            elif int(x[i]) >= sis1:
                f = True
            if f == True:
                return False,"Неверное число или система счисления"
        else:
            return False,"Неверное число или система счисления"
    st = len(x)-1
    for i in range(len(x)):
        if x[i] in s:
            a = s.index(x[i])+10
        else:
            a = int(x[i])
        dig = a*(sis1**st)
        st-=1
        newnum+=dig
    if sis2 == 10:
        return True,str(newnum)
    else:
        newnum2 = ""
        a = newnum
        if a<sis2:
            if a>9:
                return True,str(s[a-10])
            return True,str(a)
        while a>=sis2:
            if a%sis2 < 10:
                newnum2 += str(a%sis2)
            else:
                newnum2+=s[a%sis2-10]
            a//=sis2
        if a<10:
            newnum2+=str(a)
        else:
            newnum2 += s[a-10]
        return True,str(newnum2)[::-1]

def calculator(a, b, operation, sis):
    result = 0
    f1, a = perevod(str(a), sis, 10)
    f2, b = perevod(str(b), sis, 10)
    if f1 == False:
        return False, a
    elif f2 == False:
        return False, b
    a = int(a)
    b = int(b)
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '//':
        if b == 0:
            return False, 'НА НОЛЬ ДЕЛИТЬ НЕЛЬЗЯ!'
        result = a // b
    else:
        return False, "Неподдерживаемая операция"
    f3, new_result = perevod(str(result), 10, sis)
    return True, new_result





