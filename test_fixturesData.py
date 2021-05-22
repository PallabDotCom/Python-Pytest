#this file will use GetLoggerClass.py file 
import pytest

from pytestsDemo.BaseClass import BaseClass



@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad[0])
        log.info(dataLoad[1])
        
		
@pytest.mark.usefixtures("dataload")
class testexample1:
	def test_dataloadmethod(self,dataload):
		print(dataload[0])
		print(dataload[1])




