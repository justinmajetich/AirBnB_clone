#!/usr/bin/env python3
from datetime import datetime
import uuid
def create_dictionary(args:str) -> dict:
	"""Validate types and parsing it
		return a dictionary
		args format = ["Class", "key=value"]
	"""

	arguments = args.split()

	class_name = arguments.pop(0)

	dictionary = {}

	for key_value_pair in arguments:
		key = key_value_pair.split("=")[0]
		value = parse_elements(key_value_pair.split("=")[1])
		dictionary[key] = value

	dictionary['__class__'] = class_name
	dictionary['updated_at'] = datetime.now().isoformat()
	dictionary['created_at'] = datetime.now().isoformat()
	dictionary['id'] = str(uuid.uuid4())
	
	return dictionary

def parse_elements(element):
	""""
	Parse values
	String: "<value>" => starts with a double quote
			all underscores _ must be replace by spaces
	Float: <unit>.<decimal> => contains a dot .
	Integer: <number> => default case
	"""
	if element[0] == "\"":
		new_str = element[1:-1]
		new_str = new_str.replace("_", " ")

		return str(new_str)
	elif "." in element:
		return float(element)
	else:
		return int(element)

