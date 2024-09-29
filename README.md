# Quantified Website

Dit is een Django-project dat een eenvoudige webapplicatie biedt. Hieronder vind je de instructies om het project lokaal te installeren en uit te voeren.


## Vereisten

- Python 3.x 
- Live Sass Compiler - Visual Studio Code plugin
- pip - Zorg dat die up to date is


## Installatie

Volg de onderstaande stappen om het project lokaal op te zetten:


### 1. Virtuele omgeving aanmaken en activeren

Maak een virtuele omgeving aan en activeer deze door de onderstaande code uit te voeren in de terminal:

Linux/macOS:

```sh
python3 -m venv venv
source venv/bin/activate
```

Windows:

```sh
python -m venv venv
venv\Scripts\activate
```


### 2. Vereisten installeren

Installeer de benodigde pakketten door het volgende uit te voeren:

```sh
pip install -r requirements.txt
```

Mocht er in de toekomst meer `dependencies` gedownload worden moeten deze weer naar de `requirements.txt` gezet wordne door het onderstaande uit te voeren:

```sh
pip freeze > requirements.txt
```


### 3. Omgevingsvariabelen instellen

Dupliceer het bestand `.env.example` in de hoofdmap van het project en hernoem het bestand naar `.env` en voeg de volgende instellingen toe aan het bestand (de `SECRET_KEY` mag voor nu willekeurig zijn, maar het is handig om gelijk een sterke key te genereren, online of via een script kan je een key genereren):

```sh
SECRET_KEY=je_geheime_sleutel
```


### 4. Database instellen

Dupliceer het bestand `my.cnf.example` en hernoem hem naar `my.cnf`. Het bestand bevat voorbeeldinstellingen die je kunt aanpassen voordat je de database migreert. Je kan deze gewoon aanpassen voordat je begint met het migreren van de database, maar dat hoeft dus niet.

- PS: De database is nu ingesteld op MySql, je zou een andere kunnen gebruiken. Dan moet je wel in de `core_project/settings.py`, sectie `DATABASES`, aanpassen die verantwoordelijk is voor de database.


### 5. Database migraties uitvoeren

Voer de database migraties uit:

```sh
python manage.py migrate
```


### 6. Superuser aanmaken

Maak een superuser aan om toegang te krijgen tot de admininterface:

```sh
python manage.py createsuperuser
```


### 7. Server starten

Start de ontwikkelserver:

```sh
python manage.py runserver
```

Je kunt nu de applicatie openen in je browser door te gaan naar http://127.0.0.1:8000/


### Extra Informatie

Admin Interface: 
- Bezoek http://127.0.0.1:8000/admin/ en log in met je superuser-account om de admininterface te bekijken.

SCSS:
- Het project maakt gebruik van SCSS in plaats van standaard CSS. Om SCSS om te zetten naar CSS, moet je een compiler gebruiken. Installeer bijvoorbeeld de "Live Sass Compiler" plugin in Visual Studio Code.

- Zorg ervoor dat de instellingen van de Live Sass Compiler correct zijn geconfigureerd om de `.scss`-bestanden naar de gewenste outputmap te compileren.



### Structuur van het Project

- manage.py - Hoofdscript voor het beheren van de applicatie.

- core_app/ - Bevat de code van de Django-app, inclusief models.py, views.py, enz.

- core_app/templates/ - Bevat HTML-bestanden voor de weergave van de applicatie.

- core_project/settings.py - Hier kan je allerlei instellingen veranderen mocht dat nodig zijn. Advies voor nu is om hier zo min mogelijk in te veranderen.