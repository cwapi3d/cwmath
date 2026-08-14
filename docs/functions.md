# Functions

Package-level helpers re-exported from `cwmath`.

## Conversion

::: cwmath.cadwork.to_point_3d
    options:
        show_root_heading: true
        show_source: true

## Projections

::: cwmath.line3.project_point_on_line
    options:
        show_root_heading: true
        show_source: true

::: cwmath.plane3.project_point_on_plane
    options:
        show_root_heading: true
        show_source: true

## Tolerance

`ABS_TOL = 1e-6`, `REL_TOL = 1e-9`. `==` on the types is exact; callers opt
into closeness.

::: cwmath.tolerance.is_close
    options:
        show_root_heading: true
        show_source: true
