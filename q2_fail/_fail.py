import time

import biom


def task_fail(table: biom.Table, fail: bool = True) -> biom.Table:
    """task_fail.

    Parameters
    ----------
    table : biom.Table
        table
    fail : bool
        fail

    Returns
    -------
    biom.Table

    """
    if fail:
        raise ValueError("This plugin is meant to fail. Please use another plugin.")
    else:
        return table


def memory_fail(table: biom.Table, delay: float = 0.1) -> biom.Table:
    """memory_fail.

    Parameters
    ----------
    table : biom.Table
        table
    delay : float
        delay

    Returns
    -------
    biom.Table

    """
    memory_hog = []
    try:
        while True:
            memory_hog.append("x" * 1024 * 1024)
            time.sleep(delay)
    except MemoryError:
        print("Memory exhausted!")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return table
