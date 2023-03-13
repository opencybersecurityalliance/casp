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
blah blah to be filled in

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
