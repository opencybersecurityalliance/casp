# Results by Project

![projects](../Images/CASP_projects.png)

The following sections look at the results from the view of the project.
They are listed alphabetically. 

## 1. CACAO
### What is CACAO
### How did CACAO fit in the use case
### Which Orgs demonstrated CACAO
### How did CACAO relate to other projects
### What next for CACAO for the next Village


## 2. CSAF
### What is CSAF
### How did CSAF fit in the use case
### Which Orgs demonstrated CSAF
### How did CSAF relate to other projects
### What next for CSAF for the next Village

## 3. IoB
### What is IoB
### How did IoB fit in the use case
### Which Orgs demonstrated IoB
### How did IoB relate to other projects
### What next for IoB for the next Village

## 4. Kestrel
### 4.1 What is Kestrel
Kestrel is an
[Open Cybersecurity Alliance](https://opencybersecurityalliance.org/) subproject
developing a [threat hunting language](https://github.com/opencybersecurityalliance/kestrel-lang)
which provides an abstraction for threat hunters to focus on what to hunt instead of how to hunt

### How did Kestrel fit in the use case
### Which Orgs demonstrated Kestrel
### How did Kestrel relate to other projects
### What next for Kestrel for the next Village

## 5. NIEMOpen
### What is NIEMOpen
### How did NIEMOpen fit in the use case
### Which Orgs demonstrated NIEMOpen
### How did NIEMOpen relate to other projects
### What next for NIEMOpen for the next Village

## 6. OHDF
OHDF was not represented at this instance of the village.
[CASP](https://lists.oasis-open-projects.org/g/oca-casp) 
would welcome more OHDF participation
in planning, and participating in, the next Cybersecurity Automation Village.
Or even filling in sections similar to the other projects on this page, 
even if it is after the fact.

## 7. OpenC2
### What is OpenC2?
OpenC2 is a standardized language for the command and control of technologies 
that provide or support cyber defenses. 
By providing a common language for machine-to-machine communication, 
OpenC2 is vendor and application agnostic, 
enabling interoperability across a range of cyber security tools and applications.
The use of standardized interfaces and protocols 
enables interoperability of different tools, 
regardless of the vendor that developed them, 
the language they are written in or the function they are designed to fulfill.

For more info, see [https://openc2.org/](https://openc2.org/)

### How did OpenC2 fit in the use case?
Our team developed a use case centered around a ransomware scenario listed [here](https://github.com/ScreamBun/casp/blob/main/UseCases/CASP_Ransomeware_Use_Case.png). This scenario involves CACAO playbook orchestration of OpenC2 commands to the Threat Hunting AP to initiate a Kestrel Hunt on provided STIX data.
### Which Orgs demonstrated OpenC2?
The ScreamingBunny OC2 team, with members from Praxis Engineering, HII, and Bestgate Engineering provided the OC2 use case as well as an interoperable demonstration. We used the MQTT message broker provided by Dave Kemp, and were able to send commands with OC2 action-target syntax to sFractal devices. 
### How did OpenC2 relate to other projects?
OpenC2 commands passed STIX data to a Kestrel runtime, performed threat hunting operations on that data, and demonstrated that these commands can be initiated by an outside orchestration, such as CACAO.
### What's next for OpenC2 for the next Village?
We are hopeful that in the lead up to the next interworking opportunity we may have the opportunity to improve the demonstration of the existing use case, using actual CACAO instead of pseudo-CACAO logic, as well as commands in an official release of the Endpoint Response AP. With time between now and the nxt plugfest, we would like to spend time discussing how Kestrel, CACAO, or other implementations in related areas may interface with OIF and the commands it sends, implementing an OC2 Profile function, such as Threat Hunting.

## 8. OXA
### What is OXA
### How did OXA fit in the use case
### Which Orgs demonstrated OXA
### How did OXA relate to other projects
### What next for OXA for the next Village

## 9. PACE
### What is PACE
### How did PACE fit in the use case
### Which Orgs demonstrated PACE
### How did PACE relate to other projects
### What next for PACE for the next Village

## 10. SARIF
SARIF was not represented at this instance of the village.
[CASP](https://lists.oasis-open-projects.org/g/oca-casp) 
would welcome more SARIF participation
in planning, and participating in, the next Cybersecurity Automation Village.
Or even filling in sections similar to the other projects on this page, 
even if it is after the fact.

## 11. SBOM
### What is SBOM
### How did SBOM fit in the use case
### Which Orgs demonstrated SBOM
### How did SBOM relate to other projects
### What next for SBOM for the next Village

## 12. SpydeRisk
SARIF was not represented at this instance of the village.
[CASP](https://lists.oasis-open-projects.org/g/oca-casp) 
would welcome more SARIF participation
in planning, and participating in, the next Cybersecurity Automation Village.
Or even filling in sections similar to the other projects on this page, 
even if it is after the fact.

## 13. STIX/TAXII
### What are STIX and TAXII
### How did STIX/TAXII fit in the use case
### Which Orgs demonstrated STIX/TAXII
### How did STIX/TAXII relate to other projects
### What next for STIX/TAXII for the next Village

## 14. STIX Shifter
### What is STIX Shifter
### How did STIX Shifter fit in the use case
### Which Orgs demonstrated STIX Shifter
### How did STIX Shifter relate to other projects
### What next for STIX Shifter for the next Village

## 15. TAC
### What is TAC
### How did TAC fit in the use case
### Which Orgs demonstrated TAC
### How did TAC relate to other projects
### What next for TAC for the next Village

## 16. VEX
### What is VEX
### How did VEX fit in the use case
### Which Orgs demonstrated VEX
### How did VEX relate to other projects
### What next for VEX for the next Village

## 17. VSMI
### 17.1 What is VSMI
The purpose of the Value Stream Management Interoperability (VSMI) is
improving existing information representations for codifying, analyzing, and sharing of value stream data in the software supply chain and systems ecosystem. 
### 17.2 How did VSMI fit in the use case
No one really represented VSMI at the USC Village.
sFractal did some cursory handwaving on how VSMI
would gather data from almost all the projects,
and provide value data back for decision making.
### 17.3 Which Orgs demonstrated VSMI
Nothing demostrated other than cursory handwaving by sFractal
### 17.4 How did VSMI relate to other projects
sFractal did some cursory handwaving on how VSMI
would gather data from almost all the projects,
and provide value data back for decision making.
One example might be prioritization of 40 devices
being patched on day 3. 
Another example might be provieing risk analysis data
on the comply-to-connect part of day 4;
i.e. maybe some devices would be allowed to connect 
if the business value was high/urgent enough.
It might also be valuable in a future day 7
analyzing the software developement practices
of the vendors of the affected products in Days 1-3.
### 17.5 What next for VSMI for the next Village
[CASP](https://lists.oasis-open-projects.org/g/oca-casp) 
would welcome more VSMI participation
in planning, and participating in, the next Cybersecurity Automation Village.
Or even fleshig out these sections, 
even if it is after the fact.

