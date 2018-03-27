import json
from datadog import statsd

def parse_filebeat(logger, line):
   attr_list = ['esb', 'Environment:prod', 'region:us-denver', 'app-name:filebeat']
   if '{"monitoring": {"metrics": {' in line:
          myjson = line[line.find('{'):]
          jsonstr = json.loads(myjson)
          statsd.gauge('filebeat.memory_total', jsonstr['monitoring']['metrics']['beat']['memstats']['memory_total'] , tags=attr_list)
          statsd.gauge('filebeat.gc_next', jsonstr['monitoring']['metrics']['beat']['memstats']['gc_next'] , tags=attr_list)
          statsd.gauge('filebeat.memory_alloc', jsonstr['monitoring']['metrics']['beat']['memstats']['memory_alloc'] , tags=attr_list)
          statsd.gauge('filebeat.events_added', jsonstr['monitoring']['metrics']['filebeat']['events']['added'], tags=attr_list)
          statsd.gauge('filebeat.events_done', jsonstr['monitoring']['metrics']['filebeat']['events']['done'], tags=attr_list)
          statsd.gauge('filebeat.libbeat_pipeline.events_active', jsonstr['monitoring']['metrics']['libbeat']['pipeline']['events']['active'], tags=attr_list)
          statsd.gauge('filebeat.libbeat_pipeline.events_published', jsonstr['monitoring']['metrics']['libbeat']['pipeline']['queue']['acked'], tags=attr_list)
          statsd.gauge('filebeat.libbeat_pipeline.queue_acked', jsonstr['monitoring']['metrics']['libbeat']['pipeline']['events']['published'], tags=attr_list)
          statsd.gauge('filebeat.libbeat_output.events_total', jsonstr['monitoring']['metrics']['libbeat']['output']['events']['total'], tags=attr_list)
          statsd.gauge('filebeat.libbeat_output.events_acked', jsonstr['monitoring']['metrics']['libbeat']['output']['events']['acked'], tags=attr_list)
   if '504 Gateway Timeout' in line:
     title = "filebeat Gateway Timeout"
     text = """%%%
**504 Gateway Timeout** error occured
%%%"""
     statsd.event(title = title, text=text, tags=attr_list)

