from __future__ import annotations

import re
import sys
import types
from pathlib import Path

from cwmath import Point3
from fakes import FakeCadwork, FakePoint3d

README = Path(__file__).resolve().parents[1] / "README.md"


def _readme_python_example() -> str:
    text = README.read_text(encoding="utf-8")
    match = re.search(r"```python\n(.*?)```", text, re.S)
    assert match is not None, "README is missing a python example fence"
    return match.group(1)


def test_readme_example_converts_frames_and_projects() -> None:
    cadwork = types.ModuleType("cadwork")
    cadwork.point_3d = FakeCadwork.point_3d  # type: ignore[attr-defined]
    sys.modules["cadwork"] = cadwork
    try:
        namespace: dict[str, object] = {}
        exec(_readme_python_example(), namespace)  # noqa: S102
    finally:
        sys.modules.pop("cadwork", None)

    world = namespace["world"]
    foot = namespace["foot"]
    result = namespace["result"]
    assert isinstance(world, Point3)
    assert isinstance(foot, Point3)
    assert world.is_close(Point3(1050.0, 2025.0, 10.0))
    assert foot.is_close(Point3(1050.0, 2025.0, 0.0))
    assert isinstance(result, FakePoint3d)
    assert (result.x, result.y, result.z) == (1050.0, 2025.0, 0.0)
