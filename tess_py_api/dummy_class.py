from typing import Iterable


class dummy:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def __call__(self, *args, **kwargs) -> None:
        return None

    def __getattr__(self, *args, **kwargs):
        return dummy

