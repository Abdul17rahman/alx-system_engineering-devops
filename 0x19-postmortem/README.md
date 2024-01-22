# 0x19-postmortem

# Incident Report/Post mortem 172.20.1.4 server.

## Issue Summary:
At exactly 15:00 GMT on 23rd Nov 2020, my server 172.20.1.4 went completely down affecting all requests and responses to and from the server. This affected the entire operation of our system as the system was returning a 500 for an hour and this was because of a change in the configuration file by one of our team members.
## Timeline:
-        15:00 Server went off after a team member had overridden the config file.
-        15:10 Datadog monitoring detected the issue.
-        15:01 Datadog sent a notification email to the team member responsible
-        15:29 Team member started debugging the issue
-        15:35 Team member realised the change in the config file
-        15:40 Amended the file and updated the fix.
-        15:45 Rebooted the server
-        15:50 Services went back online.
## Root cause:
Our newly employed junior was instructed to deploy the new version of our app with updates we had made to our system, while doing so he ended up making changes to the web server configuration file without realising it causing the server to break down and not able to correctly handle requests from clients.
## Resolution and recovery:
After notification from our monitoring tool about the state of our server, the senior engineer went through all the files that had been deployed and realised there was a change in the web server configuration file by the person that deployed the new version. He recognized the changes and rectified the file then eventually deployed the correct version and configuration file.
## Corrective and Preventative measures:
Realising this kind of issue, going forward we decided to change our contribution strategy by not giving access to everyone to contribute to the GitHub main/master branch.We also created different users on the server so that not everyone can be able to use the root user for anything they’re doing on the server. Lastly, we changed read and write access of configuration files to specific users only.

