/**
 * Created by mocy on 2018/1/27.
 */
var url = 'http://www.baidu.com'
var page = require('webpage').create();
//����
phantom.outputEncoding = 'gb18030';
//Ĭ�Ͽ���̨�����Ϣ����ʾ����дonConsoleMessage�ÿ���̨��Ϣ��ʾ
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