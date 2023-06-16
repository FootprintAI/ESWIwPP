import unittest

from school_loader import SchoolLoader

class TestSchoolLoader(unittest.TestCase):

    def test_one(self):
        sl = SchoolLoader()
        pd = sl.load_special_education()
        print(pd)

        pd = sl.load_elementory_school()
        print(pd)

        pd = sl.load_junior_supplementary_school()
        print(pd)

        pd = sl.load_junior_high_school()
        print(pd)

        pd = sl.load_senior_high_school()
        print(pd)

        pd = sl.load_college_school()
        print(pd)

if __name__ == '__main__':
    unittest.main()
