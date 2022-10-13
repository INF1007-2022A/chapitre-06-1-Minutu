#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: Demander les valeurs ici
        values = []
        while len(values) < 10:
            values.append(input("Please enter a value\n"))

    num_values = [float(value) for value in values if value.isdigit()]
    str_values = [value for value in values if not value.isdigit()]

    return sorted(num_values) + sorted(str_values)


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        words=[]
        while len(words)<2:
            words.append('Veuillez entrer le mot:\n')



    return sorted(words[0])==sorted(words[1])


def contains_doubles(items: list) -> bool:
    return len(set(list))==len(list)


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    best_student=dict()
    for key, value in student_grades.items():
        average = sum(value)/len(value)

        if len(best_student)==0 or list(best_student.values())[0]<average:
            best_student={key:average}
    return best_student

def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres


    list_lettres = []
    for i in sentence:
        list_lettres.append(i)
    dictionnaire = dict()
    for i in list_lettres:
        if i.isalpha() == False:
            continue
        else:
            compteur = 0
            for j in list_lettres:
                if i == j:
                    compteur += 1

            dictionnaire[i] = compteur

    mark_list = sorted(dictionnaire.items(), key=lambda x: x[1])[::-1]
    affichage=''
    for i in mark_list:
        if i[1]>5:
            affichage= affichage+ f'La lettre {i[0]} a ete utilisee {i[1]} fois\n'

    return affichage


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    nom=str(input('Quel est le nom de votre recette?:\n'))
    ingredients=str(input('quels sont les noms de vos ingredients, separes par une virgule?'))
    ingredients=ingredients.split(',')

    dict={nom:ingredients}
    return dict


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    name=str(input('quel es tle nom de votre recette?:\n'))
    if name in ingredients:
        print(ingredients[name])
    else:
        print('cette recette nest pas rpesentes')

def main() -> None:
    # print(f"On essaie d'ordonner les valeurs...")
    # print(order())
    #
    # print(f"On vérifie les anagrammes...")
    # print(anagrams())
    #
    # my_list = [3, 3, 5, 6, 1, 1]
    # print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(best_grades(grades))
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    print(frequence(sentence))

    print("On enregistre les recettes...")
    recipes = get_recipes()
    print(recipes)
    print("On affiche une recette au choix...")
    print(print_recipe(recipes))


if __name__ == '__main__':
    main()
