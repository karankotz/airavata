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
import apache.airavata.model.commons.ttypes

from thrift.transport import TTransport


class GatewayApprovalStatus(object):
    REQUESTED = 0
    APPROVED = 1
    ACTIVE = 2
    DEACTIVATED = 3
    CANCELLED = 4
    DENIED = 5
    CREATED = 6
    DEPLOYED = 7

    _VALUES_TO_NAMES = {
        0: "REQUESTED",
        1: "APPROVED",
        2: "ACTIVE",
        3: "DEACTIVATED",
        4: "CANCELLED",
        5: "DENIED",
        6: "CREATED",
        7: "DEPLOYED",
    }

    _NAMES_TO_VALUES = {
        "REQUESTED": 0,
        "APPROVED": 1,
        "ACTIVE": 2,
        "DEACTIVATED": 3,
        "CANCELLED": 4,
        "DENIED": 5,
        "CREATED": 6,
        "DEPLOYED": 7,
    }


class NotificationPriority(object):
    LOW = 0
    NORMAL = 1
    HIGH = 2

    _VALUES_TO_NAMES = {
        0: "LOW",
        1: "NORMAL",
        2: "HIGH",
    }

    _NAMES_TO_VALUES = {
        "LOW": 0,
        "NORMAL": 1,
        "HIGH": 2,
    }


