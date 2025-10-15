# 解决ModuleNotFound的入门级自动化办法——自动搞定环境配置

![1](https://github.com/user-attachments/assets/82381d1c-5056-42e5-bd38-ae58aca8f354)

---

<img width="841" height="800" alt="2" src="https://github.com/user-attachments/assets/894b46af-82d5-45a5-b5cd-e12d63dd60da" />

---

<img width="1200" height="637" alt="3" src="https://github.com/user-attachments/assets/5adc9bce-6478-43ba-868a-59823184c437" />

---

<img width="1200" height="687" alt="4" src="https://github.com/user-attachments/assets/1826d45b-46d7-4a1d-9212-3099cb5f995c" />

---

<img width="1200" height="560" alt="5" src="https://github.com/user-attachments/assets/252ae135-16b8-4cd9-88eb-2cabd69b0ce0" />

---

![6](https://github.com/user-attachments/assets/f60746d4-2210-44ee-afa9-7f5f9c754708)

---
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
After running this block, the python keyword ✨import✨ has been in a magic spell. Modules of the latest version can be installed before your following imports.

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
