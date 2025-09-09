from pip import main
from importlib.metadata import distributions
installed_packages = [dist.metadata['Name'] for dist in distributions()]
normal_import = __builtins__.__import__

def install(name, globals=None, locals=None, fromlist=(), level=0):
	__builtins__.__import__ = normal_import
	if name not in installed_packages:
		main(['install', '-U', name])
	name = normal_import(name, globals, locals, fromlist, level)
	__builtins__.__import__ = install
	return name

__builtins__.__import__ = install
