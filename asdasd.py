phrase=str(input('Veuillez entrer une phrase:\n'))
lettres_phrase=phrase.split()
list_lettres=[]
for i in phrase:
    list_lettres.append(i)
dictionnaire=dict()
for i in list_lettres:
      if i.isalpha()==False:
          continue
      else:
        compteur=0
        for j in list_lettres:
            if i==j:
                compteur+=1

        dictionnaire[i]=compteur

mark_list=sorted(dictionnaire.items(), key=lambda x:x[1])
sort_dict=dict(mark_list)
print(sort_dict)