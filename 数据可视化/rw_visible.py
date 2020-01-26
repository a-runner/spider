from test import Random
import matplotlib.pyplot as plt


def run():

    rw = Random(5000)
    rw.fill_walk()
    plt.figure(figsize=(20, 15))
    num_points = list(range(rw.num_points))
    # plt.plot(rw.x_values, rw.y_values, linewidth=10)
    plt.scatter(rw.x_values[0:25000], rw.y_values[0:25000], c=num_points[0:25000], cmap=plt.cm.Reds, edgecolors='none', s=15)
    plt.scatter(rw.x_values[25000:], rw.y_values[25000:], c=num_points[25000:], cmap=plt.cm.Blues, edgecolors='none', s=15)
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()


if __name__ == '__main__':
    run()