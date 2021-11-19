import pathlib


def get_dir():
    return pathlib.Path().absolute()


def get_test_file():
    return pathlib.Path().joinpath(get_dir(), '9.webp').absolute()
