# Avtomatiziran ksilofon
 Diplomska naloga
 
 Stari Arduino: COM4, ID 1 <br>
 Novi Arduino: COM7, ID 2 <br>
 <br>
 arduino_instance_id ... ARDUINO_ID <br>
 **POZOR:** zgornje nič več ne velja, saj programiranje Arduina s Python-om na koncu ni bilo mogoče.
 <br>
 
## TODO - na novo z Arduino IDE
- [x] Usposobi Arduino IDE
- [x] Preizkusi I2C vezavo med dvema Arduinoma
  - [x] Testiranje 
    - [x] Zraven poveži še Bluetooth modul HC-05 in ga preizkusi tako, da prek telefona prižgeš LED diode, ki so priklopljene na Arduino
    - [x] Preizkusi hkratnost prižiganja in ugašanja LED diod
    - [x] LED diode sedaj zamenjaj s 4-mi motorji iz robota ter popravi program tako, da boš lahko iz telefona kontrolirala 2 robotski roki na Master Arduinu.
  - [x] Pravi program za kontroliranje Avtomatiziranega ksilofona prek Bluetooth modula
    - [x] Knjižnica Xylophone; da ni potrebe po večkratnem kopiranju kode
    - [x] Program na Master Arduinu
    - [x] Program na Slave Arduinu 
- [x] Naredi Android aplikacijo, preko katere uporabnik pošilja podatke na Bluetooth, iz katerega Master Arduino podatke prebere in določene pošlje na Slave Arduino.
  - [x] ~~Usposobi Android JS~~
  - [x] ~~Usposobi Node.js~~
    - [x] ~~Inštaliraj nvm~~
  - [x] ~~Inštaliraj Android JS~~
  - [x] Inštaliraj Android Studio; za izdelavo aplikacije sem uporabila razvojno okolje Android Studio, saj mi izdelava z Android JS ni uspela (glej **Ugotovitve**).
  - [x] Aplikacija za kontroliranje Avtomatiziranega ksilofona prek Bluetooth modula
- [x] Narejeni aplikaciji dodaj možnost nalaganja MIDI datotek, katere bo Avtomatiziran ksilofon prebral in zaigral 
  - [x] Poskusi narediti svojo knjižnico za parsanje MIDI datotek ali pa poišči delujočo Java knjižnico, ki to naredi
  - [x] Z MIDI knjižnico implementiraj Java razred, ki bo prebrala note, itd. tako, da jih bo razumel Avtomatiziran ksilofon

## Napredki
- 20/06/2022 https://youtu.be/CKBQpshl-Xo
  - Na tem posnetku je prikazano kontroliranje Arduinov (Avtomatiziranega ksilofona) prek Bluetooth modula, na katerega je povezan moj prenosnik (na COM3) 
- 24/06/2022 https://youtu.be/tT9_6YZVIwU
  - Na tem posnetku je prikazano delovanje aplikacije (Xylo BOSS), preko katere kontroliram Avtomatiziran ksilofon.
- 16/07/2022 https://youtu.be/lkloqlt3Lvk
  - Na tem posnetku je prikazano nalaganje in igranje MIDI datoteke
- 16/07/2022 https://youtube.com/shorts/2oRQ_HPKiTE?feature=share
  - Na tem posnetku je prikazano simultano igranje dveh not hkrati
- 18/09/2022 https://youtu.be/60N60lc3Bh8?list=PLrysv-m3yMSXUdyY1KENl7B7qmCYhf44p
  - Na tem posnetku je prikazano delovanje končne verzije avtomatiziranega ksilofona

## Ugotovitve
1. Stabilne in delujoče knjižnice za Bluetooth (PyBluez) za Python 3.7 ali novejše ni; Python knjižnica za Arduino deluje le za Python verzije 3.7 ali novejše, stabilna verzija je le 0.22, kar pa deluje za Python 3.3 ali starejše.
2. Programirati Arduino v Python-u s knjižnico Firmata se ne da, saj se ob izklopu Arduina iz računalnika Python program v celoti izbriše, ostane le gonilnik Firmata.
3. Vezje moram narediti še enkrat
4. Uporabila bom Arduino IDE za programiranje Arduinov in Javascript za izdelavo aplikacije za Android, saj mi bo to omogočilo pošiljanje sporočil prek Bluetooth modula
5. Uporabila bom vezavo I2C Bus, kjer je Arduino na katerega je vezan Bluetooth Master, drugi Arduino in Bluetooth modul pa sta Slave.
6. Za izdelavo aplikavije za Android sem na koncu morala uporabiti razvojno okolje Android Studio, v katerem se programira v programskem jeziku Java. Ugotovila sem, da se aplikacija, ki sem jo naredila v programskem jeziku JavaScript (knjižnici Android JS in Node.js) ni hotela prevesti.
 
## Viri in povezave
1. Knjižnica Telemetrix za programiranje Arduina v programskem jeziku Python: https://mryslab.github.io/telemetrix/
2. GitHub repozitorij primerov uporabe knjižnice Telemetrix: https://github.com/MrYsLab/telemetrix/tree/master/examples
3. Knjižnica Kivy za Android GUI aplikacijo: https://kivy.org/doc/stable/gettingstarted/installation.html
4. PCB izdelava: https://jlcpcb.com/ (pošiljajo tudi v Slovenijo)
5. Načrtovanje PCB in načrta: https://easyeda.com/editor#id=280289e818d9433c9aece03fcf519e8a|6830f085d17f4884a8d563e2a4c2cf8f
6. Inštalacija Node.js: https://docs.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-wsl
7. Inštalacija Android JS: https://android-js.github.io/
8. Android dokumentacija, ki sem jo uporabila za izdelavo aplikacije: https://developer.android.com/guide
9. Uporabljena knjižnica za MIDI: https://github.com/leffelmania/android-midi-lib
