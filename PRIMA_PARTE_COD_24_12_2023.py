from machine import Pin
from time import sleep
import _thread

btn = Pin(15, Pin.IN)  # deschide usa 
btn2 = Pin(16, Pin.IN)  # inchide usa
btn3 = Pin(13, Pin.IN)  # validare card 
led = Pin(14, Pin.OUT)

state = False  # usa e inchisa
card_state = False  # cardul nu a fost validat
btn3_state = False 

lock = _thread.allocate_lock()  # Definește lock global

def timer():
    global state, card_state, lock
    x = 20
    while x >= 0 and state: # prima conditie e pentru timer , ce a de a 2 a conditie (state) verifica daca usa e deschisa sau nu 
#         with lock: protejeaza 
        if btn3_state == True:
            print("Cardul a fost validat\nAcces permis")
            return
        x -= 1
        print(f"Mai aveți {x} secunde până se activează alarma")
        sleep(1)

def cardValidation():
    global card_state, btn3_state, lock
    lock.acquire()
    card_state = True # cardul a fost validat 
    btn3_state = True  # Actualizează starea butonului btn3, inseama ca a fost apasat 
    lock.release()




# AICI RULEAZA CODUL 

while True:
    if btn.value() == 1:
        with lock:
            state = True
        print("Usa s-a deschis")
        sleep(0.5)
        _thread.start_new_thread(timer, ())
    if btn2.value() == 1:
        sleep(5) # in momentul in care iesi din incaperea in care se afla sistemul , poti sa-l "anunti" ca iesi incaperea si se pregateste sa ia tot procesul de la inceput
        print("usa s-a inchis")
        sleep(.5)
        with lock:
            state = False  #resetarea starii usii 
            card_state = False # resetarea starii cardului
            btn3_state = False  # Resetarea stării butonului btn3
    if btn3.value() == 1:
        cardValidation()

