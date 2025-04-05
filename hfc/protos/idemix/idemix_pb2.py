# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hfc/protos/idemix/idemix.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ehfc/protos/idemix/idemix.proto\"\x1b\n\x03\x45\x43P\x12\t\n\x01x\x18\x01 \x01(\x0c\x12\t\n\x01y\x18\x02 \x01(\x0c\"6\n\x04\x45\x43P2\x12\n\n\x02xa\x18\x01 \x01(\x0c\x12\n\n\x02xb\x18\x02 \x01(\x0c\x12\n\n\x02ya\x18\x03 \x01(\x0c\x12\n\n\x02yb\x18\x04 \x01(\x0c\"\xd9\x01\n\x0fIssuerPublicKey\x12\x17\n\x0f\x61ttribute_names\x18\x01 \x03(\t\x12\x12\n\x04h_sk\x18\x02 \x01(\x0b\x32\x04.ECP\x12\x14\n\x06h_rand\x18\x03 \x01(\x0b\x32\x04.ECP\x12\x15\n\x07h_attrs\x18\x04 \x03(\x0b\x32\x04.ECP\x12\x10\n\x01w\x18\x05 \x01(\x0b\x32\x05.ECP2\x12\x14\n\x06\x62\x61r_g1\x18\x06 \x01(\x0b\x32\x04.ECP\x12\x14\n\x06\x62\x61r_g2\x18\x07 \x01(\x0b\x32\x04.ECP\x12\x0f\n\x07proof_c\x18\x08 \x01(\x0c\x12\x0f\n\x07proof_s\x18\t \x01(\x0c\x12\x0c\n\x04hash\x18\n \x01(\x0c\"7\n\tIssuerKey\x12\x0b\n\x03isk\x18\x01 \x01(\x0c\x12\x1d\n\x03ipk\x18\x02 \x01(\x0b\x32\x10.IssuerPublicKey\"S\n\nCredential\x12\x0f\n\x01\x61\x18\x01 \x01(\x0b\x32\x04.ECP\x12\x0f\n\x01\x62\x18\x02 \x01(\x0b\x32\x04.ECP\x12\t\n\x01\x65\x18\x03 \x01(\x0c\x12\t\n\x01s\x18\x04 \x01(\x0c\x12\r\n\x05\x61ttrs\x18\x05 \x03(\x0c\"X\n\x0b\x43redRequest\x12\x11\n\x03nym\x18\x01 \x01(\x0b\x32\x04.ECP\x12\x14\n\x0cissuer_nonce\x18\x02 \x01(\x0c\x12\x0f\n\x07proof_c\x18\x03 \x01(\x0c\x12\x0f\n\x07proof_s\x18\x04 \x01(\x0c\"\x98\x03\n\tSignature\x12\x15\n\x07\x61_prime\x18\x01 \x01(\x0b\x32\x04.ECP\x12\x13\n\x05\x61_bar\x18\x02 \x01(\x0b\x32\x04.ECP\x12\x15\n\x07\x62_prime\x18\x03 \x01(\x0b\x32\x04.ECP\x12\x0f\n\x07proof_c\x18\x04 \x01(\x0c\x12\x12\n\nproof_s_sk\x18\x05 \x01(\x0c\x12\x11\n\tproof_s_e\x18\x06 \x01(\x0c\x12\x12\n\nproof_s_r2\x18\x07 \x01(\x0c\x12\x12\n\nproof_s_r3\x18\x08 \x01(\x0c\x12\x17\n\x0fproof_s_s_prime\x18\t \x01(\x0c\x12\x15\n\rproof_s_attrs\x18\n \x03(\x0c\x12\r\n\x05nonce\x18\x0b \x01(\x0c\x12\x11\n\x03nym\x18\x0c \x01(\x0b\x32\x04.ECP\x12\x15\n\rproof_s_r_nym\x18\r \x01(\x0c\x12\"\n\x13revocation_epoch_pk\x18\x0e \x01(\x0b\x32\x05.ECP2\x12\x19\n\x11revocation_pk_sig\x18\x0f \x01(\x0c\x12\r\n\x05\x65poch\x18\x10 \x01(\x03\x12\x31\n\x14non_revocation_proof\x18\x11 \x01(\x0b\x32\x13.NonRevocationProof\"J\n\x12NonRevocationProof\x12\x16\n\x0erevocation_alg\x18\x01 \x01(\x05\x12\x1c\n\x14non_revocation_proof\x18\x02 \x01(\x0c\"Y\n\x0cNymSignature\x12\x0f\n\x07proof_c\x18\x01 \x01(\x0c\x12\x12\n\nproof_s_sk\x18\x02 \x01(\x0c\x12\x15\n\rproof_s_r_nym\x18\x03 \x01(\x0c\x12\r\n\x05nonce\x18\x04 \x01(\x0c\"\x90\x01\n\x1f\x43redentialRevocationInformation\x12\r\n\x05\x65poch\x18\x01 \x01(\x03\x12\x17\n\x08\x65poch_pk\x18\x02 \x01(\x0b\x32\x05.ECP2\x12\x14\n\x0c\x65poch_pk_sig\x18\x03 \x01(\x0c\x12\x16\n\x0erevocation_alg\x18\x04 \x01(\x05\x12\x17\n\x0frevocation_data\x18\x05 \x01(\x0c\x42&Z$github.com/hyperledger/fabric/idemixb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'hfc.protos.idemix.idemix_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z$github.com/hyperledger/fabric/idemix'
  _globals['_ECP']._serialized_start=34
  _globals['_ECP']._serialized_end=61
  _globals['_ECP2']._serialized_start=63
  _globals['_ECP2']._serialized_end=117
  _globals['_ISSUERPUBLICKEY']._serialized_start=120
  _globals['_ISSUERPUBLICKEY']._serialized_end=337
  _globals['_ISSUERKEY']._serialized_start=339
  _globals['_ISSUERKEY']._serialized_end=394
  _globals['_CREDENTIAL']._serialized_start=396
  _globals['_CREDENTIAL']._serialized_end=479
  _globals['_CREDREQUEST']._serialized_start=481
  _globals['_CREDREQUEST']._serialized_end=569
  _globals['_SIGNATURE']._serialized_start=572
  _globals['_SIGNATURE']._serialized_end=980
  _globals['_NONREVOCATIONPROOF']._serialized_start=982
  _globals['_NONREVOCATIONPROOF']._serialized_end=1056
  _globals['_NYMSIGNATURE']._serialized_start=1058
  _globals['_NYMSIGNATURE']._serialized_end=1147
  _globals['_CREDENTIALREVOCATIONINFORMATION']._serialized_start=1150
  _globals['_CREDENTIALREVOCATIONINFORMATION']._serialized_end=1294
# @@protoc_insertion_point(module_scope)
