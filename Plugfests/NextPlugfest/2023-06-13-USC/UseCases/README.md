# Use Cases for the Plugfest
See [overall CASP Usecases](../../../../UseCases/README.md) 
and interface-specific usecases
(fill in with links to PACE, STIX, CACAO, OpenC3...) 
for the general use cases.

This page is to tease out what 
actually will be demo'd and 
how that fits into general use cases.
For the demo's, attempts will be made to tie into
the following fictious set of use cases.

## The WhitchyWashy Zero Day
### Day 1 - Murphy’s Law LLP
During the vows at a daughter’s wedding, 
midway through an emergency root canal, 
at 8 a.m. on Christmas morning 
the CEO of Murphy’s Law LLP receives 
a most unwelcome message—a brand new exploit 
has made its world-wide zero-day debut in the company’s system. 
Fortunately, Murphy’s Law LLP had the foresight to 
adopt cybersecurity automation protocols. 
An immediate kestrel threat hunt finds the exploited systems, 
kicks the attackers out of the system using CACAO playbooks with OpenC2 commands, 
alerts law enforcement, and analyzes the tactics and exploited vulnerabilities. 
Recognizing this as a zero-day, 
STIX bundles are prepared containing the threat information (IoCs, IoBs, TAC) 
and playbooks for prevention/detection/response (CACAO, OpenC2). 
The STIX information is shared with their ISAC for distribution to others in their industry.
Because the attacks exploited previously unknown vulnernabilities 
in both commerical and open source software,
Murphy's Law LLP submits new VEX's to the new NVD API for the purpose of creating 
new CVE's.
### Day 2 - On Deck Holdings
Panic begins anew at On Deck Holdings as a stark uptick 
in server activity signals 
that yesterday’s exploits at Murphy’s Law LLP has spread to new haunts. 
Fortunately, On Deck Holdings previously received STIX information from their ISAC. 
Being similarly automated, On Deck Holdings’ cybersecurity system. 
They soon match their problem with the STIX object generated the day before, 
initiate the CACAO playbook, execute OpenC2 commands, 
and freeze out the black hat hackers that gained entry into their system.
### Day 4 - Triumvirate CleanUp Inc
As the unknown exploit becomes a known entity, the zero-day becomes an N-day.  
Triumvirate CleanUp Inc, also a subscriber to their ISAC, 
analyzes the STIX bundle and decides to use their PACE system 
to analyze their environment 
and see if they are vulnerable to the same attack that targeted Murphy’s Law and On Deck. Using their PACE system, 
they analyze their SBOMs and discover they do have 
70 devices with components that have the CVE’s reported in the STIX bundle. 
Further analysis with PACE shows that 30 of those 
potentially affected devices have VEX’s from their suppliers 
that indicate they are not susceptible to those CVE’s. 
Triumvirate CleanUp then initiates automated patching 
to harden the remaining 40 devices and avoids getting hacked.
### Day 5 - NSAANSA
The Never Say Anything and No Such Agency (NSAANSA)
in the US Dept of Useless Factiods 
has automated cybersecurity adhering to federal guidelines
including the "comply to connect" edict which requires any
new devices connecting to a network to have an acceptable security posture.
NSAANSA's ISAC feed receives the STIX bundle and their systems automagically
convert that informaton into new rules 
for calculating security posture in their PACE system.
When a new device attempts to connect to the NSAANSA environment,
their security posture assessment includes the PACE system examining 
device SBOMs and VEXs including looking for impact of the WhitchyWashy CVE's.

Although NSAANSA is not the lead agency for sharing comply-to-connect policies with
the State/Local/Tribal-Terriorities (SLTT), 
NSAANSA creates a NIEM IEP informaton packet
for SLTT consumption and implementation
and transmits that to the lead agency, CISA,for transmission to the SLTT.

## Interface/Technology -Centric views of these use cases
### STIX
STIX bundles were used ....
### CACAO
CACAO playbooks were used ...
### Kestrel
Kestrel ....
### OpenC2
OpenC2 commands ...
### IoB
Indicators of Behavior (IoB) where included in the STIX bundle ...
### TAC
Threat Actor Contex (TAC) was included in the STIX bundle ...
### STIX Shifter
Stix Shifter ....
### SBOM
SBOMs were used in securty posture assessment by PACE systems in 
Triumvirate CleanUp Inc and NSAANSA.
### VEX
VEXs were created by Murphy’s Law LLP to submit to NVD for new CVEs.
VEXs were used in securty posture assessment by PACE systems in 
Triumvirate CleanUp Inc and NSAANSA.

## Demo-Centric views of these use cases

## Participant-Centric views of the Demos
### sFractal
See {link to sFractal Sweat equity} provided end devices 
that could receive OpenC2 commands to
- retrieve SBOMs as part of Triumvirate CleanUp Inc and NSAANSA PACE posture assessment
- execute security functions (eg deny ip=1.2.3.4) as part of Murphy’s Law LLP and Triumvirate CleanUp Inc mitigation actions in CACAO playbooks
### NSA/HII
See {link to ... Sweat equity} provided ...
### IBM
See {link to ... Sweat equity} provided ... kestrel, stixshifter
### Cydarm
See {link to ... Sweat equity} provided ... CACAO
