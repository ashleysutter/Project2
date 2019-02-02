# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):

    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)
    
    def test_postfix_eval_02(self):
        self.assertAlmostEqual(postfix_eval("5 1 2 + 4 ** + 3 -"), 83)

    def test_postfix_eval_03(self):
        self.assertAlmostEqual(postfix_eval("12 6 / 4 *"), 8)

    def test_postfix_eval_04(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_05(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_06(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval_07(self):
        try:
            postfix_eval("")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_08(self):
        self.assertEqual(postfix_eval("7 1 >>"), 3)

    def test_postfix_eval_09(self):
        self.assertEqual(postfix_eval("14 1 <<"), 28)

    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
        
    def test_infix_to_postfix_02(self):
        self.assertEqual(infix_to_postfix("2 ** 3 ** 2"), "2 3 2 ** **")
        self.assertEqual(infix_to_postfix("5 * ( 6 + 3 - 7 * 3 + 2 ) / 6"), "5 6 3 + 7 3 * - 2 + * 6 /")

    def test_infix_to_postfix_03(self):
        self.assertEqual(infix_to_postfix("8 + 3 * 4 + ( 6 - 2 + 2 * ( 6 / 3 - 1 ) - 3 )"), "8 3 4 * + 6 2 - 2 6 3 / 1 - * + 3 - +")
        self.assertEqual(infix_to_postfix(""), "")

    def test_infix_to_postfix_04(self):
        self.assertEqual(infix_to_postfix(""), "")
        self.assertEqual(infix_to_postfix(""), "")

    def test_infix_to_postfix_05(self):
        self.assertEqual(infix_to_postfix("1 + 2 >> 1"), "1 2 1 >> +")
        self.assertEqual(infix_to_postfix("1 >> 2 ** 2"), "1 2 >> 2 **")

    def test_infix_to_postfix(self):
        self.assertEqual(infix_to_postfix("1 + 2 * 3"), "1 2 3 * +")
        self.assertEqual(infix_to_postfix("( 1 + 2 ) * 3"), "1 2 + 3 *")

    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")

    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("+ 1 2"), "1 2 +")

if __name__ == "__main__":
    unittest.main()
