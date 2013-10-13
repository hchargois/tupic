#!/usr/bin/python
#*-* encoding:utf8 *-*

# IMPORTS
########################################

# CONSTANTS
########################################

# FUNCTIONS
########################################

# CLASSES
########################################

class SourceFeature(object):
	"""An operation available for a Source"""

	def __init__(self, name):
		self.name = name
		
	def do(self):
		"""Execute the operation"""

		raise NotImplementedError("Abstract, override it")

class GetfromplayerSourceFeature(SourceFeature):
	"""Get the show from a given url containing the player."""
	def __init__(self):
		super(GetfromplayerSourceFeature, self).__init__("getfromplayer")

		self.url = ""
	
	def do(self):
		"""Should return a (title, server, playlist) triplet.
		This is implemented on a per-instance basis"""

		return "", "", []
	

