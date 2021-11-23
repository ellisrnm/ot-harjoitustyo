# Ohjelmistotekniikka

Tämä repositorio on tehty Helsingin Yliopiston kurssia Ohjelmistotekniikka varten

## Bugiseurantasovellus

Sovelluksen avulla sovelluksen käyttäjä voi pitää kirjaa ohjelmointiprojekteistansa ja niissä ilmenneistä virheistä/kehityskohteista. Tällä hetkellä sovelluksella on vain yksi käyttäjä.

Tällä hetkellä sovellukseen voi tallentaa projekteja, aliprojekteja ja bugeja (ainoastaan niiden nimi). Tiedot eivät kuitenkaan vielä tallennu vaan häviävät, kun sovelluksen sulkee. Tämä korjataan seuraavaksi.

Sovelluksen toiminta on testattu Python-versiolla 3.8.

### Dokumentaatio

- [Määrittelydokumentti](https://github.com/ellisrnm/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/ellisrnm/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

### Ohjelman suorittaminen

Ohjelman suoritus onnistuu komennolla:

        poetry run invoke start

Ohjelman testien suoritus onnistuu komennolla:

        poetry run invoke test

Testikattavuusraportin generointi onnistuu komennolla:

        poetry run invoke coverage-report
