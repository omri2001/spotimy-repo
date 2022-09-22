import app_interaction_texts
from functools import wraps

def handle_invalid_input(func):
    @wraps(func)
    def wrapper(self, *args):
        bools = True
        while bools:
            output = func(self, *args)
            if output != False:
                bools = False
            print(app_interaction_texts.invalid_input)
        return output
    return wrapper