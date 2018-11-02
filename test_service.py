import unittest
import pytest
from unittest.mock import MagicMock
from unittest.mock import patch
from service import Service

class TestService(unittest.TestCase):    

    # returns a random number

    # Mock it and patch it
    @patch("test_service.Service.bad_random")

    def test_bad_random(self, mock_service):

        mock_service.return_value = 199
        assert Service.bad_random() == 199
        mock_service.return_value = 0
        assert Service.bad_random() == 0
        mock_service.return_value = -199
        assert Service.bad_random() == -199
        mock_service.return_value = "jdsalkd"
        assert Service.bad_random() is not int
        return

    @patch("test_service.Service.bad_random")
    def test_divide(self, mock_service):

        mock_service.return_value = 18
        assert Service().divide(2) == 9
        with pytest.raises(ZeroDivisionError):Service().divide(0)
        assert Service().divide(-18) == -1
        assert Service().divide(-2) == -9
        return


    def test_abs_plus(self):
        assert Service.abs_plus(self, -999) == 1000
        assert Service.abs_plus(self, 999) == 1000
        assert Service.abs_plus(self, 0) == 1
        assert Service.abs_plus(self, 11) == 12
        return

    @patch("test_service.Service")
    def test_complicated_function(self, mock_service):
        # values for divide
        y = [-7, 0, 3]
        # case 1
        random = mock_service.bad_random.return_value = 49
        mock_service.divide.return_value = random / y[0]
        mock_service.complicated_function.return_value = Service.divide(y[0]), Service.bad_random() % 2

        ret = Service.complicated_function(y[0])
        print(ret)
        assert ret == (-7.0, 1)
        # case 2
        with pytest.raises(ZeroDivisionError):mock_service.divide.return_value = random / y[1]
        # will be previous value of -7.0 b/c error thrown
        mock_service.complicated_function.return_value = Service.divide(y[1]), Service.bad_random() % 2

        ret1 = Service.complicated_function(y[1])
        print(ret1)
        assert ret1 == (-7.0, 1)
        # case 3
        mock_service.divide.return_value = random / y[2]
        mock_service.complicated_function.return_value = Service.divide(y[2]), Service.bad_random() % 2

        ret2 = Service.complicated_function(y[2])
        print(ret2)
        assert ret2 == (16.333333333333332, 1)



TestService()