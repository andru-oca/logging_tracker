from typing import Any, Dict


class SingletonMetaLogger(type):
    _instances: Dict[type, object] = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwds)

        return cls._instances[cls]
