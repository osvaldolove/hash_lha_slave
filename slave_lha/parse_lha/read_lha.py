import os
import sys
import hashlib
import lhafile


class LhaSlaveArchive:
    def __init__(self, archive_path, hash_algorithm='SHA1'):
        self.original_path = archive_path
        self.hasher = self._get_hasher(hash_algorithm)
        self.absolute_path = os.path.abspath(self.original_path)
        print(self.absolute_path)
        self.lha_file = lhafile.lhafile.Lhafile(self.absolute_path)
        self.slave_file_name = None
        self.slave_file_data = None
        self.hash_digest = None

    def read_lha(self):
        archive = lhafile.lhafile.Lhafile(self.absolute_path)
        for file in archive.filelist:
            if str(file.filename).endswith('.slave'):
                self.slave_file_name = file.filename
                self.slave_file_data = archive.read(file.filename)
                return

    def get_hash(self):
        if self.slave_file_data:
            self.hasher()
        else:
            raise ValueError('No slave data to hash')

    def _get_hasher(self, hash_algorithm: str):
        if hash_algorithm is None or hash_algorithm.upper == 'SHA1':
            return self._sha1_checksum

        return self._md5_checksum

    def _sha1_checksum(self):
        sha1_hash = hashlib.sha1()
        sha1_hash.update(self.slave_file_data)
        self.hash_digest = sha1_hash.hexdigest()

    def _md5_checksum(self):
        md5_hash = hashlib.md5()
        md5_hash.update(self.slave_file_data)
        self.hash_digest = md5_hash.hexdigest()


# if __name__ == '__main__':
#     CWD = os.path.dirname(__file__)
#     FILE = os.path.join(CWD, 'test_data', 'Alcatraz.lha')
#     LHA_SLAVE = LhaSlaveArchive(archive_path=FILE)
#     LHA_SLAVE.read_lha()
#     LHA_SLAVE.get_hash()
