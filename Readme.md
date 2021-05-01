[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/guiwitz/PyImageCourse_beginner/e95337e24ae77357e24f2d49bf521203aaec6012?urlpath=lab)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/guiwitz/PyImageCourse_beginner/blob/master)

# Image processing for beginners

This repository contains a set of Jupyter notebooks to learn how to do basic image processing using Python and the scientific packages Numpy, scikit-image, Matplotlib and Pandas.

The material assumes no pre-existing knowledge in programming but some familiarity with concepts of image processing. The goal of the course is not to learn all the details of Python, but to reach as fast as possible the ability to write short image processing scripts. The course therefore focuses only on essential knowledge and is not at all *exhaustive*.

## Running the notebooks

You don't need to install anything on your computer to interactively run the notebooks. You can use the badges at the top of this Readme to run the notebooks either in the classical Jupyter environment via MyBinder or as Google Colab notebooks. The Mybinder sessions are only temporary, i.e. changes you make to notebooks or new notebooks are *erased* between sessions. When using Colab, to keep your changes, you need to *save a copy* of the notebook you are modifying. The saving is done in your Google Drive.

## Data

In this course, we are trying to reproduce a workflow used in other contexts, in particular Fiji, so that you can compare different approaches. For example you can check the excellent introduction to Fiji Macro programming by Anna Klemm [here](https://github.com/ahklemm/ImageJMacro_Introduction). We use images from the [Cell Atlas](https://www.proteinatlas.org/humanproteome/cell) of the Human Protein Atlas (HPA) project where a large collection of proteins have been tagged and imaged to determine their cellular location. Specifically, we downloaded a series of [images](images) from the Atlas, with some cells showing nucleoplasm localization and some nuclear membrane localization. The idea of the workflow is to compare the signal within the nucleus with that on its edge to determine for each image whether the protein is membrane bound or not.

The images in the [images](images) folder all come from the [Cell Atlas](https://www.proteinatlas.org/humanproteome/cell). For more information see the publication of Thul PJ et al., A subcellular map of the human proteome. **Science**. (2017) DOI: [10.1126/science.aal3321](https://doi.org/10.1126/science.aal3321). All images are covered by a [Creative Commons Attribution-ShareAlike 3.0 International License](https://creativecommons.org/licenses/by-sa/3.0/).

All images were downloaded directly from the HPA website using the same link construction and saved as tif files. For example the image [8346_22_C1_1.tif](images/8346_22_C1_1.tif) was downloaded using the link
https://images.proteinatlas.org/8346/22_C1_1_blue_red_green.jpg.

## Re-using the material and fixing errors
Feel free to re-use this material to learn or to teach image processing. If you think some changes are needed, please use the issue tracker to discuss them, as the classical pull request system is not yet ideal for Jupyter Notebooks.
