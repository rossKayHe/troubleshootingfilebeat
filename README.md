# troubleshooting filebeat

In datadog.conf put in dogstreams: /var/log/filebeat/filebeat:parsefilebeat:parse_filebeat
Place parsefilebeat.py in /opt/datadog-agent/agent
Permission the filebeat log directory chmod 2755 /var/log/filebeat
Permission the filebeat log file chmod 644 /var/log/filebeat/filebeat