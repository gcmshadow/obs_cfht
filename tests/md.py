#!/usr/bin/env python

import unittest
import lsst.utils.tests as utilsTests

import lsst.daf.persistence as dafPersist
from lsst.obs.cfht import CfhtMapper

class MetadataTestCase(unittest.TestCase):
    """Testing butler metadata retrieval"""

    def setUp(self):
        self.bf = dafPersist.ButlerFactory(mapper=CfhtMapper(
            root="./tests/data",calibRoot="./tests/data/calib"))
        self.butler = self.bf.create()

    def tearDown(self):
        del self.butler
        del self.bf

    def testTiles(self):
        """Test sky tiles"""
        tiles = self.butler.queryMetadata("raw", "skyTile", ("skyTile",))
        tiles = [x[0] for x in tiles]
        tiles.sort()
        self.assertEqual(tiles, [
            99757, 99758, 99759, 100477, 100478, 100479, 181384, 181385,
            181386, 181836, 181837, 181838, 181839, 182281, 182282, 182283,
            182284, 182719, 182720
            ])

    def testCcdsInTiles(self):
        """Test CCDs in sky tiles"""
        ccds = self.butler.queryMetadata("raw", "ccd",
                ("visit", "ccd"), skyTile=182719)
        ccds.sort()
        self.assertEqual(ccds, [(788965, 1), (792170, 1), (792933, 1)])

        ccds = self.butler.queryMetadata("raw", "ccd",
                ("visit", "ccd"), dataId={'skyTile': 181386})
        ccds.sort()
        self.assertEqual(ccds, [
            (788965, 29), (788965, 30), (788965, 31),
            (792170, 29), (792170, 30), (792170, 31),
            (792933, 29), (792933, 30), (792933, 31)
            ])

    def testVisits(self):
        """Test visits"""
        visits = self.butler.queryMetadata("raw", "visit", ("visit",), {})
        visits = [x[0] for x in visits]
        visits.sort()
        self.assertEqual(visits, [
            787650, 787731, 787784, 787796, 788033, 788052, 788455, 788548,
            788555, 788556, 788557, 788558, 788559, 788965, 789033, 792170,
            792933, 793310
            ])

    def testFilter(self):
        """Test filters"""
        filter = self.butler.queryMetadata("raw", "visit", ("filter",),
                visit=792170)
        self.assertEqual(filter, [(u'i',)])


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def suite():
    """Returns a suite containing all the test cases in this module."""

    utilsTests.init()

    suites = []
    suites += unittest.makeSuite(MetadataTestCase)
    suites += unittest.makeSuite(utilsTests.MemoryTestCase)
    return unittest.TestSuite(suites)

def run(shouldExit = False):
    """Run the tests"""
    utilsTests.run(suite(), shouldExit)

if __name__ == "__main__":
    run(True)