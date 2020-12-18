"""
{
	node: {
		tag: "",
		attr: "",
		type: only | all | <int>
	}

	type: text | attribute | dict | list
		// attribute => atrribute: ""
		// dict => properties: ""
		// list => item
	item: {
		node {

		}

		method: ""
	}

	properties: {
		property_name: {
			node: {

			}

			method: ""
		}
	}

	option {

	}
}
"""

import requests
from bs4 import BeautifulSoup

def node_handle(node_obj, node):
	if not "type" in node_obj:
		if "tag" in node_obj and "attribute" in node_obj:
			return node.find(node_obj["tag"], node_obj["attribute"])
		elif "tag" in node_obj:
			return node.find(node_obj["tag"])
		elif "attribute" in node_obj:
			return node.find(attr = node_obj["attribute"])
		else:
			return node
	elif type (node_obj["type"]) == str:
		if node_obj["type"] == "only":
			if "tag" in node_obj and "attribute" in node_obj:
				return node.find(node_obj["tag"], node_obj["attribute"])
			elif "tag" in node_obj:
				return node.find(node_obj["tag"])
			elif "attribute" in node_obj:
				return node.find(attr = node_obj["attribute"])
			else:
				return node
		elif node_obj["type"] == "all":
			if "tag" in node_obj and "attribute" in node_obj:
				return node.find_all(node_obj["tag"], node_obj["attribute"])
			elif "tag" in node_obj:
				return node.find_all(node_obj["tag"])
			elif "attribute" in node_obj:
				return node.find_all(attr = node_obj["attribute"])
			else:
				return node
		else:
			raise "node_obj: There is no type \'" + node_obj["type"] + "\'."
	elif type (node_obj["type"]) == int:
		try:
			if "tag" in node_obj and "attribute" in node_obj:
				return node.find_all(node_obj["tag"], node_obj["attribute"])[node_obj["type"]]
			elif "tag" in node_obj:
				return node.find_all(node_obj["tag"])[node_obj["type"]]
			elif "attribute" in node_obj:
				return node.find_all(attr = node_obj["attribute"])[node_obj["type"]]
			else:
				return node[node_obj["type"]]
		except Exception as e:
			raise e
	else:
		raise "node_obj: There is no type \'" + str(node_obj["type"]) + "\'."


def guide_handle(guide_obj, node):
	if "node" in guide_obj:
		if type (guide_obj["node"]) == dict:
			node = node_handle(guide_obj["node"], node)
		elif type (guide_obj["node"]) == list:
			for node_obj in guide_obj["node"]:
				node = node_handle(node_obj, node)
		else:
			raise "node: node cannot be of type int."

	result = None

	if not "type" in guide_obj:
		result = node.text
	elif guide_obj["type"] == "text":
		result = node.text
	elif guide_obj["type"] == "attribute":
		result = node[guide_obj["attribute"]]
	elif guide_obj["type"] == "available":
		result = guide_obj["available"]
	elif guide_obj["type"] == "dict":
		if not "properties" in guide_obj:
			raise "guide_obj: dict type needs \'properties\' property."

		result = {}
		for key, value in guide_obj["properties"].items():
			result[key] = guide_handle(value, node)
	elif guide_obj["type"] == "list":
		if not "properties" in guide_obj:
			raise "guide_obj: dict type needs \'properties\' property."

		result = []
		for _node in node:
			result.append(guide_handle(guide_obj["item"], _node))
	else:
		raise "guide_obj: There is no type \'" + guide_obj["type"] + "\'"

	if "option" in guide_obj:
		if "works" in guide_obj["option"]:
			for work in guide_obj["option"]["works"]:
				if work == "strip":
					result = result.lstrip().rstrip()
				elif work == "to_string":
					result = str(result)
				elif work == "to_int":
					result = int(result)
				else:
					raise "guide_obj.option.works: no \'" + work + "\'."

		if "replace" in guide_obj["option"]:
			for rt in guide_obj["option"]["replace"]:
				try:
					result = result.replace(rt[0], rt[1])
				except Exception as e:
					raise e

	return result

"""
	prm_obj:
	{
		version: "1",
		guide:
		{
		}
	}
"""
def handle(prm_obj, html_text):
	if not "version" in prm_obj:
		raise "prm_obj: There must have \'version\' property."

	if not "guide":
		raise "prm_obj: There must have \'guide\' property."

	if prm_obj["vesion"] == "1":
		guide_handle(prm_obj["guide"], html_text)
	else
		raise "prm_obj.version: no \'" + prm_obj["version"] + "\'."
