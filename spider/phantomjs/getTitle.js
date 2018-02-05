/**
 * Created by mocy on 2018/1/27.
 */
var url = 'http://www.baidu.com'
var page = require('webpage').create();
//编码
phantom.outputEncoding = 'gb18030';
//默认控制台输出信息不显示，重写onConsoleMessage让控制台信息显示
page.onConsoleMessage = function(msg){
    console.log(msg);
};
page.open(url, function (status) {
    var title = page.evaluate(function(){
        return document.title;
    });
    console.log('page title is'+title);
    phantom.exit();
});