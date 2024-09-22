import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10
        return self.distance

    def walk(self):
        self.distance += 5
        return self.distance

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        distance1 = 0
        walk1 = Runner("Tom")
        for i in range(1, 11):
            distance1 = walk1.walk()
        self.assertEqual(distance1, 50)

    def test_run(self):
        walk2 = Runner("Denis")
        distance2 = 0
        for i in range(1, 11):
            distance2 = walk2.run()
        self.assertEqual(distance2, 100)

    def test_challenge(self):
        walk3 = Runner("Maks")
        walk4 = Runner("Ivan")
        distance3 = 0
        distance4 = 0
        distance5 = 0
        distance6 = 0
        for i in range(1, 11):
            distance3 = walk3.run()
        for i in range(1, 11):
            distance4 = walk3.walk()
        self.assertNotEqual(distance3, distance4)
        for i in range(1, 11):
            distance5 = walk4.run()
        for i in range(1, 11):
            distance6 = walk4.walk()
        self.assertNotEqual(distance5, distance6)


if __name__ == "__main__":
    unittest.main()
