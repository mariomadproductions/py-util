import sys
import contextlib
import builtins

@contextlib.contextmanager
def open(file, mode, *args, **kwargs):
    if file == '-':
        if mode is None or mode == '' or 'r' in mode:
            fh = sys.stdin
        else:
            fh = sys.stdout
    else:
        fh = builtins.open(file, mode, *args, **kwargs)
    try:
        yield fh
    finally:
        if file != '-':
            fh.close()
