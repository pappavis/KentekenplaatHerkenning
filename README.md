Herken een auto kenteken met Python, OpenCV

# Stappenplan & benodigheden
Je benodig een Raspberry Pi, maar ook Windows is goed.
De instructies gelden voor Raspberry Pi en MacOS

## Stap 1: installeren bibliotheken
Login op jouw Pi als gebruiker pi.

```bash
pi@rpasberrypi: $ sudo pip install -y libjpeg-dev zlib1g-dev libfreetype6-dev liblcms1-dev libopenjp2-7 libtiff5
pi@rpasberrypi: $ pip install virtualenv
pi@rpasberrypi: $ virtualenv ~/venv
pi@rpasberrypi: $ source ~/venv/bin/activate
pi@rpasberrypi: (venv)$ pip install numpy imutils pytesseract opencv-python pillow
pi@rpasberrypi: (venv)$ git clone https://github.com/pappavis/KentekenplaatHerkenning
pi@rpasberrypi: (venv)$ cd KentekenplaatHerkenning
```

## Stap 2: Python kentekenplaat herkenning
Probeer een output

```bash
pi@rpasberrypi: (venv)$ python ./kentekenherkenning1.py
```

<img src="https://github.com/pappavis/KentekenplaatHerkenning/blob/main/voorbeeld_20210817140540-kentekenherkennen.jpg" width="40%" height="40%">

# CREDITS
Zie origineel <a href="https://circuitdigest.com/microcontroller-projects/license-plate-recognition-using-raspberry-pi-and-opencv">hier</a>

