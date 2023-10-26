#!/usr/bin/env python

"""Tests for `prime_jl6530` package."""


import unittest
from click.testing import CliRunner

from prime_jl6530 import prime_jl6530
from prime_jl6530 import cli


class TestPrime_jl6530(unittest.TestCase):
    """Tests for `prime_jl6530` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'prime_jl6530.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
