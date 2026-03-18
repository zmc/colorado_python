from typing import Any, TypeAlias

Coordinate: TypeAlias = tuple[float, float]  # (lon, lat)
LinearRing: TypeAlias = list[Coordinate]
PolygonRings: TypeAlias = list[LinearRing]  # [exterior, hole1, hole2, ...]


def to_polygon_rings(raw_polygon: Any) -> PolygonRings:
    rings: PolygonRings = []
    for raw_ring in raw_polygon or []:
        ring: LinearRing = []
        for point in raw_ring or []:
            if not isinstance(point, (list, tuple)) or len(point) < 2:
                continue
            lon = float(point[0])
            lat = float(point[1])
            ring.append((lon, lat))
        if ring:
            rings.append(ring)
    return rings


def _point_on_segment(px: float, py: float, x1: float, y1: float, x2: float, y2: float, eps: float = 1e-12) -> bool:
    cross = (py - y1) * (x2 - x1) - (px - x1) * (y2 - y1)
    if abs(cross) > eps:
        return False
    dot = (px - x1) * (px - x2) + (py - y1) * (py - y2)
    return dot <= eps


def _point_in_ring(lon: float, lat: float, ring: LinearRing) -> bool:
    if len(ring) < 3:
        return False

    inside = False
    j = len(ring) - 1
    for i in range(len(ring)):
        xi, yi = ring[i]
        xj, yj = ring[j]

        if _point_on_segment(lon, lat, xi, yi, xj, yj):
            return True  # on border = inside

        intersects = ((yi > lat) != (yj > lat)) and (
                lon < (xj - xi) * (lat - yi) / ((yj - yi) or 1e-15) + xi
        )
        if intersects:
            inside = not inside
        j = i

    return inside


def point_in_polygon(lat: float, lon: float, polygon: PolygonRings) -> bool:
    """
    polygon: [exterior_ring, hole_ring1, ...]
    """
    if not polygon:
        return False

    if not _point_in_ring(lon, lat, polygon[0]):
        return False

    for hole in polygon[1:]:
        if _point_in_ring(lon, lat, hole):
            return False

    return True
