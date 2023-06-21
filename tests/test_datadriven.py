import pytest

from TestData import TestData


class Test_DataDriven:
    @pytest.mark.datadd
    def print_sheetdata(self,getData):
        print(getData["firstname"])




    @pytest.fixture(params=TestData.TesData.get_TestData("Testcase2"))
    def getData(self, request):
        return request.param