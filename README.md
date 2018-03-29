# troubleshooting filebeat

* In datadog.conf put in dogstreams: /var/log/filebeat/filebeat:parsefilebeat:parse_filebeat
* Place parsefilebeat.py in /opt/datadog-agent/agent
* Permission the filebeat log directory chmod 2755 /var/log/filebeat
* configure the log file for reading: https://www.elastic.co/guide/en/beats/filebeat/current/configuration-logging.html

~~~
logging.files:
  path: /var/log/filebeat
  name: filebeat
  keepfiles: 7
  permissions: 0644
~~~