#Bibliothèques standard
import getpass
import sqlite3
from collections import namedtuple

#Bibliothèques tierces
from flask import Flask, jsonify, request, render_template, redirect, session
import tweepy


### Parametres du script ###
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
HOST = "127.0.0.1"

callback = "http://" + HOST + ":5000/callback"
Data = namedtuple('Data', 'id name access_token access_token_secret')


###Base de donnee ###
connexion = sqlite3.connect('comptedb.db')
c = connexion.cursor()
#On fait la table si elle existe pas
c.execute('''CREATE TABLE IF NOT EXISTS account
(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, name text, access_token text, access_token_secret text);''')
c.close()
connexion.commit()

#Requete sql pour ajouter un compte
def InsertData(name, access_token, access_token_secret) :
    connexion = sqlite3.connect('comptedb.db')
    c = connexion.cursor()
    query = 'INSERT INTO account (name, access_token, access_token_secret) VALUES (:name, :access_token, :access_token_secret)'
    c.execute(query, (name, access_token, access_token_secret,))
    c.close()
    connexion.commit()

#Requete sql pour recuperer tous les comptes
def GetData() :
    connexion = sqlite3.connect('comptedb.db')
    c = connexion.cursor()
    c.execute('''SELECT * FROM account;''')
    result = c.fetchone()
    data = []
    while result:
        data.append(dict(Data(*result)._asdict()))
        result = c.fetchone()
    c.close()
    connexion.commit()
    return data;

#Requete sql pour supprier un compte
def DeleteData(cid) :
    connexion = sqlite3.connect('comptedb.db')
    c = connexion.cursor()
    query = 'DELETE FROM account WHERE id = :cid'
    c.execute(query, (cid,))
    c.close()
    connexion.commit()


### FLASK ###

app = Flask('__name__', static_folder="res")
#Permet d'activer ou non le mode debug
app.config['DEBUG'] = False
app.config['SECRET_KEY'] = 'randomcequetuveux'

#Page principal du site
@app.route('/')
def root():
    data = GetData()
    lendata = len(data)
    username = getpass.getuser()
    return render_template('index.html', username = username, lendata = lendata, data = data, consumer_key = CONSUMER_KEY, consumer_secret = CONSUMER_SECRET)

#Permet de demander les permissions
@app.route('/auth')
def auth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET, callback)
    url = auth.get_authorization_url()
    session['request_token'] = auth.request_token
    return redirect(url)

#Une fois qu'on a les permissions
@app.route('/callback')
def twitter_callback():
    request_token = session['request_token']
    del session['request_token']
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET, callback)
    auth.request_token = request_token
    verifier = request.args.get('oauth_verifier')
    #Si l'tilisateur n'a pas annule
    if verifier :
        auth.get_access_token(verifier)
        authen = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET, callback)
        authen.set_access_token(auth.access_token, auth.access_token_secret)
        api = tweepy.API(authen)
        user = api.me()
        name = user.screen_name
        InsertData(name,auth.access_token,auth.access_token_secret)
    return redirect('/')

#Permet du supprimer un compte
@app.route('/delete/<cid>', methods=['GET'])
def delete(cid):
    DeleteData(cid)
    return redirect('/')

#Permet de lancer le serveur
app.run(host=HOST, port=5000)
