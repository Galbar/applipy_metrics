from applipy_metrics.meters import Counter


def test_counter_inc():
    counter = Counter('test')

    assert counter.get_count() == 0

    counter.inc()

    assert counter.get_count() == 1

    counter.inc()
    counter.inc()

    assert counter.get_count() == 3

    counter.inc(7)

    assert counter.get_count() == 10

    counter.inc(-4)

    assert counter.get_count() == 6
