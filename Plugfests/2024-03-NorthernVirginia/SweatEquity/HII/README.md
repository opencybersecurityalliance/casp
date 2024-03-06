# HII Sweat Equity

## Producers
HII plans to bring the following OpenC2 producer (mock a message from a CACAO playbook):
* [OIF-Orchestrator](https://github.com/oasis-open/openc2-oif-orchestrator), supporting
  - OpenC2 Language [required queries](https://docs.oasis-open.org/openc2/oc2ls/v1.0/cs02/oc2ls-v1.0-cs02.html#4-mandatory-commandsresponses)
  - OpenC2 Threat Hunting Actuator Profile (Schema) ([working version](https://github.com/dlemire60/openc2-ap-hunt/blob/working/ap-hunt-v1.0.md))
  - [MQTT Transfer Specification](https://docs.oasis-open.org/openc2/transf-mqtt/v1.0/cs01/transf-mqtt-v1.0-cs01.html#22-default-topic-structure) (v5.0)
  - [HTTPs Transfer Specification](https://docs.oasis-open.org/openc2/open-impl-https/v1.1/cs01/open-impl-https-v1.1-cs01.html)

## Consumers
* HII depends on another organization to standup a consumer to then consume OpenC2 Commands.  Here are the communication requirements needed:
* Connect to an MQTTv5 capable Broker, see connect info
* Process OpenC2 commands dropped on the Broker's Topic according to the OpenC2 MQTT Transfer Specification
* Respond by dropping an OpenC2 Reponse message on the Broker's Response Topic
* See command and response examples below

## MQTT Connection Info
### Note about the Broker: 
* We would prefer to use Dave Kemp's HiveMQ, but we're unable to connect at the moment.  For now, we can use the "test.mosquitto.org"  until we get the HiveMQ connects resolved.

### Notes aobut topics:
* oc2/cmd/device/<your-device-id> (and no, we've never spec'd a format for device ID)
* oc2/cmd/ap/<topic for every profile the consumer supports>

```
broker = "test.mosquitto.org" 
port = 1883
transport = "tcp"
listen_topics = ["oc2/cmd/all","oc2/cmd/ap/hunt","oc2/cmd/ap/slpf","oc2/cmd/device/<your-device-id>"]
resp_topics = ["oc2/rsp"]
```

## Threat Hunt Command Message Example
### Note about message properties:
* Actuator_id is optional.  Only needed internally for the OIF Orchestrator.

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
* HII intends on interfacing with any other organization's device that is listening to Threat Hunt Commands from HII on the MQTT Topics related to this effort. 
* In addition, HII intends to interface with Threat Hunt responses dropped on the provided MQTT Reposnse Topic.

## High Level Use Case Illustration
![OC2 & Kestrel HL UC](https://github.com/ScreamBun/openc2-oif-device/blob/master/assets/oc2_kestrel_use_case.png)

