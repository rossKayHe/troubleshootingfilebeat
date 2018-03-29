import json
from datadog import statsd

def parse_filebeat(logger, line):
   attr_list = ['esb', 'Environment:prod', 'region:us-denver', 'app-name:filebeat']
   if '{"monitoring": {"metrics": {' in line:
          myjson = line[line.find('{'):]
          jsonstr = json.loads(myjson)
		  jsonstr = jsonstr['monitoring']['metrics']
          statsd.gauge('filebeat.memory_total', jsonstr['beat']['memstats']['memory_total'] , tags=attr_list)
          statsd.gauge('filebeat.gc_next', jsonstr['beat']['memstats']['gc_next'] , tags=attr_list)
          statsd.gauge('filebeat.memory_alloc', jsonstr['beat']['memstats']['memory_alloc'] , tags=attr_list)
          statsd.gauge('filebeat.events_added', jsonstr['filebeat']['events']['added'], tags=attr_list)
          statsd.gauge('filebeat.events_done', jsonstr['filebeat']['events']['done'], tags=attr_list)
          statsd.gauge('filebeat.libbeat_pipeline.events_active', jsonstr['libbeat']['pipeline']['events']['active'], tags=attr_list)
          statsd.gauge('filebeat.libbeat_pipeline.events_published', jsonstr['libbeat']['pipeline']['queue']['acked'], tags=attr_list)
          statsd.gauge('filebeat.libbeat_pipeline.queue_acked', jsonstr['libbeat']['pipeline']['events']['published'], tags=attr_list)
          statsd.gauge('filebeat.libbeat_output.events_total', jsonstr['libbeat']['output']['events']['total'], tags=attr_list)
          statsd.gauge('filebeat.libbeat_output.events_acked', jsonstr['libbeat']['output']['events']['acked'], tags=attr_list)
   if 'ERROR' in line:
     attr_list = ['esb', 'Environment:prod', 'region:us-denver', 'app-name:filebeat', 'x-filebeat-error:error']
	 title = "An error has occurred"
     text = line
     statsd.event(title = title, text=text, tags=attr_list)

