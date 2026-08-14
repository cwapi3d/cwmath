# Point3

A frozen 3D position. Affine: `Point3 + Vec3 → Point3`, `Point3 - Point3 → Vec3`.
Adding two points raises `TypeError`. Build from a host value with
`Point3.from_xyz(...)`.

::: cwmath.point3.Point3
    options:
        show_root_heading: true
        show_source: true
