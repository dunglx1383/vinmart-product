from typing import Any, List, Optional, TypeVar, Callable, Type, cast
from enum import Enum

T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_int(x: Any) -> int:
    if x is None:
        return 0
    else:
        assert isinstance(x, int) and not isinstance(x, bool)
        return x


def from_float(x: Any) -> float:
    if x is None:
        return 0
    else:
        assert isinstance(x, float) and not isinstance(x, bool)
        return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_str(x: Any) -> str:
    if x is None:
        return 0
    else:
        assert isinstance(x, str)
        return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x
