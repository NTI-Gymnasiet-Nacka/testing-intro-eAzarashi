# Största skillnad

def main():
    # Skriv din lösning här nedan. Byt ut "pass" mot din kod.
    lista=input().split(', ')
    for i in range(0,len(lista)):
        lista[i]=int(lista[i])
    lista.sort()
    tal=lista[len(lista)-1]-lista[0]
    print(tal)

if __name__ == "__main__":
    main()
