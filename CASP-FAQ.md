# Frequently Asked Questions about the Cybersecurity Automation

## How does the Cybersecurity Automation relate to the OCA?
Cybersecurity Automation is an OCA subproject
similar to stixshifter, Kestrel, PACE, and IoB.
See https://opencybersecurityalliance.org/casp/.

## What will be the work products of Cybersecurity Automation SubProject?
The initial focus of the Cybersecurity Automation SubProject (CASP)
will be the Cybersecurity Automation Village.
Cybersecurity Automation Village evolved from
the Cybersecurity Automation Workshops and are
a series of events to prototype and test
interoperability among cybersecurity automation technologies.
CASP will maintain this website as well as may produce documentation
aiding awareness/adoption and/or interoperability
of cybersecurity automation interfaces.
CASP will attempt to use existing specifications/standards
wherever possible,
but may create specifications/standards if necessary.

## When will be the next Cybersecurity Automation Village?
The next Cybersecurity Automation Village will be
a two-day plugfest/workshop/hackathon/contest on March 14-15, 2024.
It will be hosted by Peraton at their office at:
* 1875 Explorer St, Reston, VA 20190

## When were previous Cybersecurity Automation Workshops?
The most recent  Cybersecurity Automation Village was
13-June-2023 hybrid at USC.
See 
[USC Village](./Plugfests/2023-06-13-USC/)
for more details.

Prior to that, the most recent event was 2-June-2022 at
the AT&T Forum in Washington, DC. See 
[ATT-DC](./Plugfests/2022-05-16-DC/) 
for more details.

For even more events, see [plugests](./Plugfests/).

