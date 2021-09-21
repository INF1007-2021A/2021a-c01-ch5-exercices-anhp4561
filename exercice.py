#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    absolute = ((number**2)**(1/2))
    return absolute

def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    noms = []
    nom=""
    for i in prefixes :
        nom =i+suffixe
        noms.append(nom)
    return noms

def prime_integer_summation() -> int:
    prime_numbers = []
    number = 2
    while True:
        if (len(prime_numbers) < 100):
            is_prime = True
            for i in range(2, number, 1):
                modulo = number % i
                if (modulo == 0):
                    is_prime = False
            if (is_prime == True):
                prime_numbers.append(number)
            number += 1
        if (len(prime_numbers) == 100):
            break
        summation= sum(prime_numbers)
    print(summation)

    return summation


def factorial(number: int) -> int:
    facto = 1
    for i in range (1,number+1,1):
        facto*=i
    return facto


def use_continue() -> None:
    liste = []
    for i in range (1,11,1):
        if (i==5):
            continue
        liste.append(i)
    print (liste)



def verify_ages(groups: List[List[int]]) -> List[bool]:
    acceptance = []
    for group in groups:
        is_acceptable = True
        if (len(group)>10 or len(group)<3):
            is_acceptable =False
        for member in group:
            if member < 18:
                is_acceptable = False
        is_fifty = 50
        if member > 70 and is_fifty in group :
            is_acceptable = False
        is_25 = 25
        if is_25 in group:
            is_acceptable = False
        acceptance.append (is_acceptable)

    return acceptance


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
