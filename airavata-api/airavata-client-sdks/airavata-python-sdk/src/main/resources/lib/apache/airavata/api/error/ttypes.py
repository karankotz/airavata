#
# Autogenerated by Thrift Compiler (0.10.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
import sys
import apache.airavata.model.experiment.ttypes

from thrift.transport import TTransport


class AiravataErrorType(object):
    """
    A list of Airavata API Error Message Types

     UNKNOWN: No information available about the error
      
     PERMISSION_DENIED: Not permitted to perform action

     INTERNAL_ERROR: Unexpected problem with the service

     AUTHENTICATION_FAILURE: The client failed to authenticate.

     INVALID_AUTHORIZATION: Security Token and/or Username and/or password is incorrect
      
     AUTHORIZATION_EXPIRED: Authentication token expired
     
     UNKNOWN_GATEWAY_ID: The gateway is not registered with Airavata.

     UNSUPPORTED_OPERATION: Operation denied because it is currently unsupported.
    """
    UNKNOWN = 0
    PERMISSION_DENIED = 1
    INTERNAL_ERROR = 2
    AUTHENTICATION_FAILURE = 3
    INVALID_AUTHORIZATION = 4
    AUTHORIZATION_EXPIRED = 5
    UNKNOWN_GATEWAY_ID = 6
    UNSUPPORTED_OPERATION = 7

    _VALUES_TO_NAMES = {
        0: "UNKNOWN",
        1: "PERMISSION_DENIED",
        2: "INTERNAL_ERROR",
        3: "AUTHENTICATION_FAILURE",
        4: "INVALID_AUTHORIZATION",
        5: "AUTHORIZATION_EXPIRED",
        6: "UNKNOWN_GATEWAY_ID",
        7: "UNSUPPORTED_OPERATION",
    }

    _NAMES_TO_VALUES = {
        "UNKNOWN": 0,
        "PERMISSION_DENIED": 1,
        "INTERNAL_ERROR": 2,
        "AUTHENTICATION_FAILURE": 3,
        "INVALID_AUTHORIZATION": 4,
        "AUTHORIZATION_EXPIRED": 5,
        "UNKNOWN_GATEWAY_ID": 6,
        "UNSUPPORTED_OPERATION": 7,
    }


