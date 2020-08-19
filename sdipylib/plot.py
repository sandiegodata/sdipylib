"""Plotting support"""

def source_attribution(ax, text ):
    ax.text(0, -.05, text, fontsize=14,
            horizontalalignment='left', verticalalignment='top',
            transform=ax.transAxes)