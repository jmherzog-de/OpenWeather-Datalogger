FROM ubuntu
LABEL maintainer="Jean-Marcel Herzog <dev@jmherzog.de>"

# Distributions Update und Upgrade durchführen
RUN apt update -y
RUN apt upgrade -y

# essentielle Dinge installieren
RUN apt install -y apt-utils locales locales-all nano cron

# Python3 und pip installieren
RUN apt install -y python3 python3-pip

# Umgebungsvariablen für Zeichenkodierung setzen
ENV LC_ALL de_DE.UTF-8
ENV LANG de_DE.UTF-8
ENV LANGUAGE de_DE.UTF-8

# benötigte pip Packete installieren
RUN pip3 install pymongo
RUN pip3 install requests

# Einstiegspunkt für Benutzer in Container setzen
ENTRYPOINT [ "/bin/bash" ]