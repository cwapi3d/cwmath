# Frame3

A frozen origin plus a right-handed orthonormal basis. Use
`from_origin_and_axes` when the axes are already unit and orthogonal, or
`from_origin_xy` to build `z = x × y` and orthonormalize.

`to_world` / `to_local` map `Point3` with translation and `Vec3` by rotation
only.

::: cwmath.frame3.Frame3
    options:
        show_root_heading: true
        show_source: true
