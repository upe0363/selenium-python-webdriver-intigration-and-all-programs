import pytest


def setup_module(module):
    print("Creating DB Connection")


def teardown_module(module):
    print("Closing DB Connection")


def test_dologin():
    print("launching browser")
    print("Executing login test")


def test_user_reg():
    print("launching browser")
    print("Executing User Reg test")
