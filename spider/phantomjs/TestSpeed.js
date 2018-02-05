/**
 * Created by mocy on 2018/1/26.
 */
var page =require('webpage').create(),
    system = require('system'),
    t,address;
if(system.args.length===1){
    console.log('usage:TestSpeed.js<some URL>');
    phantom.exit();
}
t = Date.now();
address = system.args[1];
page.open(address,function(status){
    if(status!='success'){
        console.log('fail to load address')
    }else {
        t = Date.now() - t;
        console.log('loading' + system.args[1]);
        console.log('loadtime' + t + 'mses')
    }
    phantom.exit();
})