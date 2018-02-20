import os
import time
import hashlib
import subprocess as sp
from tempfile import mkstemp
from globals import APP_PATH

__all__ = [
	'getpath',
	'timestamp',
	'minzero',
	'ispdf',
	'scanpdfs',
	'filext',
	'iscsv',
	'isexe',
	'isfile',
	'isdir',
	'dirname',
	'basename',
	'pathjoin',
	'rmfile',
	'run_cmd',
	'tmpfile',
	'has_cmd',
	'getext',
	'isxml',
	'executable',
	'oneline'
]

isfile = os.path.isfile
isdir = os.path.isdir
dirname = os.path.dirname
basename = os.path.basename
pathjoin = os.path.join
rmfile = os.remove


def getpath(path, *subpath):
	if os.path.isabs(path):
		return os.path.join(path, *subpath)
	return os.path.join(APP_PATH, path, *subpath)


def minzero(number):
	return 0 if number < 0 else number


def timestamp(fmt=None):
	return time.strftime(fmt) if fmt else time.time()


def filext(path):
	try:
		file = os.path.basename(path)
		return file.rsplit('.', maxsplit=1)[1]
	except IndexError:
		return ''


def ispdf(path):
	return os.path.isfile(path) and filext(path).lower() == 'pdf'


def iscsv(path):
	return os.path.isfile(path) and filext(path).lower() == 'csv'


def isxml(path):
	return os.path.isfile(path) and filext(path).lower() == 'xml'


def isexe(path):
	return os.path.isfile(path) and os.access(path, os.X_OK)


executable = isexe


def scanpdfs(path):
	for entry in os.scandir(path):
		if ispdf(entry.path):
			yield entry.path


def run_cmd(cmd):
	out = sp.run(cmd.split(), stdout=sp.DEVNULL, stderr=sp.DEVNULL)
	return out.returncode == 0


def tmpfile(**kwargs):
	_, path = mkstemp(**kwargs)
	return path


def has_cmd(name):
	return run_cmd('which %s' % name)


def getext(tag):
	assert hasattr(tag, 'getchildren') and hasattr(tag, 'text')
	ret = ''
	if tag.text:
		ret += tag.text
	childs = tag.getchildren()
	if childs:
		for child in childs:
			txt = getext(child)
			if txt:
				ret += txt
	return ret


def oneline(text, linesep=None, newlinesep=None, spacefix=True, strip=True):
	linesep = linesep or '\n'
	newlinesep = newlinesep or ' '
	ret = text.replace(linesep, newlinesep)
	if spacefix:
		ret = ' '.join(ret.split())
	if strip:
		ret = ret.strip()
	return ret


def md5hash(value):
	value = str(value)
	hashobj = hashlib.md5(value.encode())
	return hashobj.hexdigest()
