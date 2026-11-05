import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress


def plot_pred_vs_target(preds, targets, title=""):
    """Scatter predictions against targets; returns the unclosed (!) figure."""

    preds, targets = np.ravel(preds), np.ravel(targets)
    fit = linregress(targets, preds)  # slope < 1 = predictions compressed to the mean

    fig, ax = plt.subplots(figsize=(4, 4))
    ax.scatter(targets, preds, s=12, alpha=0.6)

    lims = [min(targets.min(), preds.min()), max(targets.max(), preds.max())]
    ax.plot(lims, lims, "k--", lw=1, label="identity")
    ax.plot(lims, fit.intercept + fit.slope * np.array(lims), "r-", lw=1, label="fit")

    ax.set_xlabel("target")
    ax.set_ylabel("prediction")
    ax.set_title(
        f"{title}\nr={fit.rvalue:.2f}  slope={fit.slope:.2f}  "
        f"sd ratio={preds.std() / targets.std():.2f}"
    )
    ax.legend(loc="upper left", fontsize=8)
    fig.tight_layout()

    return fig
