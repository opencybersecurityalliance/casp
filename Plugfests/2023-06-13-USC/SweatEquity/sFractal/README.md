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
sFractal brought the following working (if you count hand-waving) implementations:
* OpenC2_Test
* twinklyMaHa
* blinkyMaHa
* blinkyHaHa
* twinklyHaHa
* QuadBlockQuiz

### 4.1 OpenC2_Test
This webserver is used to test the other OpenC2 devices
(and eventually other people's if desired).
It consists of a server that a human can control
(via the web interface) what OpenC2 commands are
sent to which devices (and see what comes back).

For today's event, it is in it's simplest form:
* https://openc-c2-test-q353uyxfhq-uk.a.run.app/run_script
* no authorization - anyone can run it
* the only protocol is MQTTv3 (ie no MQTTv5, no HTTP/s)
* the only device to control is TwinklyMaha
* the only broker is the Mosquito Test Server
* responses are not shown (although you can see LEDs change on Twinkly)
* Note there is only one Twinkly (see below) so if multiple people use OpenC2_Test, it will get very confusing.

### 4.2 TwinklyMaHa
* "Twinkly" - this is the digital twin of Blinky (see below) ie hello world of IoT ie blinking lights but done on a webpage.
* MaHa - same as BlinkyMaHa (ie hello world of OpenC2 to blink lights)

Basically this is the digital twin of BlinkyMaHa. 

For this event, the working TwinklyMaHa is at https://twinklymaha-staging-q353uyxfhq-uk.a.run.app/twinkly

Note there is only one TwinklyMaHa MQTT server at the above address,
yet there are as many independent LED displays as people who access the page.
So things get funky if more than one person plays with MQTT (via OpenC2_Test).

Eg if two people go to Twinkly, they can independently turn on/off/color the lights
on their browser by using the button you see on the browser.
But if someone goes to OpenC2_Test and sends MQTT turn led off command,
it goes to everyone's display.

Note we are using Fire & Forget mode of MQTT, so if command is lost then it is lost.
This is not theorectical as Mosquito test server goes up and down a really lot.

See BlinkyMaha below for commands supported (too lazy to copy) 
if directly interfacing MQTTv3.

Message Headers not implemented.

An older version is available at https://twinklymaha-prod-q353uyxfhq-uk.a.run.app/ 
but it is talking to a defunct MQTT server.
However you can play with the LEDs on this one with the browser button.
Ie use this one to play around so as to not interfere with anyone using OpenC2_test


### 4.3 BlinkyMaHa
* "Blinky" - hello world of IoT ie blinking lights
* "MaHa"
  - MA - Mqtt API - ie impliments [OpenC2 MQTT Transfer Spec](https://docs.oasis-open.org/openc2/transf-mqtt/v1.0/transf-mqtt-v1.0.html)
  - HA - "Hello World Actuator" - ie implements a trivial OpenC2 "hello world" actuator profile. Actually does slightly more than that since it allows OpenC2 to blink lights as well as implementing SBOM Actuator Profile and can even fake it for [packet filtering actuator profile](http://docs.oasis-open.org/openc2/oc2slpf/v1.0/oc2slpf-v1.0.html)
  
BlinkyMaHa is a physical device that brought to the classroom at USC. 
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
It is configured for the Mosquito test broker, but not working correctly.
So handwaving is involved.

#### 4.3.1 BlinkyMaHa Support Files
* [OpenC2_profile_query](./OpenC2_profile_query.json) is an example OpenC2 command to query profile to any of:
  - blinkyMaHa
  - blinkyHaHa
  - twinklyHaHa
  - twinklyMaHa
  - OpenC2_Test
  - QuadBlockQuiz
* [OpenC2_profile_response01](./OpenC2_profile_response01.json) is an example OpenC2 response to query BlinkyMaHa profile
* [OpenC2_profile_response02](./OpenC2_profile_response02.json) is an example OpenC2 response to query TwinklyMaHa profile
   - note it's similar but different from blinky. It has the sbom profile (for responding to the software it is running itself) AND the pac profile (for responding with SBOM from other devices ie blinky since twinkly is blinky's digital twin). Note it does not have full pac capabilities - just some rudimentary to show this distinction.
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

### 4.4 BlinkyHaHa
Ditto BlinkyMaHa except using HTTP API (ie https://docs.oasis-open.org/openc2/open-impl-https/v1.1/cs01/open-impl-https-v1.1-cs01.html).
sFractal was OBE so a physical BlinkyHaHa was not brought to USC.
Note this worked 3 villages ago several years back.
It will be brought out of mothball for a future village.
For now, use handwaving.

### 4.5 TwinklyHaHa
ditto TwinklyMaHa but HTTP (ie it's digital twin of BlinkyHaHa).
TwinklyHaHa is in a similar state to BlinkyHaHa.

### 4.6 QuadBlockQuiz
QuadBlockQuiz is a 'falling blocks' game combined with a trivia quiz
and designed to teach supply chain security concepts
and all the stuff associated with CASP. 
A special CASP version was to be available for the event,
but sFractal got OBE.
Note the SBOM is available for QBQ and the website itself 
can be a node for for interworking (besides being fun to play).
The copy is still at https://quadquiz-q353uyxfhq-uk.a.run.app/ 
and will be updated or future events.

Other projects are welcome to each have their own 'category' of quiz questions.
Please submit suggestions to sFractal.

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

