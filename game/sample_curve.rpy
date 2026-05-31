init python:
    def sample_curve(points, stat_value):
        # points is a list of (x, y) tuples, sorted by x
        if stat_value <= points[0][0]:
            return points[0][1] * 100
        if stat_value >= points[-1][0]:
            return points[-1][1] * 100
        for i in range(len(points) - 1):
            x0, y0 = points[i]
            x1, y1 = points[i + 1]
            if x0 <= stat_value <= x1:
                t = (stat_value - x0) / (x1 - x0)
                return (y0 + t * (y1 - y0)) * 100
        return 0.0