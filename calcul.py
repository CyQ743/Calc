import math as m
import sys 
def main():
    while True:
        dzialanie= input("Podaj działanie: ")
        dzialanie1=dzialanie.split(" ")
        rozw=dziala(dzialanie1)
        print(rozw)
def dziala(d_1):
    n=0
    for i in ["sin","cos","tan","log","sqrt"]:
        try:
            if d_1[n].startswith(i):
                d_1[n]=d_1[n].replace(i,"")
                d_1[n]=d_1[n].replace("(","",1)
                for j in range(n,len(d_1)):
                    if ")" in d_1[j]:
                        d_1[j]=d_1[j].replace(")","",1)
                        d_2=d_1[n:j+1]
                        for _ in range(n+1,j+1):
                            d_1.pop(n+1)
                        if i=="sin":
                            d_1[n]= m.sin(dziala(d_2))
                        elif i=="cos":
                            d_1[n]= m.cos(dziala(d_2))
                        elif i=="tan":
                            try:
                                d_1[n]= m.tan(dziala(d_2))
                            except ValueError:
                                sys.exit("Błąd w liczbach")
                        elif i=="log":
                            try:
                                d_1[n]= m.log(dziala(d_2))
                            except ValueError:
                                sys.exit("Błąd w liczbach")
                        else:
                            d_1[n]= m.sqrt(dziala(d_2))
                        n= n + 1
                        break
        except (AttributeError, IndexError):
            continue
    j=0
    while len(d_1)>j: 
        if d_1[j]=='*':
            mnozenie(d_1,j)
            continue
        elif d_1[j]=='/':
            dzielenie(d_1,j)
            continue
        j+=1
    try:
        suma=float(d_1[0])
    except ValueError:
        if d_1[0]=="pi":
            suma=m.pi
        elif d_1[0]=="e":
            suma=m.e
    for i in range(1,len(d_1),2):
        if d_1[i]=='+':
            suma = dodawanie(suma,d_1,i)
        elif d_1[i]=='-':
            suma= odejmowanie(suma,d_1,i)
        else:
            continue
    return suma
#2 + 2 + 4 / 4
def dodawanie(sumka,d,n):
    try:
        sumka+=float(d[n+1])
    except ValueError:
        if d[n+1]=="pi":
            d[n+1]=m.pi
        elif d[n+1]=="e":
            d[n+1]=m.e
        try:
            sumka+=float(d[n+1])
        except ValueError:
            sys.exit("Błąd w działaniu1")
    return sumka
def odejmowanie(sumka,d,n):
    try:
        sumka-=float(d[n+1])
    except ValueError:
        if d[n+1]=="pi":
            d[n+1]=m.pi
        elif d[n+1]=="e":
            d[n+1]=m.e
        try:
            sumka-=float(d[n+1])
        except ValueError:
            sys.exit("Błąd w działaniu")
    return sumka
def mnozenie(d,n):
    try:
        d[n]=(float(d[n-1])*float(d[n+1]))
    except ValueError:
        if d[n-1]=="pi":
            d[n-1]=m.pi
        elif d[n-1]=="e":
            d[n-1]=m.e
        if d[n+1]=="pi":
            d[n+1]=m.pi
        elif d[n+1]=="e":
            d[n+1]=m.e
        try:
            d[n]=(float(d[n-1])*float(d[n+1]))
        except ValueError:
            sys.exit("Błąd w działaniu")
    d.pop(n-1)
    d.pop(n)
    return d
def dzielenie(d,n):
    try:
        d[n]=(float(d[n-1])/float(d[n+1]))
    except ValueError:
        if d[n-1]=="pi":
            d[n-1]=m.pi
        elif d[n-1]=="e":
            d[n-1]=m.e
        if d[n+1]=="pi":
            d[n+1]=m.pi
        elif d[n+1]=="e":
            d[n+1]=m.e
        try:
            d[n]=(float(d[n-1])/float(d[n+1]))
        except ValueError:
            sys.exit("Błąd w działaniu")
    d.pop(n-1)
    d.pop(n)
    return d

if __name__ == "__main__":
    main()
