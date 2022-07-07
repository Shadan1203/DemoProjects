import pytest


@pytest.fixture()
def setup():
    print("I will be executing first")
    yield
    print("I will execute last")

@pytest.fixture()
def dataLoad():
    print("Data driven approach uploaded")
    return ["Shadan","Haq","www.google.com"]
