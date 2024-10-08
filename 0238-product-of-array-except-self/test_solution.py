import pytest

from source import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [([1, 2, 3, 4], [24, 12, 8, 6]), ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0])],
)
def test_solution_correctness(nums: list[int], expected: list[int]) -> None:
    assert Solution().productExceptSelf(nums) == expected
