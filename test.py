__author__ = 'callum'


import traceback


def _read_approved(test_name):
	return open(test_name + '.approved').read()


def approved(thing, test_name_or_None=None):
	test_name = test_name_or_None if test_name_or_None else traceback.extract_stack(None, 2)[0][2]
	return thing == _read_approved(test_name)


def test_actual_is_as_approved():
	assert approved('banana')


def test_actual_is_not_as_approved():
	assert not approved('kumquat')


