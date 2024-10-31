# What are best practices for exception handling in Python and avoiding "catching too general exception"?

I write lots of batch processing code that looks something like the following:

```Python
while not work_queue.empty():
    work_item = work_queue.get()
    try:
        do_something(work_item)
    except Exception as e:
        logging.error(f"Error processing {work_item}: {e}")
    finally:
        cleanup()
```

This gives me linter warnings, "Catching too general exception Exception (W0718:broad-exception-caught)".

For sure, the linter has a good point. There are errors for which logging and continuing is a bad choice. If the machine is out of memory, for example, we should let the exception propogate upward and terminate the program.

In general, I don't know what exceptions, even custom exceptions, might be thrown from down in the guts of third party libraries. Most likely, an error means a work item has failed. Usually, the best course of action is to log the error and keep going. But, if every work item is going to fail, I want to stop.

Based on experience, you might try to classify exceptions as recoverable or not and end up with something like this:

```Python
while not work_queue.empty():
    work_item = work_queue.get()
    try:
        do_something(work_item)
    except (MemoryError, ImportError, AuthorizationError) as critical_error:
        logging.critical(f"Critical error: {critical_error}")
        raise
    except Exception as e:  # noqa: W0718
        logging.error(f"Error processing {work_item}: {e}")
    finally:
        cleanup()
```

It would be nice if the exception hierarchy gave us a little more help. But, the criticality of a given exception is very specific to the application. A recoverable error in one situation is a fatal error in another.

Pragmatically, if every work item is going to fail, I want to stop. Maybe seeing k errors in a row is a sign we should stop.


