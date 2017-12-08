import sys
import lhafile
import colorama
from .parse_lha.read_lha import LhaSlaveArchive

colorama.init(autoreset=True)


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
        print(colorama.Fore.RED +
              "Could not find LHA archive: {}".format(archive_path))
        sys.exit(1)
    except lhafile.BadLhafile:
        print(colorama.Fore.RED +
              "Could not read LHA archive: {}".format(archive_path))
        sys.exit(1)

    print(colorama.Fore.GREEN + slave_archive.absolute_path)
    slave_archive.read_lha()
    for slave in slave_archive.slaves:
        slave.get_hash()
        print(colorama.Fore.YELLOW + 'Slave Name: ', end='')
        print(slave.name)
        print(
            colorama.Fore.YELLOW +
            "{} Hash: ".format(slave.hasher.name.upper()),
            end='')
        print(slave.hash_digest)
