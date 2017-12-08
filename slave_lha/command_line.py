import sys
import lhafile
from .parse_lha.read_lha import LhaSlaveArchive


def main():
    if len(sys.argv) == 1:
        print("No file specified")
        sys.exit(1)
    if len(sys.argv) > 3:
        print("Too many arguments passed")

    archive_path = sys.argv[1]

    try:
        hash_algorithm = sys.argv[2]
    except IndexError:
        hash_algorithm = 'SHA1'

    try:
        slave_archive = LhaSlaveArchive(archive_path, hash_algorithm)
    except FileNotFoundError:
        print("Could not find LHA archive: {}".format(archive_path))
        sys.exit(1)
    except lhafile.BadLhafile:
        print("Could not read LHA archive: {}".format(archive_path))
        sys.exit(1)

    slave_archive.read_lha()
    for slave in slave_archive.slaves:
        slave.get_hash()
        print('Slave File: {}'.format(slave.name))
        print('Slave Hash: {}'.format(slave.hash_digest))
        print('')
