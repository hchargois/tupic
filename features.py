#!/usr/bin/env python3
#*-* encoding:utf8 *-*

# CLASSES
########################################
# ======================================
class SourceFeature():
	"""An operation available for a Source"""

	def __init__(self, name):
		self.name = name
		
	def do(self):
		"""Execute the operation"""

		raise NotImplementedError("Abstract, override it")

# ======================================
class GetfromplayerSourceFeature(SourceFeature):
	"""Get the show from a given url containing the player."""
	def __init__(self):
		super(GetfromplayerSourceFeature, self).__init__("getfromplayer")

		self.url = ""
	
	def do(self):
		"""Should return a (title, server, playlist) triplet.
		This is implemented on a per-instance basis"""

		return "", "", []
	
# ======================================
class ListshowsSourceFeature(SourceFeature):
	"""List the shows available for the Source."""
	def __init__(self):
		super(ListshowsSourceFeature, self).__init__('listshows')
		

	def do(self):
		"""Should return a list of dictionnaries containing info on
		each show.
		Only the 'title' element of the dictionnary, which MUST
		contain the title of the show, is mandatory.

		The other possible elements are:

		desc:			a short description of the show
		url:			the show (player) URL
		duration:		show duration, in minutes
		airdate_long:		a string for the air date
		video_rights_until:	a string indicating how much time is
					left before the video disappear
					from the server
		video_views:		the number of views for the video
		video_channels:		a string containing tags relative to
					the show
		video_rank:		the source-dependent site ranking of
					the show

		This is implemented on a per-instance basis"""

		return []

