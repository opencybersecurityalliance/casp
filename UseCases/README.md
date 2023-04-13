# Use Cases and Scenarios
## 1. Introduction
This topic is organized considering multiple dimensions:
- risks
- the interfaces involved
- lifecycle/timing
- TTPs (tactics, techniques, and procedures)
- what is demonstratable

Any use case or scenario (synonyms for this document)
involves aspects from many/all dimensions.
This documet will attempt to show how the details fit
into the big picture, 
and how all the components work together.

### 1.1. Risks
Section 2 on Risks tries to take the broadest view
and look at the risks from the enterprise's viewpoint.
The enterprise/organization may be a 
commercial business,
a non-profit,
or a government agency.
The purpose of cybersecurity and cyber resilience
is to reduce the risk of harm due from a cyber incident.
This section looks from the harm viewpoint e.g.
- ransomware
- theft
   - supplier payments
   - suctomer payments
   - payroll
- denial of service
- dis-/mis information campaign
- data breach
    - credit cards
    - medical
    - intellectual property
    - smear (eg Sony, DNC, ..)

Section 2 contains the use cases organized by the harm 
with subsections based on other factors 
as described below.

### 1.2. Interfaces
One focus of CASP is to show how the various technologies
and interfaces work together in an automated scenario.
This section lists the interfaces involved and shows
the use cases from the viewpoint 
of a particular cybersecurity technology
(e.g. STIX). 
These use cases should fit into the larger risk use cases
which show how they word together.

The interfaces being looked at include:
- STIX/TAXII
- CACAO 
- OCA/PACE
- SBOM / VEX
- IoB
- TAC
- NIEM
- OCA/stixshifter
- OCA/kestrel
- OpenC2
- OCSF
- OXA

### 1.2.1 STIX/TAXII
blah blah to be filled in

For example, 
X.1215 is an ITU recommendation on STIX use cases
{add link to reference} and contains a ransomware use case.
That use case has it's own use case page 
{add link to page - create page} 
which is in the STIX section (3.) since it relates to STIX.
It is also in section on ransomware (2.1) which shows how
this detailed use case fits into the larger risk scenario
with use cases for other interfaces.

### 1.2.2 CACAO 
blah blah to be filled in

CACAO playbooks will be used to show the control flow of most,
if not all,
of the use cases.

For example (put one in)

### 1.2.3 OCA/PACE
blah blah to be filled in

### 1.2.4 SBOM / VEX
blah blah to be filled in

### 1.2.5 IoB
blah blah to be filled in

### 1.2.6 TAC
blah blah to be filled in

### 1.2.7 NIEM
blah blah to be filled in

### 1.2.8 OCA/stixshifter
blah blah to be filled in

### 1.2.9 OCA/kestrel
blah blah to be filled in

### 1.2.10 OpenC2
blah blah to be filled in

### 1.2.11 OCSF
blah blah to be filled in

### 1.2.12 OXA
blah blah to be filled in


### 1.3. Lifecycle/timing
Section 3 lists the use cases wrt to where they occur in the lifecycle of defense/attack.

Looking from a defender viewpoint,
one aspect of lifecycle is wrt the NIST Cybersecurity Framework
{add reference}
five functions:
- identify
- protect
- detect 
- respond
- recover

Another aspect of lifecycle is from the attack viewpoint, ie:
- Recon
- Resource Development
- Initial Access
- Execution
- Persistence
- Privlege Escalation
- Defense Evasion
- Credential Access
- Discovery
- Lateral Movement
- Collection
- Command and Control
- Exfiltration
- Impact

The third aspect of lifecycle is when it occurs wrt your peer group. Is this the first enterprise detecting they are in the middle of a zero-day or an enterprise applying the learnings from their peers to prevent future incursions.

Some use cases focus at particular point in the lifecycle and those are listed in section 3.

For example, the comply-to-connect use case is focused on
preventing attacks by knowing the security posture of new devices
being added.

Another example is threat hunting triggered by detection of
an intruder in the system.

### 1.4. TTPs (tactics, techniques, and procedures)
Most use cases won't focus on any particular TTP's, but any that do will be listed in section 4.

