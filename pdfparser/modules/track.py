import pickle
from helpers import isdir, isfile, pathjoin, md5hash, rmfile
from globals import TRACK_FILE_NAME


class Tracker:

    def __init__(self, path, output):
        if not isdir(path):
            raise NotADirectoryError('Not a directory or not found: \'%s\'' % path)
        self.data = None
        self.dir = path
        self.file = pathjoin(path, TRACK_FILE_NAME)
        self._newout = output
        self._oldout = None
        self.__load()

    def __load(self):
        if isfile(self.file):
            with open(self.file, 'rb') as fp:
                self.data = pickle.load(fp)
                if 'items' not in self.data or 'file' not in self.data:
                    raise FileExistsError(
                        'Could not resume due to corrupted track file, please remove the file and try again: %s' % self.file)
                if not isfile(self.data['file']):
                    raise FileNotFoundError('Previous output file is missing, unable to resume: %s' % self.data['file'])
                self._oldout = self.data['file']
        else:
            self.data = {'items': set(), 'file': self._newout}

    @property
    def output(self):
        return self._oldout or self._newout

    def save(self):
        with open(self.file, 'wb') as fp:
            pickle.dump(self.data, fp)

    def has_data(self):
        return self.data is not None and len(self.data['items']) > 0

    def found(self, item):
        return md5hash(item) in self.data['items']

    def add(self, item):
        assert self.data is not None
        self.data['items'].add(md5hash(item))

    def reset(self):
        self.data = {'items': set(), 'file': self._newout}
        self.save()

    def cleanup(self):
        if isfile(self.file):
            rmfile(self.file)
