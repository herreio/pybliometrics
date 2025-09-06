"""Tests for `scopus.AbstractRetrieval` module."""

from pybliometrics.scopus import AbstractRetrieval, init

init()

# Base information
ab1 = AbstractRetrieval("2-s2.0-84930616647", view="FULL", refresh=30)
# Conference proceeding and no references
ab2 = AbstractRetrieval("2-s2.0-0029486824", view="FULL", refresh=30)
# Issuetitle and no affiliation
ab3 = AbstractRetrieval("2-s2.0-0001270077", view="FULL", refresh=30)
# Author group broken and author keywords
ab4 = AbstractRetrieval("2-s2.0-0000016206", view="FULL", refresh=30)
# ISBN
ab5 = AbstractRetrieval("2-s2.0-84919546381", view="FULL", refresh=30)
# Funding, sequencebanks, chemicals
ab6 = AbstractRetrieval("2-s2.0-85040230676", view="FULL", refresh=30)
# Contributor group
ab7 = AbstractRetrieval("2-s2.0-85050253030", view="FULL", refresh=30)
# REF view
ab8 = AbstractRetrieval("2-s2.0-84951753303", view="REF", refresh=30)
# Collaboration
ab9 = AbstractRetrieval("2-s2.0-85097473741", view="FULL", refresh=30)
# ENTITLED view
ar10 = AbstractRetrieval('10.1109/Multi-Temp.2019.8866947', view='ENTITLED', refresh=30)
# REF view without refs
ab11 = AbstractRetrieval('2-s2.0-85160105660', view="REF", refresh=30)
# FULL view with list of collaborations
ab12 = AbstractRetrieval('2-s2.0-85044008512', view='FULL', refresh=30)

# TODO