### 1.5. Demos
For a given workshop, this is where we will document
actual implementations showing particular interfaces
working in particular use cases.

For example sFractal providing a raspberry pi running BlinkMaHa
connecting to HII provideing a MQTT server connected to OpenC2 Integration Fabric (OIF) showing 
the 'get SBOM' (add link to OpenC2 use case) portion
of the comply-to-connect PACE use case (add link to PACE use case).

### 1.6. Examples 
Here are some examples to help understand this document.

X.1215 is an ITU recommendation on STIX use cases
{add link to reference} and contains a ransomware use case.
That use case has it's own use case page 
{add link to page - create page} which is the list
in Section 2 (risks), subsection 2.1 (ransomware).
It is also in the list in Secton 3 (interfaces), subsection 3.1 (SITX).

 ## 2. Risks
This section tries to take the broadest view
and look at the risks from the enterprise's viewpoint.
The enterprise/organization may be a 
commercial business,
a non-profit,
or a government agency.
The purpose of cybersecurity and cyber resilience
is to reduce the risk of harm due from a cyber incident.
This section looks from the harm viewpoint 
described in the following paragraphs.

### 2.1 Ransomware
Section 2 describes ransomware use cases

#### 2.1.1 Ransomware Detection and Response with CACAO, Kestrel & OpenC2

In this CASP use case, we will explore how Kestrel, OpenC2, and
CACAO can be used together to create an integrated and efficient
cybersecurity workflow for detecting, responding to, and
mitigating a cyber threat, such as a ransomware attack.

*Command Orchestration using CACAO Playbooks:* To streamline and
automate cybersecurity processes, the organization implements a
number of CACAO playbooks specifically designed for various
atomic functions. These playbooks interface with a suite of
automated actions and decision points and in our use case, will
invoke each other one after another, and use their respective
findings to inform cyber threat response functions. CACAO
orchestration in this example will make extensive use of OpenC2
commands for standardized, implementation- agnostic commands that
can perform critical Command and Control functions.

*Threat Detection using Kestrel:* The organization implements
tools for scanning and anomaly detection, including Kestrel-based
software and libraries of hunting books, specifically designed to
analyze the system anomaly behavior and detect and classify
anomalous behavior. Kestrel commands can enable the execution of
threat detection and hunting that can retrieve, join, and analyze
data as part of an orchestration flow. For our use case,
anomalous behavior may constitute elevated processor use or
suspicious network traffic. In the event of anomalous behavior,
the scanning tools will notify a security team and, at the same
time, invoke Kestrel. This will initiate Kestrel threat hunting
using OpenC2 commands to Kestrel’s STIX-shifter interface. Threat
hunting commands will use the Threat Hunting Actuator Profile (in
development) for OpenC2 to investigate threats with a threat
hunting book and analyze threat related data from various
sources, such as log files, network traffic data, and external
threat feeds. Kestrel's powerful pattern matching and correlation
capabilities enable the identification of indicators of
compromise (IoCs) associated with a known ransomware family, such
as specific file hashes, IP addresses, or domain names. 

Thus Kestrel will:
  1. Detect a threat that is impacting the system.
  2. Identify the threat as ransomware attack that has encrypted
     critical files on a server.
  3. Generate an alert and send it to the security team.

Due to the nature of the threat detected, the Detection playbook
may initiate a CACAO workflow to automatically respond to the
threat that has been detected if there is such a response
prepared. 

The response may include:

 - Blocking the IP addresses or domains associated with the
   ransomware's command and control servers.
 - Updating intrusion detection systems and endpoint protection
 platforms with the latest IoCs to detect and prevent further
 infections. -Initiating network segmentation to isolate affected
 systems and prevent the ransomware from spreading.

Due to the nature of the threat found, the Response playbook may also initiate further CACAO workflow steps to automatically remediate the affected system.

*Threat Mitigation using CACAO Playbook:* To further streamline
and automate the ransomware response process, the organization
implements a CACAO playbook specifically designed for ransomware
attacks. 

