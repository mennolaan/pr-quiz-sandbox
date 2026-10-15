def greet(name, shout=False):
    if not name:
        text = "Hello, stranger"
    else:
        text = f"Hello, {name.strip()}"
    return text.upper() + "!" if shout else text
