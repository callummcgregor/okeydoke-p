import os

__author__ = 'callum'


import traceback


def _read_approved(test_name):
	with open(test_name + '.approved') as f:
		return f.read()


def _write_actual(thing, test_name):
	with open(test_name + '.actual', 'w') as f:
		return f.write(thing)


def _write_approved(thing, test_name):
	with open(test_name + '.approved', 'w') as f:
		return f.write(thing)


def remove_if_exists(path):
	try:
		os.remove(path)
	except:
		pass


def approved(thing, test_name_or_None=None):
	test_name = test_name_or_None if test_name_or_None else traceback.extract_stack(None, 2)[0][2]
	try:
		assert thing == _read_approved(test_name)
		return True
	except FileNotFoundError:
		_write_actual(thing, test_name)
		raise AssertionError('No approved found')


def approve(thing, test_name_or_None=None):
	test_name = test_name_or_None if test_name_or_None else traceback.extract_stack(None, 2)[0][2]
	_write_approved(thing, test_name)


def test_actual_is_as_approved():
	assert os.path.exists('test_actual_is_as_approved.approved')
	assert approved('banana')


def test_actual_is_not_as_approved():
	assert os.path.exists('test_actual_is_not_as_approved.approved')
	try:
		assert approved('kumquat')
	except AssertionError as x:
		assert 'banana' and 'kumquat' in str(x)
	else:
		assert False, 'Should have thrown'


def test_no_approved():
	remove_if_exists('test_no_approved.actual')
	assert not os.path.exists('test_no_approved.approved')
	assert not os.path.exists('test_no_approved.actual')

	try:
		assert approved('banana')
	except AssertionError as x:
		assert 'No approved found' in str(x)
	else:
		assert False, 'Should have thrown'

	assert os.path.exists('test_no_approved.actual')


def test_no_approved_then_approved():
	remove_if_exists('test_no_approved_then_approved.actual')
	remove_if_exists('test_no_approved_then_approved.approved')
	assert not os.path.exists('test_no_approved_then_approved.approved')
	assert not os.path.exists('test_no_approved_then_approved.actual')
	try:
		assert approved('banana')
	except AssertionError as x:
		assert 'No approved found' in str(x)
	else:
		assert False, 'Should have thrown'
	assert os.path.exists('test_no_approved_then_approved.actual')

	approve('banana')
	assert os.path.exists('test_no_approved_then_approved.approved')
	assert approved('banana')
