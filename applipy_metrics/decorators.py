import functools

from . import global_registry


def get_qualname(obj):
    return obj.__qualname__


def count_calls(original_func=None, metric_name=None, registry=None, tags=None):
    """
    Decorator to track the number of times a function is called.

    :param original_func: the function to be decorated
    :type original_func: C{func}

    :param registry: the registry in which to create the meter

    :param tags: tags attached to the timer (e.g. {'region': 'us-west-1'})
    :type tags: C{dict}

    :return: the decorated function
    :rtype: C{func}
    """

    def _decorate(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            function_name = get_qualname(fn)
            name = metric_name or "%s.count_calls" % function_name

            _registry = registry or global_registry()
            _registry.counter(name, tags).inc()

            return fn(*args, **kwargs)

        return wrapper

    if original_func:
        return _decorate(original_func)

    return _decorate


def meter_calls(original_func=None, metric_name=None, registry=None, tags=None):
    """
    Decorator to the rate at which a function is called.

    :param original_func: the function to be decorated
    :type original_func: C{func}

    :param registry: the registry in which to create the meter

    :param tags: tags attached to the timer (e.g. {'region': 'us-west-1'})
    :type tags: C{dict}

    :return: the decorated function
    :rtype: C{func}
    """

    def _decorate(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            function_name = get_qualname(fn)
            name = metric_name or "%s.meter_calls" % function_name

            _registry = registry or global_registry()
            _registry.meter(name, tags).mark()

            return fn(*args, **kwargs)

        return wrapper

    if original_func:
        return _decorate(original_func)

    return _decorate


def hist_calls(original_func=None, metric_name=None, registry=None, tags=None):
    """
    Decorator to check the distribution of return values of a function.

    :param original_func: the function to be decorated
    :type original_func: C{func}

    :param registry: the registry in which to create the histogram

    :param tags: tags attached to the timer (e.g. {'region': 'us-west-1'})
    :type tags: C{dict}

    :return: the decorated function
    :rtype: C{func}
    """
    def _decorate(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            function_name = get_qualname(fn)
            name = metric_name or "%s.hist_calls" % function_name

            _registry = registry or global_registry()

            rtn = fn(*args, **kwargs)
            if type(rtn) in (int, float):
                _registry.histogram(name, tags).update(rtn)
            return rtn

        return wrapper

    if original_func:
        return _decorate(original_func)

    return _decorate


def hist_async_calls(original_func=None, metric_name=None, registry=None, tags=None):
    """
    Decorator to check the distribution of return values of a function.

    :param original_func: the function to be decorated
    :type original_func: C{func}

    :param registry: the registry in which to create the histogram

    :param tags: tags attached to the timer (e.g. {'region': 'us-west-1'})
    :type tags: C{dict}

    :return: the decorated function
    :rtype: C{func}
    """
    def _decorate(fn):
        @functools.wraps(fn)
        async def wrapper(*args, **kwargs):
            function_name = get_qualname(fn)
            name = metric_name or "%s.hist_async_calls" % function_name

            _registry = registry or global_registry()

            rtn = await fn(*args, **kwargs)
            if type(rtn) in (int, float):
                _registry.histogram(name, tags).update(rtn)
            return rtn

        return wrapper

    if original_func:
        return _decorate(original_func)

    return _decorate


def time_calls(original_func=None, metric_name=None, registry=None, tags=None):
    """
    Decorator to time the execution of the function.

    :param original_func: the function to be decorated
    :type original_func: C{func}

    :param registry: the registry in which to create the timer

    :param tags: tags attached to the timer (e.g. {'region': 'us-west-1'})
    :type tags: C{dict}

    :return: the decorated function
    :rtype: C{func}
    """
    def _decorate(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            function_name = get_qualname(fn)
            name = metric_name or "%s.time_calls" % function_name

            _registry = registry or global_registry()
            _timer = _registry.timer(name, tags)

            with _timer.time():
                return fn(*args, **kwargs)

        return wrapper

    if original_func:
        return _decorate(original_func)

    return _decorate


def time_async_calls(original_func=None, metric_name=None, registry=None, tags=None):
    """
    Decorator to time the execution of the function.

    :param original_func: the function to be decorated
    :type original_func: C{func}

    :param registry: the registry in which to create the timer

    :param tags: tags attached to the timer (e.g. {'region': 'us-west-1'})
    :type tags: C{dict}

    :return: the decorated function
    :rtype: C{func}
    """
    def _decorate(fn):
        @functools.wraps(fn)
        async def wrapper(*args, **kwargs):
            function_name = get_qualname(fn)
            name = metric_name or "%s.time_async_calls" % function_name

            _registry = registry or global_registry()
            _timer = _registry.timer(name, tags)

            with _timer.time():
                return await fn(*args, **kwargs)

        return wrapper

    if original_func:
        return _decorate(original_func)

    return _decorate
