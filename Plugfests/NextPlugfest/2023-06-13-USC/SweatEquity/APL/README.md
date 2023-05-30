# APL - IOB  Sweat Equity

# 1. Attendance

APL intends to have at least one participant from the IOB project available during the plugfest.

# 2. Contributions

IOB will provide a reference implementation Javascript Object Notation (JSON) for IOB representation of the relevant Use Case(s) used in the event. IOB may also use a publicly available python script to convert IOB bundles into Neo4J graph database and provide queries.

# 3. Planned Technologies

## 3.1 Machine to Machine

IOB behavior bundle JSON and python converter script available at [this github link](https://github.com/opencybersecurityalliance/oca-iob/tree/main/STIX2NEO4J%20Converter).

## 3.2 Human to Machine

IOB will provide Neo4J the following graph database queries

```
// Sample Neo4J queries assuming the script was used with a "bundlesource" named CASPDEMO

// See the Behavior Set
MATCH(A) WHERE A.bundlesource="CASPDEMO" RETURN A

// Show the Detection Relationships (requires APOC enabled on Neo4j)
MATCH (A)-[r:detects]->(B:`x-oca-behavior`) 
WHERE A.bundlesource="CASPDEMO" 
Return A.name as DetectionName, apoc.convert.fromJsonMap(A.analytic).type as AnalyticType, apoc.text.base64Decode(apoc.convert.fromJsonMap(A.analytic).rule) as AnalyticRule, type(r) , B.name as BehaviorName, B.technique as BehaviorTechnique
ORDER BY BehaviorName

// Show the Kestrel Huntbook (requires APOC enabled)
MATCH(A) WHERE A.bundlesource="CASPDEMO" 
UNWIND apoc.convert.fromJsonList(A.correlation_workflows) AS WFDATA
RETURN A.name, A.description, WFDATA.type as Corr_Type, WFDATA.note as Corr_Note, 
apoc.text.base64Decode(WFDATA.workflow) as Corr_Workflow

//Show the CACAO Playbook Data (Requires APOC enabled on NEo4j)
MATCH (A:`x-oca-playbook`)-[r]->(B:`course-of-action`) 
WHERE A.bundlesource="CASPDEMO" 
RETURN A.name,A.playbook_type,A.playbook_format,
apoc.text.base64Decode(A.playbook_bin),type(r),B.name

```

# 4. Planned Use Cases

IOB plans to support use cases based on the planned Kestrel Huntbooks for use in the event.
