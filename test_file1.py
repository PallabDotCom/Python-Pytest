
import pytest



@pytest.mark.smoke
def test_firstProgram(setup):# before and after statement will be printed as defined under conftest.py setup.
    print("Hello")


@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("Good Morning")

#This test will use data from conftest.py data parameterization
def test_crossBrowser(crossBrowser):
	print(crossbrowser[0])
    print(crossBrowser[1])







