# BotTwitter-AccountCreator
Permet d'obtenir l'Access Token et Access Token Secret de plusieurs comptes Twitter à partir d'une seule application.
Ce script est une extension pour le bot concours de twitter. Il permet d'avoir des accès API pour tous les comptes que vous voulez à partir d'un seul compte développeur.


### Dépendances du script :
Vous devez installer ces librairies pour que le script fonctionne.
```
Tweepy
Flask
```

### Installation :
* Dans un premier temps pour utiliser le script vous allez avoir besoin d'un compte développeur Twitter et de récupérer vos accès à l'API.
 Vous pouvez demander cet accès sur le site développeur de Twitter : [Twitter Developer](https://developer.twitter.com/)

* Vous devez ensuite installer une version 3.x de Python : [Python 3.x](https://www.python.org/downloads/)

* Et pour finir vous devez installer les librairies.
 Pour vous faciliter les choses vous pouvez les installer avec pip3 (pour python3).
 Et faire la commande dans votre console (cmd pour Windows) : 
 ```
 python3 -m pip install -r requirements.txt
 ou
 py -m pip install -r requirements.txt
 ```
 Cette commande va permettre d'installer automatiquement les librairies Tweepy et Flask.
 Si pip n'est pas reconnu vous devez l'installer.

### Configuration :
Tout d'abord vous devez cocher dans les réglages de votre app Twitter (sur le site developpeur) la mention 
"Sign in with Twitter" puis ajouter le callback : http://127.0.0.1:5000/callback
<br/>
![Test Image 1](https://github.com/j4rj4r/BotTwitter-AccountCreator/blob/master/github_assets/image1.png)
<br/>
<br/>
Puis vous devez récuperer vos Consumer Api keys :
<br/>
![Test Image 1](https://github.com/j4rj4r/BotTwitter-AccountCreator/blob/master/github_assets/image2.png)
<br/>
<br/>
 Les ajouter dans le fichier server.py dans les bonnes variables :
<br/>
![Test Image 1](https://github.com/j4rj4r/BotTwitter-AccountCreator/blob/master/github_assets/image3.png)
<br/>
Pour lancer le script vous devez faire : 
```
python3 server.py
ou
py server.py
```
Et enfin vous allez juste rentrer dans votre navigateur favoris cette url : http://127.0.0.1:5000/
Dès que vous avez ajouter des comptes pour chaque compte vous avez les 4 tokens nécessaires pour utiliser le bot twitter.


