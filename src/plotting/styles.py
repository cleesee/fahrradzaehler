import matplotlib.pyplot as plt
import numpy as np
import tueplots.bundles as bundles
import tueplots.fontsizes as fontsizes
from cycler import cycler
import matplotlib.colors as mcolors


def get_style(font_adjustment=0, rel_width=1, alpha=0.7, display_dpi=200):
    jmlr_style = bundles.jmlr2001(rel_width=rel_width)

    base_colors = [
        'tab:blue',
        'tab:orange',
        'tab:green',
        'tab:red',
        'tab:purple',
        'tab:brown',
        'tab:pink',
        'tab:gray',
        'tab:olive',
        'tab:cyan',
    ]
    rgba_colors = [mcolors.to_rgba(c, alpha=alpha) for c in base_colors]

    jmlr_style.update({
        'font.size': 10.95 + font_adjustment,
        'axes.labelsize': 10.95 + font_adjustment,
        'legend.fontsize': 8.95 + font_adjustment,
        'xtick.labelsize': 8.95 + font_adjustment,
        'ytick.labelsize': 8.95 + font_adjustment,
        'axes.titlesize': 10.95 + font_adjustment,
        'axes.prop_cycle': cycler(color=rgba_colors),
                # Quality (raster)
        'figure.dpi': display_dpi,
        'savefig.dpi': 300,
    })

    return jmlr_style

def latex_escape(text: str) -> str:
    repl = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    for k, v in repl.items():
        text = text.replace(k, v)
    return text

