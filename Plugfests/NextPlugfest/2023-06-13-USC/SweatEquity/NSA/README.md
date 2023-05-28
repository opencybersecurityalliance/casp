# NSA Sweat Equity

NSA to provide data on JADN, OpenC2 work, STIX work, 
interactions with HII, ...
and info on use cases

NSA keynoting?

## 1. Attendance
1 in person, 1 virtual
Participating country: USA

## 2. Contributions
### 2.1. MQTT Broker
OpenC2 producers and consumers can communicate through a message broker using the
[MQTT](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html) publish-subscribe protocol,
following the [OpenC2 MQTT](https://docs.oasis-open.org/openc2/transf-mqtt/v1.0/transf-mqtt-v1.0.html)
transfer specification. Using an Internet-accessible broker allows developers to
test interoperability of their producers and consumers, both prior to a plugfest
event and remotely during the event.

Python example producer and consumer code is available in the [MQTT_Broker](MQTT_Broker)
directory, and a broker is online now to facilitate testing. Access details are available
to plugfest participants on request.
