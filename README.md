# TEMA DE SEMESTRU 

## SISTEM DE SECURITATE CU RASPBERRY PI PICO W

# Ce face programul?
- Aceasta aplicatie reprezinta un sistem de securitate. Sistemul asteapta dechiderea usii, iar in momentul deschiderii incepe patea de rulare a codului prin inceperea un timer si,in intervalul de x secunde (se poate odifica din cod), se doreste validarea unui card. Daca cardul nu este validat corect in intervalul de x secunde alarma incepe sa sune si se trimite un mesaj automat pe telegram de alerta.

# Contributie Ghica Antonio Stefan

# Despre ce este vorba in partea mea de cod
- Codul urmator este doar o parte din proiectul de casa final. Acesta ar trebui sa indeplineasca urmatoarea functie: de a transmite un mesaj de alert automat pe telegram in cazul in care cineva incearca sa patrunda intr-o locuinta daca nu a satisfacut cerintele sistemului de securitate.
1. CE TREBUIE INSTALAT
   - pentru a rula acest cod trebuie instalata biblioteca requests din terminalul mediului de programare in care lucrati. Pentru instalare biblioteci folositi urmatoarea comanda: pip install requests sau python -m pip install requests.
2. CUM SE RULEAZA
   - rularea programului se face apasand pe butonul de run din partea superioara a ecranului (in cazul in care folositi Pycharm) sau Run->Run Module (daca folositi Python IDLE)
3. REFERINTE RELEVANTE
     - [Getting Started: Using Raspberry Pi Pico W with Telegram Bot](https://www.youtube.com/watch?v=hHQu4O9OnVo)
     - [How to create a Telegram Bot in Python](https://www.youtube.com/watch?v=URPIZZNr_2M)
     - [Chat GPT](https://chat.openai.com/share/4d0a8dca-6bb5-41d2-89af-977259f9a3ca)
    



# Contributie Rocsin Dragos Teodor

## Cum se rulează programul?

- Se descarcă fișierul sistem_securitate.py în memoria internă a Raspberry Pi Pico W.
- Pentru a rula programul fără a fi conectat la calculator, se schimbă numele fișierului **sistem_securitate.py** în **main.py**.

## Ce trebuie instalat?

- Se instalează IDE-ul Thonny, pentru a comunica cu microcontroler.
- Trebuie instalată biblioteca pentru RFID, care se găsește în **Referințe**. După ce o descarci, se caută fișierul descărcat în Thonny la secțiunea **Files** și se descarcă în fișierul root al lui Raspberry Pi Pico W.

## Cum se configureaza Thonny?

- dupa ce se instaleaza ultima versiune [4.1.4](https://thonny.org/),se deschide meniul de Tools->Options->Interpreter si se alege MicroPython(Raspberry Pi Pico).Pentru a putea rula MicroPython,tot in fereastra cu Interpreter se apasa pe **Install or update MicroPython**.
- Din meniul View se selecteaza optiunea Files pentru a putea vizualiza fisierele locale de pe calculatorul propriu si cele de pe Raspberry Pi Pico.

## Referințe

- [Pico W cu RFID](https://www.tomshardware.com/how-to/raspberry-pi-pico-powered-rfid-lighting)
- [Bibliotecă + Documentație RFID](https://github.com/danjperron/micropython-mfrc522)
- [Dual Cores](https://www.youtube.com/watch?v=9vvobRfFOwk&t=356s)
- [Dual Cores](https://www.youtube.com/watch?v=ZEgqrNXuBvk&t=1652s)
- [Chat GPT](https://chat.openai.com/share/94c98430-95df-4ef7-90f5-489854a2063b)

