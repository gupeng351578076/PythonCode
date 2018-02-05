/**
 * Created by mocy on 2018/1/27.
 */
phantom.outputEncoding = 'gb18030';
var page = require('webpage').create();
//Ä¬ÈÏuserAgent
console.log('the default user agent is'+page.settings.userAgent);
page.settings.userAgent = 'pengpengAgent';
page.open('http://www.baidu.com', function (status) {
    if(status!='success'){
        console.log('unable to access network');
    }else{
        var ua = page.evaluate(function(){
            return document.getElementById('u').textContent;
        });
        console.log(ua);
    }
    phantom.exit();
});