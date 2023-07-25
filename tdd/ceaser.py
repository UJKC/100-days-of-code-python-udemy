import unittest

alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s" ,"t", "u", "v", "w", "x", "v", "z"]

#Function of testing
def encrypt(message):
    safe = []
    for i in message:
        j = 0
        while alpha:
            if i == alpha[j]:
                break
            j += 1
        after = alpha[j + 1]
        safe.append(after)
    ele = "".join(safe)
    return ele

class TestEncryption(unittest.TestCase):
    def setUp(self):
        self.mymessage = "banana"

    #Test here
    #input is not empty
    def test_inputExist(self):
        self.assertIsNotNone(self.mymessage)

    #test input data type
    def test_inputType(self):
        self.assertIsInstance(self.mymessage, str)

    #test output data type
    def test_outputType(self):
        self.assertIsInstance(encrypt(self.mymessage), str)

    #Output is not empty
    def test_functionReturnsSomething(self):
        self.assertIsNotNone(encrypt(self.mymessage))

    #Test the kength of IO
    def test_lengthIO(self):
        self.assertEqual(len(self.mymessage), len(encrypt(self.mymessage)))

    #If input message is revealed within outpur message
    def test_notEqual(self):
        self.assertNotIn(self.mymessage, encrypt(self.mymessage))

    #If input message is revealed within outpur message
    def test_inputIsNotEqualToOutput(self):
        self.assertNotEqual(self.mymessage, encrypt(self.mymessage)) 

if __name__ == "__main__":
    unittest.main()