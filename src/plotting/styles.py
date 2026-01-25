import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from cycler import cycler

from tueplots import bundles
from tueplots.constants.color import rgb


def get_style(
    column="half",
    nrows=1,
    ncols=1,
    font_adjustment=0.0,
    rel_width=None,
    alpha=0.7,
    display_dpi=200,
    use_tue_palette=True,
):
    """
    Returns an rcParams dict compatible with:
        plt.rcParams.update(get_style_icml2024(...))

    Parameter:
      - column: "full" oder "half" (tueplots bundle option)
      - nrows, ncols: subplot layout (tueplots bundle option)
      - font_adjustment: additive Anpassung der Schriftgrößen
      - alpha: Transparenz für die Linienfarben
      - display_dpi: DPI fürs Notebook/Screen-Rendering
      - use_tue_palette: Uni-Tübingen Farbpalette statt Matplotlib default
    """
    style = bundles.icml2024(column=column, nrows=nrows, ncols=ncols)

    # Schriftgrößen: icml2024 bringt schon Defaults mit; wir verschieben sie konsistent.
    # (Matplotlib rcParams keys: font.size, axes.labelsize, legend.fontsize, xtick.labelsize, ytick.labelsize, axes.titlesize)
    if font_adjustment != 0:
        for k in [
            "font.size",
            "axes.labelsize",
            "legend.fontsize",
            "xtick.labelsize",
            "ytick.labelsize",
            "axes.titlesize",
        ]:
            if k in style and style[k] is not None:
                style[k] = style[k] + font_adjustment

    # Uni-Tübingen Farben (aus tueplots.constants.colors.rgb)
    # Hinweis: rgb.<name> sind Tripel in 0..1; wir machen RGBA mit alpha draus.
    if use_tue_palette:
        tue_colors_rgb = [
            rgb.tue_blue,
            rgb.tue_red,
            rgb.tue_green,
            rgb.tue_orange,
            rgb.tue_brown,
            rgb.tue_gray,
            rgb.tue_lightgold,
            rgb.tue_violet,
        ]
        tue_colors_rgba = [(*c, alpha) for c in tue_colors_rgb]
        style["axes.prop_cycle"] = cycler(color=tue_colors_rgba)

    # Qualität / DPI
    style.update(
        {
            "figure.dpi": display_dpi,
            "savefig.dpi": 300,
        }
    )

    return style


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

