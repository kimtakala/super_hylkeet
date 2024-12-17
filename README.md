[![codecov](https://codecov.io/github/kimtakala/super_hylkeet/graph/badge.svg?token=W3WD4WF2HB)](https://codecov.io/github/kimtakala/super_hylkeet)

# Ohtu miniprojekti 

Lue [täältä](https://ohjelmistotuotanto-hy.github.io/flask/) lisää.

[Product backlog](https://docs.google.com/spreadsheets/d/192OH0Gq0Nh96UT-f3r_uvsDfvzk0OrMsJ6RSW5z-ffw/edit?gid=0#gid=0)


## Käynnistysohjeet

Luo tietokanta.

Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon. Luo sinne .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:

```
DATABASE_URL=postgresql://xxx
TEST_ENV=true
SECRET_KEY=satunnainen_merkkijono
```

Lataa sovelluksen riippuvuudet komennolla:

````
poetry install
````

Siirry virtuaaliympäristöön komennolla:

````
poetry shell
````

Luo tietokantataulut komennolla:
````
python src/db_helper.py
````


Käynnistä sovellus komennolla:

````
python3 src/index.py
````

Tietokantaan voi luoda esimerkki sisältöä komennolla:
````
robot populate_database/1_generate_data.robot
````

Tietokannan voi tyhjentää komennolla:
````
robot populate_database/2_clear_db.robot
````

Testit voi suorittaa komennolla:
````
robot src/story_tests/
````


### Valmiin määritelmä

Ryhmämme määrittää ominaisuuden valmiiksi kun se:
- toimii halutulla tavalla
- on testattu
- on integroitu sovellukseen onnistuneesti


# Raportti
https://docs.google.com/document/d/1vVZflxoTBw85qeFPYgWaDHGju7mM0eVwULu1zpogyvk
