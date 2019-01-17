import matplotlib.pyplot as plt


def lineplot(x_data, y_data, x_label="", y_label="", title="", name="default"):
    # Create the plot object
    fig, ax = plt.subplots()

    # Plot the best fit line, set the linewidth (lw), color and
    # transparency (alpha) of the line
    ax.plot(x_data, y_data, lw=2, color='#539caf', alpha=5)

    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    fig.savefig(f'../image/{name}.png')  # save the figure to file
    plt.close(fig)  # close the figure


def lineplot2(x_data, y_data, x_label="", y_label="", title="", name="default", color="r", yscale_log=False):
    # Create the plot object
    fig, ax = plt.subplots()

    # Plot the data, set the size (s), color and transparency (alpha)
    # of the points
    ax.scatter(x_data, y_data, s=5, color=color, alpha=0.75)

    if yscale_log == True:
        ax.set_yscale('log')

    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    fig.savefig(f'../image/{name}.png')  # save the figure to file
    plt.close(fig)  # close the figure


def histogram(data, n_bins, cumulative=False, x_label="", y_label="", title="", name="default"):
    fig, ax = plt.subplots()
    ax.hist(data, n_bins=n_bins, cumulative=cumulative, color='#539caf')
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
    fig.savefig(f'../image/{name}.png')  # save the figure to file
    plt.close(fig)  # close the figure