## How does PACE relate to the Cybersecurity Automation SubProject?
[Posture Attribute Collection & Evaluation (PACE)](https://opencybersecurityalliance.org/pace/)
is a comprehensive automated strategy
for understanding security posture and what to do about it.
At the last Cybersecurity Automation Workshop,
use cases for cybersecurity automation where demonstrated where
automation was used for PACE collecting SBOMs as security attributes.
Use cases were also conceptualized for using
PACE evaluation (ie security posture) for decision making within
CACAO playbooks to initiate OpenC2 actions.

## How does Kestrel relate to the Cybersecurity Automation SubProject?
[Kestrel](https://github.com/opencybersecurityalliance/kestrel-lang)
is a threat hunting language,
providing an abstraction for threat hunters
to focus on what to hunt instead of how to hunt.
At the last Cybersecurity Automation Workshop,
Kestrel use cases showed automated threat hunting.
Use cases were also conceptualized for
PACE security posture being used in
CACAO playbooks initiating Kestrel threat hunting using OpenC2 actions.

## How does IoB relate to the Cybersecurity Automation SubProject?
The [Indicators of Behavior (IoB)](https://github.com/opencybersecurityalliance/oca-iob) Subproject
is creating a structured representation of reusable adversary behaviors,
detections of those behaviors,
and correlation workflows to aid network defenders.
IoB is data that can control workflows in CACAO playbooks
in automation scenarios.

## How does stixshifter relate to the Cybersecurity Automation SubProject?
[Stixshifter](https://github.com/opencybersecurityalliance/stix-shifter)
is a patterning library which allows
data to be normalized across domains
for comprehensive security analysis.

## How does CACAO relate to the Cybersecurity Automation SubProject?
[Collaborative automated course of action operations (CACAO)](https://www.oasis-open.org/standard/cacao-security-playbooks-version-1-0/)
defines the schema and taxonomy for
security playbooks
and how these playbooks can be created, documented, and shared
in a structured and standardized way across organizational boundaries
and technological solutions.
Much of the automation demonstrated at Cybersecurity Automation Workshops
can be shared using CACAO playbooks.

## How does TAC relate to the Cybersecurity Automation SubProject?
[Threat Actor Context](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=tac)
seeks to resolve ambiguity across different sources and solutions
to support organizing what is known and sharing information
about threat actors.
It establishes a common knowledge framework
that enables semantic interoperability
of threat actor contextual information
and develop standardized vocabularies
for threat actor characterization.
Similar to IoB, PACE, STIX, and stixshifer,
TAC is data that can control workflows in CACAO playbooks
in automation scenarios.

## How does OpenC2 relate to the Cybersecurity Automation SubProject?
[Open Command & Control (OpenC2)](https://openc2.org/)
is a standardized language for the command and control
of technologies that provide or support cyber defenses.
By providing a common language for machine-to-machine communication,
OpenC2 is vendor and application agnostic,
enabling interoperability across a range of cyber security tools
and applications.
The use of standardized interfaces and protocols
enables interoperability of different tools,
regardless of the vendor that developed them,
the language they are written in
or the function they are designed to fulfill.

## How does SBOM relate to the Cybersecurity Automation SubProject?
[Software Bill of Materials (SBOM)](https://www.cisa.gov/sbom)
has emerged as a key building block in
software security and software supply chain risk management.
An SBOM is a nested inventory, a list of ingredients
that make up software components.
SBOM is a valuable security posture driving PACE automation.

## How does VEX relate to the Cybersecurity Automation SubProject?
[Vulnerability Exploitability eXchange (VEX)](https://www.cisa.gov/sites/default/files/publications/VEX_Use_Cases_Aprill2022.pdf)
allows a software supplier or other parties
to assert the status of specific vulnerabilities in a particular product.
Examples include:
- this product does **not** contain Log4j, the vulnerable software in CVE-2021-44228
- this product does contain Log4j, the vulnerable software in CVE-2021-44228, but the product is **not** vulnerable because ...
- this product does contain Log4j, the vulnerable software in CVE-2021-44228, and is **vulnerable** so users should invoke compensating controls ...

VEX information enhances SBOM information in PACE usecases and both
are valuable security posture driving PACE automation.

## How does CSAF relate to the Cybersecurity Automation SubProject?
The [Common Security Advisory Framework (CSAF)](https://docs.oasis-open.org/csaf/csaf/v2.0/csaf-v2.0.html)
has a VEX profile for automated creation/consumption of VEX information. See previous question.

## How does STIX relate to the Cybersecurity Automation SubProject?
add STIX/CASP text here

## How does JADN relate to the Cybersecurity Automation SubProject?
add JADN/CASP text here

## How does VSMI relate to the Cybersecurity Automation SubProject?
add VSMI/CASP text here

## How does CSAF relate to the Cybersecurity Automation SubProject?
add CSAF/CASP text here

## How does NIEM relate to the Cybersecurity Automation SubProject?
add NIEM/CASP text here

## How does OCSF relate to the Cybersecurity Automation SubProject?
add OCSF/CASP text here

## How does CASP relate to US National Cybersecurity Strategy?
The US National Cybersecurity Strategy can be found in 
https://www.whitehouse.gov/briefing-room/statements-releases/2023/03/02/fact-sheet-biden-harris-administration-announces-national-cybersecurity-strategy/ .
CASP ....

## How does CASP relate to US National Standards Strategy for Critical and Emerging Technology?
The US National Standards Strategy for Critical and Emerging Technology
can be found in
https://www.whitehouse.gov/briefing-room/statements-releases/2023/05/04/fact-sheet-biden-harris-administration-announces-national-standards-strategy-for-critical-and-emerging-technology/ .
CASP ...

## When will the next CASP event be?
See [Next Plugfest](./Plugfests/NextPlugfest/README.md).

## What is the "handwaving lycan"?
Interworking involves interfaces from one system interworking with 
interfaces from another system 
using one of the standard interfaces of the workshop.
Ideally the systems implement the standard interfaces
If not, an open source “lycan” or “shifter” (see footnote below) 
may be used to convert back and forth 
between the vendor interface and the standard interface.
For the purpose of demonstrating use cases, 
the “hand waving lycan” can be used when actual lycan has not yet been coded.
Hackathon activities may focus on creating a real lycan from a hand waving lycan.
Example hand waving lycans can be 
seen {Link here to blinky pace sfractal use cases designed to explain this}

Footnote - Both OpenC2 and Stixshifter use
werewolf/lycanthrope/shapeshifter terminology.
Instead of transforming between wolf and human,
these shims transform between vendor and standard interfaces.
Stix uses “shifter” and OpenC2 uses “lycan”.