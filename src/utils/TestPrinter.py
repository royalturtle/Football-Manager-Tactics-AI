import inspect


def _TP(classname=None, functionname=None, inputs: dict = None, outputs=None):
    if classname is None:
        print("ERROR : classname is empty.")
        return
    string: str = "[C-" + classname + "]"

    if functionname is None:
        print(string)
        return
    string += "[F-" + functionname + "]"

    if inputs is not None:
        string += "  inputs {"
        if "self" in inputs.keys():
            del inputs["self"]

        for key, val in inputs.items():
            if type(val) is str:
                string += str(key) + ":'" + val + "'/"
            else:
                string += str(key) + ":" + str(val) + "/"
        string += "}"
    elif outputs is not None:
        string += "  outputs : " + str(outputs)

    print(string)


def get_class_name(obj) -> str:
    if type(obj) == str:
        result = obj
    else:
        result = obj.__class__.__name__
    return result


def get_function_name() -> str:
    return inspect.stack()[2][3]


def get_inputs_args() -> dict:
    return locals()


def _TPI(obj, para):
    _TP(get_class_name(obj), get_function_name(), para)
