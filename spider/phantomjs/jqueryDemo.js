/**
 * Created by mocy on 2018/1/27.
 */
var page = require('webpage').create();
page.open('https://www.baidu.com',function(){
    page.includeJs('http://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js',function(){
        page.evaluate(function(){
            return a = $("button").click();
            console.log(a)
        });
        phantom.exit();
    });
});