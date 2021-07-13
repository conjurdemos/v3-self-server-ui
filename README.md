# Self-Server UI

Fat-client UIs written in Python w/ the tkinter UI module.

There are three UIs for specific roles:
 - 1-submit-accreq.sh - starts request UI for developer/project admin role
 - 2-review-accreqs.sh - starts approval & provisioning UI for security admin role
 - 3-govern.py - starts review UI for auditor role

## Python source
### Common
 - config.py
   - points to tomcat server cybr endpoint
   - provides values for Vault, CPM and LOB names
 - CORPORATE_LOGO.png - acme logo - replace with customer logo - must be png
 - loginwin.py - could be enhanced to actually authenticate user.

### Submit access request
 - main-submit.py
 - accesssubmit.py
 - projectinfo.py - could be part of accesssubmit.py
 - identityinfo.py - could be part of accesssubmit.py
 - accountinfo.py - (no longer used - could be deleted)

### Approve/Provision/Reject/Revoke access requests
 - main-requests.py
 - accessrequests.py

### Review provisioned, unrevoked access requests
 - main-govern.py
 - accessgovern.py

## Helper scripts
 - _checkin.sh - checks changes in to specified github branch
 - appgovdb-status.sh - lists active/stale connections to server
 - exec-to-db.sh - interactive MySQL cli
 - tomcat-debug-logs.sh - cats logs for debugging

## mysql directory
 - mysql.config - URL of database (container values for MySQL)
 - exec-to-db-server.sh - interactive mysql cli
 - mysql-pids-cleanup.sh - deletes stale connections
 - mysql-pids-status.sh - list active/stale connections to server
 - appgovdb - create/load/query appgovdb
 - azure - for appgovdb in azure
 - docinabox - target DB create/load/query
 - petclinic - target db create/load/query
