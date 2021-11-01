import numpy as np
import matplotlib.pyplot as plt


def jarvis(points):
    left_point = points[0]
    for p in points:
        if left_point[0] > p[0]:
            left_point = p
    hull = [left_point]
    while True:
        hull_point = points[0]
        for p in points:
            orientation = np.cross(p-hull_point, hull_point-hull[-1])
            if orientation > 0:
                hull_point = p
        hull.append(hull_point)
        if np.all(hull[0] == hull[-1]):
            break
    return np.array(hull)


if __name__ == "__main__":

    points = np.random.normal(-5, 5, (100, 2))
    hull = jarvis(points)

    plt.scatter(points[:, 0], points[:, 1])
    plt.plot(hull[:, 0], hull[:, 1])
    plt.show()
