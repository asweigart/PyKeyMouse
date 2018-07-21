# PyKeyMouse
A simple, cross-platform Python 2/3 module to detect mouse and keyboard input.

**NOTE: THIS MODULE IS UNDER CONSTRUCTION AND NOT YET WORKING.**

# Installation

    pip install pykeymouse

# Example Usage

Getting all the events that have happened since the last call to `pykeymouse.get()`:

    >>> import pykeymouse
    >>> events = pykeymouse.get()
    >>> events
    ['<KEY_DOWN key=H mod=None>', '<KEY_DOWN key=H mod=None>']

Setting up a callback function for all key press events:

    >>> import pykeymouse
    >>> myKeyDownCallback = lambda key, mod: print('%s key pressed down' % key)
    >>> pykeymouse.onKeyDown(myKeyDownCallback)

Setting up a callback function when Ctrl+Q or Shift+Right Click happens:

    >>> import pykeymouse
    >>> myCallback = lambda key, mod: print('Ctrl+Q was pressed.')
    >>> pykeymouse.listenFor('ctrl+q', myKeyDownCallback)
    >>> myOtherCallback = lambda pos, button: print('Shift click happened.')
    >>> pykeymouse.listenFor('shift+rightclick', myOtherCallback)

