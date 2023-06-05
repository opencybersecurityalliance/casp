HII to add stuff here on 
OIF, etc 
and ties to kestrel, stixshifter 
interworking as part of ransomware use case

# HII Mission Technologies Sweat Equity

## 1. About HII Mission Technologies

[HII Mission Technologies](https://hii.com/what-we-do/divisions/mission-technologies/) is a division of [HII](https://hii.com) that develops integrated solutions for defense and intelligence. 

Our systems engineering and software team supports government customers with cybersecurity auomation tooling.

## 2. Attendance

Five personnel plan to attend (all virtual)

 * Larry Feldman (systems engineer)
 * Matt Roberts (software team lead)
 * Kevin Cressman (software developer)
 * Kaitlyn Hsu (software developer)
 * Kouloum Abidji (software developer)

Team is based in Maryland, USA

## 3. Contributions

HII's team plans to contribute the following:

 * [OIF-Orchestrator](https://github.com/oasis-open/openc2-oif-orchestrator) -- JSON schema-driven OpenC2 Producer, supporting transfers over HTTPS and MQTT 
* [OIF-Device](https://github.com/oasis-open/openc2-oif-device) -- JSON schema-driven OpenC2 Consumer, supporting transfers over HTTPS and MQTT 
* [Yuuki](https://github.com/oasis-open/openc2-yuuki) -- OpenC2 Consumer implemented in Python

We have been working on the development of an OpenC2 [Actuator Profile](https://docs.oasis-open.org/openc2/oc2arch/v1.0/cs01/oc2arch-v1.0-cs01.html#e1-application-of-actuator-profiles-and-transfer-specifications) for [Threat Hunting](https://github.com/oasis-tcs/openc2-ap-hunt/blob/working/ap-hunt-v1.0.md) (link to work-in-progress draft document and schema) in concert with the OCA [Kestrel](https://github.com/opencybersecurityalliance/kestrel-lang) team, and will demonstrate the use of OpenC2 to;

 * query a TH Consumer regarding available huntbooks and data sources
 * initiate a hunt using a specified huntbook, data source(s), and hunt arguments
 * return data from Kestrel using a mix of OIF-Device and Yuuki Consumers

The capability to invoke threat hunting via OpenC2 is an extension of the original [Kestral Black Hat USA 2022 demonstration](https://github.com/opencybersecurityalliance/black-hat-us-2022) using OpenC2 mechanisms based on OASIS specifciations. 

We also plan to show a [CACAO](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=cacao) playbook keyed to the events of the CASP [Ransomware use case](https://github.com/opencybersecurityalliance/casp/tree/main/UseCases#21-ransomware).