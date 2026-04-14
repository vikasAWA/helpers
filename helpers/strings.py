def clean_multiline(text: str) -> str:
    """
    Remove common indentation from multiline strings.
    Keeps relative indentation intact.
    """

    lines = text.split('\n')
    while lines and lines[0] == '': lines.pop(0)
    while lines and lines[-1] == '': lines.pop()
    min_indent = min(len(l) - len(l.lstrip()) for l in lines if l.strip())
    return '\n'.join(l[min_indent:] for l in lines)

def is_int(s: str) -> bool:
    """
    Check if input represents an integer.
    Handles strings with spaces and +/- signs.
    Returns True for int type as well.
    """

    try: int(s); return True
    except ValueError: return False

if __name__ == "__main__":
    t2 = """
        hello
            world
        foo
    """

    print(clean_multiline(t2))

