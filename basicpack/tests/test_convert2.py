"""Tests for `basicpack` package."""
import pytest
from basicpack import basicpack


def test_convert(capsys):
    """Correct name argument prints"""
    basicpack.convert("rimo")
    captured = capsys.readouterr()
    assert "rimo" in captured.out
