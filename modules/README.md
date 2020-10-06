Si tu veux réutiliser des fonctions que tu as créer dans un autre fichier, tu devrais utiliser la structure de fichier suivante :

## mes_fonctions.py

 
```python
def ma_fonction_a_reutiliser():

    # code

# ...

if __name__ == "__main__":

    # script qui test les fonctions
```



## un_script.py


```python
import mes_fonctions as mf

#...

# utilise les fonctions importées
mf.ma_fonction_a_reutiliser()

#...

```
