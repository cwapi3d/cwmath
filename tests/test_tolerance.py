from __future__ import annotations

import cwmath
from cwmath.tolerance import ABS_TOL, REL_TOL, is_close


def test_package_imports() -> None:
    assert cwmath.__name__ == 'cwmath'


def test_default_tolerances() -> None:
    assert ABS_TOL == 1e-6
    assert REL_TOL == 1e-9


def test_is_close_exact() -> None:
    assert is_close(1.0, 1.0)
    assert is_close(0.0, 0.0)


def test_is_close_within_abs_tol() -> None:
    assert is_close(0.0, ABS_TOL)
    assert is_close(1.0, 1.0 + ABS_TOL)


def test_is_close_outside_abs_tol() -> None:
    assert not is_close(0.0, ABS_TOL * 2)
    assert not is_close(1.0, 1.0 + 1e-3)


def test_is_close_respects_rel_tol_for_large_values() -> None:
    large = 1e9
    # |Δ| = 0.5 is above ABS_TOL but within REL_TOL * |large| (= 1.0).
    assert is_close(large, large + 0.5)
    assert not is_close(large, large + 2.0)


def test_is_close_accepts_override_tolerances() -> None:
    assert is_close(0.0, 0.5, abs_tol=0.5, rel_tol=0.0)
    assert not is_close(0.0, 0.5, abs_tol=0.1, rel_tol=0.0)
