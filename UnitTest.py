from DP_Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()
        self.testCases = {
            1: {'expression': "2-1-1", 'output': [0,2]},
            2: {'expression': "2*3-4*5", 'output': [-34,-14,-10,-10,10]}
        }

    @timeout(0.5)
    def test_Case1(self):
        try:
            case = self.testCases[1]
            res = self.obj.diffWaysToCompute(case['expression'])
            self.assertIsInstance(res, list)
            self.assertEqual(len(res), len(case['output']))
            self.assertEqual(res.sort(), case['output'].sort())
        except Exception as e:
            raise e
        
    @timeout(0.5)
    def test_Case2(self):
        try:
            case = self.testCases[2]
            res = self.obj.diffWaysToCompute(case['expression'])
            self.assertIsInstance(res, list)
            self.assertEqual(len(res), len(case['output']))
            self.assertEqual(res.sort(), case['output'].sort())
        except Exception as e:
            raise e
        

if __name__ == '__main__':
    unittest.main()