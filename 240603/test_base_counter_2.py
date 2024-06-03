import pytest

from base_counter import base_count


@pytest.mark.parametrize(
    ("seq", "exp"),
    [("AATC", {"A": 2, "C": 1, "T": 1}), ("ACGTAAA", {"A": 4, "C": 1, "G": 1, "T": 1})],
)
def test_base_count(seq, exp):
    assert base_count(seq) == exp
