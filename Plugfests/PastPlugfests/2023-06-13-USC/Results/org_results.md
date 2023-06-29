# Results by Organization

## APL

## Cydarm

## DKS

## HII Mission Technologies Results

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

To send an OpenC2 Command to one of our devices and demonstrate interoperability, please see the [DKI Sweat Equity page](https://github.com/opencybersecurityalliance/casp/blob/main/Plugfests/NextPlugfest/2023-06-13-USC/SweatEquity/DKI/README.md)


## sFractal