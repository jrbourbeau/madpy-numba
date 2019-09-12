# Accelerating Numerical Python with Numba @ Madpy

This repository contains the materials for my "Accelerating Numerical Python with Numba" talk at the September 2019 Madpy meetup.

An live version of the notebook from this talk is available by clicking the "launch binder" button below:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jrbourbeau/madpy-numba/master?urlpath=lab/tree/numerical-computing-with-numba.ipynb)


You can also run the notebook locally by following the setup instructions below.

## Setup

**Step 1: Create Conda environment**

A Conda environment with the dependencies needed to run the notebook from this talk can be created with:

```terminal
conda env create --name madpy-numba --file environment.yml
```

**Step 2: Activate Conda environment**

Activate the Conda environment:

```terminal
conda activate madpy-numba
```

**Step 4: Launch JupyterLab**

The notebook can then be launched with:

```terminal
jupyter lab numerical-computing-with-numba.ipynb
```

## License

[MIT LICENSE](LICENSE)
