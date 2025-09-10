# ModuleNotFound? Cast a Magic Spell on the "Import" Command!
[🎬 Demo](https://github.com/Magic-Abracadabra/magic-import/blob/main/Demo.mp4)

A brief way to use your codes. Just copy the source code to start with.
```python
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


# start coding from here
```
Now, the python keyword "import" has been in a magic spell. Modules of the latest version can be installed before your following imports.

# For example:

If you don't have the numpy,
```python
import numpy as np
```
will install it first, and then this module will be successfully imported. Yeah, that easy.

After importing one package, the following libraries will work, too:
```python
import pyaudio, pymovie, pyautogui, ...
```
