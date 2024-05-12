#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from parameterized import parameterized_class, parameterized
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos
import requests

class TestGithubOrgClient(unittest.TestCase):
    """
    Test cases for GithubOrgClient class.
    """
    @patch('requests.get')
    def test_org(self, mock_get):
        """
        Test org method of GithubOrgClient.
        """
        mock_get.return_value.json.return_value = org_payload
        github_client = GithubOrgClient('google')
        self.assertEqual(github_client.org, org_payload)

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('requests.get')
    def test_org_parametrized(self, org_name, mock_get):
        """
        Parameterized test for org method of GithubOrgClient.
        """
        mock_get.return_value.json.return_value = org_payload
        github_client = GithubOrgClient(org_name)
        self.assertEqual(github_client.org, org_payload)

    @patch('client.GithubOrgClient._public_repos_url', new_callable=lambda: 'url')
    @patch('client.GithubOrgClient.org')
    def test_public_repos_url(self, mock_org, mock_url):
        """
        Test _public_repos_url method of GithubOrgClient.
        """
        mock_org.return_value = org_payload
        github_client = GithubOrgClient('google')
        self.assertEqual(github_client._public_repos_url, 'url')

    @patch('requests.get')
    def test_public_repos(self, mock_get):
        """
        Test public_repos method of GithubOrgClient.
        """
        mock_get.return_value.json.return_value = repos_payload
        github_client = GithubOrgClient('google')
        self.assertEqual(github_client.public_repos(), expected_repos)

    @patch('client.GithubOrgClient._public_repos_url', new_callable=lambda: 'url')
    @patch('requests.get')
    def test_public_repos_with_license(self, mock_get, mock_url):
        """
        Test public_repos method of GithubOrgClient with license parameter.
        """
        mock_get.return_value.json.return_value = apache2_repos
        github_client = GithubOrgClient('google')
        self.assertEqual(github_client.public_repos('apache-2.0'), apache2_repos)

@parameterized_class(('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'), [
    (org_payload, repos_payload, expected_repos, apache2_repos),
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test cases for GithubOrgClient class.
    """
    @classmethod
    def setUpClass(cls):
        """
        Setup class method.
        """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = [
            mock_response(cls.org_payload),
            mock_response(cls.repos_payload)
        ]

    @classmethod
    def tearDownClass(cls):
        """
        Teardown class method.
        """
        cls.get_patcher.stop()

    def test_public_repos_integration(self):
        """
        Integration test for public_repos method of GithubOrgClient.
        """
        github_client = GithubOrgClient('google')
        self.assertEqual(github_client.public_repos(), self.expected_repos)

    def test_public_repos_with_license_integration(self):
        """
        Integration test for public_repos method of GithubOrgClient
        with license parameter.
        """
        github_client = GithubOrgClient('google')
        self.assertEqual(github_client.public_repos
                ('apache-2.0'), self.apache2_repos)

def mock_response(payload):
    """
    Mock response function.
    """
    mock_resp = requests.Response()
    mock_resp.json = lambda: payload
    return mock_resp

if __name__ == '__main__':
    unittest.main()
