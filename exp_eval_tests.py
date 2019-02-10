# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):

    def test_general_tests(self):
        self.assertEqual(postfix_eval("1 1 +"), 2)
        self.assertEqual(postfix_eval("2 1 -"), 1)
        self.assertEqual(postfix_eval("2 2 *"), 4)
        self.assertEqual(postfix_eval("4 2 /"), 2)
        self.assertEqual(postfix_eval("3 2 **"), 9)
        self.assertEqual(postfix_eval("2 1 <<"), 4)
        self.assertEqual(postfix_eval("4 1 >>"), 2)

    def test_more_tests(self):
        self.assertEqual(postfix_eval("5 1 2 + 4 ** + 3 -"), 83)
        self.assertEqual(infix_to_postfix("1 + 2"), "1 2 +")
        self.assertEqual(infix_to_postfix("1 + 2 * 3"), "1 2 3 * +")
        self.assertEqual(infix_to_postfix("( 1 + 2 ) * 3"), "1 2 + 3 *")
        self.assertEqual(infix_to_postfix("1 + 2 >> 1"), "1 2 1 >> +")
        self.assertEqual(infix_to_postfix("1 >> 2 ** 2"), "1 2 >> 2 **")
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"), "3 4 2 * 1 5 - 2 3 ** ** / +")
        self.assertEqual(prefix_to_postfix("+ 1 2"), "1 2 +")
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6 "), "3 2 1 / - 4 5 / 6 - *")
        self.assertEqual(postfix_eval("1.2"), 1.2)
        
    def test_postfix_eval_00(self):
        try:
            postfix_eval('1.1 4 >>')
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)
    
    def test_postfix_eval_02(self):
        self.assertAlmostEqual(postfix_eval("5 1 2 + 4 ** + 3 -"), 83)

    def test_postfix_eval_03(self):
        self.assertAlmostEqual(postfix_eval("12 6 / 4 *"), 8)

    def test_postfix_eval_04(self):
        try:
            postfix_eval("blah")
#            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_05(self):
        try:
            postfix_eval("4 +")
#            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_06(self):
        try:
            postfix_eval("1 2 3 +")
#            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval_07(self):
        try:
            postfix_eval("")
#            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_08(self):
        self.assertEqual(postfix_eval("7 1 >>"), 3)

    def test_postfix_eval_09(self):
        self.assertEqual(postfix_eval("14 1 <<"), 28)

    def test_postfix_eval_10(self):
        try:
            postfix_eval("2 0 /")
        except ValueError:
            pass

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

    def test_infix_to_postfix_06(self):
        self.assertEqual(infix_to_postfix("1 + 2 * 3"), "1 2 3 * +")
        self.assertEqual(infix_to_postfix("( 1 + 2 ) * 3"), "1 2 + 3 *")

    def test_prefix_to_postfix_07(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")

    def test_prefix_to_postfix_08(self):
        self.assertEqual(prefix_to_postfix("+ 1 2"), "1 2 +")

    def test_prefix_to_postfix_09(self):
        self.assertEqual(prefix_to_postfix(""), "")

    #Profssor Humer's Tests
    def test_01postfix_eval_add(self):
        self.assertAlmostEqual(12.0, postfix_eval("12"))

    def test_02_postfix_eval_sub(self):
        self.assertAlmostEqual(-1.9, postfix_eval("5.1 7 -"))

    def test_03_postfix_eval_mult(self):
        self.assertAlmostEqual(35.7, postfix_eval("5.1 7 *"))

    def test_04_postfix_eval_basic_div(self):
        self.assertAlmostEqual(0.728571429, postfix_eval("5.1 7 /"))

    def test_05_postfix_eval_mixed(self):
        self.assertAlmostEqual(25, postfix_eval("25"))

    def test_06_postfix_eval_complex(self):
        self.assertAlmostEqual(5589.854285714286, postfix_eval("3 2 + 8 3 / 17 * + 12 4.2 / 1.2 / 8 6 * - 6.9 17 * 23 6 / + 2.2 - 3.2 - 56 21 / 1.4 * - 2.3 4.1 * + * -"))

    def test_18_prefix_to_postfix_single_value(self):
        self.assertEqual("1.234", prefix_to_postfix("1.234"))

    def test_07_postfix_eval_test_postfix_eexceptions(self):
        try:
            postfix_eval("99 38 1.2 * 3.6 2.8 / + 6 - 3.7 2 / 5 / + 3 - 23 + 1.1 / 2.2 + 2.4 5 / - 1 - 1.6 3 / 9 / 2.8 * 3 - 6.2 4 / 12.8 2 * 1.1 / 4.4 3.2 1.1 5.2 / 9.9 * - / - + - +")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_13_infix_to_postfix_complex(self):
        self.assertEqual("3 2 + 8 3 / 17 * + 12 4.2 / 1.2 / 8 6 * - 6.9 17 * 23 6 / + 2.2 - 3.2 - 56 21 / 1.4 * - 2.3 4.1 * + * -", infix_to_postfix("( 3 + 2 ) + 8 / 3 * 17 - ( 12 / 4.2 / 1.2 - 8 * 6 ) * ( ( 6.9 * 17 + 23 / 6 - 2.2 ) - 3.2 - ( 56 / 21 * 1.4 ) + 2.3 * 4.1 )"))

    def test_14_infix_to_postfix_complex(self):
        self.assertEqual("3 2 >> 8 >> 3 / 17 12 4.2 / 1.2 8 << / 6 * << * 6.9 17 23 >> * 6 2.2 << / 3.2 << 56 21 / 1.4 * << 2.3 >> 4.1 * *", infix_to_postfix("( 3 >> 2 ) >> 8 / 3 * 17 << ( 12 / 4.2 / 1.2 << 8 * 6 ) * ( ( 6.9 * 17 >> 23 / 6 << 2.2 ) << 3.2 << ( 56 / 21 * 1.4 ) >> 2.3 * 4.1 )"))

    def test_15_infix_to_postfix_single_value(self):
        self.assertEqual("1.234", infix_to_postfix("1.234"))

    def test_16_prefix_to_postfix_basic(self):
        self.assertEqual(prefix_to_postfix("+ + + 5 -7.1 11 3"), "5 -7.1 + 11 + 3 +")

    def test_17_prefix_to_postfix_complex(self):
        self.assertEqual(prefix_to_postfix("- + + 3 2 * / 8 3 17 * - / / 12 4.2 1.2 * 8 6 + - - - + * 6.9 17 / 23 6 2.2 3.2 * / 56 21 1.4 * 2.3 4.1"), "3 2 + 8 3 / 17 * + 12 4.2 / 1.2 / 8 6 * - 6.9 17 * 23 6 / + 2.2 - 3.2 - 56 21 / 1.4 * - 2.3 4.1 * + * -")

    def test_19_postfix_eval_bit_shift(self):
        try:
            postfix_eval('1.1 4 <<')
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

if __name__ == "__main__":
    unittest.main()
