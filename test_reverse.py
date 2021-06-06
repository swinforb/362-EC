"""
Tests for reverse_string
"""

import reverse_string


class TestReverseString:
	def test_expected(self):
		expected = input("What do you expect the reverse to be: ")
		assert expected == reverse_string.main()

	def test_subtract(self):
		expectedLen = input("What should the str len be: ")
		assert expectedLen == len(reverse_string.main())
