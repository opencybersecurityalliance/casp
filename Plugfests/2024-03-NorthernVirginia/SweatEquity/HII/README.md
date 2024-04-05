# HII Sweat Equity

## Consumers
HII plans to bring the following OpenC2 consumers:
* [OIF-Device](https://github.com/oasis-open/openc2-oif-device), supporting
  - OpenC2 Language [required queries](https://docs.oasis-open.org/openc2/oc2ls/v1.0/cs02/oc2ls-v1.0-cs02.html#4-mandatory-commandsresponses)
  - OpenC2 Threat Hunting AP ([working version](https://github.com/dlemire60/openc2-ap-hunt/blob/working/ap-hunt-v1.0.md))
  - [MQTT Transfer Specification](https://docs.oasis-open.org/openc2/transf-mqtt/v1.0/cs01/transf-mqtt-v1.0-cs01.html#appendix-e-examples) (v3.1.1 or v5.0)
  - [HTTPs Transfer Specification](https://docs.oasis-open.org/openc2/open-impl-https/v1.1/cs01/open-impl-https-v1.1-cs01.html)

## Project-centric Interfaces
### OpenC2
fill in on general, Threat Hunting AP, maybe fake some of endpoint AP commands?

## Use Case Support
HII will participate in a demonstration session with Kestrel to illustrate the
use of OpenC2 to invoke Kestrel capabilities in a hunting operation. This
demonstration will employ the Olympic Destroyer data set developed by the
Indicators of Behavior project, the Kestrel hunting engine, OpenC2 Consumers
provided by IBM and HII supporting the Threat Hunting AP, and an OpenC2 Producer
provided by HII.

## CACAO Playbook
HII has developer a [CACAO
playbook](./playbook--b3682304-868d-4cf0-a315-2db02e8c8f37__2024-04-03T14_50_14.504Z.json)
that captures the flow of the hunting operation from this demonstration. This
playbook aligns with the hunting process described in Kestrel's 
[Jupyter Notebook](https://github.com/opencybersecurityalliance/casp/blob/main/Plugfests/2024-03-NorthernVirginia/SweatEquity/IBM/complete_hunt.ipynb)
for the demonstration.