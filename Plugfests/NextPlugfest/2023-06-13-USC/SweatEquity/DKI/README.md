# DKI Sweat Equity
David Kemp, individual contributor.

## 1. Attendance
David Kemp, virtual 
Participating from: Maryland, USA

## 2. Contributions
### 2.1. MQTT Brokers
OpenC2 producers and consumers can communicate through a message broker using the
[MQTT](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html) publish-subscribe protocol,
following the [OpenC2 MQTT](https://docs.oasis-open.org/openc2/transf-mqtt/v1.0/transf-mqtt-v1.0.html)
transfer specification. Using an Internet-accessible broker allows developers to
test interoperability of their producers and consumers, both prior to a plugfest
event and remotely during the event.

[Participants](../openc2-mqtt-topics.md) lists the available MQTT brokers and the publish and subscribe
topics used by plugfest participants.

### 2.2 Python Example MQTT Clients
Python example producer and consumer code is available in the [MQTT_Broker](MQTT_Broker)
directory, and a broker is online now to facilitate testing. Access details are available
to plugfest participants on request.

### 2.3 OpenC2 Actuator Profile Testing
The OpenC2 Technical Committee maintains an
[Actuator Profile Test Repository](https://github.com/oasis-open/openc2-jadn-software)
that supports members in creating TC work products.
The repo contains schemas, example messages to be validated against the schemas, and property tables
generated from the schemas to be used in OpenC2 actuator profile documents.

Anyone may view existing schemas and test messages or submit new ones; OASIS membership is not required.
Developers may submit custom actuator profiles reflecting their C2 use cases,
and schemas for their OpenC2 producer or consumer devices using existing or new profiles.
The repo includes a
[Python script](https://github.com/oasis-open/openc2-jadn-software/blob/master/test-poc.py)
to run device tests, with data either stored locally or fetched directly from the GitHub repo.
