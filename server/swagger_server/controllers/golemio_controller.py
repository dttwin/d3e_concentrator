import connexion
import six

from swagger_server.models.inline_response2004 import InlineResponse2004  # noqa: E501
from swagger_server import util


def golemio_get_last_data(updated_since, lineid=None):  # noqa: E501
    """Get last data uploaded from the Golemio platform

     # noqa: E501

    :param updated_since: Limit results to the ones updated after (timestamp greater than)
    :type updated_since: str
    :param lineid: Line IDs (PT schedule numbers) to retrieve data from
    :type lineid: List[str]

    :rtype: List[InlineResponse2004]
    """
    return 'do some magic!'


def golemio_get_lines():  # noqa: E501
    """Retrieve list of public transport lines covered by golemio

     # noqa: E501


    :rtype: List[str]
    """
    return 'do some magic!'
