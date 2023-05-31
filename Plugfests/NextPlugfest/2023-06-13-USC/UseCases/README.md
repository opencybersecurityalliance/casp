# Use Cases for the Plugfest
See [overall CASP Usecases](../../../../UseCases/README.md) 
and interface-specific usecases
(fill in with links to PACE, STIX, CACAO, OpenC2...) 
for the general use cases.

This page is to tease out what 
actually will be demo'd and 
how that fits into general use cases.
For the demo's, attempts will be made to tie into
the following fictious set of use cases.

## The WhitchyWashy Zero Day
### Day 1 - Murphy’s Law LLP
During the vows at a daughter’s wedding, midway through an
emergency root canal, at 8 a.m. on Christmas morning the CEO of
Murphy’s Law LLP receives a most unwelcome message—a brand new
exploit has made its world-wide zero-day debut in the company’s
system. Fortunately, Murphy’s Law LLP had the foresight to adopt
cybersecurity automation protocols. An immediate kestrel threat
hunt finds the exploited systems, kicks the attackers out of the
system using CACAO playbooks with OpenC2 commands, alerts law
enforcement, and analyzes the tactics and exploited
vulnerabilities. Recognizing this as a zero-day, STIX bundles are
prepared containing the threat information (IoCs, IoBs, TAC) and
playbooks for prevention/detection/response (CACAO, OpenC2). The
STIX information is shared with their ISAC for distribution to
others in their industry. Because the attacks exploited
previously unknown vulnernabilities in both commerical and open
source software, Murphy's Law LLP submits new VEX's to the new
NVD API for the purpose of creating new CVE's.

### Day 2 - On Deck Holdings
Panic begins anew at On Deck Holdings as a stark uptick in server
activity signals that yesterday’s exploits at Murphy’s Law LLP
has spread to new haunts. Fortunately, On Deck Holdings
previously received STIX information from their ISAC. Being
similarly automated, On Deck Holdings’ cybersecurity system. They
soon match their problem with the STIX object generated the day
before, initiate the CACAO playbook, execute OpenC2 commands, and
freeze out the black hat hackers that gained entry into their
system.

### Day 3 - Triumvirate CleanUp Inc
As the unknown exploit becomes a known entity, the zero-day
becomes an N-day.  
Triumvirate CleanUp Inc, also a subscriber to their ISAC,
analyzes the STIX bundle and decides to use their PACE system to
analyze their environment and see if they are vulnerable to the
same attack that targeted Murphy’s Law and On Deck. Using their
PACE system, they analyze their SBOMs and discover they do have
70 devices with components that have the CVE’s reported in the
STIX bundle. Further analysis with PACE shows that 30 of those
potentially affected devices have VEX’s from their suppliers that
indicate they are not susceptible to those CVE’s. Triumvirate
CleanUp then initiates automated patching to harden the remaining
40 devices and avoids getting hacked.

### Day 4 - NSAANSA
The Never Say Anything and No Such Agency (NSAANSA) in the US
Dept of Useless Factiods has automated cybersecurity adhering to
federal guidelines including the "comply to connect" edict which
requires any new devices connecting to a network to have an
acceptable security posture. NSAANSA's ISAC feed receives the
STIX bundle and their systems automagically convert that
informaton into new rules for calculating security posture in
their PACE system. When a new device attempts to connect to the
NSAANSA environment, their security posture assessment includes
the PACE system examining device SBOMs and VEXs including looking
for impact of the WhitchyWashy CVE's.

Although NSAANSA is not the lead agency for sharing
comply-to-connect policies with the
State/Local/Tribal-Terriorities (SLTT), NSAANSA creates a NIEM
IEP informaton packet for SLTT consumption and implementation and
transmits that to the lead agency, CISA,for transmission to the
SLTT.

### Day 5 - Law Enforcement
Law enforcement was involved thorughout and 
prepared multiple NIEM Message Exchange Packages (MEP)
for entry in the Law Enforcement National Data Exchange (N-DEx),
and for exchanges with the Royal Canadian Mounted Police (RCMP),
Europol, and Interpol.
A criminal takedown across 6 countries occurred and 23 miscreants
were put behind bars using evidence and e-filings using NIEM MEPs.
  

