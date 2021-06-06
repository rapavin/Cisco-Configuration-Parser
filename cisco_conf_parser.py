import textfsm
import os

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
					switch_data[each_textfsm_templates_list[0:-4]] = data[0]
				except:
					switch_data[each_textfsm_templates_list[0:-4]] = ["N/A"]

Cisco_Configuration_parser.read_input_file()
Cisco_Configuration_parser.import_textfsm_template()

print(switch_data)