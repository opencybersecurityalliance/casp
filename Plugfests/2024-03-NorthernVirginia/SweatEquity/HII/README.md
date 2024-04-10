# HII Sweat Equity

## Table of Contents
1.  [Use Case Support](#use-case-support)
2.  [CACAO Playbook](#cacao-playbook)
3.  [OC2 Producers](#producers)
4.  [OC2 Consumers](#consumers)
5.  [MQTT Connection](#mqtt-connection-info)
6.  [Example TH Command](#threat-hunt-command-message-example)
7.  [Example TH Response](#threat-hunt-response-message-example)
8.  [Setting Up OIF](#further-oif-assistance)
9.  [Interfaces](#project-centric-interfaces)
10. [High-level UC](#high-level-use-case-illustration)
11. [Demo Commands](#demo-with-ibm-kestrel-team)
    * [Command 1](#command-1)
    * [Command 2](#command-2)
    * [Command 3](#command-3)
    * [Command 4](#command-4)
    * [Command 5](#command-5)
12. [SBOMs](#sboms)

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
* [OIF-Orchestrator](https://github.com/ScreamBun/openc2-oif-orchestrator-2), supporting
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
## Threat Hunt Command Message Example

```
{
    'headers': {
        'request_id': '40eac796-43c2-4f3e-8ab1-a51e37380e0e',
        'from': 'oif-orch',
        'to': 'oc2/cmd/ap/hunt',
        'created' : 1709671071578
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
  },
  "body": {
    "openc2": {
      "response": {
        "status": 200,
        "results": {
          "th": {
            "inv_returns": [{
                "stix_sco": [{
                    "Process": {
                      "type": "process",
                      "id": "process-one",
                      "pid": 11111
                    }
                  }, {
                    "Process": {
                      "type": "process",
                      "id": "process-two",
                      "pid": 2222222
                    }
                  }, ""],
                "string_returns": ["so foul and fair a day i have not seen", "now is the winter of our discontent"]
              }]
          }
        }
      }
    }
  }
}
```

## Further OIF Assistance
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

## Demo with IBM Kestrel Team
* Our team plans to send the following OC2 Commands over MQTT to multiple devices to trigger Kestrel Huntflows on data provided by the IOB team from the OlympicDestroyer dataset. Each command will include a brief description and a link to the Kestrel team's huntflows (in their Sweat Equity).

### Command 1
This command does not perform a kestrel hunt, but requests a list of huntflows stored in the hunt directory.
```
{
    "action": "query",
    "target": {
        "th": {
            "huntflows": {
                "path": "./"
            }
        }
    }
}
``` 
### Command 2
This command triggers a [huntflow to detect IoB T1562.004 'Disable or Modify System Firewall'](https://github.com/ScreamBun/casp/blob/main/Plugfests/2024-03-NorthernVirginia/SweatEquity/IBM/oc2-hunt-1.hf) and returns the matching process.
```
{
  "action": "investigate",
  "target": {
      "th": {
      "hunt": "./hunts/jinja/oc2-hunt-1.jhf"
      }
  }
}
```
### Command 3
This command triggers a Kestrel hunt to [Discover Parent Processes](https://github.com/ScreamBun/casp/blob/main/Plugfests/2024-03-NorthernVirginia/SweatEquity/IBM/oc2-hunt-2.hf) of the process discovered in Command 2.
```
{
    "action": "investigate",
    "target": {
        "th": {
        "hunt": "./hunts/jinja/oc2-hunt-2.jhf"
        }
    },
    "args": {
        "th": {
        "huntargs": {
        "string_args": ["filename_1:disablefw.json", "filename_2:hosts.json"]
        }
        }
    }
}
```
### Command 4
This command triggers a Kestrel hunt to [Discover Sibling Processes](https://github.com/ScreamBun/casp/blob/main/Plugfests/2024-03-NorthernVirginia/SweatEquity/IBM/oc2-hunt-3.hf) of the process discovered in Command 2.
```
{
    "action": "investigate",
    "target": {
        "th": {
        "hunt": "./hunts/jinja/oc2-hunt-3.jhf"
        }
    },
    "args": {
        "th": {
        "huntargs": {
        "string_args": ["filename_1:disablefw.json", "filename_2:hosts.json"]
        }
        }
    }
}
```
### Command 5
This command triggers a Kestrel hunt to [Correlate Networking](https://github.com/ScreamBun/casp/blob/main/Plugfests/2024-03-NorthernVirginia/SweatEquity/IBM/oc2-hunt-4.hf) to find the impact of this process.
```
{
    "action": "investigate",
    "target": {
        "th": {
        "hunt": "./hunts/jinja/oc2-hunt-4.jhf"
        }
    },
    "args": {
        "th": {
        "huntargs": {
            "string_args": ["filename_1:siblings.json", "filename_2:hosts.json"]
            }
        }
    }
}
```

## SBOMs
SPDX SBOMs created through GitHub for OpenC2 Integration Framework (OIF) components.
* [OIF Orchestrator SBOM](https://github.com/ScreamBun/casp/blob/main/Plugfests/2024-03-NorthernVirginia/SweatEquity/HII/openc2-oif-orchestrator-2_ScreamBun_a39c6cdf0582bd59dd0e156d224e61b777c87718.json)
* [OIF Consumer Device SBOM](https://github.com/ScreamBun/casp/blob/main/Plugfests/2024-03-NorthernVirginia/SweatEquity/HII/openc2-oif-device_ScreamBun_d7b24a8056b5e4410af192e0f1811025375f7b5d.json)