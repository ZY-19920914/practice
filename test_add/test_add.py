import pytest
import yaml


class Test_yaml:
    @pytest.mark.parametrize(("a","b"),yaml.safe_load(open("./data.yaml")))
    def test_add_1(self,a,b):
        result=a+b
        print(result)
        assert 30==result

