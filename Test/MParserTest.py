import pytest
from .. import Parsely

class MParserTest(TestCase):
    def create_parser(self):
        self.test_1 = MParser(r"./Test/TestData/Input-001.meshtal")
        assert self.test_1.file is not null

    def test_read_int(self):
        #Check exponent
        assert self.test_1.read_int("8E-2") == .08
        assert self.test_1.read_int("6E2") == 600
        #Check decimal point
        assert self.test_1.read_int(".2E-2") == .002
        assert self.test_1.read_int("2.4E4") == 24000
        #Check raised errors
        with pytest.raises(Error):
            #Invalid exponent
            self.test_1.read_int("5EABD")
            #Invalid base
            self.test_1.read_int("E552")
    # def test_read_data_line():
