import unittest

import HtmlTestRunner

from pages.test_douglas_page import TestDouglasPage


class TestDouglasSuite(unittest.TestCase):

    def test_suite(self):
        test_suite = unittest.TestSuite()
        test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestDouglasPage))

        runner = HtmlTestRunner.HTMLTestRunner(

            combine_reports=True,
            report_title="Test Douglas Page",
            report_name="Test Results"
        )

        runner.run(test_suite)
