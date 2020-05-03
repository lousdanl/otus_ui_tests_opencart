from contextlib import contextmanager


@contextmanager
def context_manager_for_read_file(path_read):
    try:
        file_open = open(path_read, 'r')
        yield file_open
    except OSError:
        print('File not found or unavailable')
    finally:
        file_open.close()


@contextmanager
def context_manager_for_correction_file(path_write):
    try:
        file_open = open(path_write, 'w')
        yield file_open
    except OSError:
        print('File not found or unavailable')
    finally:
        file_open.close()
