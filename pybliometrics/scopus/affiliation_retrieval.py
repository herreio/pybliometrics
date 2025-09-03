from typing import Union

from pybliometrics.superclasses import Retrieval
from pybliometrics.utils import check_parameter_value, VIEWS


class AffiliationRetrieval(Retrieval):

    def __init__(self,
                 aff_id: Union[int, str],
                 refresh: Union[bool, int] = False,
                 view: str = "STANDARD",
                 **kwds: str
                 ) -> None:
        """Interaction with the Affiliation Retrieval API.

        :param aff_id: Scopus ID or EID of the affiliation profile.
        :param refresh: Whether to refresh the cached file if it exists or not.
                        If int is passed, cached file will be refreshed if the
                        number of days since last modification exceeds that value.
        :param view: The view of the file that should be downloaded.  Allowed
                     values: `LIGHT`, `STANDARD`, `ENTITLED`, where `STANDARD` includes all
                     information of the `LIGHT` view.  For details see
                     https://dev.elsevier.com/sc_affil_retrieval_views.html.
                     Note: Neither the `BASIC` view nor `DOCUMENTS` or `AUTHORS`
                     views are active, although documented. `ENTITLED` only contains the `document_entitlement_status`.
        :param kwds: Keywords passed on as query parameters.  Must contain
                     fields and values mentioned in the API specification at
                     https://dev.elsevier.com/documentation/AffiliationRetrievalAPI.wadl.

        Raises
        ------
        ValueError
            If any of the parameters `refresh` or `view` is not
            one of the allowed values.

        Notes
        -----
        The directory for cached results is `{path}/{view}/{aff_id}`,
        where `path` is specified in your configuration file.
        """
        # Checks
        check_parameter_value(view, VIEWS['AffiliationRetrieval'], "view")

        # Load xml
        self._view = view
        self._refresh = refresh
        aff_id = str(int(str(aff_id).split('-')[-1]))
        Retrieval.__init__(self, aff_id, **kwds)
