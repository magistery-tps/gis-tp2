# UBA - Maestria en Explotación de Datos y Descubrimiento de Conocimiento - Sistemas de información geografica

## TP 2 - Clasificación de imágenes satelitales para la detección de cultivos y cuantificación de áreas sembradas en Argentina

## Informe

* [Google Docs](https://docs.google.com/document/d/1mUeEoCTk2aUe1CdnY4_59gIrKjuVLAEfztIrKQQddIw/edit)

### Notebooks:

* [Download dataset](https://github.com/magistery-tps/gis-tp2/tree/main/notebooks/dataset.ipynb)
* Pixel Clasification
    * [Preprocesamiento y clasificación utilizando OTB](https://github.com/magistery-tps/gis-tp2/tree/main/notebooks/pixel-clasification.ipynb)
    * [Utilizando un modelo estadistico](https://github.com/magistery-tps/gis-tp2/tree/main/notebooks/clasificador_estadistico.ipynb)
    * [Utilizando un modelo estadistico 2](https://github.com/magistery-tps/gis-tp2/tree/main/notebooks/clasificador_estadistico_2.ipynb): Similar al anterior. En lugar de mostrar las diferentes medias y std para cada cada cultivo en cada mes y para cada indice, mostramos la variacion entre meses consecutivos. Es decir, cuanto varia en promedio por ejemplo, el ndvi para maiz de octubre a noviembre
    

### Analisis con Orange DM
 
* [Orange DM Project](https://github.com/magistery-tps/gis-tp2/blob/main/orange-project.ows)
* [Resultados](https://docs.google.com/document/d/1X5HmZg_e37KCm9dcRhPinQeWEgeBwduzGbRHXTOYlA4/edit?usp=sharing)

### Links

* [Teledetección - Orfeo Toolbox - Google Cloud](https://docs.google.com/document/d/1V5d6icd6FHN4cgtVkrzZ2r7HdtUg5CaChsi9wT5yDkA)
* [Bitácora ejercicios teledetección](https://docs.google.com/document/d/1zE4oFIGIQ0yXZJmgxsoPdYhyew2kUoMXQmr5WwbEMwY)
* [Scripts](https://github.com/fedebayle/tp-2-gis-dm-uba)
* [Clase: Clasificacion en OTB](https://youtu.be/S4gN10fTaEY)
* [Trabajo Práctico N° 2 Clasificación de imágenes satelitales para la detección de cultivos y cuantificación de áreas sembradas en Argentina](http://157.92.26.246/campus/pluginfile.php/2087/mod_resource/content/2/GIS-UBA-DM%20-%20TP%20Teledeteccion%202022.pdf)


### Requisites

* [Orange Datamining](https://orangedatamining.com/download/#linux)
* [Orfeo toolbox](https://gist.github.com/adrianmarino/d471f961d789d79270d3f2631d017bd7)
* [anaconda](https://www.anaconda.com/products/individual) / [miniconda](https://docs.conda.io/en/latest/miniconda.html)
* [QGis](https://www.qgis.org) (Optional)
* [DB Browser for SQLite](https://sqlitebrowser.org) (Optional)

### Getting started

**Step 1**: Clone repo.

```bash
$ git clone https://github.com/magistery-tps/gis-tp2.git
$ cd gis-tp2
```

**Step 2**: Create environment.

```bash
$ conda env create -f environment.yml
```

## See notebooks in jupyter lab

**Step 1**: Enable project environment.

```bash
$ conda activate gis-tp2
```

**Step 2**: Under project directory boot jupyter lab.

```bash
$ jupyter lab

Jupyter Notebook 6.1.4 is running at:
http://localhost:8888/?token=45efe99607fa6......
```

**Step 3**: Go to http://localhost:8888.... as indicated in the shell output.
