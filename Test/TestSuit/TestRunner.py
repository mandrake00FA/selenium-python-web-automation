from unittest import TestLoader, TestSuite, TextTestRunner
from selenium-python-web-automation.Test.Scripts.test_ProductSearch import ProductSearch


if __name__ == "__main__":

    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(ProductSearch)
        ))

    #Run tests sequentially using TextTestRunner
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)
