#!/usr/bin/env sh

# 1st huntflow: no argument
# it will generate disablefw.json and hosts.json to send back

kestrel oc2-hunt-1.hf

# 2nd huntflow: two arguments
# oc2 will write the arguments down to file so there is no edit in huntflow
# let's mimic the receiving/creation of the files in this script
# it will generate ancestors.json to send back

cp disablefw.json targetprocs.json
cp hosts.json targethosts.json

kestrel oc2-hunt-2.hf

# 3rd huntflow: two arguments
# oc2 will write the arguments down to file so there is no edit in huntflow
# let's mimic the receiving/creation of the files in this script
# it will generate siblings.json and binaries.json to send back

cp disablefw.json targetprocs.json
cp hosts.json targethosts.json

kestrel oc2-hunt-3.hf

# 4th huntflow: two arguments
# oc2 will write the arguments down to file so there is no edit in huntflow
# let's mimic the receiving/creation of the files in this script
# it will generate remoteip.json to send back

cp siblings.json targetprocs.json
cp hosts.json targethosts.json

kestrel oc2-hunt-4.hf
