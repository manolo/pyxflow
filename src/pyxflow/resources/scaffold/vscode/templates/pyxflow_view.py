from pyxflow import *
from pyxflow.components import *


@Route("{{route}}")
class {{classname}}(Div):
    def __init__(self):
        self.set_size_full()

        self.add(H3("hello"))
