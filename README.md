
![1](https://github.com/user-attachments/assets/d97396b8-331a-4786-8336-739aaf4cedb8)
<img width="1200" height="560" alt="5" src="https://github.com/user-attachments/assets/e5aede02-95e4-4c9d-b8ea-745ba462b276" />
<img width="1200" height="687" alt="4" src="https://github.com/user-attachments/assets/1b6d8f98-4651-46c6-aaba-d0f009473686" />
<img width="1200" height="637" alt="3" src="https://github.com/user-attachments/assets/5e66a87f-a347-426d-90c3-513ad609028a" />
<img width="841" height="800" alt="2" src="https://github.com/user-attachments/assets/2d3bd03a-9116-49f5-a452-3ffc6afcab0e" />
![6](https://github.com/user-attachments/assets/2910f9d0-9e77-4b6e-94ac-d725a72f2b3f)




# ModuleNotFound? Cast a Magic Spell on the ✨Import✨ Command!
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
Now, the python keyword ✨import✨ has been in a magic spell. Modules of the latest version can be installed before your following imports.

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
