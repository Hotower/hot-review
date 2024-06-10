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

def formatListPrint(printList, indent = 4, sep = (",\n", "\n"), initIndent = 0, end = 1):
    ret = " "*initIndent + "[" + sep[1]
    for subList in printList:
        if type(subList) == list:
            ret = ret + formatListPrint(subList, indent = indent, sep = sep, initIndent = initIndent + indent, end = printList.index(subList) == len(printList) - 1)
        else:
            if type(subList) == str:
                ret = ret + " "*(initIndent + indent) + "\"" + subList + "\"" + sep[printList.index(subList) == len(printList) - 1]
            else:
                ret = ret + " "*(initIndent + indent) + str(subList) + sep[printList.index(subList) == len(printList) - 1]
    ret = ret + " "*initIndent + "]" + sep[end]
    return ret

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

    print(formatListPrint([[["aaa", 2, 3], [4, 5]], [6, 7, 8],  9]))

    print("--- test end ---")