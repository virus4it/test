import unittest
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        ktoto = Runner("Аболтус")
        for i in range(10):
            ktoto.walk()
        self.assertEqual(ktoto.distance,50)
    def test_run(self):
        ktoto = Runner("Аболтус")
        for i in range(10):
            ktoto.run()
        self.assertEqual(ktoto.distance,100)
    def test_chalage(self):
        ktoto=Runner("Аболтус")
        ktoto2=Runner("СвиНота")
        for i in range(10):
            ktoto.walk()
            ktoto2.run()
        self.assertNotEqual(ktoto.distance,ktoto2.distance)
if __name__ =="__main__":
    unittest.main()
