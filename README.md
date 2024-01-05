#TEMA DE SEMESTRU 
##SISTEM DE SECURITATE W RASPBERRY PI PICO W

#Ce componente iti trebuie?
-2 LED-uri, unul verde , unul rosu
-3 butoane
-2 rezistente de 220Ohm, o  rezistente de 1kohm si 3 de 10kohm
-2n2222 ( tranzistor de tip  NPN)
-un active buzzer
-un modul RFID_RD522
-o placuta Raspberry pi Pico W

#Cum se monteaza circuitul?
-Se urmareste ```circuit.png``` pentru asamblarea circuitului

#Cum se ruleaza programul?
-Se descarca fisierul sistem_securitate.py in memoria interna a Raspberry pi Pico W.
-Pentu a rula programul fara a fi conectat la calculator, se schimba numele fisierului  ```sistem_securitate.py``` , in ```main.py````


#Ce trebuie instalat?
-Se instaleaza IDE-ul Thonny, pentru a comunica cu microcontroler
-Trebuie instalata este biblioteca pentru RFID care  se gaseste in ```Referinte````. Dupa ce o descarca se cauta fisierul descarcat in Thonny la sectiunea  ```Files```, si se descarca in fisierul root al lui Raspberry pi Pico W.



##Referinte
-[PicoW cu RFID](https://www.tomshardware.com/how-to/raspberry-pi-pico-powered-rfid-lighting)
-[Biblioteca+Documentatie RFID](https://github.com/danjperron/micropython-mfrc522)
-[Dual Cores](https://www.youtube.com/watch?v=9vvobRfFOwk&t=356s)
-[Dual Cores](https://www.youtube.com/watch?v=ZEgqrNXuBvk&t=1652s)

-[ChatGBT](https://chat.openai.com/share/94c98430-95df-4ef7-90f5-489854a2063b)
