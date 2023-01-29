import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server import util


def strategic_get_endpoints():  # noqa: E501
    """Retrieve strategic detector ids

    No parameters. Returns information about all intersections and their  detectors that are currently hosted by the data store. # noqa: E501


    :rtype: List[InlineResponse200]
    """
    return 'do some magic!'


def strategic_get_last_data(updated_since, iid=None):  # noqa: E501
    """Retrieve last data from strategic detectors

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param updated_since: Limit results to the ones updated after (timestamp greater than)
    :type updated_since: str
    :param iid: Intersection IDs to retrieve data from
    :type iid: List[str]

    :rtype: List[InlineResponse2002]
    """
    return 'do some magic!'
