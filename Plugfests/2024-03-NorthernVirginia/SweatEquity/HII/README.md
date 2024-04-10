# HII Sweat Equity

<<<<<<< main
## Use Case Support
HII will participate in a demonstration session with Kestrel to illustrate the
use of OpenC2 to invoke Kestrel capabilities in a hunting operation. This
demonstration will employ the Olympic Destroyer data set developed by the
Indicators of Behavior project, the Kestrel hunting engine, OpenC2 Consumers
provided by IBM and HII supporting the Threat Hunting AP, and an OpenC2 Producer
provided by HII.

## CACAO Playbook
HII has developer a [CACAO playbook](./playbook--OpenC2-Kestrel-Hunting-Demo_2024-04-10T14_57_42.134Z.json)
that captures the flow of the hunting operation from this demonstration. This
playbook aligns with the hunting process described in Kestrel's 
[Jupyter Notebook](https://github.com/opencybersecurityalliance/casp/blob/main/Plugfests/2024-03-NorthernVirginia/SweatEquity/IBM/complete_hunt.ipynb)
for the demonstration.


## Producers
HII plans to bring the following OpenC2 producer (mock a message from a CACAO playbook):
* [OIF-Orchestrator](https://github.com/oasis-open/openc2-oif-orchestrator), supporting
  - OpenC2 Language [required queries](https://docs.oasis-open.org/openc2/oc2ls/v1.0/cs02/oc2ls-v1.0-cs02.html#4-mandatory-commandsresponses)
  - OpenC2 Threat Hunting Actuator Profile (Schema) ([working version](https://github.com/dlemire60/openc2-ap-hunt/blob/working/ap-hunt-v1.0.md))
  - [MQTT Transfer Specification](https://docs.oasis-open.org/openc2/transf-mqtt/v1.0/cs01/transf-mqtt-v1.0-cs01.html#appendix-e-examples) (v5.0)
  - [HTTPs Transfer Specification](https://docs.oasis-open.org/openc2/open-impl-https/v1.1/cs01/open-impl-https-v1.1-cs01.html)

## Consumers
* HII depends on other organizations to stand up consumers to then consume OpenC2 Commands.  Here are the communication requirements needed:
* Connect to an MQTTv5 capable Broker, see connect info
* Process OpenC2 commands dropped on the Broker's Topic according to the [OpenC2 MQTT Transfer Specification](https://docs.oasis-open.org/openc2/transf-mqtt/v1.0/cs01/transf-mqtt-v1.0-cs01.html#22-default-topic-structure) 
* Respond by dropping an OpenC2 Reponse message on the Broker's Response Topic
* See command and response examples below

## MQTT Connection Info
### Note about the Broker: 
* We are using Dave Kemp's HiveMQ, see connection info below.  If issues pop up we can jump to "test.mosquitto.org" as a backup option

### Notes aobut topics:
* oc2/cmd/device/<your-device-id> (and no, we've never spec'd a format for device ID)
* oc2/cmd/ap/<topic for every profile the consumer supports>

MQTT Broker:
```
broker = "3271a3ddd2eb43caa7c4b195c7d6cabd.s2.eu.hivemq.cloud" 
port = 8883
transport = "tcp"
username = 'Cav01'
password = 'Tango01Village'
listen_topics = ["oc2/cmd/all","oc2/cmd/ap/hunt","oc2/cmd/ap/slpf","oc2/cmd/device/<your-device-id>"]
resp_topics = ["oc2/rsp"]
```

Backup MQTT Broker:
```
broker = "test.mosquitto.org" 
port = 1883
transport = "tcp"
listen_topics = ["oc2/cmd/all","oc2/cmd/ap/hunt","oc2/cmd/ap/slpf","oc2/cmd/device/<your-device-id>"]
resp_topics = ["oc2/rsp"]
```

### Notes about message creation
* The OpenC2 Integration Framework is schema-driven, and uses this JSON conversion of the 
 [Threathunting Profile draft](https://github.com/oasis-tcs/openc2-ap-hunt/blob/working/schemas/resolved%20schemas/resolved-hunt.json).

* Message Property Actuator_id is optional.  Only needed internally for the OIF Orchestrator.
 ## Threat Hunt Command Message Example

```
{
    'headers': {
        'request_id': '40eac796-43c2-4f3e-8ab1-a51e37380e0e',
        'from': 'oif-orch',
        'to': 'oc2/cmd/ap/hunt',
        'created' : 1709671071578,
        'actuator_id' : '8144acd3-f5d6-4bda-b1bd-a964f4a19677'
    },
    'body': {
        'openc2': {
            'request': {
                'action': 'investigate',
                'target': {
                    'th': {
                    'hunt': './hunts/huntflow/find_data_via_stixshifter.hf'
                    }
                }
            }
        }
    }
}
```

## Threat Hunt Response Message Example
```
{
  "headers": {
    "request_id": "40eac796-43c2-4f3e-8ab1-a51e37380e0e",
    "created": 1709671082933,
    "from": "oif-device-9baf5863-fe55-4bc5-9537-eb9282a08a50",
    "to": "oc2/rsp"
    "actuator_id": "8144acd3-f5d6-4bda-b1bd-a964f4a19677"
  },
  "body": {
    "openc2": {
      "response": {
        "status": 200,
        "results": {
          "x_unique_id": "MYORGIDX-01aac66c-00000820-00000000-1d70c280e79cd04",
          "name": "compattelrunner.exe",
          "pid": 2080,
          "id": "process--69e78267-5a16-513a-b4e5-ecd8577dae1b",
          "command_line": null,
          "created": null,
          "binary_ref.name": "compattelrunner.exe"
        }
      }
    }
  }
}
```

## Further Assistance
Need help setting up a device and connecting an MQTT or HTTP endpoint?  No problem, check out our OIF Device code.
* [openc2-oif-device](https://github.com/ScreamBun/openc2-oif-device)
  * The mqtt_test.py provides a small example of connecting to an MQTT Broker

## Project-centric Interfaces
### OpenC2
* HII intends to interface with any other organization's device that is listening to Threat Hunt Commands from HII on the MQTT Topics related to this effort. 
* In addition, HII intends to interface with Threat Hunt responses dropped on the provided MQTT Response Topic.

## High Level Use Case Illustration
* We plan to show the following implementation of the [OrchestratedHunt](https://github.com/ScreamBun/casp/tree/main/Plugfests/2024-03-NorthernVirginia/UseCases/PractitionerUseCases/OrchestratedHunt) Practicioner Use Case, focused on steps 3 and 4. 

![OC2 & Kestrel HL UC](https://github.com/ScreamBun/openc2-oif-device/blob/master/assets/oc2_kestrel_use_case.png)