Actions and decision points outlined in this playbook may include:

  - Detecting ransomware infections based on specific IoCs or
    behavioral patterns.
  - Containing the infection by isolating affected systems and
    disabling network shares.
  - Gathering forensic evidence to be used by the security team
    for conducting root cause analysis to identify the infection
    vector and prevent future incidents.
  - Recovering encrypted data from secure backups and restoring
    affected systems to a known good state.
  - Sharing information about the ransomware attack, including
    IoCs and mitigation strategies, with industry partners or
    collaborative platforms like ISACs.

*Continuous Improvement:* After the ransomware incident has been
successfully resolved, the organization uses insights from the
Kestrel analysis, OpenC2 response actions, and CACAO playbook
execution to continuously improve its security posture. This may
include updating security policies, enhancing security awareness
training, or implementing additional security controls to prevent
future ransomware attacks.

In conclusion, the combined use of Kestrel, OpenC2, and CACAO
creates a powerful and integrated cybersecurity workflow that
enables organizations to quickly detect, respond to, and mitigate
cyber threats, such as ransomware attacks. By leveraging these
technologies, organizations can improve their overall security
posture and better defend against the evolving cyber threat
landscape.


### 2.2 Theft
Section 3 describes threat use cases

Although ransomware does cause a lot of loss, 
and does grab alot of headlines,
theft actually accounts for larger losses
{add reference}. 

#### 2.2.1 Supplier payments
If attackers gain access to the supplier payment systems, 
money intended for your suppliers instead is paid to the threat actors.

#### 2.2.2 Customer payments
If attackers gain access to your customer invoicing 
and/or accounts receivable systems,
the threat actors get your customers to pay the threat actor
instead of your enterprise. 

#### 2.2.3 Payroll
Gaining access to the payroll systems allows
threat actors
to reroute payments to the threat actors
instead of paying the employees.

### 2.3 denial of service
blah blah to be filled in

### 2.4 dis-/mis- information campaign
blah blah to be filled in
### 2.5 data breach
blah blah to be filled in

## 3. Interfaces
- TODO - go thru http://www.cybersecurityautomationworkshop.org/DemoUseCases/ and http://www.cybersecurityautomationworkshop.org/SweatEquity/ and make sure all previous use cases included

## 3.1 STIX/TAXII
X.1215 - ransomware
X.1215 - crypto attack

## 3.2 CACAO 
blah blah to be filled in

## 3.3 OCA/PACE
blah blah to be filled in

https://securityattributes.org/By_Example/
has 22 use cases from a PACE perspective.
Need to transform them to here.
One exampel would be  https://securityattributes.org/By_Example/Scenario_05.html whcih can be used to show how PACE relates with
SBOM, VEX, OpenC2, and CACAO. 
It doesn't get into "why" the use case is for "heightened threat",
but that could be fleshed out and maybe tied to 
STIX,  stixshifter, kestrel, etc.

- TODO - go thru https://github.com/opencybersecurityalliance/PACE/tree/main/docs/UseCases and pull any appropriate to go in CASP

## 3.4 SBOM / VEX
blah blah to be filled in

- TODO - go thru https://ntia.gov/sites/default/files/publications/ntia_sbom_use_cases_roles_benefits-nov2019_0.pdf and pull any appropriate to go in CASP
- TODO - go thru https://www.cisa.gov/resources-tools/resources/vulnerability-exploitability-exchange-vex-use-case-document-april-2022 and pull any appropriate to go in CASP

## 3.5 IoB
blah blah to be filled in

## 3.6 TAC
blah blah to be filled in

## 3.7 NIEM
blah blah to be filled in

## 3.8 OCA/stixshifter
blah blah to be filled in

## 3.9 OCA/kestrel
blah blah to be filled in

## 3.10 OpenC2
blah blah to be filled in

- TODO - go thru https://github.com/oasis-tcs/openc2-usecases and pull any appropriate to go in CASP

## 3.11 OCSF
blah blah to be filled in

## 3.12 OXA
blah blah to be filled in

## 4. Lifecycle/timing
blah blah to be filled in

## 5. TTPs (tactics, techniques, and procedures)


## 6. Demos
