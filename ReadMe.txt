Moodle Login Automation Tester

Automatiseeritud testskript, mis kasutab Pythonit ja Seleniumit, et testida sisselogimist Moodle keskkonda juhuslikult genereeritud paroolidega.
Projekt loob mitu juhuslikku parooli ja proovib nendega sisse logida, salvestades iga katse tulemuse.



Funktsionaalsus

* Genereerib juhuslikke paroole:

  * pikkus 5–12 märki (saab muuta)
  * sisaldab tähti ja numbreid
* Avab veebilehitseja automaatselt
* Navigeerib Moodle login lehele
* Sisestab kasutajanime ja genereeritud parooli
* Käivitab mitu testkatset järjest
* Kuvab iga testi tulemuse terminalis



Kasutatud tehnoloogiad

* Python
* Selenium
* Google Chrome + ChromeDriver



Paigaldamine

1. Klooni projekt
2. Paigalda vajalikud paketid

pip install selenium
pip install webdriver-manager

3. Seadistamine

Muuda skripti alguses olevad konfiguratsioonid:

URL = "https://moodle.tktk.ee/"
USERNAME = "sinu_kasutajanimi"
TEST_COUNT = 5

Parameetrid

| Muutuja      | Kirjeldus               |
| ------------ | ----------------------- |
| `URL`        | Moodle veebiaadress     |
| `USERNAME`   | Testitav kasutajanimi   |
| `TEST_COUNT` | Mitu testkatset tehakse |

4. Käivitamine

Käivita skript käsurealt:


Koodi ülesehitus
`generate_password()`
Genereerib juhusliku parooli.

`perform_login()`
Teostab veebis sisselogimise Seleniumiga.

`run_tests()`
Käivitab kõik testid, kogub tulemused ja sulgeb brauseri.

Võimalikud edasiarendused
* CSV raporti salvestamine
* Logifailide loomine
* Eduka/ebaeduka login kontroll
* Erinevate brauserite tugi
* Paralleliseeritud testimine

Autor
Rannar Robin Laast