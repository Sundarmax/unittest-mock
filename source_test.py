import unittest
from unittest.mock import patch,MagicMock

import source
from source import *

class TestUser(unittest.TestCase):
    @patch('source.get_user')
    def test_len_user(self, mock_get_user):
        mock_get_user.return_value = [1, 2, 4]
        self.assertEqual(len_user(), 3)

    @patch('source.requests')
    def test_get_user(self,mock_request):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'data':[1, 2]}
        mock_request.get.return_value = mock_response

        self.assertEqual(get_user(), [1,2])