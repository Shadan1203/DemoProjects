import pytest

from pyTestDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample7(BaseClass):

    def test_editProfile(self, dataLoad):
        log = self.getlogger()
        log.info(dataLoad[0])
        log.info(dataLoad[2])
        print(dataLoad[2])