### Day 6 - MilOps
It can neither be confirmed nor denied whether
rouge nation states were involved in this use case;
just as it can neither be confirmed nor denied whether
NIEM MilOps extensions were distributed among NATO allies
and hunt forward operations bricked adersary servers behind the attack.
Day 6 is out-of-scope for the Cybersecurity Automation Village. 

## Interface/Technology -Centric views of these use cases
### STIX
STIX bundles were used:
* Day 1 by Murphy’s Law LLP and by the ISAC
* Day 2 by On Deck Holdings
* Day 3 by Triumvirate CleanUp 
* Day 4 by NSAANSA
* STIX was not used per se on Days 5&6 but many of the NIEM Cyber Domain objects were from the Cyber Domain STIX adapter. 

For sweat equity / village interworking demo's of STIX for these use cases, see:
- tbd (eg link to IBM sweat equity)

For example STIX bundles used above, see:
- tbd

### CACAO
CACAO playbooks were used:
* Day 1 by Murphy’s Law LLP 
* Day 2 by On Deck Holdings
* Day 3 by Triumvirate CleanUp
* Day 4 by NSAANSA

For sweat equity / village interworking demo's of CACAO for these use cases, see:
- tbd (eg link to Cydsarn sweat equity)

For example CACAO playbooks used above, see:
- tbd

### Kestrel
Kestrel huntbooks were used:
* Day 1 by Murphy’s Law LLP
* Day 2 by On Deck Holdings

For sweat equity / village interworking demo's of Kestrel huntbooks for these use cases, see:
- tbd (eg link to IBM sweat equity)

For example Kestrel huntbooks used above, see:
- tbd

### OpenC2
OpenC2 commands were used:
* Day 1 by Murphy’s Law LLP 
* Day 2 by On Deck Holdings
* Day 3 by Triumvirate CleanUp
* Day 4 by NSAANSA

For sweat equity / village interworking demo's of OpenC2 for these use cases, see:
- tbd (eg link to sFratal, HII sweat equity)

For example OpenC2 commands used above, see:
- tbd

### IoB
Indicators of Behavior (IoB) where included in the STIX bundle ...

For sweat equity / village interworking demo's used for these use cases, see:
- tbd 

For example IoB used above, see:
- tbd

### TAC
Threat Actor Contex (TAC) was included in the STIX bundle ...

For examples of TAC in the bundles used, see:
- add links
-  

### STIX Shifter
Stix Shifter ....

For examples of what was used, see:
- add links

### PACE
PACE systems were used:
* Day 3 by Triumvirate CleanUp
* Day 4 by NSAANSA

### SBOM
SBOMs were used:
* Day 3 by Triumvirate CleanUp
* Day 4 by NSAANSA

For sweat equity / village interworking demo's used for these use cases, see:
- tbd 

For example SBOMs used above, see:
- tbd

### VEX
VEXs were used:
* Day 1 by Murphy’s Law LLP 
* Day 3 by Triumvirate CleanUp
* Day 4 by NSAANSA

For sweat equity / village interworking demo's used for these use cases, see:
- tbd 

For example Vexs used above, see:
- tbd

### NIEM
NIEM Message Exchange Packages (MEPs) were used:
* Day 1 by Murphy’s Law LLP and law enforcement
* Day 2 by On Deck Holdings and law enforcement
* Day 5 by law enforcement and the courts
* Day 6 by the military

For sweat equity / village interworking demo's used for these use cases, see:
- tbd 

For example NIEM MEPs used above, see:
- tbd


## Demo-Centric views of these use cases

add some pics of which systems talk to which systems (machine to machine, human, or handwaving) 
and which steps in use cases they relate to

## Participant-Centric views of the Demos
### sFractal
[sFractal Sweat equity(../SweatEquity/sFractal) provided end devices 
that could receive OpenC2 commands to
- retrieve SBOMs from devices as part of Triumvirate CleanUp Inc and NSAANSA PACE posture assessment
- execute security functions (eg deny ip=1.2.3.4) as part of Murphy’s Law LLP and Triumvirate CleanUp Inc mitigation actions in CACAO playbooks
- retreive VEXs from PACE systems as part of Triumvirate CleanUp Inc and NSAANSA PACE posture assessment
- blink lights so participants would actually see something happening :-). No actual value to use cases.

### NSA/HII
See {link to ... Sweat equity} provided ...

### IBM
See {link to ... Sweat equity} provided ... kestrel, stixshifter

### Cydarm
See {link to ... Sweat equity} provided ... CACAO
