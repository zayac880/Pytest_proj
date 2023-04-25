import utils.arrs as arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], -1, "test") == "test"
    assert arrs.get([1, 2, 3], 4, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4]
    assert arrs.my_slice([1, 2, 3, 4, 5], 1) == [2, 3, 4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5], -3) == [3, 4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5], -3, -1) == [3, 4]


def test_slice_empty():
    assert arrs.my_slice([]) == []


def test_slice_negative_start_beyond():
    assert arrs.my_slice([1, 2, 3], -4, 1) == [1]


def test_slice_negative_start_before():
    assert arrs.my_slice([1, 2, 3], -2, 3) == [2, 3]


def test_slice_negative_end_beyond():
    assert arrs.my_slice([1, 2, 3], 1, -4) == []


def test_slice_negative_end_before():
    assert arrs.my_slice([1, 2, 3], 1, -1) == [2]
