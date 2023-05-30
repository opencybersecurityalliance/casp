
## Publish-Subscribe Message Broker
An MQTT Message Broker based on [Apache ActiveMQ](https://activemq.apache.org/)
and hosted on [Amazon Web Services](https://aws.amazon.com/amazon-mq/)
is available for use by [CASP](https://github.com/opencybersecurityalliance/casp)
participants for interoperability testing prior to and during the June 13, 2023
[Cybersecurity Automation Village](https://github.com/opencybersecurityalliance/casp/tree/main/Plugfests/NextPlugfest).

## Python Client Examples
A cloud-hosted publish/subscribe ([Pub/Sub](https://ably.com/topic/pub-sub)) message service allows devices
located within separate local network environments to communicate, facilitating virtual plugfest participation.
This directory includes three examples:
* Producer - a "manager" or "controller" client that publishes a single command to a topic that may be
observed by one or more clients
* Consumer - a "managed device" client that establishes a connection with the broker and subscribes to
a topic, then waits for commands. When a command is received, the consumer processes the command
returns a response to the producer, then waits for the next command.
* Monitor - a client that receives and displays all messages from all clients, for debugging.
## OpenC2 Use Case
Pub/sub supports symmetric relationships between devices where each can publish and/or subscribe.
OpenC2 (Open Command and Control) establishes an asymmetric client/server relationship where the
producer (client) originates actions and the consumer (server) reacts to them by performing
the requested actions and returning responses to the producer. A single device may act in both
producer and consumer roles, but in each role it is either the initiator or the responder.

The OpenC2 Message payload contains a request ID and "to" and "from" device IDs,
unlike bare pub/sub where the source of a message is unknown to the receiver.  This allows the
consumer to send a response back to the producer, and for the producer to correlate multiple
responses to the same request.