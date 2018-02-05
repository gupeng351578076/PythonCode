/**
 * Created by mocy on 2018/1/26.
 */
var page = require('webpage').create();
page.viewportSize = {width:1024,height:768};
page.clipRect = {top:0,left:0,width:1024,height:768};
page.open('http://www.csdn.net',function(status){
    console.log('Status:'+status);
    if(status==="success"){
        page.render('example.png');
    }
    phantom.exit();
});