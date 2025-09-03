from typing import Union

from pybliometrics.superclasses import Retrieval
from pybliometrics.utils import check_parameter_value, detect_id_type, VIEWS


class AbstractRetrieval(Retrieval):

    def __init__(self,
                 identifier: Union[int, str] = None,
                 refresh: Union[bool, int] = False,
                 view: str = 'META_ABS',
                 id_type: str = None,
                 **kwds: str
                 ) -> None:
        """Interaction with the Abstract Retrieval API.

        :param identifier: The identifier of a document.  Can be the Scopus EID
                           , the Scopus ID, the PII, the Pubmed-ID or the DOI.
        :param refresh: Whether to refresh the cached file if it exists or not.
                        If int is passed, cached file will be refreshed if the
                        number of days since last modification exceeds that value.
        :param id_type: The type of used ID. Allowed values: None, 'eid', 'pii',
                        'scopus_id', 'pubmed_id', 'doi'.  If the value is None,
                        the function tries to infer the ID type itself.
        :param view: The view of the file that should be downloaded.  Allowed
                     values: META, META_ABS, REF, FULL, ENTITLED, where FULL includes all
                     information of META_ABS view and META_ABS includes all
                     information of the META view.  For details see
                     https://dev.elsevier.com/sc_abstract_retrieval_views.html.
                     Note: `ENTITLED` view only contains the `document_entitlement_status`.
        :param kwds: Keywords passed on as query parameters.  Must contain
                     fields and values listed in the API specification at
                     https://dev.elsevier.com/documentation/AbstractRetrievalAPI.wadl.

        Raises
        ------
        ValueError
            If any of the parameters `id_type`, `refresh` or `view` is not
            one of the allowed values.

        Notes
        -----
        The directory for cached results is `{path}/{view}/{identifier}`,
        where `path` is specified in your configuration file.  In case
        `identifier` is a DOI, an underscore replaces the forward slash.
        """
        # Checks
        identifier = str(identifier)
        check_parameter_value(view, VIEWS['AbstractRetrieval'], "view")
        if id_type is None:
            id_type = detect_id_type(identifier)
        else:
            allowed_id_types = ('eid', 'pii', 'scopus_id', 'pubmed_id', 'doi')
            check_parameter_value(id_type, allowed_id_types, "id_type")

        # Load xml
        self._view = view
        self._refresh = refresh
        Retrieval.__init__(self, identifier=identifier, id_type=id_type, **kwds)
