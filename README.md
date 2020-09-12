# Wetterlogger
Wetterdaten für konfigurierbare Standorte über die openweathermap.org API abrufen und in einer mongodb Datenbank speichern. Dieses Projekt wurde für den RaspberryPi 3 entwickelt. Dank der Container-Architektur kann dieses Programm jedoch auch auf andere Systeme portiert werden.

## Openweathermap.org API
Die Organisation openweathermap stelle eine kostenlose API bereit, mit der Wetterdaten bis zu 1000x am Tag abgerufen werden können (max. 60 Abrufe pro Stunde). Alternativ muss auf eine kostenpflichtige Variante zurückgegriffen werden (stand 15.04.2020).
Nach der erfolgreichen Registrierung können beliebig viele API Keys generiert werden. Diese müssen anschließend im Programm hinterlegt werden.

Weitere Informationen:  
[1] https://openweathermap.org/current

## Docker Container
Mittels docker-compose werden zwei Container erzeugt. Einer beinhaltet die mongodb Datenbank und der andere stellt eine Python3 Umgebung zum Abrufen der Wetterdaten bereit.  
Die Container können mit <i>docker-compose</i> generiert werden.
```
docker-compose build
```
Nach dem erstellen können die Container mit dem folgenden Befehl gestartet werden.
```
docker-compose up -d
```

### Datenbank
Der Datenbankcontainer basiert auf einem ARM kompatiblen Image für mongodb V2. Ein Zugriff auf die Datenbank ist über den Port 27017 möglich. Es sind keine weiteren Benutzerdaten erforderlich.

### Python3 Container
Dieser Container basiert auf einem Ubuntu Image und stellt eine Python3 Umgebung bereit mit den installierten Python-Bibliotheken pymongo und requests.  
Hinweis: Es muss ggf. die Zeitzone im Container geändert werden, sodass die generierten Zeitstempel mit der tatsächlichen Uhrzeit übereinstimmen.

#### Python3 Container - Zeitzone ändern
Nachdem der Container erstellt wurde muss ggf. die Zeitzone noch angepasst werden. Hierzu muss das Paket <b>tzdata</b> installiert werden. Während der Installation erfolgt auch die Einstellung der benötigten Zeitzone.
```
apt install tzdata
```

## Wetterdaten abrufen
Die Wetterdaten werden mit dem Python Skript <i>get_weather.py</i> abgerufen und gesichert. Hierfür empfiehlt es sich, einen cronjob anzulegen.

### Cronjob anlegen
Damit die Wetterdaten automatisiert abgerufen werden, kann ein entsprechender Cronjob eingerichtet werden. Im Terminal muss dafür folgender Befehl eingegeben werden:
```
crontab -e
```
Im folgenden Beispiel werden die Wetterdaten alle 30 min abgerufen.
```
LANG=de_DE.UTF-8
LANGUAGE=de
LC_TYPE=de_DE.UTF-8
PYTHONENCODING=utf8

*/30 * * * * python3 /home/src/get_weather.py >> /home/sc/logfile 2&>1
```
Alle Bildschirmausgaben des Programms werden im logfile (/home/src/logfile) gespeichert.  
Abschließend muss der crontab Service noch gestartet werden.
```
service cron start
```

## Wetterdaten ausgeben
Um die bereits gespeicherten Wetterdaten auf der Konsole auszugeben, kann die Datei <i>show_entries.py</i> ausgeführt werden.
