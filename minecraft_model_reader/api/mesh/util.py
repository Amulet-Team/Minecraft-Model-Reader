import numpy


def rotate_3d(
    verts: numpy.ndarray, rx: float, ry: float, rz: float, dx: float, dy: float, dz: float, rescale: bool = False
) -> numpy.ndarray:
    radians = numpy.radians([rx, ry, rz])
    sx, sy, sz = numpy.sin(radians)
    cx, cy, cz = numpy.cos(radians)
    trmtx = numpy.array(
        [
            [cz * cy, sz * cy, -sy],
            [cz * sy * sx - sz * cx, sz * sy * sx + cz * cx, cy * sx],
            [cz * sy * cx + sz * sx, sz * sy * cx - cz * sx, cy * cx],
        ]
    )
    origin = numpy.array([dx, dy, dz])
    offset_verts = verts - origin
    if rescale:
        offset_verts[:, 0] /= max(cy * cz, 1e-6, key=abs)
        offset_verts[:, 1] /= max(cx * cz, 1e-6, key=abs)
        offset_verts[:, 2] /= max(cx * cy, 1e-6, key=abs)

    return numpy.matmul(offset_verts, trmtx) + origin  # type: ignore
