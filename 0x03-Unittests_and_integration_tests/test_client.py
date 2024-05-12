#!/usr/bin/env python3

"""
Integration test module for the GithubOrgClient class in client.py.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized_class
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos
from client import GithubOrgClient


@parameterized_class
(
        ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
        [(org_payload, repos_payload, expected_repos, apache2_repos),]
        )


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test class for the GithubOrgClient class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method.
        Mock requests.get to return example payloads found in the fixtures.
        """
        cls.get_patcher = patch('client.requests.get')

        # Mock the requests.get side effect to return
        # the correct fixtures based on the URL
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = cls.mock_requests_get

    @classmethod
    def tearDownClass(cls):
        """
        Tear down class method.
        Stop the patcher.
        """
        cls.get_patcher.stop()

    @classmethod
    def mock_requests_get(cls, url):
        """
        Mock method for requests.get.
        Returns the appropriate payload based on the URL.
        """
        if 'orgs/example_org' in url:
            return Mock(json=lambda: cls.org_payload)
        elif 'orgs/example_org/repos' in url:
            return Mock(json=lambda: cls.repos_payload)
        else:
            return Mock(json=lambda: [])

    def test_public_repos(self):
        """
        Integration test method for the GithubOrgClient.public_repos property.
        Verifies that public_repos returns the expected list of repos
        based on the mocked payloads.
        """
        # Create a GithubOrgClient instance
        org_client = GithubOrgClient("example_org")

        # Call the public_repos property
        result = org_client.public_repos

        # Check that the result is correct based on the mocked payloads
        self.assertEqual(result, self.expected_repos)

     def test_public_repos_with_license(self):
        """
        Integration test method for the GithubOrgClient.public_repos
        property with a specified license.
        Verifies that public_repos returns the expected list of repos
        with the specified license.
        """
        # Create a GithubOrgClient instance
        org_client = GithubOrgClient("example_org")

        # Call the public_repos property with a specified license
        result = org_client.public_repos(license="apache-2.0")

        # Check that the result is correct based on the mocked
        # apache2_repos fixture
        self.assertEqual(result, self.apache2_repos)



if __name__ == "__main__":
    unittest.main()
