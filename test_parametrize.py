import pytest


def get_data():
    return [

        ("trainer@way2automation.com", "ksdhvsudvuajv"),
        ("java@way2automation.com", "dhvhc"),
        ("info@way2automation.com", "sdhvsc")

    ]


@pytest.mark.parametrize("username,password", get_data())
def test_dologin(username, password):
    print(username, "---", password)
