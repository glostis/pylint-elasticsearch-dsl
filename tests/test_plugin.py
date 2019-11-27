# pylint: disable=redefined-outer-name, missing-docstring
import os
import subprocess

import pytest


@pytest.fixture()
def script_to_lint():
    here = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(here, "data", "script_to_lint.py")


def test_lint_without_plugin(script_to_lint):
    process = subprocess.run(["pylint", script_to_lint], capture_output=True, check=False)
    assert process.returncode == 2
    output = process.stdout.decode("utf-8")
    assert "invalid-unary-operand-type" in output


def test_lint_with_plugin(script_to_lint):
    process = subprocess.run(
        ["pylint", "--load-plugins", "pylint_elasticsearch_dsl", script_to_lint],
        capture_output=True,
        check=False,
    )
    assert process.returncode == 0