class Group(object):
    """
    Attributes:
     - groupName
     - description
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'groupName', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'description', 'UTF8', None, ),  # 2
    )

    def __init__(self, groupName=None, description=None,):
        self.groupName = groupName
        self.description = description

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
                    self.groupName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.description = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('Group')
        if self.groupName is not None:
            oprot.writeFieldBegin('groupName', TType.STRING, 1)
            oprot.writeString(self.groupName.encode('utf-8') if sys.version_info[0] == 2 else self.groupName)
            oprot.writeFieldEnd()
        if self.description is not None:
            oprot.writeFieldBegin('description', TType.STRING, 2)
            oprot.writeString(self.description.encode('utf-8') if sys.version_info[0] == 2 else self.description)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.groupName is None:
            raise TProtocolException(message='Required field groupName is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Project(object):
    """
    Attributes:
     - projectID
     - owner
     - gatewayId
     - name
     - description
     - creationTime
     - sharedUsers
     - sharedGroups
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'projectID', 'UTF8', "DO_NOT_SET_AT_CLIENTS", ),  # 1
        (2, TType.STRING, 'owner', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'gatewayId', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'name', 'UTF8', None, ),  # 4
        (5, TType.STRING, 'description', 'UTF8', None, ),  # 5
        (6, TType.I64, 'creationTime', None, None, ),  # 6
        (7, TType.LIST, 'sharedUsers', (TType.STRING, 'UTF8', False), None, ),  # 7
        (8, TType.LIST, 'sharedGroups', (TType.STRING, 'UTF8', False), None, ),  # 8
    )

    def __init__(self, projectID=thrift_spec[1][4], owner=None, gatewayId=None, name=None, description=None, creationTime=None, sharedUsers=None, sharedGroups=None,):
        self.projectID = projectID
        self.owner = owner
        self.gatewayId = gatewayId
        self.name = name
        self.description = description
        self.creationTime = creationTime
        self.sharedUsers = sharedUsers
        self.sharedGroups = sharedGroups

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
                    self.projectID = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.owner = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.gatewayId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.description = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.creationTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.LIST:
                    self.sharedUsers = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.sharedUsers.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.LIST:
                    self.sharedGroups = []
                    (_etype9, _size6) = iprot.readListBegin()
                    for _i10 in range(_size6):
                        _elem11 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.sharedGroups.append(_elem11)
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
        oprot.writeStructBegin('Project')
        if self.projectID is not None:
            oprot.writeFieldBegin('projectID', TType.STRING, 1)
            oprot.writeString(self.projectID.encode('utf-8') if sys.version_info[0] == 2 else self.projectID)
            oprot.writeFieldEnd()
        if self.owner is not None:
            oprot.writeFieldBegin('owner', TType.STRING, 2)
            oprot.writeString(self.owner.encode('utf-8') if sys.version_info[0] == 2 else self.owner)
            oprot.writeFieldEnd()
        if self.gatewayId is not None:
            oprot.writeFieldBegin('gatewayId', TType.STRING, 3)
            oprot.writeString(self.gatewayId.encode('utf-8') if sys.version_info[0] == 2 else self.gatewayId)
            oprot.writeFieldEnd()
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 4)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        if self.description is not None:
            oprot.writeFieldBegin('description', TType.STRING, 5)
            oprot.writeString(self.description.encode('utf-8') if sys.version_info[0] == 2 else self.description)
            oprot.writeFieldEnd()
        if self.creationTime is not None:
            oprot.writeFieldBegin('creationTime', TType.I64, 6)
            oprot.writeI64(self.creationTime)
            oprot.writeFieldEnd()
        if self.sharedUsers is not None:
            oprot.writeFieldBegin('sharedUsers', TType.LIST, 7)
            oprot.writeListBegin(TType.STRING, len(self.sharedUsers))
            for iter12 in self.sharedUsers:
                oprot.writeString(iter12.encode('utf-8') if sys.version_info[0] == 2 else iter12)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.sharedGroups is not None:
            oprot.writeFieldBegin('sharedGroups', TType.LIST, 8)
            oprot.writeListBegin(TType.STRING, len(self.sharedGroups))
            for iter13 in self.sharedGroups:
                oprot.writeString(iter13.encode('utf-8') if sys.version_info[0] == 2 else iter13)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.projectID is None:
            raise TProtocolException(message='Required field projectID is unset!')
        if self.owner is None:
            raise TProtocolException(message='Required field owner is unset!')
        if self.gatewayId is None:
            raise TProtocolException(message='Required field gatewayId is unset!')
        if self.name is None:
            raise TProtocolException(message='Required field name is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class User(object):
    """
    Attributes:
     - airavataInternalUserId
     - userName
     - gatewayId
     - firstName
     - lastName
     - email
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'airavataInternalUserId', 'UTF8', "DO_NOT_SET_AT_CLIENTS", ),  # 1
        (2, TType.STRING, 'userName', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'gatewayId', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'firstName', 'UTF8', None, ),  # 4
        (5, TType.STRING, 'lastName', 'UTF8', None, ),  # 5
        (6, TType.STRING, 'email', 'UTF8', None, ),  # 6
    )

    def __init__(self, airavataInternalUserId=thrift_spec[1][4], userName=None, gatewayId=None, firstName=None, lastName=None, email=None,):
        self.airavataInternalUserId = airavataInternalUserId
        self.userName = userName
        self.gatewayId = gatewayId
        self.firstName = firstName
        self.lastName = lastName
        self.email = email

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
                    self.airavataInternalUserId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.userName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.gatewayId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.firstName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.lastName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.email = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('User')
        if self.airavataInternalUserId is not None:
            oprot.writeFieldBegin('airavataInternalUserId', TType.STRING, 1)
            oprot.writeString(self.airavataInternalUserId.encode('utf-8') if sys.version_info[0] == 2 else self.airavataInternalUserId)
            oprot.writeFieldEnd()
        if self.userName is not None:
            oprot.writeFieldBegin('userName', TType.STRING, 2)
            oprot.writeString(self.userName.encode('utf-8') if sys.version_info[0] == 2 else self.userName)
            oprot.writeFieldEnd()
        if self.gatewayId is not None:
            oprot.writeFieldBegin('gatewayId', TType.STRING, 3)
            oprot.writeString(self.gatewayId.encode('utf-8') if sys.version_info[0] == 2 else self.gatewayId)
            oprot.writeFieldEnd()
        if self.firstName is not None:
            oprot.writeFieldBegin('firstName', TType.STRING, 4)
            oprot.writeString(self.firstName.encode('utf-8') if sys.version_info[0] == 2 else self.firstName)
            oprot.writeFieldEnd()
        if self.lastName is not None:
            oprot.writeFieldBegin('lastName', TType.STRING, 5)
            oprot.writeString(self.lastName.encode('utf-8') if sys.version_info[0] == 2 else self.lastName)
            oprot.writeFieldEnd()
        if self.email is not None:
            oprot.writeFieldBegin('email', TType.STRING, 6)
            oprot.writeString(self.email.encode('utf-8') if sys.version_info[0] == 2 else self.email)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.airavataInternalUserId is None:
            raise TProtocolException(message='Required field airavataInternalUserId is unset!')
        if self.gatewayId is None:
            raise TProtocolException(message='Required field gatewayId is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Gateway(object):
    """
    Attributes:
     - airavataInternalGatewayId
     - gatewayId
     - gatewayApprovalStatus
     - gatewayName
     - domain
     - emailAddress
     - gatewayAcronym
     - gatewayURL
     - gatewayPublicAbstract
     - reviewProposalDescription
     - gatewayAdminFirstName
     - gatewayAdminLastName
     - gatewayAdminEmail
     - identityServerUserName
     - identityServerPasswordToken
     - declinedReason
     - oauthClientId
     - oauthClientSecret
     - requestCreationTime
     - requesterUsername
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'airavataInternalGatewayId', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'gatewayId', 'UTF8', None, ),  # 2
        (3, TType.I32, 'gatewayApprovalStatus', None, None, ),  # 3
        (4, TType.STRING, 'gatewayName', 'UTF8', None, ),  # 4
        (5, TType.STRING, 'domain', 'UTF8', None, ),  # 5
        (6, TType.STRING, 'emailAddress', 'UTF8', None, ),  # 6
        (7, TType.STRING, 'gatewayAcronym', 'UTF8', None, ),  # 7
        (8, TType.STRING, 'gatewayURL', 'UTF8', None, ),  # 8
        (9, TType.STRING, 'gatewayPublicAbstract', 'UTF8', None, ),  # 9
        (10, TType.STRING, 'reviewProposalDescription', 'UTF8', None, ),  # 10
        (11, TType.STRING, 'gatewayAdminFirstName', 'UTF8', None, ),  # 11
        (12, TType.STRING, 'gatewayAdminLastName', 'UTF8', None, ),  # 12
        (13, TType.STRING, 'gatewayAdminEmail', 'UTF8', None, ),  # 13
        (14, TType.STRING, 'identityServerUserName', 'UTF8', None, ),  # 14
        (15, TType.STRING, 'identityServerPasswordToken', 'UTF8', None, ),  # 15
        (16, TType.STRING, 'declinedReason', 'UTF8', None, ),  # 16
        (17, TType.STRING, 'oauthClientId', 'UTF8', None, ),  # 17
        (18, TType.STRING, 'oauthClientSecret', 'UTF8', None, ),  # 18
        (19, TType.I64, 'requestCreationTime', None, None, ),  # 19
        (20, TType.STRING, 'requesterUsername', 'UTF8', None, ),  # 20
    )

    def __init__(self, airavataInternalGatewayId=None, gatewayId=None, gatewayApprovalStatus=None, gatewayName=None, domain=None, emailAddress=None, gatewayAcronym=None, gatewayURL=None, gatewayPublicAbstract=None, reviewProposalDescription=None, gatewayAdminFirstName=None, gatewayAdminLastName=None, gatewayAdminEmail=None, identityServerUserName=None, identityServerPasswordToken=None, declinedReason=None, oauthClientId=None, oauthClientSecret=None, requestCreationTime=None, requesterUsername=None,):
        self.airavataInternalGatewayId = airavataInternalGatewayId
        self.gatewayId = gatewayId
        self.gatewayApprovalStatus = gatewayApprovalStatus
        self.gatewayName = gatewayName
        self.domain = domain
        self.emailAddress = emailAddress
        self.gatewayAcronym = gatewayAcronym
        self.gatewayURL = gatewayURL
        self.gatewayPublicAbstract = gatewayPublicAbstract
        self.reviewProposalDescription = reviewProposalDescription
        self.gatewayAdminFirstName = gatewayAdminFirstName
        self.gatewayAdminLastName = gatewayAdminLastName
        self.gatewayAdminEmail = gatewayAdminEmail
        self.identityServerUserName = identityServerUserName
        self.identityServerPasswordToken = identityServerPasswordToken
        self.declinedReason = declinedReason
        self.oauthClientId = oauthClientId
        self.oauthClientSecret = oauthClientSecret
        self.requestCreationTime = requestCreationTime
        self.requesterUsername = requesterUsername

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
                    self.airavataInternalGatewayId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.gatewayId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.gatewayApprovalStatus = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.gatewayName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.domain = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.emailAddress = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.gatewayAcronym = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.gatewayURL = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRING:
                    self.gatewayPublicAbstract = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.reviewProposalDescription = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRING:
                    self.gatewayAdminFirstName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.STRING:
                    self.gatewayAdminLastName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.STRING:
                    self.gatewayAdminEmail = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.STRING:
                    self.identityServerUserName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 15:
                if ftype == TType.STRING:
                    self.identityServerPasswordToken = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 16:
                if ftype == TType.STRING:
                    self.declinedReason = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 17:
                if ftype == TType.STRING:
                    self.oauthClientId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 18:
                if ftype == TType.STRING:
                    self.oauthClientSecret = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 19:
                if ftype == TType.I64:
                    self.requestCreationTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 20:
                if ftype == TType.STRING:
                    self.requesterUsername = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('Gateway')
        if self.airavataInternalGatewayId is not None:
            oprot.writeFieldBegin('airavataInternalGatewayId', TType.STRING, 1)
            oprot.writeString(self.airavataInternalGatewayId.encode('utf-8') if sys.version_info[0] == 2 else self.airavataInternalGatewayId)
            oprot.writeFieldEnd()
        if self.gatewayId is not None:
            oprot.writeFieldBegin('gatewayId', TType.STRING, 2)
            oprot.writeString(self.gatewayId.encode('utf-8') if sys.version_info[0] == 2 else self.gatewayId)
            oprot.writeFieldEnd()
        if self.gatewayApprovalStatus is not None:
            oprot.writeFieldBegin('gatewayApprovalStatus', TType.I32, 3)
            oprot.writeI32(self.gatewayApprovalStatus)
            oprot.writeFieldEnd()
        if self.gatewayName is not None:
            oprot.writeFieldBegin('gatewayName', TType.STRING, 4)
            oprot.writeString(self.gatewayName.encode('utf-8') if sys.version_info[0] == 2 else self.gatewayName)
            oprot.writeFieldEnd()
        if self.domain is not None:
            oprot.writeFieldBegin('domain', TType.STRING, 5)
            oprot.writeString(self.domain.encode('utf-8') if sys.version_info[0] == 2 else self.domain)
            oprot.writeFieldEnd()
        if self.emailAddress is not None:
            oprot.writeFieldBegin('emailAddress', TType.STRING, 6)
            oprot.writeString(self.emailAddress.encode('utf-8') if sys.version_info[0] == 2 else self.emailAddress)
            oprot.writeFieldEnd()
        if self.gatewayAcronym is not None:
            oprot.writeFieldBegin('gatewayAcronym', TType.STRING, 7)
            oprot.writeString(self.gatewayAcronym.encode('utf-8') if sys.version_info[0] == 2 else self.gatewayAcronym)
            oprot.writeFieldEnd()
        if self.gatewayURL is not None:
            oprot.writeFieldBegin('gatewayURL', TType.STRING, 8)
            oprot.writeString(self.gatewayURL.encode('utf-8') if sys.version_info[0] == 2 else self.gatewayURL)
            oprot.writeFieldEnd()
        if self.gatewayPublicAbstract is not None:
            oprot.writeFieldBegin('gatewayPublicAbstract', TType.STRING, 9)
            oprot.writeString(self.gatewayPublicAbstract.encode('utf-8') if sys.version_info[0] == 2 else self.gatewayPublicAbstract)
            oprot.writeFieldEnd()
        if self.reviewProposalDescription is not None:
            oprot.writeFieldBegin('reviewProposalDescription', TType.STRING, 10)
            oprot.writeString(self.reviewProposalDescription.encode('utf-8') if sys.version_info[0] == 2 else self.reviewProposalDescription)
            oprot.writeFieldEnd()
        if self.gatewayAdminFirstName is not None:
            oprot.writeFieldBegin('gatewayAdminFirstName', TType.STRING, 11)
            oprot.writeString(self.gatewayAdminFirstName.encode('utf-8') if sys.version_info[0] == 2 else self.gatewayAdminFirstName)
            oprot.writeFieldEnd()
        if self.gatewayAdminLastName is not None:
            oprot.writeFieldBegin('gatewayAdminLastName', TType.STRING, 12)
            oprot.writeString(self.gatewayAdminLastName.encode('utf-8') if sys.version_info[0] == 2 else self.gatewayAdminLastName)
            oprot.writeFieldEnd()
        if self.gatewayAdminEmail is not None:
            oprot.writeFieldBegin('gatewayAdminEmail', TType.STRING, 13)
            oprot.writeString(self.gatewayAdminEmail.encode('utf-8') if sys.version_info[0] == 2 else self.gatewayAdminEmail)
            oprot.writeFieldEnd()
        if self.identityServerUserName is not None:
            oprot.writeFieldBegin('identityServerUserName', TType.STRING, 14)
            oprot.writeString(self.identityServerUserName.encode('utf-8') if sys.version_info[0] == 2 else self.identityServerUserName)
            oprot.writeFieldEnd()
        if self.identityServerPasswordToken is not None:
            oprot.writeFieldBegin('identityServerPasswordToken', TType.STRING, 15)
            oprot.writeString(self.identityServerPasswordToken.encode('utf-8') if sys.version_info[0] == 2 else self.identityServerPasswordToken)
            oprot.writeFieldEnd()
        if self.declinedReason is not None:
            oprot.writeFieldBegin('declinedReason', TType.STRING, 16)
            oprot.writeString(self.declinedReason.encode('utf-8') if sys.version_info[0] == 2 else self.declinedReason)
            oprot.writeFieldEnd()
        if self.oauthClientId is not None:
            oprot.writeFieldBegin('oauthClientId', TType.STRING, 17)
            oprot.writeString(self.oauthClientId.encode('utf-8') if sys.version_info[0] == 2 else self.oauthClientId)
            oprot.writeFieldEnd()
        if self.oauthClientSecret is not None:
            oprot.writeFieldBegin('oauthClientSecret', TType.STRING, 18)
            oprot.writeString(self.oauthClientSecret.encode('utf-8') if sys.version_info[0] == 2 else self.oauthClientSecret)
            oprot.writeFieldEnd()
        if self.requestCreationTime is not None:
            oprot.writeFieldBegin('requestCreationTime', TType.I64, 19)
            oprot.writeI64(self.requestCreationTime)
            oprot.writeFieldEnd()
        if self.requesterUsername is not None:
            oprot.writeFieldBegin('requesterUsername', TType.STRING, 20)
            oprot.writeString(self.requesterUsername.encode('utf-8') if sys.version_info[0] == 2 else self.requesterUsername)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.gatewayId is None:
            raise TProtocolException(message='Required field gatewayId is unset!')
        if self.gatewayApprovalStatus is None:
            raise TProtocolException(message='Required field gatewayApprovalStatus is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Notification(object):
    """
    Attributes:
     - notificationId
     - gatewayId
     - title
     - notificationMessage
     - creationTime
     - publishedTime
     - expirationTime
     - priority
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'notificationId', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'gatewayId', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'title', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'notificationMessage', 'UTF8', None, ),  # 4
        (5, TType.I64, 'creationTime', None, None, ),  # 5
        (6, TType.I64, 'publishedTime', None, None, ),  # 6
        (7, TType.I64, 'expirationTime', None, None, ),  # 7
        (8, TType.I32, 'priority', None, None, ),  # 8
    )

    def __init__(self, notificationId=None, gatewayId=None, title=None, notificationMessage=None, creationTime=None, publishedTime=None, expirationTime=None, priority=None,):
        self.notificationId = notificationId
        self.gatewayId = gatewayId
        self.title = title
        self.notificationMessage = notificationMessage
        self.creationTime = creationTime
        self.publishedTime = publishedTime
        self.expirationTime = expirationTime
        self.priority = priority

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
                    self.notificationId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.gatewayId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.title = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.notificationMessage = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.creationTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.publishedTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I64:
                    self.expirationTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.priority = iprot.readI32()
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
        oprot.writeStructBegin('Notification')
        if self.notificationId is not None:
            oprot.writeFieldBegin('notificationId', TType.STRING, 1)
            oprot.writeString(self.notificationId.encode('utf-8') if sys.version_info[0] == 2 else self.notificationId)
            oprot.writeFieldEnd()
        if self.gatewayId is not None:
            oprot.writeFieldBegin('gatewayId', TType.STRING, 2)
            oprot.writeString(self.gatewayId.encode('utf-8') if sys.version_info[0] == 2 else self.gatewayId)
            oprot.writeFieldEnd()
        if self.title is not None:
            oprot.writeFieldBegin('title', TType.STRING, 3)
            oprot.writeString(self.title.encode('utf-8') if sys.version_info[0] == 2 else self.title)
            oprot.writeFieldEnd()
        if self.notificationMessage is not None:
            oprot.writeFieldBegin('notificationMessage', TType.STRING, 4)
            oprot.writeString(self.notificationMessage.encode('utf-8') if sys.version_info[0] == 2 else self.notificationMessage)
            oprot.writeFieldEnd()
        if self.creationTime is not None:
            oprot.writeFieldBegin('creationTime', TType.I64, 5)
            oprot.writeI64(self.creationTime)
            oprot.writeFieldEnd()
        if self.publishedTime is not None:
            oprot.writeFieldBegin('publishedTime', TType.I64, 6)
            oprot.writeI64(self.publishedTime)
            oprot.writeFieldEnd()
        if self.expirationTime is not None:
            oprot.writeFieldBegin('expirationTime', TType.I64, 7)
            oprot.writeI64(self.expirationTime)
            oprot.writeFieldEnd()
        if self.priority is not None:
            oprot.writeFieldBegin('priority', TType.I32, 8)
            oprot.writeI32(self.priority)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.gatewayId is None:
            raise TProtocolException(message='Required field gatewayId is unset!')
        if self.title is None:
            raise TProtocolException(message='Required field title is unset!')
        if self.notificationMessage is None:
            raise TProtocolException(message='Required field notificationMessage is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
