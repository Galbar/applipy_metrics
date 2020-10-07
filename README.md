# Applipy Metrics

    pip install applipy_metrics@git+ssh://git@gitlab.com/Galbar2/applipy.git@<VERSION>#subdirectory=applipy_metrics



> Note: This is a hard fork of
> [Lightricks/PyFormance](https://github.com/Lightricks/pyformance) at commit
> [`d59501e`](https://github.com/Lightricks/pyformance/commit/d59501ec06299b6af3b758f0ba9ce3f57bf6c73d)

A Python port of the core portion of a [Java Metrics library by Coda Hale](http://metrics.dropwizard.io/), with inspiration by [YUNOMI - Y U NO MEASURE IT?](https://github.com/richzeng/yunomi)

Applipy Metrics is a toolset for performance measurement and statistics, with a signaling mechanism that allows to issue events in cases of unexpected behavior

## Core Features

### Gauge
A gauge metric is an instantaneous reading of a particular value.

### Counter
Simple interface to increment and decrement a value. For example, this can be used to measure the total number of jobs sent to the queue, as well as the pending (not yet complete) number of jobs in the queue. Simply increment the counter when an operation starts and decrement it when it completes.

### Summary
Measures the statistical distribution of values in a data stream. Keeps track of minimum, maximum, mean, standard deviation, etc. It also measures median, 75th, 90th, 95th, 98th, 99th, and 99.9th percentiles. An example use case would be for looking at the number of daily logins for 99 percent of your days, ignoring outliers.

### Regex Grouping
Useful when working with APIs. A RegexRegistry allows to group API calls and measure from a single location instead of having to define different timers in different places.

    >>> from applipy_metrics.registry import RegexRegistry
    >>> reg = RegexRegistry(pattern='^/api/(?P<model>)/\d+/(?P<verb>)?$')
    >>> def rest_api_request(path):
    ...     with reg.timer(path).time():
    ...         # do stuff
    >>> print reg.dump_metrics()

## Examples

### Decorators
The simplest and easiest way to use the Applipy Metrics library.

##### Counter
You can use the 'count_calls' decorator to count the number of times a function is called.

    >>> from applipy_metrics import counter, count_calls
    >>> @count_calls
    ... def test():
    ...     pass
    ... 
    >>> for i in range(10):
    ...     test()
    ... 
    >>> print counter("test_calls").get_count()
    10

##### Timer
You can use the 'time_calls' decorator to time the execution of a function and get distribution data from it.

    >>> import time
    >>> from applipy_metrics import summary, time_calls
    >>> @time_calls
    ... def test():
    ...     time.sleep(0.1)
    ... 
    >>> for i in range(10):
    ...     test()
    ... 
    >>> print summary("test_calls").get_snapshot().get_mean()
    0.100820207596

### With statement
You can also use a timer using the with statement
##### Chronometer

    >>> import time
    >>> from applipy_metrics import summary, Chronometer
    >>> with Chronometer(on_stop=lambda x: summary("test").add(x)):
    ...    time.sleep(0.1)
    >>> print summary("test").get_snapshot().get_mean()
    0.10114598274230957
