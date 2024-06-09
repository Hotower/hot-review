def clearScreen():
    print('\033[2J\033[H', end='')

def getCh():
    def _GetchUnix():
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    def _GetchWindows():
        import msvcrt
        return msvcrt.getch()

    try:
        impl = _GetchWindows()
    except ImportError:
        impl = _GetchUnix()
    return impl.decode()

if __name__ == "__main__":
    clearScreen()
    print("--- test start ---")

    '''getCh() func test
    print("input 'o' to continue...", end = "")
    a = getCh()
    while a != "o":
        print(f"\n{a} received, 'o' required to continue",end = "")
        a = getCh()
    print("\n")
    '''

    print("--- test end ---")