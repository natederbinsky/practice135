import unittest
from unittest.mock import patch, Mock

from main import (
    greet_human,

    is_it_cold_f,
    TEMP_THRESHOLD_F
)

class TestMainApp(unittest.TestCase):

    def test_isitcoldf_freezing(self) -> None:
        """Tests is_it_cold_f for freezing"""
        self.assertTrue(is_it_cold_f(32))

    def test_isitcoldf_boiling(self) -> None:
        """Tests is_it_cold_f for boiling"""
        self.assertFalse(is_it_cold_f(212))

    def test_isitcoldf_negative(self) -> None:
        """Tests is_it_cold_f for negative temps"""
        self.assertTrue(is_it_cold_f(-40))

    def test_isitcoldf_thresh(self) -> None:
        """Tests is_it_cold_f for threshold"""
        self.assertFalse(is_it_cold_f(TEMP_THRESHOLD_F))

    def test_isitcoldf_above(self) -> None:
        """Tests is_it_cold_f for above the threshold"""
        self.assertFalse(is_it_cold_f(TEMP_THRESHOLD_F+1))

    def test_isitcoldf_below(self) -> None:
        """Tests is_it_cold_f for below the threshold"""
        self.assertTrue(is_it_cold_f(TEMP_THRESHOLD_F-1))

    @patch('builtins.input', side_effect=['alice'])
    @patch('builtins.print')
    def test_greethuman_alice(self, mock_print: Mock, _: Mock) -> None:
        """"Test inputting alice to greet_human"""
        greet_human()
        expected_calls = [
            unittest.mock.call("hello alice"),
        ]
        mock_print.assert_has_calls(expected_calls)

if __name__ == "__main__":
    unittest.main()
