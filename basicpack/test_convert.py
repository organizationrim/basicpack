"""Tests for `basicpack` package."""
import pytest
from basicpack import basicpack


def test_convert(capsys):
    """Correct my_name argument prints"""
    basicpack.convert("rim")
    captured = capsys.readouterr()
    assert "rim" in captured.out