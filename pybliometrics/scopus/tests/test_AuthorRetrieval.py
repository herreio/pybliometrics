"""Tests for `scopus.AuthorRetrieval` module."""

from pybliometrics.scopus import AuthorRetrieval, init

init()

metrics = AuthorRetrieval("7004212771", refresh=30, view="METRICS")
light = AuthorRetrieval("7004212771", refresh=30, view="LIGHT")
standard = AuthorRetrieval("7004212771", refresh=30, view="STANDARD")
enhanced = AuthorRetrieval("7004212771", refresh=30, view="ENHANCED")
entitled = AuthorRetrieval(36009348900, view='ENTITLED')

# TODO
