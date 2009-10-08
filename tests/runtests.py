#!/usr/bin/env python
import os
import sys
from unittest import defaultTestLoader, TextTestRunner, TestSuite

TESTS = ['form', 'fields', 'validators', 'widgets']

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

suite = TestSuite()
suite.addTest(defaultTestLoader.loadTestsFromNames(TESTS))

runner = TextTestRunner(verbosity=(sys.argv.count('-v') - sys.argv.count('-q') + 1))
result = runner.run(suite)
sys.exit(not result.wasSuccessful())
