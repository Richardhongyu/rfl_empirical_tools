import matplotlib.pyplot as plt
import numpy as np

import matplotlib
import matplotlib as mpl
from matplotlib import colors

data_sched = np.load("../data/out_np_1_10.npy").T
data_none = np.load("../data/out_np.npy").T
data = [data_sched, data_none]
sched = np.array([])
none = np.array([])
bs = [4,8,16,32,64,128]
# bs = bs[2:6]
jobs = [1,2,3,4]
data_index = [0,1,3,4]
avg = []
# title = np.array(['seq write', 'seq read', 'seq readwrite', 'rand write', 'rand read', 'rand readwrite']).reshape(2,3)
title = [['seq write', 'seq read', 'rand write', 'rand read'], ['seq write', 'seq read', 'rand write', 'rand read']]
label_font_conf = {
    # "weight": "bold",
    "size": "18"
}

def heatmap(data, row_labels, col_labels, ax=None,
            cbar_kw=None, cbarlabel="", **kwargs):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Parameters
    ----------
    data
        A 2D numpy array of shape (M, N).
    row_labels
        A list or array of length M with the labels for the rows.
    col_labels
        A list or array of length N with the labels for the columns.
    ax
        A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If
        not provided, use current axes or create a new one.  Optional.
    cbar_kw
        A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional.
    cbarlabel
        The label for the colorbar.  Optional.
    **kwargs
        All other arguments are forwarded to `imshow`.
    """

    if ax is None:
        ax = plt.gca()

    if cbar_kw is None:
        cbar_kw = {}

    # Plot the heatmap
    im = ax.imshow(data, **kwargs)

    # Create colorbar
    # cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    # cbar.ax.set_ylabel(cbarlabel, va="bottom")
    cbar = None

    # Show all ticks and label them with the respective list entries.
    ax.set_xticks(np.arange(data.shape[1]), labels=col_labels, **label_font_conf)
    ax.set_yticks(np.arange(data.shape[0]), labels=row_labels, **label_font_conf)

    # Let the horizontal axes labeling appear on top.
    # ax.tick_params(top=True, bottom=False,
    #                labeltop=True, labelbottom=False)

    ax.tick_params(bottom=False, labelbottom=True, left=False, labelleft=True)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), ha="center",
             rotation_mode="anchor")

    # Turn spines off and create white grid.
    ax.spines[:].set_visible(False)

    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)

    return im, cbar

def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
                     textcolors=("black", "white"),
                     threshold=None, **textkw):
    """
    A function to annotate a heatmap.

    Parameters
    ----------
    im
        The AxesImage to be labeled.
    data
        Data used to annotate.  If None, the image's data is used.  Optional.
    valfmt
        The format of the annotations inside the heatmap.  This should either
        use the string format method, e.g. "$ {x:.2f}", or be a
        `matplotlib.ticker.Formatter`.  Optional.
    textcolors
        A pair of colors.  The first is used for values below a threshold,
        the second for those above.  Optional.
    threshold
        Value in data units according to which the colors from textcolors are
        applied.  If None (the default) uses the middle of the colormap as
        separation.  Optional.
    **kwargs
        All other arguments are forwarded to each call to `text` used to create
        the text labels.
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalize the threshold to the images color range.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)

    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts

fig, axs = plt.subplots(2,4,figsize=(14,6),dpi=100)
jobs_y = 0
fig.supylabel("blocksize (KiB)", x=0.03, y=jobs_y+0.5, **label_font_conf)
fig.supxlabel("Number of IO jobs", x=0.44, y=jobs_y, **label_font_conf)

images = []
for i in range(2):
    for j in range(4):
        matrix = data[i][data_index[j]].reshape(6,6)[:, :4]
        # matrix = data[i][data_index[j]].reshape(6,6)[2:6, :4]
        # if i == 0:
        #     if sched.shape[0] == 0:
        #         sched = matrix
        #     else:
        #         sched = np.concatenate((sched, matrix), axis=1)
        # else:
        #     if none.shape[0] == 0:
        #         none = matrix
        #     else:
        #         none = np.concatenate((none, matrix), axis=1)
        avg.append(np.mean(matrix))
        im, cbar = heatmap(matrix, bs, jobs, ax=axs[i,j], cmap="RdYlGn", aspect='auto', vmin=-40, vmax=40)
        images.append(im)
        texts = annotate_heatmap(im, valfmt="{x:.0f}", fontsize=13, textcolors=("#A52A2A", "darkgreen"))
        axs[i, j].label_outer()
        if i == 0 :
            axs[i, j].set_title(title[i][j], fontsize=20)
# avg_sched = np.mean(sched)
# avg_none = np.mean(none)
# print(f'avg_sched: {avg_sched}, avg_none: {avg_none}')
print(avg)

# 自适应创建colorbar的范围
# vmin = min(image.get_array().min() for image in images)
# vmax = max(image.get_array().max() for image in images)
# norm = colors.Normalize(vmin=vmin, vmax=vmax)
# for im in images:
#     im.set_norm(norm)

cbar = fig.colorbar(images[0], ax=axs, pad=0.05)
cbar.ax.tick_params(labelsize=16)
cbar.set_label("The Performance Superiority of Rust Over C (%)", size=16)
axs[0,0].set_ylabel('sched=None', size=16)
axs[1,0].set_ylabel('sched=mq-deadline', size=16)
plt.savefig("../imgs/figure5.pdf", bbox_inches="tight")