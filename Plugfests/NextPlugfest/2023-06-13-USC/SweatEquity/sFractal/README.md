# sFractal Sweat Equity

## 1. About sFractal
sFractal Consulting is a boutique consultancy assiting boards
with including cybersecurity risk in the business decision analytics. 

## 2. Attendance
sFractral intends to have 1 participant: 
* 1 (Duncan Sparrell) attending physically
* 0 attending virtual-only

For 'participating countries': USA

## 3. Use Case Sweat Equity Metric
See [Use Case Sweat Equity](../UseCases/use_case_tech.md) for explanation
of relating organizaiton's sweat equity to
Technologies / Standards / Open Source Projects to which "days" in
the [use case](../UseCases/README.md).

Leave/Augment those of the following that apply 
to what your organizaiton brings as sweat equity,
delete those that don't:
* Day 1 - CACAO
  - Human Interface (walk thru human playbooks, QuadBlockQuiz)
  - Hand-waving Lycan (create hand-waving playbooks)
* Day 1 - OpenC2
  - Human Interface (OpenC2_Test server in GCP, QuadBlockQuiz)
  - Machine Interface (Blinky/Twinkly-MaHa/HaHa, OpenC2_Test, QuadBlockQuiz)
* Day 2 - CACAO
  - Human Interface (walk thru human playbooks, QuadBlockQuiz)
  - Hand-waving Lycan (create hand-waving playbooks)
* Day 2 - OpenC2
  - Human Interface (OpenC2_Test server in GCP, QuadBlockQuiz)
  - Machine Interface (Blinky/Twinkly-MaHa/HaHa, OpenC2_Test, QuadBlockQuiz)
* Day 3 - CACAO
  - Human Interface (walk thru human playbooks, QuadBlockQuiz)
  - Hand-waving Lycan (create hand-waving playbooks)
* Day 3 - CSAF, OpenC2, PACE, SBOM, VEX
  - Human Interface (OpenC2_Test server in GCP, QuadBlockQuiz)
  - Machine Interface  (Blinky/Twinkly-MaHa/HaHa, OpenC2_Test, QuadBlockQuiz)
* Day 4 - CSAF, OpenC2, PACE, SBOM, VEX
  - Human Interface (OpenC2_Test server in GCP, QuadBlockQuiz)
  - Machine Interface (Blinky/Twinkly-MaHa/HaHa, OpenC2_Test, QuadBlockQuiz)
* Day 5 - NIEM Open
  - Human Interface (walk thru NIEM Open Scenarios, QuadBlockQuiz)
  - Hand-waving Lycan (create hand-waving NIEM Open MEPs)
* Day 6 - NIEM Open
  - Human Interface (walk thru NIEM Open Scenarios, QuadBlockQuiz)
  - Hand-waving Lycan (create hand-waving NIEM Open MEPs)


## 4. Contributions
Besides herding cats organizing,
sFractal intends to bring the following working implementations:
* blinkyMaHa
* blinkyHaHa
* twinklyHaHa
* twinklyMaHa
* OpenC2_Test
* QuadBlockQuiz

### 4.1 BlinkyMaHa
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

#### 4.1.1 BlinkyMaHa Support Files
* [OpenC2_profile_query](./OpenC2_profile_query.json) is an example OpenC2 command to query profile to any of:
  - blinkyMaHa
  - blinkyHaHa
  - twinklyHaHa
  - twinklyMaHa
  - OpenC2_Test
  - QuadBlockQuiz
* [OpenC2_profile_response01](./OpenC2_profile_response01.json) is an example OpenC2 response to query BlinkyMaHa profile
* [OpenC2_profile_response02](./OpenC2_profile_response02.json) is an example OpenC2 response to query TwinklyMaHa profile
* [OpenC2_led_off](./OpenC2_led_off.json) is an example OpenC2 command to shut the LED's off in any of:
  - blinkyMaHa
  - blinkyHaHa
  - twinklyHaHa
  - twinklyMaHa
* [OpenC2_ok](./OpenC2_ok.json) is the response to the previous command and any other command that doesn't return data
* [OpenC2_led_on01](./OpenC2_led_on01.json) is an example OpenC2 command to turn the LED's red in any of:
  - blinkyMaHa
  - blinkyHaHa
  - twinklyHaHa
  - twinklyMaHa
* [OpenC2_sbom_list_query](./OpenC2_sbom_list_query.json) is an example OpenC2 command to query sbom_list to any of:
  - blinkyMaHa
  - blinkyHaHa
  - twinklyHaHa
  - twinklyMaHa
  - OpenC2_Test
  - QuadBlockQuiz
*  [OpenC2_sbom_list_response01](./OpenC2_sbom_list_response01.json) is an example OpenC2 response to query BlinkyMaHa sbom_list
*  [OpenC2_sbom_query](./OpenC2_sbom_query.json) is an example command to query for an sbom from blinky_maha
*  [OpenC2_sbom_response](./OpenC2_sbom_response.json) is an example blinky_maha sbom response

### 4.2 BlinkyHaHa
Ditto BlinkyMaHa except using HTTP API (ie https://docs.oasis-open.org/openc2/open-impl-https/v1.1/cs01/open-impl-https-v1.1-cs01.html)

### 4.3 TwinklyMaHa
* "Twinkly" - this is the digital twin of Blink ie hello world of IoT ie blinking lights but done on a webpage.
* MaHa - same as BlinkyMaHa

Basically this is the digital twin of BlinkyMaHa. 

An older version is available at https://twinklymaha-prod-q353uyxfhq-uk.a.run.app/ but will be updated prior to event.


### 4.4 TwinklyHaHa
ditto TwinklyMaHa but HTTP (ie it's digital twin of BlinkyHaHa).

### 4.5 OpenC2_Test
The webserver is used to test the other sFractal devices
(and other people's if desired).
It consists of a server that a human can control
(via the web interface) what OpenC2 commands are
sent to which devices (and see what comes back).

### 4.6 QuadBlockQuiz
QuadBlockQuiz is a 'falling blocks' game combined with a trivia quiz
and designed to teach supply chain security concepts
and all the stuff associated with CASP. 
A special CASP version will be available for the event.
Note the SBOM is available for QBQ and the website itself 
can be a node for for interworking (besides being fun to play).
Older copy is at https://quadquiz-q353uyxfhq-uk.a.run.app/ 
and will be updated by event

## 5. Planned Use Cases
See Section 3.

Other use cases supported are Business Email Compromise, payroll hijack, ...

## 6. Planned Interactions
Plan is to interwork all the sFractal OpenC2 consumers (Blinky/Twinkly-MaHa/HaHa)
with sFractal OpenC2 producers (OpenC2_Test)
and with HII OpenC2 producers (OIF),
as well as any others present.

Plan is to interwork sFractal OpenC2 producers (OpenC2_Test)
with HII OpenC2 consumers (OIF, Yukki).

Put desription of detailed command/responses here with links to command files.

