# Projet_programmation_reseau
![photo_2022-04-01_15-32-30](https://user-images.githubusercontent.com/78869773/161454897-0b291e99-80b9-4fa9-86ce-76844d358741.jpg)


 
 
Le but du projet est de pouvoir mettre en place un dispositif permettant d’analyser un packet. L’analyse mettra en évidence la compréhension de l’encapsulation des données et de l’utilisation des bibliothèques adéquates pour le faire. Il sera aussi mis en évidence une maitrise assez minimaliste de la programmation shell. 

#Spécification de l’environnement technique
Dans notre environnement technique, nous avons utiliser les outils suivants :
Le logiciel VMWARE avec deux machines linux 
Sur la machine Serveur on a installé un serveur de base de données mysql , on a aussi installé un iredmail.
On a aussi fixé l 'adresse ip de la machine et configure les services DHCP et DNS.
Sur la deuxième machine qui est la machine cliente on a installé un serveur de base données et la machine serveur attribut à la machine cliente une adresse ip par dhcp.
Wireshark
Pour les scripts que nous avons :
Des scripts .sh pour les dépendances mysql :
INSTALL_MYSQL.SH : on démarre avec bash./INSTALLER_mysql.SH
Des scripts python dont trois server.py ,client.py et database.py
 bash ./server.py
bash ./client.py
bash ./database.py
INSTALL_Python.SH :on démarre  avec bash ./INSTALLER_PYTHON.sh

La base de données
•	Notre base de données nommée projet_reseau
•	Nous avons la table user dans cette base de données
o	La table aura les colonnes suivantes :
nom
mail
password
confirm
Le serveur
-	Récupérer  nom, email, password
-	Verifier les identifiants
-	if exist accept la connexion et envoi au client message de connexion réussi
-	sinon envoi message erreur d'identifiant
On a  la fonction VerificationInfoBd() pour vérifier :

la base de donnée
Inscription qui permet au serveur de récupérer les informations d'inscription d'un client.
Connexion qui permet au serveur de récupérer les informations de connexion d'un client.
OpenServer qui permet au serveur d'initialiser une connexion en attente d'un client et d'interagir avec en lui offrant les possibilités de s'inscrire et de se connecter
Le client
Pour la mise en place du client qui permet au client de s’inscrire ou de se connecter.
