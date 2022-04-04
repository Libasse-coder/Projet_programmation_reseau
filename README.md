# Analyseur de traffic avec Python/Wireshark

![photo_2022-04-01_15-32-30](https://user-images.githubusercontent.com/78869773/161454897-0b291e99-80b9-4fa9-86ce-76844d358741.jpg)

 
Le but du projet est de pouvoir mettre en place un dispositif permettant d’analyser un packet. L’analyse mettra en évidence la compréhension de l’encapsulation des données et de l’utilisation des bibliothèques adéquates pour le faire. Il sera aussi mis en évidence une maitrise assez minimaliste de la programmation shell. 

Spécification de l’environnement technique
Dans notre environnement technique, nous avons utiliser les outils suivants :
Le logiciel VMWARE avec deux machines linux 
	Sur la machine Serveur on a installé un serveur de base de données mysql , on a aussi installé un iredmail
	On a aussi fixé l 'adresse ip de la machine et configure les services DHCP et DNS.
	Sur la deuxième machine qui est la machine cliente on a installé un serveur de base données et la machine serveur attribut à la machine cliente une adresse ip par dhcp.<br/>
Pour les scripts que nous avons :<br/>
Des scripts .sh pour les dépendances mysql :<br/>
INSTALL_MYSQL.SH : installation de mysql<br/>
Des scripts python dont trois server.py ,client.py, wireshark.py<br/>
bash ./server.py pour lancer le serveur<br/>
bash ./client.py pour lancer la requete d'inscription du client et d'authebtification vers le serveur 192.168.10.1<br/>
bash ./wireshark.py pour analyser les informations receuillies de la capture faite via wireshark entre le client et le serveur<br/>
INSTALL_Python.SH :installation de Python3<br/>
<br/>
La base de données<br/>
•	Notre base de données nommée projet_reseau
•	Nous avons la table user dans cette base de données
o	La table aura les colonnes suivantes :<br/>
-	nom<br/><br/><br/>
-	mail<br/><br/>
-	password<br/>
-	confirm<br/><br/>
Le serveur<br/>
-	Récupérer  nom, email, password<br/>
-	Verifier les identifiants<br/>
-Environnement de Develeppoment de notre GUi: Qt Design Studio pour la realisation des interfaces graphiques.
