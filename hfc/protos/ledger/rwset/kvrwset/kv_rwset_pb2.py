# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hfc/protos/ledger/rwset/kvrwset/kv_rwset.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.hfc/protos/ledger/rwset/kvrwset/kv_rwset.proto\x12\x07kvrwset\"\xb3\x01\n\x07KVRWSet\x12\x1e\n\x05reads\x18\x01 \x03(\x0b\x32\x0f.kvrwset.KVRead\x12\x33\n\x12range_queries_info\x18\x02 \x03(\x0b\x32\x17.kvrwset.RangeQueryInfo\x12 \n\x06writes\x18\x03 \x03(\x0b\x32\x10.kvrwset.KVWrite\x12\x31\n\x0fmetadata_writes\x18\x04 \x03(\x0b\x32\x18.kvrwset.KVMetadataWrite\"\x9c\x01\n\x0bHashedRWSet\x12)\n\x0chashed_reads\x18\x01 \x03(\x0b\x32\x13.kvrwset.KVReadHash\x12+\n\rhashed_writes\x18\x02 \x03(\x0b\x32\x14.kvrwset.KVWriteHash\x12\x35\n\x0fmetadata_writes\x18\x03 \x03(\x0b\x32\x1c.kvrwset.KVMetadataWriteHash\"8\n\x06KVRead\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x07version\x18\x02 \x01(\x0b\x32\x10.kvrwset.Version\"8\n\x07KVWrite\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x11\n\tis_delete\x18\x02 \x01(\x08\x12\r\n\x05value\x18\x03 \x01(\x0c\"I\n\x0fKVMetadataWrite\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x07\x65ntries\x18\x02 \x03(\x0b\x32\x18.kvrwset.KVMetadataEntry\"A\n\nKVReadHash\x12\x10\n\x08key_hash\x18\x01 \x01(\x0c\x12!\n\x07version\x18\x02 \x01(\x0b\x32\x10.kvrwset.Version\"F\n\x0bKVWriteHash\x12\x10\n\x08key_hash\x18\x01 \x01(\x0c\x12\x11\n\tis_delete\x18\x02 \x01(\x08\x12\x12\n\nvalue_hash\x18\x03 \x01(\x0c\"R\n\x13KVMetadataWriteHash\x12\x10\n\x08key_hash\x18\x01 \x01(\x0c\x12)\n\x07\x65ntries\x18\x02 \x03(\x0b\x32\x18.kvrwset.KVMetadataEntry\".\n\x0fKVMetadataEntry\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\",\n\x07Version\x12\x11\n\tblock_num\x18\x01 \x01(\x04\x12\x0e\n\x06tx_num\x18\x02 \x01(\x04\"\xc4\x01\n\x0eRangeQueryInfo\x12\x11\n\tstart_key\x18\x01 \x01(\t\x12\x0f\n\x07\x65nd_key\x18\x02 \x01(\t\x12\x15\n\ritr_exhausted\x18\x03 \x01(\x08\x12(\n\traw_reads\x18\x04 \x01(\x0b\x32\x13.kvrwset.QueryReadsH\x00\x12?\n\x13reads_merkle_hashes\x18\x05 \x01(\x0b\x32 .kvrwset.QueryReadsMerkleSummaryH\x00\x42\x0c\n\nreads_info\"/\n\nQueryReads\x12!\n\x08kv_reads\x18\x01 \x03(\x0b\x32\x0f.kvrwset.KVRead\"Z\n\x17QueryReadsMerkleSummary\x12\x12\n\nmax_degree\x18\x01 \x01(\r\x12\x11\n\tmax_level\x18\x02 \x01(\r\x12\x18\n\x10max_level_hashes\x18\x03 \x03(\x0c\x42r\n2org.hyperledger.fabric.protos.ledger.rwset.kvrwsetZ<github.com/hyperledger/fabric-protos-go/ledger/rwset/kvrwsetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'hfc.protos.ledger.rwset.kvrwset.kv_rwset_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n2org.hyperledger.fabric.protos.ledger.rwset.kvrwsetZ<github.com/hyperledger/fabric-protos-go/ledger/rwset/kvrwset'
  _globals['_KVRWSET']._serialized_start=60
  _globals['_KVRWSET']._serialized_end=239
  _globals['_HASHEDRWSET']._serialized_start=242
  _globals['_HASHEDRWSET']._serialized_end=398
  _globals['_KVREAD']._serialized_start=400
  _globals['_KVREAD']._serialized_end=456
  _globals['_KVWRITE']._serialized_start=458
  _globals['_KVWRITE']._serialized_end=514
  _globals['_KVMETADATAWRITE']._serialized_start=516
  _globals['_KVMETADATAWRITE']._serialized_end=589
  _globals['_KVREADHASH']._serialized_start=591
  _globals['_KVREADHASH']._serialized_end=656
  _globals['_KVWRITEHASH']._serialized_start=658
  _globals['_KVWRITEHASH']._serialized_end=728
  _globals['_KVMETADATAWRITEHASH']._serialized_start=730
  _globals['_KVMETADATAWRITEHASH']._serialized_end=812
  _globals['_KVMETADATAENTRY']._serialized_start=814
  _globals['_KVMETADATAENTRY']._serialized_end=860
  _globals['_VERSION']._serialized_start=862
  _globals['_VERSION']._serialized_end=906
  _globals['_RANGEQUERYINFO']._serialized_start=909
  _globals['_RANGEQUERYINFO']._serialized_end=1105
  _globals['_QUERYREADS']._serialized_start=1107
  _globals['_QUERYREADS']._serialized_end=1154
  _globals['_QUERYREADSMERKLESUMMARY']._serialized_start=1156
  _globals['_QUERYREADSMERKLESUMMARY']._serialized_end=1246
# @@protoc_insertion_point(module_scope)
