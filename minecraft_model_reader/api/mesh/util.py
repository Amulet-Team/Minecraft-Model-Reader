import numpy


def rotate_3d(
    verts: numpy.ndarray, x: float, y: float, z: float, dx: float, dy: float, dz: float
) -> numpy.ndarray:
    radians = numpy.radians([x, y, z])
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
    return numpy.matmul(verts - origin, trmtx) + origin  # type: ignore
