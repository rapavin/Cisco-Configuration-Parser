import textfsm
import os
import csv

class Cisco_Configuration_parser:

	def read_input_file():
		global reading_running_conf_read_string
		'''Reads the input file. The input is in string format'''
		reading_running_conf = open("42.1.txt", mode="r")
		reading_running_conf_read_string = reading_running_conf.read()

	def import_textfsm_template():
		global switch_data
		'''Find the location directory of the templates. Currently located at "textfsm_templates"'''
		switch_data = {}
		textfsm_templates_list = os.listdir("/Users/nethelp/Downloads/textfsm_templates")
		for each_textfsm_templates_list in textfsm_templates_list:
			with open("/Users/nethelp/Downloads/textfsm_templates/"+each_textfsm_templates_list) as all_textfsm_templates:
				regex_table_fsm_data = textfsm.TextFSM(all_textfsm_templates)
				data = regex_table_fsm_data.ParseText(reading_running_conf_read_string)
				try:
					if len(data)==1:
						switch_data[each_textfsm_templates_list[0:-4]] = data[0]
					elif len(data)==0:
						switch_data[each_textfsm_templates_list[0:-4]] = ["N/A"]
					elif len(data)>1:
						switch_data[each_textfsm_templates_list[0:-4]] = data
				except:
					pass	

Cisco_Configuration_parser.read_input_file()
Cisco_Configuration_parser.import_textfsm_template()

with open('services_'+switch_data['cisco_show_run_hostname'][0]+'.txt', 'w') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow(["HOSTNAME",switch_data['cisco_show_run_hostname'][0]])
	writer.writerow(["VTP MODE",switch_data['cisco_show_run_vtp_mode'][0]])
	writer.writerow(["VTP DOMAIN",switch_data['cisco_show_run_vtp_domain'][0]])
	writer.writerow(["DOMAIN NAME",switch_data['cisco_show_run_ip_domain_name'][0]])
	writer.writerow(["CLOCK INFORMATION",str(switch_data['cisco_show_run_clock']).replace("[","").replace("]","").replace('"',"").replace("'","".replace('"',""))])
	
#print(switch_data)