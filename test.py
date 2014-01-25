__author__ = 'callum'


def _read_approved():
	return open('my_test.approved').read()


def approved(thing):
	return thing == _read_approved()


def test_actual_is_as_approved():
	assert approved('banana')


def test_actual_is_not_as_approved():
	assert not approved('kumquat')
