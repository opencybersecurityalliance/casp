# Cybersecurity Automation SubProject (CASP) Charter

## 1. Project Name

Cybersecurity Automation SubProject (CASP)

## 2. Abstract
The OCA Cybersecurity Automation SubProject (CASP)
is comprised of global like-minded cybersecurity vendors, end users,
thought leaders and individuals
who are interested in cybersecurity automation.

It is a forum where products
from all vendors, researchers, and software publishers
can freely exchange information, insights, and reference implementations
via commonly developed code and tooling,
using mutually agreed upon technologies, specifications, and procedures.

For Frequently Asked Questions about CASP,
see [FAQ](./CASP-FAQ.md).


## 3. Purpose and Scope
The reality of the current cyber threat landscape is daunting.
Attacks are becoming more frequent, more impactful, and more sophisticated.
Attackers make use of sophisticated tools operating at machine speed.

Today, cyber defense technologies, systems and applications
often use proprietary software and commands to
control system configurations.
Most environments within a company or enterprise
are comprised of hundreds of different types of cyber-defense devices.

When security incidents are detected or configuration changes are required,
manual commands and real time system updates are required,
increasing incident response time and potentially introducing human error.

The intent of CASP is to be vendor and application agnostic,
enabling interoperability across a range of
cyber security tools and applications.
The use of standardized interfaces and protocols enables
interoperability of different tools,
regardless of the vendor that developed them,
the language they are written in
or the function they are designed to fulfill.

With CASP, security professionals can orchestrate automated,
tactical threat responses across a wide range of
cyber-defense technologies at speeds significantly
greater than previously imagined.

As a subproject of the Open Cybersecurity Alliance,
an OASIS Open Project,
the community of cyber-security stakeholders across government agencies,
small to large industries across all sectors, and academia
can join together to innovate and evolve this cyberdefense approach.

The initial focus of the Cybersecurity Automation SubProject (CASP)
will be the Cybersecurity Automation Workshops.
Cybersecurity Automation Workshops are
a series of events to prototype and test
interoperability among cybersecurity automation technologies.
CASP will maintain this website as well as may produce documentation
aiding awareness/adoption and/or interoperability
of cybersecurity automation interfaces.

Another area of CASP focus will be use cases.
Many of the related projects have use cases specific
to the interfaces they are defining, e.g.
[X.1215](https://www.itu.int/rec/T-REC-X.1215/en)
for STIX use cases.
CASP will concentrate on use cases across the technologies involved,
e.g. taking the malware use case in X.1215 and looking at it from
an enterprise viewpoint across
[STIX](https://oasis-open.github.io/cti-documentation/stix/intro.html),
[Kestrel](https://github.com/opencybersecurityalliance/kestrel-lang),
[stixshifter](https://github.com/opencybersecurityalliance/stix-shifter),
[CACAO](https://docs.oasis-open.org/cacao/security-playbooks/v1.0/security-playbooks-v1.0.html),
[PACE](https://opencybersecurityalliance.org/pace/),
[OpenC2](https://openc2.org/),
[IoB](https://github.com/opencybersecurityalliance/oca-iob),
[TAC](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=tac),
[VSMI](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=vsmi),
[SBOM](https://www.cisa.gov/sbom),
[CSAF](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=csaf)/[VEX](https://www.cisa.gov/sites/default/files/publications/VEX_Use_Cases_Aprill2022.pdf),
[JADN](https://www.oasis-open.org/standard/specification-for-json-abstract-data-notation-jadn-version-1-0-committee-specification-01/),
[NIEM](https://github.com/niemopen/oasis-open-project#readme),
[OCSF](https://github.com/ocsf/), ...

CASP will attempt to use existing specifications/standards
wherever possible,
but the scope of this subproject
includes creating standards-track specifications
if necessary.
For example, to aid interworking,
CASP may select certain specifications
or options among competing choices.
Some potential specification topics are included in
[ExampleSpecTopics.md](./ExampleSpecTopics.md)

## 4. Organization Benefits
By its nature, CASP shares many of the benefits of OCA overall.
As shown by the JHU/APL research (add ref),
automation reduces the dwell time of attackers
by several orders of magnitude (hours instead of weeks),
leading to significant cost savings and risk reduction.
Automation requires integration across the tool chain.
End user organizations have consistently wanted to be able
to integrate ‘best-of-breed’ products and solutions
into their operational environments with minimal effort and time.
However, they have been unable to because of the
lack of real interoperability at the communications and data levels.
CASP enables end users to respond quicker with fewer resources
focused on the most important tasks.

For vendors, the ability to integrate cybersecurity products
with multiple vendors
using one common set of communication capabilities and tooling will greatly
reduce the expense of engineering resources spent on integration.
Easy integration also mitigates the problem of having to be too selective
and narrow in focus when it comes to choosing which
vendor technologies to integrate with.
Resources previously spent on integrations can then be re-deployed
to other parts of the product pipeline, enabling higher value functionality
to be developed in the products.

## 5. Relationship to Other Projects
By its nature, CASP has relationships with many other
projects, including the other 4 OCA subprojects and
many OASIS Technical Committees
as well as other organizations.
For related activities, see the
[FAQ](./OCA-Automation-FAQ.md).

## 6. Repositories and Licenses
CASP expects to launch with one repository
for development of the Cybersecurity Automation Workshop.
The Cybersecurity Automation Workshop repository
will be under
the CC BY 4.0 open-source license
for non-code contributions
and is not forseen to contain software.

CASP may propose additional repositories in the future
and would seek OCA TSC approval before doing so.
Potential additional repositories may include:
* a CASP "awareness & adoption" website repository. To begin with the workshop repository will serve both for workshop logistics and promoting cybersecurity automation in general. But with time, these may be split into two websites.
* repos for any standards-track work products proposed for development.
E.g. an overarching CASP interworking requirements & conformance specification.
Some potential specification topics are included
[here](./ExampleSpecTopics.md)

Any proposed repositories would include a proposed license
(from approved OCA list).

## 7. Initial Contributions from Existing Work
sFractal is contributing the contents of
this Cybersecurity Automation Workshop website.

## 8. Contributors
It is expected that most, if not all,
of the previous workshop contributors
would contribute.
The [previous Cybersecurity Automation Workshop](http://www.cybersecurityautomationworkshop.org/Results/)
had over 100 participants from around the globe
and included participation from the
PACE, SBOM, OpenC2, OCA, CSAF,
VSM, Kestrel, stix-shifter, STIX/TAXII, TAC,
and CACAO communities.
It included 'sweat equity'from
'[24 organizations](http://www.cybersecurityautomationworkshop.org/SweatEquity/)'.

Initial technical contributors are expected to include:
* Jane Ginn (CTIN)
* Dmitry Raidman (Cybeats)
* Duncan Sparrell (sFractal)
