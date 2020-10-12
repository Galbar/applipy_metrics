from applipy_metrics.meters import SimpleGauge

def test_simple_gauge():
    gauge = SimpleGauge('test', 0)

    assert gauge.get_value() == 0

    gauge.set_value(5)

    assert gauge.get_value() == 5

    gauge.set_value(-10)

    assert gauge.get_value() == -10

    gauge.set_value(15)

    assert gauge.get_value() == 15
