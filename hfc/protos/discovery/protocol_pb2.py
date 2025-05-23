# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hfc/protos/discovery/protocol.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from hfc.protos.gossip import message_pb2 as hfc_dot_protos_dot_gossip_dot_message__pb2
from hfc.protos.msp import msp_config_pb2 as hfc_dot_protos_dot_msp_dot_msp__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#hfc/protos/discovery/protocol.proto\x12\tdiscovery\x1a\x1fhfc/protos/gossip/message.proto\x1a\x1fhfc/protos/msp/msp_config.proto\"3\n\rSignedRequest\x12\x0f\n\x07payload\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\"Y\n\x07Request\x12+\n\x0e\x61uthentication\x18\x01 \x01(\x0b\x32\x13.discovery.AuthInfo\x12!\n\x07queries\x18\x02 \x03(\x0b\x32\x10.discovery.Query\"3\n\x08Response\x12\'\n\x07results\x18\x01 \x03(\x0b\x32\x16.discovery.QueryResult\"A\n\x08\x41uthInfo\x12\x17\n\x0f\x63lient_identity\x18\x01 \x01(\x0c\x12\x1c\n\x14\x63lient_tls_cert_hash\x18\x02 \x01(\x0c\"\xe8\x01\n\x05Query\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\t\x12.\n\x0c\x63onfig_query\x18\x02 \x01(\x0b\x32\x16.discovery.ConfigQueryH\x00\x12\x34\n\npeer_query\x18\x03 \x01(\x0b\x32\x1e.discovery.PeerMembershipQueryH\x00\x12-\n\x08\x63\x63_query\x18\x04 \x01(\x0b\x32\x19.discovery.ChaincodeQueryH\x00\x12\x30\n\x0blocal_peers\x18\x05 \x01(\x0b\x32\x19.discovery.LocalPeerQueryH\x00\x42\x07\n\x05query\"\xd9\x01\n\x0bQueryResult\x12!\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x10.discovery.ErrorH\x00\x12\x30\n\rconfig_result\x18\x02 \x01(\x0b\x32\x17.discovery.ConfigResultH\x00\x12\x37\n\x0c\x63\x63_query_res\x18\x03 \x01(\x0b\x32\x1f.discovery.ChaincodeQueryResultH\x00\x12\x32\n\x07members\x18\x04 \x01(\x0b\x32\x1f.discovery.PeerMembershipResultH\x00\x42\x08\n\x06result\"\r\n\x0b\x43onfigQuery\"\x82\x02\n\x0c\x43onfigResult\x12/\n\x04msps\x18\x01 \x03(\x0b\x32!.discovery.ConfigResult.MspsEntry\x12\x37\n\x08orderers\x18\x02 \x03(\x0b\x32%.discovery.ConfigResult.OrderersEntry\x1a\x41\n\tMspsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.msp.FabricMSPConfig:\x02\x38\x01\x1a\x45\n\rOrderersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.discovery.Endpoints:\x02\x38\x01\"C\n\x13PeerMembershipQuery\x12,\n\x06\x66ilter\x18\x01 \x01(\x0b\x32\x1c.discovery.ChaincodeInterest\"\xa2\x01\n\x14PeerMembershipResult\x12\x45\n\x0cpeers_by_org\x18\x01 \x03(\x0b\x32/.discovery.PeerMembershipResult.PeersByOrgEntry\x1a\x43\n\x0fPeersByOrgEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.discovery.Peers:\x02\x38\x01\"A\n\x0e\x43haincodeQuery\x12/\n\tinterests\x18\x01 \x03(\x0b\x32\x1c.discovery.ChaincodeInterest\"A\n\x11\x43haincodeInterest\x12,\n\nchaincodes\x18\x01 \x03(\x0b\x32\x18.discovery.ChaincodeCall\"k\n\rChaincodeCall\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x10\x63ollection_names\x18\x02 \x03(\t\x12\x18\n\x10no_private_reads\x18\x03 \x01(\x08\x12\x18\n\x10no_public_writes\x18\x04 \x01(\x08\"I\n\x14\x43haincodeQueryResult\x12\x31\n\x07\x63ontent\x18\x01 \x03(\x0b\x32 .discovery.EndorsementDescriptor\"\x10\n\x0eLocalPeerQuery\"\xf0\x01\n\x15\x45ndorsementDescriptor\x12\x11\n\tchaincode\x18\x01 \x01(\t\x12T\n\x13\x65ndorsers_by_groups\x18\x02 \x03(\x0b\x32\x37.discovery.EndorsementDescriptor.EndorsersByGroupsEntry\x12\"\n\x07layouts\x18\x03 \x03(\x0b\x32\x11.discovery.Layout\x1aJ\n\x16\x45ndorsersByGroupsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.discovery.Peers:\x02\x38\x01\"\x89\x01\n\x06Layout\x12\x45\n\x13quantities_by_group\x18\x01 \x03(\x0b\x32(.discovery.Layout.QuantitiesByGroupEntry\x1a\x38\n\x16QuantitiesByGroupEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"\'\n\x05Peers\x12\x1e\n\x05peers\x18\x01 \x03(\x0b\x32\x0f.discovery.Peer\"i\n\x04Peer\x12$\n\nstate_info\x18\x01 \x01(\x0b\x32\x10.gossip.Envelope\x12)\n\x0fmembership_info\x18\x02 \x01(\x0b\x32\x10.gossip.Envelope\x12\x10\n\x08identity\x18\x03 \x01(\x0c\"\x18\n\x05\x45rror\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\"2\n\tEndpoints\x12%\n\x08\x65ndpoint\x18\x01 \x03(\x0b\x32\x13.discovery.Endpoint\"&\n\x08\x45ndpoint\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\r2F\n\tDiscovery\x12\x39\n\x08\x44iscover\x12\x18.discovery.SignedRequest\x1a\x13.discovery.ResponseB\\\n\'org.hyperledger.fabric.protos.discoveryZ1github.com/hyperledger/fabric-protos-go/discoveryb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'hfc.protos.discovery.protocol_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\'org.hyperledger.fabric.protos.discoveryZ1github.com/hyperledger/fabric-protos-go/discovery'
  _globals['_CONFIGRESULT_MSPSENTRY']._options = None
  _globals['_CONFIGRESULT_MSPSENTRY']._serialized_options = b'8\001'
  _globals['_CONFIGRESULT_ORDERERSENTRY']._options = None
  _globals['_CONFIGRESULT_ORDERERSENTRY']._serialized_options = b'8\001'
  _globals['_PEERMEMBERSHIPRESULT_PEERSBYORGENTRY']._options = None
  _globals['_PEERMEMBERSHIPRESULT_PEERSBYORGENTRY']._serialized_options = b'8\001'
  _globals['_ENDORSEMENTDESCRIPTOR_ENDORSERSBYGROUPSENTRY']._options = None
  _globals['_ENDORSEMENTDESCRIPTOR_ENDORSERSBYGROUPSENTRY']._serialized_options = b'8\001'
  _globals['_LAYOUT_QUANTITIESBYGROUPENTRY']._options = None
  _globals['_LAYOUT_QUANTITIESBYGROUPENTRY']._serialized_options = b'8\001'
  _globals['_SIGNEDREQUEST']._serialized_start=116
  _globals['_SIGNEDREQUEST']._serialized_end=167
  _globals['_REQUEST']._serialized_start=169
  _globals['_REQUEST']._serialized_end=258
  _globals['_RESPONSE']._serialized_start=260
  _globals['_RESPONSE']._serialized_end=311
  _globals['_AUTHINFO']._serialized_start=313
  _globals['_AUTHINFO']._serialized_end=378
  _globals['_QUERY']._serialized_start=381
  _globals['_QUERY']._serialized_end=613
  _globals['_QUERYRESULT']._serialized_start=616
  _globals['_QUERYRESULT']._serialized_end=833
  _globals['_CONFIGQUERY']._serialized_start=835
  _globals['_CONFIGQUERY']._serialized_end=848
  _globals['_CONFIGRESULT']._serialized_start=851
  _globals['_CONFIGRESULT']._serialized_end=1109
  _globals['_CONFIGRESULT_MSPSENTRY']._serialized_start=973
  _globals['_CONFIGRESULT_MSPSENTRY']._serialized_end=1038
  _globals['_CONFIGRESULT_ORDERERSENTRY']._serialized_start=1040
  _globals['_CONFIGRESULT_ORDERERSENTRY']._serialized_end=1109
  _globals['_PEERMEMBERSHIPQUERY']._serialized_start=1111
  _globals['_PEERMEMBERSHIPQUERY']._serialized_end=1178
  _globals['_PEERMEMBERSHIPRESULT']._serialized_start=1181
  _globals['_PEERMEMBERSHIPRESULT']._serialized_end=1343
  _globals['_PEERMEMBERSHIPRESULT_PEERSBYORGENTRY']._serialized_start=1276
  _globals['_PEERMEMBERSHIPRESULT_PEERSBYORGENTRY']._serialized_end=1343
  _globals['_CHAINCODEQUERY']._serialized_start=1345
  _globals['_CHAINCODEQUERY']._serialized_end=1410
  _globals['_CHAINCODEINTEREST']._serialized_start=1412
  _globals['_CHAINCODEINTEREST']._serialized_end=1477
  _globals['_CHAINCODECALL']._serialized_start=1479
  _globals['_CHAINCODECALL']._serialized_end=1586
  _globals['_CHAINCODEQUERYRESULT']._serialized_start=1588
  _globals['_CHAINCODEQUERYRESULT']._serialized_end=1661
  _globals['_LOCALPEERQUERY']._serialized_start=1663
  _globals['_LOCALPEERQUERY']._serialized_end=1679
  _globals['_ENDORSEMENTDESCRIPTOR']._serialized_start=1682
  _globals['_ENDORSEMENTDESCRIPTOR']._serialized_end=1922
  _globals['_ENDORSEMENTDESCRIPTOR_ENDORSERSBYGROUPSENTRY']._serialized_start=1848
  _globals['_ENDORSEMENTDESCRIPTOR_ENDORSERSBYGROUPSENTRY']._serialized_end=1922
  _globals['_LAYOUT']._serialized_start=1925
  _globals['_LAYOUT']._serialized_end=2062
  _globals['_LAYOUT_QUANTITIESBYGROUPENTRY']._serialized_start=2006
  _globals['_LAYOUT_QUANTITIESBYGROUPENTRY']._serialized_end=2062
  _globals['_PEERS']._serialized_start=2064
  _globals['_PEERS']._serialized_end=2103
  _globals['_PEER']._serialized_start=2105
  _globals['_PEER']._serialized_end=2210
  _globals['_ERROR']._serialized_start=2212
  _globals['_ERROR']._serialized_end=2236
  _globals['_ENDPOINTS']._serialized_start=2238
  _globals['_ENDPOINTS']._serialized_end=2288
  _globals['_ENDPOINT']._serialized_start=2290
  _globals['_ENDPOINT']._serialized_end=2328
  _globals['_DISCOVERY']._serialized_start=2330
  _globals['_DISCOVERY']._serialized_end=2400
# @@protoc_insertion_point(module_scope)
