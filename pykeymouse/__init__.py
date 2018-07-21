
# Copied from PyAutoGUI for compatibility.
KEY_NAMES = ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
     ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
     '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
     'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
     'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
     'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
     'browserback', 'browserfavorites', 'browserforward', 'browserhome',
     'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
     'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
     'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
     'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
     'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
     'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
     'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
     'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
     'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
     'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
     'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
     'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
     'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
     'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
     'command', 'option', 'optionleft', 'optionright']


class PyKeyMouseException(Exception):
    """PyKeyMouse will always raise this exception for user errors. If
    PyKeyMouse raises an of the built-in error messages, assume that this is
    caused by a bug in PyKeyMouse."""
    pass

# Names and values made to be similar Pygame.
KEY_DOWN          = 2
KEY_UP            = 3
MOUSE_MOTION      = 4
MOUSE_BUTTON_UP   = 5
MOUSE_BUTTON_DOWN = 6

# TODO - how to implement click, double click, and key press? What do we do for getting the doubleclick speed or keyboard repeat speed?

# NOTE: The primary button is the left mouse button and the secondary button is
# the right mouse button, unless the OS has swapped them for left-handed users.
PRIMARY_BUTTON     = BUTTON_1 = 1
MIDDLE_BUTTON      = BUTTON_2 = 2
SECONDARY_BUTTON   = BUTTON_3 = 3
SCROLL_UP_BUTTON   = BUTTON_4 = 4
SCROLL_DOWN_BUTTON = BUTTON_5 = 5


EVENT_ENUM_TO_NAME_MAP = {2: 'KEY_DOWN',
                          3: 'KEY_UP',
                          4: 'MOUSE_MOTION',
                          5: 'MOUSE_BUTTON_UP',
                          6: 'MOUSE_BUTTON_DOWN'}

class Event(object):
    def __init__(self, type, key=None, mod=None, pos=None, rel=None, buttons=None, button=None):
        self.type = type # Yes, type is a built-in name, but this is to keep compatibility with Pygame's conventions.

        if type in (KEY_DOWN, KEY_UP):
            if key is None:
                raise PyKeyMouseException('the key parameter is required for KEY_DOWN & KEY_UP events')
            self.key = key
            self.mod = mod
        elif type == MOUSE_MOTION:
            if pos is None or rel is None or buttons is None:
                raise PyKeyMouseException('the pos, rel, and buttons parameters are required for MOUSE_MOTION events')
            self.pos = pos
            self.rel = rel
            self.buttons = buttons
        elif type in (MOUSE_BUTTON_UP, MOUSE_BUTTON_DOWN):
            if pos is None or button is None:
                raise PyKeyMouseException('the pos and button parameters are required for MOUSE_BUTTON_UP/MOUSE_BUTTON_DOWN events')
            self.pos = pos
            self.button = button
        else:
            raise PyKeyMouseException('the type argument must be one of KEY_DOWN, KEY_UP, MOUSE_MOTION, MOUSE_BUTTON_UP, or MOUSE_BUTTON_DOWN')

    def __str__(self):
        if self.type in (KEY_DOWN, KEY_UP):
            return '<%s key=%s mod=%s>' % (EVENT_ENUM_TO_NAME_MAP[self.type], self.key, self.mod)
        elif type == MOUSE_MOTION:
            return '<MOUSE_MOTION pos=%s, rel=%s, buttons=%s>' % (self.pos, self.rel, self.buttons)
        elif type in (MOUSE_BUTTON_UP, MOUSE_BUTTON_DOWN):
            return '<%s pos=%s, button=%s>' % (EVENT_ENUM_TO_NAME_MAP[self.type], self.pos, self.button)

    def __repr__(self):
        if self.type in (KEY_DOWN, KEY_UP):
            return 'Event(type=%s, key=%s mod=%s)' % (self.type, repr(self.key), repr(self.mod))
        elif type == MOUSE_MOTION:
            return 'Event(type=%s, pos=%s, rel=%s, buttons=%s)' % (self.type, self.pos, self.rel, self.buttons)
        elif type in (MOUSE_BUTTON_UP, MOUSE_BUTTON_DOWN):
            return 'Event(type=%s, pos=%s, button=%s)' % (self.type, self.pos, self.button)

# These lists contain callback functions. They are called in order
keyDownListeners = []
keyUpListeners = []
mouseMotionListeners = []
mouseButtonUpListeners = []
mouseBUttonDownListeners = []

# TODO: How do we add the clickListeners and pressListeners aliases?

def onKeyDown(callbackFunc):
    """Sets callbackFunc as the sole key down event handler. This function is passed two arguments: key and mod."""
    global keyDownListeners
    keyDownListeners.clear()
    keyDownListeners.append(callbackFunc)

def onKeyUp(callbackFunc):
    """Sets callbackFunc as the sole key up event handler. This function is passed two arguments: key and mod."""
    global keyUpListeners
    keyUpListeners.clear()
    keyUpListeners.append(callbackFunc)

def onMouseMotion(callbackFunc):
    """Sets callbackFunc as the sole mouse motion event handler. This function is passed three arguments: pos, rel, and buttons."""
    global mouseMotionListeners
    mouseMotionListeners.clear()
    mouseMotionListeners.append(callbackFunc)

def onMouseButtonUp(callbackFunc):
    """Sets callbackFunc as the sole mouse button up event handler. This function is passed two arguments: pos and button."""
    global mouseButtonUpListeners
    mouseButtonUpListeners.clear()
    mouseButtonUpListeners.append(callbackFunc)

def onMouseButtonDown(callbackFunc):
    """Sets callbackFunc as the sole mouse button down event handler. This function is passed two arguments: pos and button."""
    global mouseButtonDownListeners
    mouseButtonDownListeners.clear()
    mouseButtonDownListeners.append(callbackFunc)

def listenFor(eventDescription, callbackFunc):
    pass

def _startListeningThread():
    """Called the first time an "on event" functon is called or a listener is added to one of the listeners lists."""
    pass