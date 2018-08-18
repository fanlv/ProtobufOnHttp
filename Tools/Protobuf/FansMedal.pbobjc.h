// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: fansMedal.proto

// This CPP symbol can be defined to use imports that match up to the framework
// imports needed when using CocoaPods.
#if !defined(GPB_USE_PROTOBUF_FRAMEWORK_IMPORTS)
 #define GPB_USE_PROTOBUF_FRAMEWORK_IMPORTS 0
#endif

#if GPB_USE_PROTOBUF_FRAMEWORK_IMPORTS
 #import <Protobuf/GPBProtocolBuffers.h>
#else
 #import "GPBProtocolBuffers.h"
#endif

#if GOOGLE_PROTOBUF_OBJC_VERSION < 30002
#error This file was generated by a newer version of protoc which is incompatible with your Protocol Buffer library sources.
#endif
#if 30002 < GOOGLE_PROTOBUF_OBJC_MIN_SUPPORTED_VERSION
#error This file was generated by an older version of protoc which is incompatible with your Protocol Buffer library sources.
#endif

// @@protoc_insertion_point(imports)

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"

CF_EXTERN_C_BEGIN

@class RoomInfo;

NS_ASSUME_NONNULL_BEGIN

#pragma mark - FansMedalRoot

/**
 * Exposes the extension registry for this file.
 *
 * The base class provides:
 * @code
 *   + (GPBExtensionRegistry *)extensionRegistry;
 * @endcode
 * which is a @c GPBExtensionRegistry that includes all the extensions defined by
 * this file and all files that it depends on.
 **/
@interface FansMedalRoot : GPBRootObject
@end

#pragma mark - RoomInfo

typedef GPB_ENUM(RoomInfo_FieldNumber) {
  RoomInfo_FieldNumber_RoomId = 1,
  RoomInfo_FieldNumber_StartTime = 2,
  RoomInfo_FieldNumber_EndTime = 3,
  RoomInfo_FieldNumber_Md5 = 4,
  RoomInfo_FieldNumber_ZipURL = 5,
  RoomInfo_FieldNumber_SIdArray = 6,
};

@interface RoomInfo : GPBMessage

@property(nonatomic, readwrite, copy, null_resettable) NSString *roomId;

@property(nonatomic, readwrite) uint64_t startTime;

@property(nonatomic, readwrite) uint64_t endTime;

@property(nonatomic, readwrite, copy, null_resettable) NSString *md5;

@property(nonatomic, readwrite, copy, null_resettable) NSString *zipURL;

@property(nonatomic, readwrite, strong, null_resettable) NSMutableArray<NSString*> *sIdArray;
/** The number of items in @c sIdArray without causing the array to be created. */
@property(nonatomic, readonly) NSUInteger sIdArray_Count;

@end

#pragma mark - FansMedal

typedef GPB_ENUM(FansMedal_FieldNumber) {
  FansMedal_FieldNumber_RoomsArray = 1,
};

@interface FansMedal : GPBMessage

@property(nonatomic, readwrite, strong, null_resettable) NSMutableArray<RoomInfo*> *roomsArray;
/** The number of items in @c roomsArray without causing the array to be created. */
@property(nonatomic, readonly) NSUInteger roomsArray_Count;

@end

NS_ASSUME_NONNULL_END

CF_EXTERN_C_END

#pragma clang diagnostic pop

// @@protoc_insertion_point(global_scope)
