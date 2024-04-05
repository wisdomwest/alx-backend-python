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

    @patch('client.get_json')
    def test_public_repos(self, mock):
        '''Test the GithubOrgClient.public_repos method.'''
        payload = [{"name": "google"}]
        mock.return_value = payload
        with patch('client.GithubOrgClient._public_repos_url') as mock_pub:
            test = GithubOrgClient("google")
            self.assertEqual(test.public_repos(), ["google"])
            mock_pub.assert_called_once()
            mock.assert_called_once_with("google")
