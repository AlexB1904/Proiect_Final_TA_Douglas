import unittest

import HtmlTestRunner

from pages.test_douglas_page import TestDouglasPage


class TestDouglasSuite(unittest.TestCase):

    def test_suite(self):
        test_suite = unittest.TestSuite()  # blocul de cod in care sunt grupate testele in suita
        test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestDouglasPage))

        runner = HtmlTestRunner.HTMLTestRunner(
            # se ruleaza testele prin intermediul unui runner html care genereaza un raport.
            combine_reports=True,  # care o sa contina un titllu si un rezultat
            report_title="Test Douglas Page",
            report_name="Test Results"
        )

        runner.run(test_suite)
