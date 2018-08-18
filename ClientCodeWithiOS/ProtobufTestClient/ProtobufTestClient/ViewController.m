//
//  ViewController.m
//  ProtobufTestClient
//
//  Created by Fan Lv on 2018/1/19.
//  Copyright © 2018年 DouYu. All rights reserved.
//

#import "ViewController.h"
#import "FansMedal.pbobjc.h"

#define SCREEN_HEIGHT                   [[UIScreen mainScreen] bounds].size.height
#define SCREEN_WIDTH                    [[UIScreen mainScreen] bounds].size.width

@interface ViewController ()
{
    UILabel *_infolabel;
    UITextView *_textView;
}
@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    _textView = [[UITextView alloc] initWithFrame:CGRectMake(0,64, SCREEN_WIDTH, 200)];
    _textView.editable = NO;
    _textView.font = [UIFont systemFontOfSize:16];
    _textView.backgroundColor = [UIColor grayColor];
    [self.view addSubview:_textView];
    
    _infolabel = [[UILabel alloc] initWithFrame:CGRectMake(10, 280, SCREEN_WIDTH - 20, 30)];
    _infolabel.textColor = [UIColor blackColor];
    _infolabel.font = [UIFont systemFontOfSize:12];
    _infolabel.text = @"数据大小：0K";
    [self.view addSubview:_infolabel];

    UIButton *aBtn = [[UIButton alloc] initWithFrame:CGRectMake(10, 340, SCREEN_WIDTH - 20, 50)];
    aBtn.backgroundColor = [UIColor orangeColor];
    aBtn.layer.cornerRadius = 25;
    aBtn.clipsToBounds = YES;
    [aBtn setTitle:@"请求" forState:UIControlStateNormal];
    [aBtn addTarget:self action:@selector(requestHttp) forControlEvents:UIControlEventTouchUpInside];
    [self.view addSubview:aBtn];
    
    UIButton *bBtn = [[UIButton alloc] initWithFrame:CGRectMake(10, 400, SCREEN_WIDTH - 20, 50)];
    bBtn.backgroundColor = [UIColor orangeColor];
    bBtn.layer.cornerRadius = 25;
    bBtn.clipsToBounds = YES;
    [bBtn setTitle:@"请求Protobuf格式数据" forState:UIControlStateNormal];
    [bBtn addTarget:self action:@selector(requestHttpProtobuf) forControlEvents:UIControlEventTouchUpInside];
    [self.view addSubview:bBtn];

}

- (void)requestHttp
{
    NSDate *startDate = [NSDate date];
    for (int i = 0; i<=100 ; i++) {
        [self getUrl:@"http://127.0.0.1:8080/" dataBody:nil Completetion:^(id result, NSError *error) {
            if (!error && [result isKindOfClass:[NSData class]]) {
                NSData *data = (NSData *)result;
                NSError *pError;
                id obj = [NSJSONSerialization JSONObjectWithData:data options:NSJSONReadingAllowFragments error:&pError];
                if (!pError && i==100) {
                    NSDate *endDate1 = [NSDate date];
                    _infolabel.text = [NSString stringWithFormat:@"数据大小 ： %.3f KB, 请求耗时：%f",[data length]/1000.0,[endDate1 timeIntervalSinceDate:startDate]];
                    _textView.text = [obj description];
                }
            }
        }];
    }
}


- (void)requestHttpProtobuf
{
    
    NSDate *startDate = [NSDate date];
    
    for (int i = 0; i<=100 ; i++) {
        [self getUrl:@"http://127.0.0.1:8080/pb" dataBody:nil Completetion:^(id result, NSError *error) {
            if (!error && [result isKindOfClass:[NSData class]]) {
                NSData *data = (NSData *)result;
                NSError *pError;
                FansMedal *fansMedal = [[FansMedal alloc] initWithData:data error:&pError];
                if (!pError && i==100) {
                    NSDate *endDate1 = [NSDate date];
                    _infolabel.text = [NSString stringWithFormat:@"数据大小 ： %.3f KB, 请求耗时：%f",[data length]/1000.0,[endDate1 timeIntervalSinceDate:startDate]];
                    _textView.text = fansMedal.description;
                }
            }
        }];

    }
}

- (void)getUrl:(NSString *)url dataBody:(NSDictionary *)dataBody Completetion:(void (^) (id result,NSError * error))completion
{
    if ([url length] == 0) completion(@"",nil);
    
    
    NSString *urlWithGetParm = url;//[self addCommonData:dataBody ToUrl:url];
    
    
    //第一步，创建URL
    NSURL *tmpUrl = [NSURL URLWithString:urlWithGetParm];
    //第二步，通过URL创建网络请求
    //NSURLRequest初始化方法第一个参数：请求访问路径，第二个参数：缓存协议，第三个参数：网络请求超时时间（秒）
    NSURLRequest *request = [[NSURLRequest alloc]initWithURL:tmpUrl cachePolicy:NSURLRequestUseProtocolCachePolicy timeoutInterval:10];
    
    
    
    [[[NSURLSession sharedSession] dataTaskWithRequest:request
                                     completionHandler:^(NSData * _Nullable data, NSURLResponse * _Nullable response, NSError * _Nullable error) {
                                         NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *) response;
                                         
                                         //                                         NSLog(@"response status code: %ld", (long)[httpResponse statusCode]);
                                         if ([httpResponse statusCode] == 200)
                                         {
                                             //                                             NSString *aString = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];
                                             //                                             NSLog(@"%@",aString);
//                                             NSError *error1;
//                                             id returnValue = [NSJSONSerialization JSONObjectWithData:data options:NSJSONReadingAllowFragments error:&error1];
                                             dispatch_async(dispatch_get_main_queue(), ^{
                                                 completion(data,nil);
                                             });
                                             
                                         }
                                         else
                                         {
                                             dispatch_async(dispatch_get_main_queue(), ^{
                                                 completion(nil,error);
                                             });

                                         }
                                         
                                     }] resume];
    
}



@end
