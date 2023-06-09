<!-- title: Your Title --> 
# HII Mission Technologies Sweat Equity

- [1. About HII Mission Technologies](#1-about-hii-mission-technologies)
- [2. Attendance](#2-attendance)
- [3. Contributions](#3-contributions)
  - [3.1 Software Components](#31-software-components)
  - [3.2 Threat Hunting (TH) Actuator Profile (AP)](#32-threat-hunting-th-actuator-profile-ap)
  - [3.3 CACAO Playbook Example](#33-cacao-playbook-example)

## 1. About HII Mission Technologies

[HII Mission Technologies](https://hii.com/what-we-do/divisions/mission-technologies/) is a division of [HII](https://hii.com) that develops integrated solutions for defense and intelligence. 

Our systems engineering and software team supports government customers with cybersecurity auomation tooling.

## 2. Attendance

Five personnel plan to attend (all virtual):

| **Name** | **Role** | **Company** |
|---|---|---|
| Larry Feldman | systems engineer | HII-MT |
| Matt Roberts | software team lead | Bestgate Engineering |
| Kevin Cressman | software developer | Praxis Engineering |
|  Kaitlyn Hsu | software developer | Bestgate Engineering | 
| Kouloum Abidji | software developer | HII-MT |

Team is based in Maryland, USA

## 3. Contributions

HII's team plans to contribute the following:

### 3.1 Software Components

 * [OIF-Orchestrator](https://github.com/oasis-open/openc2-oif-orchestrator) -- JSON schema-driven OpenC2 Producer, supporting transfers over HTTPS and MQTT 
* [OIF-Device](https://github.com/oasis-open/openc2-oif-device) -- JSON schema-driven OpenC2 Consumer, supporting transfers over HTTPS and MQTT 
* [Yuuki](https://github.com/oasis-open/openc2-yuuki) -- OpenC2 Consumer implemented in Python

### 3.2 Threat Hunting (TH) Actuator Profile (AP)

We have been working on the development of an OpenC2 [Actuator Profile](https://docs.oasis-open.org/openc2/oc2arch/v1.0/cs01/oc2arch-v1.0-cs01.html#e1-application-of-actuator-profiles-and-transfer-specifications) for [Threat Hunting (TH)](https://github.com/oasis-tcs/openc2-ap-hunt/blob/working/ap-hunt-v1.0.md) (link is to work-in-progress draft document and schema) in concert with the OCA [Kestrel](https://github.com/opencybersecurityalliance/kestrel-lang) team, and will demonstrate the use of OpenC2 to:

 * query a TH Consumer regarding available huntbooks and data sources
 * initiate a hunt using a specified huntbook, data source(s), and hunt arguments
 * return data from Kestrel using a mix of OIF-Device and Yuuki Consumers

The capability to invoke threat hunting via OpenC2 is an extension of the original [Kestral Black Hat USA 2022 demonstration](https://github.com/opencybersecurityalliance/black-hat-us-2022) using OpenC2 mechanisms based on OASIS specifciations. 

### 3.3 CACAO Playbook Example

We also plan to show a [CACAO](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=cacao) playbook keyed to the events of the CASP [Ransomware use case](https://github.com/opencybersecurityalliance/casp/tree/main/UseCases#21-ransomware).

### 3.4 Interoperability

To send an OpenC2 Command to one of our devices and demonstrate interoperability, please see the [DKI Sweat Equity page](https://github.com/opencybersecurityalliance/casp/blob/main/Plugfests/NextPlugfest/2023-06-13-USC/SweatEquity/DKI/README.md)
