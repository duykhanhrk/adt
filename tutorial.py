import requests
from bs4 import BeautifulSoup

# node_obj: it is dict, contains the properties
#	> tag: it is a tag of html
#	> attribute: it is an dict, contains the attribute of tag.
#	> type: includes the values 'only' | 'all' | <int>
# node: it is a string.
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

# guide_obj is a dict, it includes the properties
# 	> node: { }, it is a node_obj
#	> type: "type", types of type property include
#		> 'text': if type is this then guide_obj doesn't need any property.
#		> 'attribute': if type is this then guide_obj need to have a property which is 'attribute'.
#		> 'dict': if type is this then guide_obj need to have a property which is 'properties'.
#		  'properties' property contains properties's name and guide_obj.
#		  Example: 'properties': { 'property_1': { node: {}, type: 'type', 'property_for_type': { } }, 'property_2': { }, .. }
#		> 'list': if type is this then guide_obj need to have a rpoperty which is 'item', it is a guide_obj.
# 	> option: {}, it is a dict, includes the properties
#		> works: it is an array, contains the values 'strip' | 'to_string' | 'to_int'.
#		> replace: it is an array, contrains the arrays, which contain two values ['word_need_to_replace', 'word replace'].
# node is a string.
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

# tutorial_obj is a dict, it includes two properties
#	> version: "1"
#	> guide: { } : it is guide_obj.
# html_text is a string.
def handle(tutorial_obj, html_text):
	if not "version" in tutorial_obj:
		raise "tutorial_obj: There must have \'version\' property."

	if not "guide":
		raise "tutorial_obj: There must have \'guide\' property."

	if tutorial_obj["version"] == "1":
		guide_handle(tutorial_obj["guide"], html_text)
	else
		raise "tutorial_obj.version: no \'" + tutorial_obj["version"] + "\'."
