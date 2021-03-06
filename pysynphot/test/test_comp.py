from __future__ import division, print_function
from unittest import TestCase
from testutil import skip
try:
    from pysynphot.graphtab import CompTable
except ImportError:
    print("not implemented yet")

class CompCase(TestCase):
    @skip
    def setUp(self):
        self.fname='something'
        self.C=CompTable(self.fname)

    def test_nodups(self):
        #Test for duplicate filenames.
        #Duplicate compnames will be caught at construction
        self.assertTrue(self.C._dupcheck())

    def testvalid(self):
        #C is dictionary-like
        self.assertTrue(self.C.validate())

class BadComp(TestCase):
    @skip
    def setUp(self):
        self.fname='somethingelse'

    def testdupcomp(self):
        self.assertRaises(Comptab,
                          self.fname,
                          KeyError)

