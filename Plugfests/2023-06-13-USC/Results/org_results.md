# Results by Organization

## APL

## Cydarm

## DK

## HII Mission Technologies

Five personnel attended (all virtual):

| **Name** | **Role** | **Company** |
|---|---|---|
| Larry Feldman | systems engineer | HII-MT |
| Matt Roberts | software team lead | Bestgate Engineering |
| Kevin Cressman | software developer | Praxis Engineering |
| Kaitlyn Hsu | software developer | Bestgate Engineering | 
| Kouloum Abidji | software developer | HII-MT |


HII's team contributed the following for interoperability and as part of their demonstration:

 * [OIF-Orchestrator](https://github.com/oasis-open/openc2-oif-orchestrator) -- JSON schema-driven OpenC2 Producer, supporting transfers over HTTPS and MQTT 
* [OIF-Device](https://github.com/oasis-open/openc2-oif-device) -- JSON schema-driven OpenC2 Consumer, supporting transfers over HTTPS and MQTT 
* [Yuuki](https://github.com/oasis-open/openc2-yuuki) -- OpenC2 Consumer implemented in Python

We have been working on the development of an OpenC2 [Actuator Profile](https://docs.oasis-open.org/openc2/oc2arch/v1.0/cs01/oc2arch-v1.0-cs01.html#e1-application-of-actuator-profiles-and-transfer-specifications) for [Threat Hunting (TH)](https://github.com/oasis-tcs/openc2-ap-hunt/blob/working/ap-hunt-v1.0.md) (link is to work-in-progress draft document and schema) in concert with the OCA [Kestrel](https://github.com/opencybersecurityalliance/kestrel-lang) team, and demonstrated the use of OpenC2 to:

 * query a TH Consumer regarding available huntbooks and data sources
 * initiate a hunt using a specified huntbook, data source(s), and hunt arguments
 * return data from Kestrel using a mix of OIF-Device and Yuuki Consumers

The capability to invoke threat hunting via OpenC2 is an extension of the original [Kestral Black Hat USA 2022 demonstration](https://github.com/opencybersecurityalliance/black-hat-us-2022) using OpenC2 mechanisms based on OASIS specifciations. 

We also planned to show a [CACAO](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=cacao) playbook keyed to the events of the CASP [Ransomware use case](https://github.com/opencybersecurityalliance/casp/tree/main/UseCases#21-ransomware), but did not get it completed in time for the event, so we provided logic to indicate the proposed playbook's functions instead.

To send an OpenC2 Command to one of our devices and demonstrate interoperability, please see the [DKI Sweat Equity page](https://github.com/opencybersecurityalliance/casp/blob/main/Plugfests/2023-06-13-USC/SweatEquity/DKI/README.md)


## sFractal
One participant (Duncan Sparrell) attended physically.

### sFractal TwinklyMaha
sFractal contributed a working TwinklyMaha
* code at [TwinklyMaHa](https://github.com/sFractal-Podii/TwinklyMaHa)
* instantiated at [TwinklyMaHa](https://twinklymaha-staging-q353uyxfhq-uk.a.run.app/twinkly)
   - note it intantiates when accessed, so give it a couple of minutes when you first access in a session

TwinklyMaha was part of Days 1,2,3 demonstrating:
* SBOM as part of build, and used in use case  as part of PACE security posture
* VEX demonstrating CSAF/VEX and used in use case as part of PACE security posture
* working OpenC2 code (note different programming language than HII with which it was interoperable - sort of) over MQTT
* caused "virtual" leds to blink via OpenC2 commands - simulated cybersecurity commands as part of use case
* retreived SBOMs via OpenC2 commands as part of use case
* hand-waved retreived VEXs via OpenC2 commands as part of use case
### sFractal OpenC2 Test
sFractal contributed a working (mostly) working website to be the 
OpenC2 producer to talk MQTT to OpenC2 consumers like 
TwinklyMaha, BlinkyMaHa, OIF, Yukki.
There were issues that sFractal stuff only worked with the Mosquito MQTT3.1 test
broker and not the AWS MQTT3.1 or the HiveMQ MQTT5 text brokers.
But it did work for sFractal TwinklyMaHa and HII TwinklyMaHa as well.
### sFractal BlinkyMaHa
sFractal contributed a working (mostly) Raspberry Pi running 
[BlinkyMaHa](oops - need to commit new version from local) demonstrating:
* ditto TwinklyMaHa with exception that blinking lights was direct from laptop, not via test MQTT brokers due to networking issues.

### sFractal Other
Unfortunately sFractal did not get TwinklyHaHa or BlinkyHaHa operational 
for this event. Next time.
QuadBlockQuiz was operational but not optimized for this event 
and we didn't have time to play the game or have a contest. Next time.

