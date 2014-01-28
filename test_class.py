import inspect


class TestClass:

	def name_method(self, method):
		return type(self).__name__, method.__name__


	def _read_approved(self):
		return open('my_test.approved').read()


	def approved(self, thing):
		return thing == self._read_approved()


	def test_actual_is_as_approved(self):
		assert self.approved('banana')


	def test_actual_is_not_as_approved(self):
		assert not self.approved('kumquat')


	def test_can_get_test_name(self):
		"""
		See http://docs.python.org/3.3/library/inspect.html
		  and http://stackoverflow.com/questions/5063607/is-there-a-self-flag-can-reference-python-function-inside-itself
		"""
		#temp = globals()[inspect.getframeinfo(inspect.currentframe()).function]
		#assert type(self).__name__ == 'TestClass'
		#assert temp.__name__ == 'test_can_get_test_name'
		assert self.name_method() == "TestClass", "test_can_get_test_name"