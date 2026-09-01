import sys
import contextlib
import builtins

#removed the "except AttributeError" bit as it could hide errors?
@contextlib.contextmanager
def open(filename: str, mode: str = 'r', *args, **kwargs):
    if filename == '-':
        if 'r' in mode:
            stream = sys.stdin
        else:
            stream = sys.stdout
        if 'b' in mode:
            fh = stream.buffer
        else:
            fh = stream
        close = False
    else:
        fh = builtins.open(filename, mode, *args, **kwargs)
        close = True

    try:
        yield fh
    finally:
        if close:
            fh.close()
