import pytest


#If you want to run fixture for only before and after class execution , not for all the method like above then define scope in conftest.py file.

@pytest.fixture(scope="class")
def setup():
	print ("first execution")
	yield
	print("last execution")
	



@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Pallab","Debnath","kitchener"]

#Running test with multiple dat sets - data parameterization
@pytest.fixture(params=[("chrome","Pallab",), ("Firefox","Debnath"), ("IE","Kitchener)])
def crossBrowser(request):
    return request.param


