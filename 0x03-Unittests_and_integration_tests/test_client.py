#!/usr/bin/env python3
'''Module for testing the client module.'''

from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
import json
import unittest
from fixtures import TEST_PAYLOAD
from unittest.mock import PropertyMock, patch


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
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://api.github.com/"
            test = GithubOrgClient("google")
            assert test.public_repos() == ["google"]
            mock.assert_called_once_with("https://api.github.com/")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ unit-test for GithubOrgClient.has_license """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)

    @parameterized_class(
        ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
        TEST_PAYLOAD
    )
    class TestIntegrationGithubOrgClient(unittest.TestCase):
        '''Integration tests for the GithubOrgClient class.'''
        @classmethod
        def setUpClass(cls):
            '''called before class test are run'''
            config = {'return_value.json.side_effect':
                      [cls.org_payload, cls.repos_payload]}

            cls.get_patcher = patch('requests.get', **config)

            cls.mock = cls.get_patcher.start()

        @classmethod
        def tearDownClass(cls):
            '''called after class tests have run'''
            cls.get_patcher.stop()
