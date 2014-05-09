__author__ = 'harrigan'

from . import mcmd


class WriteDirectoryListing(mcmd.Parsable):
    """List files and write them in a directory.

    :param out_fn: Where to write the file
    :param glob_str: How to glob files
    :param limit: Max number of files or -1 for all

    """

    def __init__(self, out_fn, glob_str='sample/*.txt', limit=-1):
        pass

    def main(self):
        pass


class WriteOnlyPart(WriteDirectoryListing):
    """Write only filename or dirname."""

    def __init__(self, super_args, which='dirname'):
        pass


def parse():
    pass


if __name__ == "__main__":
    parse()