/**
 * Created by mocy on 2018/1/27.
 */
var url = 'http://www.baidu.com';
var page = require('webpage').create();
page.onResourceRequested = function(request){
    console.log('request'+JSON.stringify(request,undefined,4));
};
page.onResourceReceived = function (response) {
    console.log('response'+JSON.stringify(response,undefined,4));
};
page.open(url);
phantom.exit();