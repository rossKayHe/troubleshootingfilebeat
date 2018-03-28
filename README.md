# troubleshooting filebeat

* In datadog.conf put in dogstreams: /var/log/filebeat/filebeat:parsefilebeat:parse_filebeat
* Place parsefilebeat.py in /opt/datadog-agent/agent
* Permission the filebeat log directory chmod 2755 /var/log/filebeat
* Add umask 022 to the filebeat init script to permission the log file as read for all