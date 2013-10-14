#!/usr/bin/env python3
#*-* encoding:utf8 *-*

# CLASSES
########################################
class UnrecognizedSourceError(Exception):
	"""The URL cannot be parsed as a known Source."""
	
	def __init__(self, url):
		self.url = url

	def __str__(self):
		return 'The URL \'' + self.url + '\' cannot be parsed as a known Source'

class UnsupportedSourceError(Exception):
    """The Source being used is not yet supported."""
    
    def __init__(self, source):
        self.source = source

    def __str__(self):
        return 'The source \'' + self.source + '\' you are trying to use is not supported yet'

class UnsupportedFeatureError(Exception):
	"""The Feature is not supported for the used Source"""
	
	def __init__(self, source, feature):
		self.source = source
		self.feature = feature

	def __str__(self):
		return 'The \'' + self.feature + '\' Feature is not available for the \'' + self.source +'\' Source'
