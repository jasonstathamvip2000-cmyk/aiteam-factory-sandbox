import os
import unittest


class TestNotOnGitHubActions(unittest.TestCase):
    def test_controlled_ci_failure(self):
        # Controlled SAFE_AUTO test: passes locally, fails on GitHub Actions on purpose.
        self.assertNotEqual(os.environ.get('GITHUB_ACTIONS'), 'true')
