import logging
logging.basicConfig(level=logging.INFO)

print('Hello, World\!')

def greet(name):
    return f"Hello, {name}!"

print(greet("World"))

def greet(name):
    logging.info(f"Greeting {name}")
    return f"Hello, {name}!"