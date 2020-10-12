from applipy_metrics.meters import Summary


def test_summary():
    summary = Summary('test')

    assert summary.get_count() == 0
    assert summary.get_sum() == 0

    summary.add(15)

    assert summary.get_count() == 1
    assert summary.get_sum() == 15

    summary.add(1)

    assert summary.get_count() == 2
    assert summary.get_sum() == 16

    summary.add(-56)

    assert summary.get_count() == 3
    assert summary.get_sum() == -40
