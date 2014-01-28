__author__ = 'callum'
import inspect


def _read_approved():
	return open('my_test.approved').read()


def approved(thing):
	return thing == _read_approved()


def test_actual_is_as_approved():
	assert approved('banana')


def test_actual_is_not_as_approved():
	assert not approved('kumquat')


def name_of_test():
	"""
	Now redundant as temp must be assigned within the current function
	"""
	temp = globals()[inspect.getframeinfo(inspect.currentframe()).function]
	return temp.__name__


def test_can_get_test_name():
	"""
	See http://docs.python.org/3.3/library/inspect.html
	  and http://stackoverflow.com/questions/5063607/is-there-a-self-flag-can-reference-python-function-inside-itself
	"""
	temp = globals()[inspect.getframeinfo(inspect.currentframe()).function]
	assert temp.__name__ == 'test_can_get_test_name'
