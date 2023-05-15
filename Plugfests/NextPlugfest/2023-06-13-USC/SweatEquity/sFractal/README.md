# sFractal Sweat Equity

## 1. Attendance
sFractal intends to have one participant (Duncan Sparrell)
who will attend physically 
(assuming I don't get sent to hospital like last time).
For 'participating countries': USA

## 2. Contributions
Besides herding cats organizing,
sFractal intends to bring the following working implementations:
* blinkyMaHa
* blinkyHaHa
* twinklyHaHa
* twinklyMaHa
* OpenC2_Test
* QuadBlockQuiz

### 2.1 BlinkyMaHa
* "Blinky" - hello world of IoT ie blinking lights
* "MaHa"
  - MA - Mqtt API - ie impliments [OpenC2 MQTT Transfer Spec](https://docs.oasis-open.org/openc2/transf-mqtt/v1.0/transf-mqtt-v1.0.html)
  - HA - "Hello World Actuator" - ie implements a trivial OpenC2 "hello world" actuator profile. Actually does slightly more than that since it allows OpenC2 to blink lights as well as implementing SBOM Actuator Profile and can even fake it for [packet filtering actuator profile](http://docs.oasis-open.org/openc2/oc2slpf/v1.0/oc2slpf-v1.0.html)
  
BlinkyMaHa is a physical device that will be brought to USC. 
It is a raspberry pi, running the Nerves operating system,
that implements a custom OpenC2 Actuator profile interfacing over the
MQTT OpenC2 transfer specification.

Attached to the raspberry pi is an LED panel.
The LEDs can be controlled via OpenC2 commands:
![blinkylights](https://www.youtube.com/watch?v=RcnRFfFtKQY | width=250)

Other OpenC2 commands include:
* query profile - returns which profiles the device supports
* query SBOM - returns a list of SBOM, or a specific SBOM, from the device

BlinkyMaHa is implemented in opensource. 
The repo can be found at https://github.com/sFractal-Podii/BlinkyMaha.

The intent is for BlinkyMaHa to communicate with 
anything that will talk MQTT with it. 
It will initially be configured for the Mosquito test broker.

sFractal - sFractal tests can be run by controlling BLinkyMaHa
from the OpenC2 test server.

### 2.2 BlinkyHaHa
Ditto BlinkyMaHa except using HTTP API (ie https://docs.oasis-open.org/openc2/open-impl-https/v1.1/cs01/open-impl-https-v1.1-cs01.html)

### 2.3 TwinklyMaHa
* "Twinkly" - this is the digital twin of Blink ie hello world of IoT ie blinking lights but done on a webpage.
* MaHa - same as BlinkyMaHa

Basically this is the digital twin of BlinkyMaHa. 

An older version is available at https://twinklymaha-prod-q353uyxfhq-uk.a.run.app/ but will be updated prior to event.


### 2.4 TwinklyHaHa
ditto TwinklyMaHa but HTTP (ie it's digital twin of BlinkyHaHa).

### 2.5 OpenC2_Test
The webserver is used to test the other sFractal devices
(and other people's if desired).
It consists of a server that a human can control
(via the web interface) what OpenC2 commands are
sent to which devices (and see what comes back).

### 2.6 QuadBlockQuiz
QuadBlockQuiz is a 'falling blocks' game combined with a trivia quiz
and designed to teach supply chain security concepts
and all the stuff associated with CASP. 
A special CASP version will be available for the event.
Note the SBOM is available for QBQ and the website itself 
can be a node for for interworking (besides being fun to play).
Older copy is at https://quadquiz-q353uyxfhq-uk.a.run.app/ 
and will be updated by event

## 3. Planned Technologies
### 3.1 Machine to Machine
fill in which interfaces of which devices talk which technologies
### 3.2 Human to Machine

### 3.3 Handwaving
eg cacao - sFractal only has CACAO flow charts for a human to follow,
not actual SOAR using machine readable CACAO playbook

## 4. Planned Use Cases
sFractal intends to participate in 3 usecases 
(maybe more if we can figure out how):
* Comply to Connect
* Ransomware
* Business Email Compromise
### 4.1 Comply to Connect

### 4.2 Ransomware

### 4.3 Business Email Compromise

## 5. Planned Interactions