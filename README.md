# Ohjelmistotekniikka

Tämä repositorio on tehty Helsingin Yliopiston kurssia Ohjelmistotekniikka varten

## Bugiseurantasovellus

Sovelluksen avulla sovelluksen käyttäjä voi pitää kirjaa ohjelmointiprojekteistansa ja niissä ilmenneistä virheistä/kehityskohteista. Tällä hetkellä sovelluksella on vain yksi käyttäjä.

Tällä hetkellä sovellukseen voi tallentaa projekteja, aliprojekteja ja bugeja (ainoastaan niiden nimi). Tiedot eivät kuitenkaan vielä tallennu vaan häviävät, kun sovelluksen sulkee. Tämä korjataan seuraavaksi.

Sovelluksen toiminta on testattu Python-versiolla 3.8.

### Release

- [Viikon 5 release](https://github.com/ellisrnm/ot-harjoitustyo/releases/tag/viikko5)
- [Viikon 6 release](https://github.com/ellisrnm/ot-harjoitustyo/releases/tag/viikko6)

### Dokumentaatio

- [Määrittelydokumentti](https://github.com/ellisrnm/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/ellisrnm/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

### Aloitus

Varmista, että poetry on asennettuna ja *poetry*-komento on suoritettavissa. Poetryn asennus *PATH*-muuttujaan onnistuu esimerkiksi komennolla:

        source $HOME/.poetry/env

Alusta projekti ja asenna riippuvuudet komennolla:

        poetry install

Siirry suorittamaan koodi virtuaaliympäristössä:

        poetry shell

Alusta tietokanta komennolla:

        python3 src/initialize_database.py

### Ohjelman suorittaminen

Alusta tietokanta komennolla:

        python3 src/initialize_database.py

Ohjelman suoritus onnistuu komennolla:

        poetry run invoke start

### Ohjelman testaaminen

Ohjelman testit suoritetaan komennolla:

        poetry run invoke test

Testikattavuusraportin voi luoda komennolla:

        poetry run invoke coverage-report

Avaa raportti komennolla:

        open htmlcov/index.html
