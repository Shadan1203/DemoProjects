import pytest


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixtureprogram(self):
        print("I will be executing after setup is executed")

    def test_fixtureprogram1(self):
        print("I will be executing after setup is executed")

    def test_fixtureprogram2(self):
        print("I will be executing after setup is executed")

    def test_fixtureprogram3(self):
        print("I will be executing after setup is executed")
