"""Shared closeness policy for scalar and geometry comparisons."""

from __future__ import annotations

import math

ABS_TOL = 1e-6
REL_TOL = 1e-9


def is_close(
    a: float,
    b: float,
    *,
    abs_tol: float = ABS_TOL,
    rel_tol: float = REL_TOL,
) -> bool:
    """Return whether two scalars are close under the package tolerances.

    Uses :func:`math.isclose` so every type shares one millimetre-scale policy.
    ``==`` on public types stays exact IEEE equality; callers opt in here.
    """
    return math.isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)
