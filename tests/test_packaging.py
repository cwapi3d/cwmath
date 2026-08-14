from __future__ import annotations

import subprocess
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_wheel_excludes_tests(tmp_path: Path) -> None:
    subprocess.run(
        ["uv", "build", "--wheel", "--out-dir", str(tmp_path)],
        check=True,
        cwd=ROOT,
    )
    wheels = list(tmp_path.glob("cwmath-*.whl"))
    assert len(wheels) == 1
    names = zipfile.ZipFile(wheels[0]).namelist()
    assert any(name.startswith("cwmath/") for name in names)
    assert any(
        name == "cwmath/py.typed" or name.endswith("/cwmath/py.typed") for name in names
    )
    assert not any(
        name.startswith("cwmath/tests/") or name.startswith("tests/") for name in names
    )
    lowered = [name.lower() for name in names]
    assert not any("cwvector3d" in name or "cwplane3d" in name for name in lowered)


def test_kept_files_present() -> None:
    assert (ROOT / "CODEOWNERS").is_file()
    assert (ROOT / "LICENSE").is_file()
