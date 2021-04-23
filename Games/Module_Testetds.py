import unittest
import Test_Games

calcTestSuite = unittest.TestSuite()
calcTestSuite.addTest(unittest.makeSuite(Test_Games.olimTest))
print("count of tests: " + str(calcTestSuite.countTestCases()) + "\n")

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestSuite)