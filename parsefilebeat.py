import json
from datadog import statsd

def parse_sxgfilebeat(logger, line):
   attr_list = ['esb', 'Environment:prod', 'region:us-denver', 'app-name:filebeat']
   #statsd.gauge('sxg_audit.transaction_time', transaction_time, tags=attr_list)
   if '{"monitoring": {"metrics": {' in line:
          myjson = line[line.find('{'):]
          jsonstr = json.loads(myjson)
          statsd.gauge('filebeat.memory_total', jsonstr['monitoring']['metrics']['beat']['memstats']['memory_total'] , tags=attr_list)
          # print jsonstr['monitoring']['metrics']['beat']['memstats']['memory_total'] # gauge
          statsd.gauge('filebeat.events_added', jsonstr['monitoring']['metrics']['filebeat']['events']['added']
 , tags=attr_list)
          # print jsonstr['monitoring']['metrics']['filebeat']['events']['added']
          statsd.gauge('filebeat.events_done', jsonstr['monitoring']['metrics']['filebeat']['events']['done'], tags-attr_list)
          # print jsonstr['monitoring']['metrics']['filebeat']['events']['done']
          statsd.gauge('filebeat.events_active, jsonstr['monitoring']['metrics']['libbeat']['events']['active'], tags-attr_list)
          # print jsonstr['monitoring']['metrics']['libbeat']['pipeline']['events']['active'] # gauge
          statsd.gauge('filebeat.events_published', jsonstr['monitoring']['metrics']['libbeat']['pipeline']['events']['published'], tags-attr_list)
          # print jsonstr['monitoring']['metrics']['libbeat']['pipeline']['events']['published']
          statsd.gauge('filebeat.events_total', jsonstr['monitoring']['metrics']['libbeat']['output']['events']['total'], tags-attr_list)
          # print jsonstr['monitoring']['metrics']['libbeat']['output']['events']['total']
          statsd.gauge('filebeat.events_acked', jsonstr['monitoring']['metrics']['libbeat']['output']['events']['acked'], tags-attr_list)
          # print jsonstr['monitoring']['metrics']['libbeat']['output']['events']['acked']

