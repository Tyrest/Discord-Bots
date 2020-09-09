import string

def close(file):
	"""Closes the file object passed in. """
	file.close()

def readable(file):
	"""Return True if this file can be read from. """
	return file.readable()

def readline(file):
	"""
	Return the first unread line from this file,
	or the empty string if all lines are read.
	"""
	return file.readline()

def readlines(file):
	"""
	Return all unread lines in a list.
	"""
	return file.readlines()

############################
# String utility functions #
############################

def lower(s):
	"""Return a copy of string s with all letters converted to lowercase."""
	return s.lower()


def split(s, sep=None):
	"""
	Returns a list of words contained in s, which are
	sequences of characters separated by a string sep.

	By default, this splits on whitespace (spaces, tabs, etc.)
	but by defining a different sep, you can split on arbitrary
	characters.
	"""
	return s.split(sep)

def strip(s, chars=None):
	"""
	Return a version of s with characters in chars removed
	from the start and end.

	By default, removes whitespace characters.
	"""
	return s.strip(chars)

def lines_from_file(path):
    file = open(path)
    assert readable(file), "File is unreadable and may be corrupted"
    list = readlines(file)
    list = [strip(i) for i in list]
    close(file)
    return list
