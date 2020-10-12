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


def test_counter_dec():
    counter = Counter('test')

    assert counter.get_count() == 0

    counter.dec()

    assert counter.get_count() == -1

    counter.dec()
    counter.dec()

    assert counter.get_count() == -3

    counter.dec(7)

    assert counter.get_count() == -10

    counter.dec(-4)

    assert counter.get_count() == -6


def test_counter_clear():
    counter = Counter('test')

    assert counter.get_count() == 0

    counter.inc(15)

    assert counter.get_count() == 15

    counter.clear()

    assert counter.get_count() == 0
