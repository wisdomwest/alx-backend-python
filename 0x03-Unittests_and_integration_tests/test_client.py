#!/usr/bin/env python3
'''Module for testing the client module.'''

from client import GithubOrgClient
from parameterized import parameterized
import json
import unittest
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    '''Tests for the GithubOrgClient class.'''

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org, mock):
        '''Test the GithubOrgClient.org method.'''
        test = GithubOrgClient(org)
        test.org()
        mock.assert_called_once_with(f"https://api.github.com/orgs/{org}")
