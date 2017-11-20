# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.8.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1ContainerStateTerminated(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'container_id': 'str',
        'exit_code': 'int',
        'finished_at': 'datetime',
        'message': 'str',
        'reason': 'str',
        'signal': 'int',
        'started_at': 'datetime'
    }

    attribute_map = {
        'container_id': 'containerID',
        'exit_code': 'exitCode',
        'finished_at': 'finishedAt',
        'message': 'message',
        'reason': 'reason',
        'signal': 'signal',
        'started_at': 'startedAt'
    }

    def __init__(self, container_id=None, exit_code=None, finished_at=None, message=None, reason=None, signal=None, started_at=None):
        """
        V1ContainerStateTerminated - a model defined in Swagger
        """

        self._container_id = None
        self._exit_code = None
        self._finished_at = None
        self._message = None
        self._reason = None
        self._signal = None
        self._started_at = None
        self.discriminator = None

        if container_id is not None:
          self.container_id = container_id
        self.exit_code = exit_code
        if finished_at is not None:
          self.finished_at = finished_at
        if message is not None:
          self.message = message
        if reason is not None:
          self.reason = reason
        if signal is not None:
          self.signal = signal
        if started_at is not None:
          self.started_at = started_at

    @property
    def container_id(self):
        """
        Gets the container_id of this V1ContainerStateTerminated.
        Container's ID in the format 'docker://<container_id>'

        :return: The container_id of this V1ContainerStateTerminated.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        """
        Sets the container_id of this V1ContainerStateTerminated.
        Container's ID in the format 'docker://<container_id>'

        :param container_id: The container_id of this V1ContainerStateTerminated.
        :type: str
        """

        self._container_id = container_id

    @property
    def exit_code(self):
        """
        Gets the exit_code of this V1ContainerStateTerminated.
        Exit status from the last termination of the container

        :return: The exit_code of this V1ContainerStateTerminated.
        :rtype: int
        """
        return self._exit_code

    @exit_code.setter
    def exit_code(self, exit_code):
        """
        Sets the exit_code of this V1ContainerStateTerminated.
        Exit status from the last termination of the container

        :param exit_code: The exit_code of this V1ContainerStateTerminated.
        :type: int
        """
        if exit_code is None:
            raise ValueError("Invalid value for `exit_code`, must not be `None`")

        self._exit_code = exit_code

    @property
    def finished_at(self):
        """
        Gets the finished_at of this V1ContainerStateTerminated.
        Time at which the container last terminated

        :return: The finished_at of this V1ContainerStateTerminated.
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """
        Sets the finished_at of this V1ContainerStateTerminated.
        Time at which the container last terminated

        :param finished_at: The finished_at of this V1ContainerStateTerminated.
        :type: datetime
        """

        self._finished_at = finished_at

    @property
    def message(self):
        """
        Gets the message of this V1ContainerStateTerminated.
        Message regarding the last termination of the container

        :return: The message of this V1ContainerStateTerminated.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this V1ContainerStateTerminated.
        Message regarding the last termination of the container

        :param message: The message of this V1ContainerStateTerminated.
        :type: str
        """

        self._message = message

    @property
    def reason(self):
        """
        Gets the reason of this V1ContainerStateTerminated.
        (brief) reason from the last termination of the container

        :return: The reason of this V1ContainerStateTerminated.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this V1ContainerStateTerminated.
        (brief) reason from the last termination of the container

        :param reason: The reason of this V1ContainerStateTerminated.
        :type: str
        """

        self._reason = reason

    @property
    def signal(self):
        """
        Gets the signal of this V1ContainerStateTerminated.
        Signal from the last termination of the container

        :return: The signal of this V1ContainerStateTerminated.
        :rtype: int
        """
        return self._signal

    @signal.setter
    def signal(self, signal):
        """
        Sets the signal of this V1ContainerStateTerminated.
        Signal from the last termination of the container

        :param signal: The signal of this V1ContainerStateTerminated.
        :type: int
        """

        self._signal = signal

    @property
    def started_at(self):
        """
        Gets the started_at of this V1ContainerStateTerminated.
        Time at which previous execution of the container started

        :return: The started_at of this V1ContainerStateTerminated.
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """
        Sets the started_at of this V1ContainerStateTerminated.
        Time at which previous execution of the container started

        :param started_at: The started_at of this V1ContainerStateTerminated.
        :type: datetime
        """

        self._started_at = started_at

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1ContainerStateTerminated):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
