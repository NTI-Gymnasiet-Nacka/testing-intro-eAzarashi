# Medelvärde

def main():
    # Skriv din lösning här nedan. Byt ut "pass" mot din kod.
    lista=input().split(', ')
    for i in range(0,len(lista)):
        lista[i]=float(lista[i])
    medel_värde=sum(lista)/len(lista)
    print(medel_värde)

if __name__ == "__main__":
    main()
