# Vokalräkning

def main():
    # Skriv din lösning här nedan. Byt ut "pass" mot din kod.
    vokaler='aeiouyåäö'
    sträng=input().lower()
    antal=0
    for i in sträng:
        if i in vokaler:
            antal+=1
    print(antal)


if __name__ == "__main__":
    main()
