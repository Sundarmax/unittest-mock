import unittest
from unittest.mock import patch, MagicMock
import responses
from source import *


class TestUser(unittest.TestCase):
    @patch("source.get_user")
    def test_len_user(self, mock_get_user):
        mock_get_user.return_value = [1, 2, 4]
        self.assertEqual(len_user(), 3)

    @patch("source.requests")
    def test_get_user(self, mock_request):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": [1, 2]}
        mock_request.get.return_value = mock_response

        self.assertEqual(get_user(), [1, 2])

    @responses.activate
    def test_get_return_a_user(self):
        responses.add(
            method=responses.GET,
            url="https://reqres.in/api/users?page=2",
            status=200,
            json={"data": [1, 2, 3]},
        )
        self.assertEqual(get_user(), [1, 2, 3])

    @responses.activate
    def test_get_user_exception(self):
        responses.add(
            method=responses.GET,
            url="https://reqres.in/api/users?page=2",
            status=500,
            json={},
        )
        res = "Connection error was raised"
        self.assertEqual(get_user(), res)

    def test_value_error(self):
        self.assertRaises(ValueError, convert_integer, "x")
