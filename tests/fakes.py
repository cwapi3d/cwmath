"""Duck-typed doubles for the cadwork host types.

CI never imports ``cadwork``. Later seeds inject ``FakeCadwork`` as the
``point_3d`` factory and build values through ``FakePoint3d``.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class FakePoint3d:
    """Stand-in for ``cadwork.point_3d`` (``.x`` / ``.y`` / ``.z``)."""

    x: float
    y: float
    z: float

    def __getitem__(self, index: int) -> float:
        if index == 0:
            return self.x
        if index == 1:
            return self.y
        if index == 2:
            return self.z
        raise IndexError(index)


class FakeCadwork:
    """Stand-in for the host ``cadwork`` module object."""

    @staticmethod
    def point_3d(x: float, y: float, z: float) -> FakePoint3d:
        return FakePoint3d(x, y, z)
