from typing import Hashable, Callable


class ClassNotFoundError(ValueError):
    ...


class SubjectOne(object):
    ...


class SubjectTwo(object):
    ...


class Factory(object):
    @staticmethod
    def get(class_name: Hashable) -> object:
        if not isinstance(class_name, Hashable):
            raise ValueError("class_name must be a Hashable type!")
        
        classes: dict[Hashable, Callable[..., object]] = {
            "SubjectOne": SubjectOne,
            "SubjectTwo": SubjectTwo
        }

        class_ = classes.get(class_name, None)
        if class_ is not None:
            return class_

        raise ClassNotFoundError


# Usage
class_ = Factory.get("SubjectOne")
