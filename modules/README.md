Si tu veux réutiliser des fonctions que tu as créer dans un autre fichier, tu devrais utiliser la structure de fichier suivante :

## mes_fonctions.py

 
```python
def ma_fonction_a_reutiliser():

    # code

# ...

if __name__ == "__main__":

    # script qui test les fonctions
    # tout ce qui est ici ne sera pas appliqué dans
    # un autre fichier qui importe ce fichier ici
    # ***SEULEMENT LES DÉFINITIONS DE FONCTIONS seront
    # alors accessibles aux autres fichiers
```



## un_script.py


```python
import mes_fonctions as mf

#...

# utilise les fonctions importées
mf.ma_fonction_a_reutiliser()

#...

```

# \_\_name\_\_ == "\_\_main\_\_"
Python assigne automatiquement le nom `__main__` au fichier python qui est exécuté.

Jusqu'à présent, tous nos programmes rentrent dans un seul fichier, alors ils on tous eu le nom `__main__` lors de l'exécution. Par contre, la ligne `import` ajoute le contenu de
différents fichiers python à ton propre fichier. Leurs noms ne seront pas changés. **Exécuter les fichiers master.py et helper.py pour le voir.**

Alors la ligne `if __name__ == "__main__":` vérifie si le fichier est celui qui est excécuté actuellement par python. Si non - quand c'est un fichier importé - tout ce qui est sous cette condition n'affecte pas les autres fichiers.