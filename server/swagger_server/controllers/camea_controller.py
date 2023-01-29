import connexion
import six

from swagger_server.models.inline_response2003 import InlineResponse2003  # noqa: E501
from swagger_server import util


def camea_get_endpoints():  # noqa: E501
    """Retrieve detector ids

    No parameters. Returns information about all Camea detectors that are  actually stored in our data store. # noqa: E501


    :rtype: List[InlineResponse2003]
    """
    return 'do some magic!'


def camea_get_last_data():  # noqa: E501
    """Retrieve last data from CAMEA detectors

    Returns data received since the given timestamp for the given set  of detector names (or data of all available detectors). # noqa: E501


    :rtype: List[InlineResponse2003]
    """
    return 'do some magic!'
