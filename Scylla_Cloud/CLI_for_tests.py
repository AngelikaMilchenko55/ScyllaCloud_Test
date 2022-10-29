import argparse
import pytest


parser = argparse.ArgumentParser(description="Tests runner")
parser.add_argument("-a", "--all", action="store_true", help="run all tests for the registration and login pages")
parser.add_argument("-sut", "--testSU", action="store_true", help="run test in class TestSignUpPage")
parser.add_argument("-si", "--testSI", action="store_true", help="run test in class TestSignInPage")
parser.add_argument("-sut1", "--testSU1", action="store_true", help="run test test_signup in class TestSignUpPage")
parser.add_argument("-sut2", "--testSU2", action="store_true", help="run test test_signup_link in class TestSignUpPage")
parser.add_argument("-sut3", "--testSU3", action="store_true", help="run test test_invalid_password in class TestSignUpPage")
parser.add_argument("-sit1", "--testSI1", action="store_true", help="run test test_signin in class TestSignInPage")
parser.add_argument("-sit2", "--testSI2", action="store_true", help="run test test_signin_link in class TestSignInPage")

args = parser.parse_args()
if args.all:
    pytest.main(args=["-v", "tests.py"])
elif args.testSU:
    pytest.main(args=["-v", "tests.py::TestSignUpPage"])
elif args.testSI:
    pytest.main(args=["-v", "tests.py::TestSignInPage"])
elif args.testSU1:
    pytest.main(args=["-v", "tests.py::TestSignUpPage::test_signup"])
elif args.testSU2:
    pytest.main(args=["-v", "tests.py::TestSignUpPage::test_signup_link"])
elif args.testSU3:
    pytest.main(args=["-v", "tests.py::TestSignUpPage::test_invalid_password"])
elif args.testSI1:
    pytest.main(args=["-v", "tests.py::TestSignInPage::test_signin"])
elif args.testSI2:
    pytest.main(args=["-v", "tests.py::TestSignInPage::test_signin_link"])



print(args)