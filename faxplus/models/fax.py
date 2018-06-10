# coding: utf-8

"""
    FAX.PLUS REST API

    This is the fax.plus API v1 developed for third party developers and organizations. In order to have a better coding experience with this API, let's quickly go through some points:<br /><br /> - This API assumes **/accounts** as an entry point with the base url of **https://restapi.fax.plus/v1**. <br /><br /> - This API treats all date and times sent to it in requests as **UTC**. Also, all dates and times returned in responses are in **UTC**<br /><br /> - Once you have an access_token, you can easily send a request to the resource server with the base url of **https://restapi.fax.plus/v1** to access your permitted resources. As an example to get the user's profile info you would send a request to **https://restapi.fax.plus/v1/accounts/self** when **Authorization** header is set to \"Bearer YOUR_ACCESS_TOKEN\" and custom header of **x-fax-clientid** is set to YOUR_CLIENT_ID  # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from faxplus.models.fax_cost_details import FaxCostDetails  # noqa: F401,E501


class Fax(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'comment': 'str',
        'cost': 'int',
        'direction': 'str',
        'from_number': 'str',
        'status': 'str',
        'scheduled_time': 'str',
        'description': 'str',
        'is_spam': 'bool',
        'submit_time': 'str',
        'cost_details': 'FaxCostDetails',
        'header': 'str',
        'file': 'str',
        'file_name': 'str',
        'retry_delay': 'int',
        'max_retry': 'int',
        'pages': 'int',
        'start_time': 'str',
        'to': 'str',
        'duration': 'int',
        'last_update': 'str',
        'is_read': 'bool',
        'owner_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'comment': 'comment',
        'cost': 'cost',
        'direction': 'direction',
        'from_number': 'from',
        'status': 'status',
        'scheduled_time': 'scheduled_time',
        'description': 'description',
        'is_spam': 'is_spam',
        'submit_time': 'submit_time',
        'cost_details': 'cost_details',
        'header': 'header',
        'file': 'file',
        'file_name': 'file_name',
        'retry_delay': 'retry_delay',
        'max_retry': 'max_retry',
        'pages': 'pages',
        'start_time': 'start_time',
        'to': 'to',
        'duration': 'duration',
        'last_update': 'last_update',
        'is_read': 'is_read',
        'owner_id': 'owner_id'
    }

    def __init__(self, id=None, comment=None, cost=None, direction=None, from_number=None, status=None, scheduled_time=None, description=None, is_spam=None, submit_time=None, cost_details=None, header=None, file=None, file_name=None, retry_delay=None, max_retry=None, pages=None, start_time=None, to=None, duration=None, last_update=None, is_read=None, owner_id=None):  # noqa: E501
        """Fax - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._comment = None
        self._cost = None
        self._direction = None
        self._from_number = None
        self._status = None
        self._scheduled_time = None
        self._description = None
        self._is_spam = None
        self._submit_time = None
        self._cost_details = None
        self._header = None
        self._file = None
        self._file_name = None
        self._retry_delay = None
        self._max_retry = None
        self._pages = None
        self._start_time = None
        self._to = None
        self._duration = None
        self._last_update = None
        self._is_read = None
        self._owner_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if comment is not None:
            self.comment = comment
        if cost is not None:
            self.cost = cost
        if direction is not None:
            self.direction = direction
        if from_number is not None:
            self.from_number = from_number
        if status is not None:
            self.status = status
        if scheduled_time is not None:
            self.scheduled_time = scheduled_time
        if description is not None:
            self.description = description
        if is_spam is not None:
            self.is_spam = is_spam
        if submit_time is not None:
            self.submit_time = submit_time
        if cost_details is not None:
            self.cost_details = cost_details
        if header is not None:
            self.header = header
        if file is not None:
            self.file = file
        if file_name is not None:
            self.file_name = file_name
        if retry_delay is not None:
            self.retry_delay = retry_delay
        if max_retry is not None:
            self.max_retry = max_retry
        if pages is not None:
            self.pages = pages
        if start_time is not None:
            self.start_time = start_time
        if to is not None:
            self.to = to
        if duration is not None:
            self.duration = duration
        if last_update is not None:
            self.last_update = last_update
        if is_read is not None:
            self.is_read = is_read
        if owner_id is not None:
            self.owner_id = owner_id

    @property
    def id(self):
        """Gets the id of this Fax.  # noqa: E501


        :return: The id of this Fax.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Fax.


        :param id: The id of this Fax.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def comment(self):
        """Gets the comment of this Fax.  # noqa: E501


        :return: The comment of this Fax.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this Fax.


        :param comment: The comment of this Fax.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def cost(self):
        """Gets the cost of this Fax.  # noqa: E501


        :return: The cost of this Fax.  # noqa: E501
        :rtype: int
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this Fax.


        :param cost: The cost of this Fax.  # noqa: E501
        :type: int
        """

        self._cost = cost

    @property
    def direction(self):
        """Gets the direction of this Fax.  # noqa: E501


        :return: The direction of this Fax.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this Fax.


        :param direction: The direction of this Fax.  # noqa: E501
        :type: str
        """

        self._direction = direction

    @property
    def from_number(self):
        """Gets the from_number of this Fax.  # noqa: E501


        :return: The from_number of this Fax.  # noqa: E501
        :rtype: str
        """
        return self._from_number

    @from_number.setter
    def from_number(self, from_number):
        """Sets the from_number of this Fax.


        :param from_number: The from_number of this Fax.  # noqa: E501
        :type: str
        """

        self._from_number = from_number

    @property
    def status(self):
        """Gets the status of this Fax.  # noqa: E501


        :return: The status of this Fax.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Fax.


        :param status: The status of this Fax.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def scheduled_time(self):
        """Gets the scheduled_time of this Fax.  # noqa: E501


        :return: The scheduled_time of this Fax.  # noqa: E501
        :rtype: str
        """
        return self._scheduled_time

    @scheduled_time.setter
    def scheduled_time(self, scheduled_time):
        """Sets the scheduled_time of this Fax.


        :param scheduled_time: The scheduled_time of this Fax.  # noqa: E501
        :type: str
        """

        self._scheduled_time = scheduled_time

    @property
    def description(self):
        """Gets the description of this Fax.  # noqa: E501


        :return: The description of this Fax.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Fax.


        :param description: The description of this Fax.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def is_spam(self):
        """Gets the is_spam of this Fax.  # noqa: E501


        :return: The is_spam of this Fax.  # noqa: E501
        :rtype: bool
        """
        return self._is_spam

    @is_spam.setter
    def is_spam(self, is_spam):
        """Sets the is_spam of this Fax.


        :param is_spam: The is_spam of this Fax.  # noqa: E501
        :type: bool
        """

        self._is_spam = is_spam

    @property
    def submit_time(self):
        """Gets the submit_time of this Fax.  # noqa: E501


        :return: The submit_time of this Fax.  # noqa: E501
        :rtype: str
        """
        return self._submit_time

    @submit_time.setter
    def submit_time(self, submit_time):
        """Sets the submit_time of this Fax.


        :param submit_time: The submit_time of this Fax.  # noqa: E501
        :type: str
        """

        self._submit_time = submit_time

    @property
    def cost_details(self):
        """Gets the cost_details of this Fax.  # noqa: E501


        :return: The cost_details of this Fax.  # noqa: E501
        :rtype: FaxCostDetails
        """
        return self._cost_details

    @cost_details.setter
    def cost_details(self, cost_details):
        """Sets the cost_details of this Fax.


        :param cost_details: The cost_details of this Fax.  # noqa: E501
        :type: FaxCostDetails
        """

        self._cost_details = cost_details

    @property
    def header(self):
        """Gets the header of this Fax.  # noqa: E501


        :return: The header of this Fax.  # noqa: E501
        :rtype: str
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this Fax.


        :param header: The header of this Fax.  # noqa: E501
        :type: str
        """

        self._header = header

    @property
    def file(self):
        """Gets the file of this Fax.  # noqa: E501


        :return: The file of this Fax.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this Fax.


        :param file: The file of this Fax.  # noqa: E501
        :type: str
        """

        self._file = file

    @property
    def file_name(self):
        """Gets the file_name of this Fax.  # noqa: E501


        :return: The file_name of this Fax.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this Fax.


        :param file_name: The file_name of this Fax.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def retry_delay(self):
        """Gets the retry_delay of this Fax.  # noqa: E501


        :return: The retry_delay of this Fax.  # noqa: E501
        :rtype: int
        """
        return self._retry_delay

    @retry_delay.setter
    def retry_delay(self, retry_delay):
        """Sets the retry_delay of this Fax.


        :param retry_delay: The retry_delay of this Fax.  # noqa: E501
        :type: int
        """

        self._retry_delay = retry_delay

    @property
    def max_retry(self):
        """Gets the max_retry of this Fax.  # noqa: E501


        :return: The max_retry of this Fax.  # noqa: E501
        :rtype: int
        """
        return self._max_retry

    @max_retry.setter
    def max_retry(self, max_retry):
        """Sets the max_retry of this Fax.


        :param max_retry: The max_retry of this Fax.  # noqa: E501
        :type: int
        """

        self._max_retry = max_retry

    @property
    def pages(self):
        """Gets the pages of this Fax.  # noqa: E501


        :return: The pages of this Fax.  # noqa: E501
        :rtype: int
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """Sets the pages of this Fax.


        :param pages: The pages of this Fax.  # noqa: E501
        :type: int
        """

        self._pages = pages

    @property
    def start_time(self):
        """Gets the start_time of this Fax.  # noqa: E501


        :return: The start_time of this Fax.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Fax.


        :param start_time: The start_time of this Fax.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def to(self):
        """Gets the to of this Fax.  # noqa: E501


        :return: The to of this Fax.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this Fax.


        :param to: The to of this Fax.  # noqa: E501
        :type: str
        """

        self._to = to

    @property
    def duration(self):
        """Gets the duration of this Fax.  # noqa: E501


        :return: The duration of this Fax.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Fax.


        :param duration: The duration of this Fax.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def last_update(self):
        """Gets the last_update of this Fax.  # noqa: E501


        :return: The last_update of this Fax.  # noqa: E501
        :rtype: str
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this Fax.


        :param last_update: The last_update of this Fax.  # noqa: E501
        :type: str
        """

        self._last_update = last_update

    @property
    def is_read(self):
        """Gets the is_read of this Fax.  # noqa: E501


        :return: The is_read of this Fax.  # noqa: E501
        :rtype: bool
        """
        return self._is_read

    @is_read.setter
    def is_read(self, is_read):
        """Sets the is_read of this Fax.


        :param is_read: The is_read of this Fax.  # noqa: E501
        :type: bool
        """

        self._is_read = is_read

    @property
    def owner_id(self):
        """Gets the owner_id of this Fax.  # noqa: E501


        :return: The owner_id of this Fax.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this Fax.


        :param owner_id: The owner_id of this Fax.  # noqa: E501
        :type: str
        """

        self._owner_id = owner_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Fax):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other