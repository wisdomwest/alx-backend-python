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

    def test_public_repos_url(self):
        '''Test the GithubOrgClient._public_repos_url method.'''
        with patch('client.GithubOrgClient._public_repos_url') as mock:
            test = GithubOrgClient("google")
            test._public_repos_url()
            mock.assert_called_once()
