"""Tests for `scopus.AffiliationRetrieval` module."""

from pybliometrics.scopus import AffiliationRetrieval, init

init()


light = AffiliationRetrieval('60000356', refresh=30, view="LIGHT")
standard = AffiliationRetrieval('60000356', refresh=30, view="STANDARD")
entitled = AffiliationRetrieval('60000356', refresh=30, view='ENTITLED')

# TODO
