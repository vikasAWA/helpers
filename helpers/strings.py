def clean_multiline(text: str) -> str:
    lines = text.split('\n')
    while lines and lines[0] == '': lines.pop(0)
    while lines and lines[-1] == '': lines.pop()
    min_indent = min(len(l) - len(l.lstrip()) for l in lines if l.strip())
    return '\n'.join(l[min_indent:] for l in lines)

if __name__ == "__main__":
    t2 = """
        hello
            world
        foo
    """

    print(clean_multiline(t2))

