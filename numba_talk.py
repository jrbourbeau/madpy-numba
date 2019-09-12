# Adapted from https://github.com/lmcinnes/umap/blob/80f1247de0d60eb60d7222a3cdf9aef9452ab38e/doc/basic_usage.rst

from io import BytesIO
from PIL import Image
import base64

import numpy as np
import pandas as pd
from bokeh.plotting import figure, show, output_notebook
from bokeh.models import HoverTool, ColumnDataSource, CategoricalColorMapper
from bokeh.palettes import Spectral10


def embeddable_image(data):
    img_data = 255 - 15 * data.astype(np.uint8)
    image = Image.fromarray(img_data, mode="L").resize((64, 64), Image.BICUBIC)
    buffer = BytesIO()
    image.save(buffer, format="png")
    for_encoding = buffer.getvalue()
    return "data:image/png;base64," + base64.b64encode(for_encoding).decode()


def plot_embedding(embedding, digits):

    output_notebook()

    digits_df = pd.DataFrame(embedding, columns=("x", "y"))
    digits_df["digit"] = [str(x) for x in digits.target]
    digits_df["image"] = list(map(embeddable_image, digits.images))

    datasource = ColumnDataSource(digits_df)
    color_mapping = CategoricalColorMapper(
        factors=[str(9 - x) for x in digits.target_names], palette=Spectral10
    )

    plot_figure = figure(
        title="UMAP projection of the Digits dataset",
        plot_width=600,
        plot_height=600,
        tools=("pan, wheel_zoom, reset"),
    )

    plot_figure.add_tools(
        HoverTool(
            tooltips="""
    <div>
        <div>
            <img src='@image' style='float: left; margin: 5px 5px 5px 5px'/>
        </div>
        <div>
            <span style='font-size: 16px; color: #224499'>Digit:</span>
            <span style='font-size: 18px'>@digit</span>
        </div>
    </div>
    """
        )
    )

    plot_figure.circle(
        "x",
        "y",
        source=datasource,
        color=dict(field="digit", transform=color_mapping),
        line_alpha=0.6,
        fill_alpha=0.6,
        size=4,
    )
    show(plot_figure)
