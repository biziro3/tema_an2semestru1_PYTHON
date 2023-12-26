from machine import Pin
from time import sleep
import _thread
from mfrc522 import MFRC522
import utime


btn = Pin(15, Pin.IN)  # deschide usa 
btn2 = Pin(16, Pin.IN)  # inchide usa 
btn3 = Pin(13, Pin.IN)  # validare card 

reader = MFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=1,rst=0)
redLED = Pin(18,Pin.OUT)
redLED.value(0)
greenLED = Pin(19,Pin.OUT)
greenLED.value(0)

state = False  # usa e inchisa || se trimite la bot-ul pt wapp/telegram
card_state = False  # cardul nu a fost validat || se trimite la bot-ul pt wapp/telegram
btn3_state = False
Keycard = [0x93, 0xAF, 0x86, 0x0E] #uid
Keyfob = [0xEA, 0x62, 0xA7, 0xB1] #uid

lock = _thread.allocate_lock()  # Definește lock global

def timer():
    global state, card_state, lock
    x = 20
    while x >= 0 and state: # prima conditie e pentru timer , ce a de a 2 a conditie (state) verifica daca usa e deschisa sau nu 
#         with lock: protejeaza 
        if card_state == True:
            print("Cardul a fost validat\nAcces permis")
            return
        x -= 1
        print(f"Mai aveți {x} secunde până se activează alarma")
        sleep(1)

def cardValidation():
    global card_state, btn3_state, lock
    lock.acquire()
    card_state = True # cardul a fost validat 
#     btn3_state = True  # Actualizează starea butonului btn3, inseama ca a fost apasat 
    lock.release()

def green():
    greenLED.value(1)
    utime.sleep(.5)
    greenLED.value(0)
    utime.sleep(.5)
    
def red():
    redLED.value(1)
    utime.sleep(.5)
    redLED.value(0)
    utime.sleep(.5) 


# AICI RULEAZA CODUL 

while True:
    if btn.value() == 1:
        with lock:
            state = True
        print("Usa s-a deschis")
        print("scaneaza cardul")
        sleep(0.5)
        _thread.start_new_thread(timer, ())
    if btn2.value() == 1:
        sleep(5) # in momentul in care iesi din incaperea in care se afla sistemul , poti sa-l "anunti" ca iesi incaperea si se pregateste sa ia tot procesul de la inceput
        print("usa s-a inchis")
        sleep(.5)
        with lock:
            state = False  #resetarea starii usii 
            card_state = False # resetarea starii cardului
#             btn3_state = False  # Resetarea stării butonului btn3
    
#     if btn3.value() == 1:
#         cardValidation()
    
    reader.init()
    (stat,tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat,uid) = reader.SelectTagSN()
        if uid == Keycard:
            cardValidation()
            green()
        elif uid == Keyfob:
            red()
        elif uid != Keycard:
            red()