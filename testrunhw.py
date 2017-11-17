import unittest
from runhw import test, get_num_test_cases, find_which_runs


class TestBehavior(unittest.TestCase):
    """Test that certain things are true about the structure of the program."""

    def test_bool(self):
        a = test(["first", "second"], 1)
        self.assertIsInstance(a, bool)

    def test_getnum(self):
        a = test(["first", "second"], 1, getnum=True)
        self.assertIsInstance(a, int)
        b = get_num_test_cases()
        self.assertIsInstance(b, int)
        self.assertEqual(a, b)

    def test_which_runs(self):
        vals = ["Hello", "World"]
        a = find_which_runs(vals)
        self.assertEqual(len(a), get_num_test_cases())
        for res in a:
            self.assertIsInstance(res, bool)
        

class TestSuccess(unittest.TestCase):
    """Test that certain things are true about the function of the program."""

    def test_first(self):
        hello = test(["Hello", "World"], 1)
        greet = test(["Greetings", "Kleiner"], 1)
        salut = test(["Salutations", "Morrison"], 1)
        self.assertTrue(hello)
        self.assertFalse(greet)
        self.assertFalse(salut)

    def test_second(self):
        hello = test(["Hello", "World"], 2)
        greet = test(["Greetings", "Kleiner"], 2)
        salut = test(["Salutations", "Morrison"], 2)
        self.assertFalse(hello)
        self.assertTrue(greet)
        self.assertFalse(salut)

    def test_third(self):
        hello = test(["Hello", "World"], 3)
        greet = test(["Greetings", "Kleiner"], 3)
        salut = test(["Salutations", "Morrison"], 3)
        self.assertFalse(hello)
        self.assertFalse(greet)
        self.assertTrue(salut)

    def test_consecutive(self):
        test(["Hello", "World"], 1)
        a = test(["Hello", "World"], 1)
        self.assertTrue(a)

    def test_getnum(self):
        a = test(["first", "second"], 1, getnum=True)
        self.assertEqual(a, 3)
        b = get_num_test_cases()
        self.assertEqual(b, 3)

    def test_which_runs(self):
        helloworld = find_which_runs(["Hello", "World"])
        self.assertEqual(helloworld, [True, False, False])
        greetings = find_which_runs(["Greetings", "Kleiner"])
        self.assertEqual(greetings, [False, True, False])
        sals = find_which_runs(["Salutations", "Morrison"])
        self.assertEqual(sals, [False, False, True])

class TestFails(unittest.TestCase):
    """Test that certain things are false about the function of the program."""

    def test_arg_polution(self):
        a = test(["Hello", "World"], 2)
        self.assertFalse(a)
        b = test(["Greetings", "Kleiner"], 1)
        self.assertFalse(b)


if __name__ == "__main__":
    unittest.main()

