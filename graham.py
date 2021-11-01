import numpy as np
import matplotlib.pyplot as plt
from functools import cmp_to_key


def keygen(init_point):
    def key(x):
        angle = np.arctan2(x[1]-init_point[1], x[0]-init_point[0])
        if angle < 0:
            print(angle)
            angle += 2*np.pi
        return angle
    return key


def graham_scan(points):
    points = sorted(points, key=lambda x: 1000*x[1] + x[0])
    init_point = points[0]
    points = sorted(points, key=keygen(init_point))
    points = np.array(points)
    stack = [init_point]
    for p in points:
        while len(stack) > 1 and np.cross(p-stack[-1],stack[-1]-stack[-2]) >= 0:
            stack.pop()
        stack.append(p)
    stack.append(init_point)
    return np.array(stack)


if __name__ == "__main__":
    points = np.random.normal(0, 5, (100, 2)).tolist()

    hull = graham_scan(points)
    points = np.array(points)
    plt.scatter(points[:, 0], points[:, 1])
    plt.plot(hull[:, 0], hull[:, 1])
    plt.show()
