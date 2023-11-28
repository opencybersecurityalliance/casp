# March 2024 CASP Plugfest Test Matrix

The CASP [Charter](../../CHARTER.md) includes:
> the intent of CASP is to be vendor and application agnostic,
enabling interoperability across a range of cyber security tools and applications.
The use of standardized interfaces and protocols enables interoperability of different tools,
regardless of the vendor that developed them, the language they are written in
or the function they are designed to fulfill.

Because each plugfest event tests interoperability using standardized interfaces and protocols,
this test matrix lists the organizations interested in promoting cross-vendor interoperability,
organized by data or protocol standard to facilitate test planning.

## Data Interoperability Tests

Each object defined by a data standard may be **Produced** or **Consumed** by an application.
The test matrix includes a Role column to indicate which data role(s) the participant intends
to test.

### [CACAO](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=cacao)

| Participant | Role | Notes |
|-------------|------|-------|
|             |      |       |
|             |      |       |

### [CSAF](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=csaf)

| Participant | Role | Notes |
|-------------|------|-------|
|             |      |       |
|             |      |       |

### [CycloneDX](https://cyclonedx.org/specification/overview/)

| Participant | Role | Notes |
|-------------|------|-------|
|             |      |       |
|             |      |       |

### [Indicators of Behavior - IOB](https://opencybersecurityalliance.org/iob/)

| Participant | Role | Notes |
|-------------|------|-------|
|             |      |       |
|             |      |       |

### [OCSF](https://github.com/ocsf/)

| Participant | Role | Notes |
|-------------|------|-------|
|             |      |       |
|             |      |       |

### [OpenC2 Content](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=openc2)
Actions supporting automated:
* Protection: Configuration Management, Anti-virus, SBOM, Security Assessment and Approval
* Sensing: SIEM, Threat Hunting
* Defense: SOAR, XDR

| Participant | Role | Notes |
|-------------|------|-------|
|             |      |       |
|             |      |       |

### [Open Security Controls Assessment Language - OSCAL](https://pages.nist.gov/OSCAL/)

| Participant | Role | Notes |
|-------------|------|-------|
|             |      |       |
|             |      |       |

### [Open XDR Architecture - OXA](https://github.com/opencybersecurityalliance/oxa)

| Participant | Role | Notes |
|-------------|------|-------|
|             |      |       |
|             |      |       |

### [SPDX](https://spdx.dev/)

| Participant | Role | Notes |
|-------------|------|-------|
|             |      |       |
|             |      |       |

### [STIX](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=cti)

| Participant | Role | Notes |
|-------------|------|-------|
|             |      |       |
|             |      |       |

### [Threat Actor Context - TAC](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=tac)

| Participant | Role | Notes |
|-------------|------|-------|
|             |      |       |
|             |      |       |

### [VEX](https://github.com/openvex/spec)

| Participant | Role | Notes |
|-------------|------|-------|
|             |      |       |
|             |      |       |

## Protocol/Interface Tests

Each protocol may support **Initiator** (Client/Producer), **Responder** (Server/Consumer)
or **Symmetric** interaction roles.  The test matrix includes a Role column to indicate
which interaction role(s) the participant intends to test.

### [TAXII](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=cti)

| Participant | Role | Notes |
|-------------|------|-------|
|             |      |       |
|             |      |       |

### [OpenC2 Message](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=openc2)

| Participant     | Role | Notes               |
|-----------------|------|---------------------|
| [sFractal](SweatEquity/sFractal/README.md) | I,R  | Blinky - HTTP, MQTT |
| [sFractal](SweatEquity/sFractal/README.md) | I,R  | SBOM - MQTT         |

OpenC2 has published specifications for message transfer over [MQTT
v5.0](https://docs.oasis-open.org/openc2/transf-mqtt/v1.0/transf-mqtt-v1.0.html) and
[HTTPS](https://docs.oasis-open.org/openc2/open-impl-https/v1.1/cs01/open-impl-https-v1.1-cs01.html).
MQTT is preferred to avoid the need to open inbound paths to a local enclave if
testing across the Internet.  The HTTPS Transfer Specification supports a
[Testing mode](https://docs.oasis-open.org/openc2/open-impl-https/v1.1/cs01/open-impl-https-v1.1-cs01.html#421-testing-target-conformance-requirements)
that drops the requirement for TLS authentication and its associated certificate
management challenges.

For assistance applying these OpenC2 specifications use the [CASP mail
list](mailto:oca-casp@lists.oasis-open-projects.org) or open an issue in the
associated GitHub repository
([MQTT](https://github.com/oasis-tcs/openc2-transf-mqtt/issues) /
[HTTPS](https://github.com/oasis-tcs/openc2-impl-https/issues)).


## Protocol Support

The following message brokers are being used for testing OpenC2-based interoperability:
* [**Mosquitto**](https://test.mosquitto.org/) - Eclipse foundation public test server at
`mqtt://test.mosquitto.org:xxxx` - see documentation for port options
* [**HiveMQ**](https://www.hivemq.com/) - MQTT v3.1 and v5 at
`mqtt+ssl://3271a3ddd2eb43caa7c4b195c7d6cabd.s2.eu.hivemq.cloud:8883`

The HiveMQ broker uses TLS session encryption and requires basic (username/password)
authentication. Participants should request authentication info (see [contributing](../../CONTRIBUTING.md)
and provide device IDs (any name you wish) to be included in the topic lists to allow other participants to
communicate with you.