class ExperimentNotFoundException(TException):
    """
    This exception is thrown when a client asks to perform an operation on an experiment that does not exist.

    identifier:  A description of the experiment that was not found on the server.

    key:  The value passed from the client in the identifier, which was not found.

    Attributes:
     - message
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'message', 'UTF8', None, ),  # 1
    )

    def __init__(self, message=None,):
        self.message = message

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.message = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ExperimentNotFoundException')
        if self.message is not None:
            oprot.writeFieldBegin('message', TType.STRING, 1)
            oprot.writeString(self.message.encode('utf-8') if sys.version_info[0] == 2 else self.message)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.message is None:
            raise TProtocolException(message='Required field message is unset!')
        return

    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ProjectNotFoundException(TException):
    """
    1:  optional  string identifier,
    2:  optional  string key


    Attributes:
     - message
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'message', 'UTF8', None, ),  # 1
    )

    def __init__(self, message=None,):
        self.message = message

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.message = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ProjectNotFoundException')
        if self.message is not None:
            oprot.writeFieldBegin('message', TType.STRING, 1)
            oprot.writeString(self.message.encode('utf-8') if sys.version_info[0] == 2 else self.message)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.message is None:
            raise TProtocolException(message='Required field message is unset!')
        return

    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class InvalidRequestException(TException):
    """
    This exception is thrown for invalid requests that occur from any reasons like required input parameters are missing,
     or a parameter is malformed.

     message: contains the associated error message.

    Attributes:
     - message
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'message', 'UTF8', None, ),  # 1
    )

    def __init__(self, message=None,):
        self.message = message

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.message = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('InvalidRequestException')
        if self.message is not None:
            oprot.writeFieldBegin('message', TType.STRING, 1)
            oprot.writeString(self.message.encode('utf-8') if sys.version_info[0] == 2 else self.message)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.message is None:
            raise TProtocolException(message='Required field message is unset!')
        return

    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class TimedOutException(TException):
    """
    This exception is thrown when RPC timeout gets exceeded.
    """

    thrift_spec = (
    )

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('TimedOutException')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class AuthenticationException(TException):
    """
    This exception is thrown for invalid sshKeyAuthentication requests.

     message: contains the cause of the authorization failure.

    Attributes:
     - message
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'message', 'UTF8', None, ),  # 1
    )

    def __init__(self, message=None,):
        self.message = message

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.message = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('AuthenticationException')
        if self.message is not None:
            oprot.writeFieldBegin('message', TType.STRING, 1)
            oprot.writeString(self.message.encode('utf-8') if sys.version_info[0] == 2 else self.message)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.message is None:
            raise TProtocolException(message='Required field message is unset!')
        return

    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class AuthorizationException(TException):
    """
    This exception is thrown for invalid authorization requests such user does not have acces to an aplication or resource.

     message: contains the authorization failure message

    Attributes:
     - message
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'message', 'UTF8', None, ),  # 1
    )

    def __init__(self, message=None,):
        self.message = message

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.message = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('AuthorizationException')
        if self.message is not None:
            oprot.writeFieldBegin('message', TType.STRING, 1)
            oprot.writeString(self.message.encode('utf-8') if sys.version_info[0] == 2 else self.message)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.message is None:
            raise TProtocolException(message='Required field message is unset!')
        return

    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class DuplicateEntryException(TException):
    """
    This exception is thrown when you try to save a duplicate entity that already exists
      in the database.

      message: contains the associated error message


    Attributes:
     - message
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'message', 'UTF8', None, ),  # 1
    )

    def __init__(self, message=None,):
        self.message = message

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.message = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('DuplicateEntryException')
        if self.message is not None:
            oprot.writeFieldBegin('message', TType.STRING, 1)
            oprot.writeString(self.message.encode('utf-8') if sys.version_info[0] == 2 else self.message)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.message is None:
            raise TProtocolException(message='Required field message is unset!')
        return

    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class AiravataClientException(TException):
    """
    This exception is thrown by Airavata Services when a call fails as a result of
    a problem that a client may be able to resolve.  For example, if the user
    attempts to execute an application on a resource gateway does not have access to.

    This exception would not be used for internal system errors that do not
    reflect user actions, but rather reflect a problem within the service that
    the client cannot resolve.

    airavataErrorType:  The message type indicating the error that occurred.
      must be one of the values of AiravataErrorType.

    parameter:  If the error applied to a particular input parameter, this will
      indicate which parameter.

    Attributes:
     - airavataErrorType
     - parameter
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'airavataErrorType', None, None, ),  # 1
        (2, TType.STRING, 'parameter', 'UTF8', None, ),  # 2
    )

    def __init__(self, airavataErrorType=None, parameter=None,):
        self.airavataErrorType = airavataErrorType
        self.parameter = parameter

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.airavataErrorType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.parameter = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('AiravataClientException')
        if self.airavataErrorType is not None:
            oprot.writeFieldBegin('airavataErrorType', TType.I32, 1)
            oprot.writeI32(self.airavataErrorType)
            oprot.writeFieldEnd()
        if self.parameter is not None:
            oprot.writeFieldBegin('parameter', TType.STRING, 2)
            oprot.writeString(self.parameter.encode('utf-8') if sys.version_info[0] == 2 else self.parameter)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.airavataErrorType is None:
            raise TProtocolException(message='Required field airavataErrorType is unset!')
        return

    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ValidatorResult(object):
    """
    Attributes:
     - result
     - errorDetails
    """

    thrift_spec = (
        None,  # 0
        (1, TType.BOOL, 'result', None, None, ),  # 1
        (2, TType.STRING, 'errorDetails', 'UTF8', None, ),  # 2
    )

    def __init__(self, result=None, errorDetails=None,):
        self.result = result
        self.errorDetails = errorDetails

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.BOOL:
                    self.result = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.errorDetails = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ValidatorResult')
        if self.result is not None:
            oprot.writeFieldBegin('result', TType.BOOL, 1)
            oprot.writeBool(self.result)
            oprot.writeFieldEnd()
        if self.errorDetails is not None:
            oprot.writeFieldBegin('errorDetails', TType.STRING, 2)
            oprot.writeString(self.errorDetails.encode('utf-8') if sys.version_info[0] == 2 else self.errorDetails)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.result is None:
            raise TProtocolException(message='Required field result is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ValidationResults(object):
    """
    Attributes:
     - validationState
     - validationResultList
    """

    thrift_spec = (
        None,  # 0
        (1, TType.BOOL, 'validationState', None, None, ),  # 1
        (2, TType.LIST, 'validationResultList', (TType.STRUCT, (ValidatorResult, ValidatorResult.thrift_spec), False), None, ),  # 2
    )

    def __init__(self, validationState=None, validationResultList=None,):
        self.validationState = validationState
        self.validationResultList = validationResultList

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.BOOL:
                    self.validationState = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.validationResultList = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = ValidatorResult()
                        _elem5.read(iprot)
                        self.validationResultList.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ValidationResults')
        if self.validationState is not None:
            oprot.writeFieldBegin('validationState', TType.BOOL, 1)
            oprot.writeBool(self.validationState)
            oprot.writeFieldEnd()
        if self.validationResultList is not None:
            oprot.writeFieldBegin('validationResultList', TType.LIST, 2)
            oprot.writeListBegin(TType.STRUCT, len(self.validationResultList))
            for iter6 in self.validationResultList:
                iter6.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.validationState is None:
            raise TProtocolException(message='Required field validationState is unset!')
        if self.validationResultList is None:
            raise TProtocolException(message='Required field validationResultList is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class LaunchValidationException(TException):
    """
    Attributes:
     - validationResult
     - errorMessage
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRUCT, 'validationResult', (ValidationResults, ValidationResults.thrift_spec), None, ),  # 1
        (2, TType.STRING, 'errorMessage', 'UTF8', None, ),  # 2
    )

    def __init__(self, validationResult=None, errorMessage=None,):
        self.validationResult = validationResult
        self.errorMessage = errorMessage

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.validationResult = ValidationResults()
                    self.validationResult.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.errorMessage = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('LaunchValidationException')
        if self.validationResult is not None:
            oprot.writeFieldBegin('validationResult', TType.STRUCT, 1)
            self.validationResult.write(oprot)
            oprot.writeFieldEnd()
        if self.errorMessage is not None:
            oprot.writeFieldBegin('errorMessage', TType.STRING, 2)
            oprot.writeString(self.errorMessage.encode('utf-8') if sys.version_info[0] == 2 else self.errorMessage)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.validationResult is None:
            raise TProtocolException(message='Required field validationResult is unset!')
        return

    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class AiravataSystemException(TException):
    """
    This exception is thrown by Airavata Services when a call fails as a result of
    a problem in the service that could not be changed through client's action.

    airavataErrorType:  The message type indicating the error that occurred.
      must be one of the values of AiravataErrorType.

    message:  This may contain additional information about the error


    Attributes:
     - airavataErrorType
     - message
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'airavataErrorType', None, None, ),  # 1
        (2, TType.STRING, 'message', 'UTF8', None, ),  # 2
    )

    def __init__(self, airavataErrorType=None, message=None,):
        self.airavataErrorType = airavataErrorType
        self.message = message

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.airavataErrorType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.message = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('AiravataSystemException')
        if self.airavataErrorType is not None:
            oprot.writeFieldBegin('airavataErrorType', TType.I32, 1)
            oprot.writeI32(self.airavataErrorType)
            oprot.writeFieldEnd()
        if self.message is not None:
            oprot.writeFieldBegin('message', TType.STRING, 2)
            oprot.writeString(self.message.encode('utf-8') if sys.version_info[0] == 2 else self.message)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.airavataErrorType is None:
            raise TProtocolException(message='Required field airavataErrorType is unset!')
        return

    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
