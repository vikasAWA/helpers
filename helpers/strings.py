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

def replace_many(text: str, mapping:dict) -> str:
    """Replace multiple substrings in text using a mapping.

    Longer keys take priority over shorter ones, so 'hello' will
    match before 'he' if both are in the mapping.

    Args:
        text: The input string to process.
        mapping: A dict of {old: new} replacements.

    Returns:
        A new string with all replacements applied.

    Example:
        >>> replace_many("hello world", {"hello": "hi", "world": "earth"})
        'hi earth'
    """
    res = []
    i = 0
    sorted_keys =  sorted(mapping, key=len, reverse=True)
    while i < len(text):
        replaced = False
        for key in sorted_keys:
            if text.startswith(key, i):
                res.append(mapping[key])
                i += len(key)
                replaced = True
                break 
        if not replaced:
            res.append(text[i])
            i += 1
    return "".join(res)
if __name__ == "__main__":
    t2 = """
        hello
            world
        foo
    """

    print(clean_multiline(t2))
    mapping = {"he": "SHE", "hello": "HI"}
    print(replace_many("hello", mapping))

