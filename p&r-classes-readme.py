"""Point and Rectangle classes.

Point  -- point with (x,y) coordinates
Rect  -- two points, forming a rectangle
"""


class Point:
    """A point identified by (x,y) coordinates.

    supports: +, -, *, /, str, repr

    length  -- calculate length of vector to point from origin
    distance_to  -- calculate distance between two points
    as_tuple  -- construct tuple (x,y)
    clone  -- construct a duplicate
    integerise  -- convert x & y to integers
    floatise  -- convert x & y to floats
    move_to  -- reset x & y
    slide  -- move (in place) +dx, +dy, as spec'd by point
    slide_xy  -- move (in place) +dx, +dy
    rotate  -- rotate around the origin
    rotate_about  -- rotate around another point
    """


def rotate(self, rad):
    """Rotate counter-clockwise by rad radians.

    Positive y goes *up,* as in traditional mathematics.

    Interestingly, you can use this in y-down computer graphics, if
    you just remember that it turns clockwise, rather than
    counter-clockwise.

    The new position is returned as a new Point.
    """


def rotate_about(self, p, theta):
    """Rotate counter-clockwise around a point, by theta degrees.

    Positive y goes *up,* as in traditional mathematics.

    The new position is returned as a new Point.
    """


class Rect:
    """A rectangle identified by two points.

    The rectangle stores left, top, right, and bottom values.

    Coordinates are based on screen coordinates.

    origin                               top
       +-----> x increases                |
       |                           left  -+-  right
       v                                  |
    y increases                         bottom

    set_points  -- reset rectangle coordinates
    contains  -- is a point inside?
    overlaps  -- does a rectangle overlap?
    top_left  -- get top-left corner
    bottom_right  -- get bottom-right corner
    expanded_by  -- grow (or shrink)
    """


def expanded_by(self, n):
    """Return a rectangle with extended borders.

    Create a new rectangle that is wider and taller than the
    immediate one. All sides are extended by "n" points.
    """
