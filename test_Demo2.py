import pytest


@pytest.mark.skip
def test_firstDemo(setup):
    msg= "Hello"
    assert msg == "Hi", "Test failed Msg did not matched"

@pytest.mark.smoke
def test_secondDemo():
    a=4
    b=6
    assert a+b == 10, "Sum matched"