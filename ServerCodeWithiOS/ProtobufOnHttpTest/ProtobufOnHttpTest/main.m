//
//  main.m
//  ProtobufOnHttpTest
//
//  Created by Fan Lv on 2018/1/19.
//  Copyright © 2018年 DouYu. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "GCDWebServer.h"
#import "GCDWebServerDataResponse.h"
#import "FansMedal.pbobjc.h"

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        // Create server
        GCDWebServer* webServer = [[GCDWebServer alloc] init];
        
        // Add a handler to respond to GET requests on any URL
        [webServer addDefaultHandlerForMethod:@"GET"
                                 requestClass:[GCDWebServerRequest class]
                                 processBlock:^GCDWebServerResponse *(GCDWebServerRequest* request) {

                                     if ([request.path isEqualToString:@"/pb"]) {
                                         FansMedal *fansMedal = [[FansMedal alloc] init];
                                         fansMedal.roomsArray = [[NSMutableArray alloc] init];
                                         for (int i = 0; i<=2 ; i++) {
                                             RoomInfo *roomInfo = [[RoomInfo alloc] init];
                                             roomInfo.md5 = @"437f4ea71386e873d6f5aa31abb9e873";
                                             roomInfo.zipURL = @"https://staticlive.douyucdn.cn/storage/webpic_resources/upload/fans_medal_resource/17cd936c18ca95bf3acfd7068bec9818.zip";
                                             roomInfo.startTime = 1515125290;
                                             roomInfo.endTime = 1517846400;
                                             roomInfo.roomId = @"special_47";
                                             roomInfo.sIdArray = [[NSMutableArray alloc] init];
                                             [roomInfo.sIdArray addObject:@"271934"];
                                             [roomInfo.sIdArray addObject:@"606118"];
                                             [roomInfo.sIdArray addObject:@"70231"];
                                             [roomInfo.sIdArray addObject:@"530791"];
                                             [roomInfo.sIdArray addObject:@"4809"];
                                             [roomInfo.sIdArray addObject:@"677406"];
                                             [roomInfo.sIdArray addObject:@"414818"];
                                             [roomInfo.sIdArray addObject:@"549212"];
                                             [roomInfo.sIdArray addObject:@"1047629"];
                                             [roomInfo.sIdArray addObject:@"2400799"];
                                             [fansMedal.roomsArray addObject:roomInfo];
                                         }
                                         NSData *data = [fansMedal data];
                                         return [GCDWebServerDataResponse responseWithData:data contentType:@"application/x-protobuf"];
                                     }else{
                                         NSString *path = [[NSBundle mainBundle] pathForResource:@"fans_medal" ofType:@"json"];
                                         NSString *content = [[NSString alloc] initWithContentsOfFile:path encoding:NSUTF8StringEncoding error:nil];
                                         return [GCDWebServerDataResponse responseWithHTML:content];
                                      }
                                 }];
        
        // Use convenience method that runs server on port 8080
        // until SIGINT (Ctrl-C in Terminal) or SIGTERM is received
        [webServer runWithPort:8080 bonjourName:nil];
        NSLog(@"Visit %@ in your web browser", webServer.serverURL);

        
    
    }
    return 0;
}
