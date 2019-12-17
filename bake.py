#!/bin/python

import os
import zipfile


def main():
    path = os.path.abspath(os.path.curdir)
    import shutil
    shutil.make_archive('converge-' + path.split('/')[-1], 'zip', path)


if __name__ == "__main__":
    main()
