#!/bin/bash
#This is Test Shell file

PROJECT_NAME=ProtobufTestClient
CONFIGURATION=Debug
CURRENT_SHEME=ProtobufTestClient
BOUNDLE_VERSION=1.0.0
ROOT_PATH=/Users/fanlv/Documents/MaYun/iOSTest/ProtobufOnHttpTest/ProtobufTestClient
SHELL_PATH=$ROOT_PATH/shells/xocdebuildTest


cd $ROOT_PATH


echo "================= 清除目录 - Start ================="
rm -rf $SHELL_PATH/build
echo "================= 清除目录 - End ================="

xcodebuild -list

echo "================= xcodebuild clean - Start ================="
xcodebuild clean  -workspace  ${PROJECT_NAME}.xcworkspace \
                  -scheme ${CURRENT_SHEME} \
                  -configuration ${CONFIGURATION} \

echo "================= xcodebuild clean - End ================="


echo "================= archive - Start ================="
xcodebuild archive -workspace ${PROJECT_NAME}.xcworkspace \
                   -scheme ${CURRENT_SHEME} \
                   -configuration ${CONFIGURATION} \
                   -archivePath $SHELL_PATH/build/${CURRENT_SHEME}.xcarchive \
                #    -OBJROOT=${SHELL_PATH}/build \
                #    -SYMROOT=${SHELL_PATH}/build \
echo "================= archive - End ================="


echo "================= xcodebuild -exportArchive - Start ================="

xcodebuild -exportArchive -archivePath "$SHELL_PATH/build/${CURRENT_SHEME}.xcarchive" -exportPath $SHELL_PATH/build -exportOptionsPlist $SHELL_PATH/ExportOptions.plist

echo "================= xcodebuild -exportArchive - End ================="
