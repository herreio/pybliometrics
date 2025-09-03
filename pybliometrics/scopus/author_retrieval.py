from typing import Union

from pybliometrics.superclasses import Retrieval
from pybliometrics.utils import check_parameter_value, VIEWS


class AuthorRetrieval(Retrieval):

    def __init__(self,
                 author_id: Union[int, str],
                 refresh: Union[bool, int] = False,
                 view: str = "ENHANCED",
                 **kwds: str
                 ) -> None:
        """Interaction with the Author Retrieval API.

        :param author_id: The ID or the EID of the author.
        :param refresh: Whether to refresh the cached file if it exists or not.
                        If int is passed, cached file will be refreshed if the
                        number of days since last modification exceeds that value.
        :param view: The view of the file that should be downloaded.  Allowed
                     values: `METRICS`, `LIGHT`, `STANDARD`, `ENHANCED`, `ENTITLED`, where `STANDARD`
                     includes all information of `LIGHT` view and `ENHANCED`
                     includes all information of any view.  For details see
                     https://dev.elsevier.com/sc_author_retrieval_views.html.
                     Note: Neither the `BASIC` nor the `DOCUMENTS` view are active,
                     although documented. `ENTITLED` only contains the `document_entitlement_status`.
        :param kwds: Keywords passed on as query parameters.  Must contain
                     fields and values mentioned in the API specification at
                     https://dev.elsevier.com/documentation/AuthorRetrievalAPI.wadl.

        Raises
        ------
        ValueError
            If any of the parameters `refresh` or `view` is not
            one of the allowed values.

        Notes
        -----
        The directory for cached results is `{path}/ENHANCED/{author_id}`,
        where `path` is specified in your configuration file, and `author_id`
        is stripped of an eventually leading `'9-s2.0-'`.
        """
        # Checks
        check_parameter_value(view, VIEWS['AuthorRetrieval'], "view")

        # Load xml
        self._id = str(author_id).split('-')[-1]
        self._view = view
        self._refresh = refresh
        Retrieval.__init__(self, identifier=self._id, **kwds)
