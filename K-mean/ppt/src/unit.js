/**
 * Created by Administrator on 2016/4/8 0008.
 */
define(function(require){
    /**
     * 判断是否为对象
     * @param   {Any}  obj   输入的任意类型
     * @return  {Boolean}   是否为对象
     */
    var isObject = function(obj){
        return Object.prototype.toString.call(obj) == "[object Object]";
    };

    /**
     * 数组去重
     * @param   {Array} arr 输入的数组
     * @return  {Array} 去重后的数组
     */
    var uniqueArr = function(arr){
        var i,j;
        for(i = 0;i<arr.length;i++){
            for(j =i+1;j<arr.length;j++){
                if(arr[i] === arr[j]){
                    arr.splice(j,1);
                    j--;
                }
            }
        }
        return arr;
    };

    /**
     * 实现一个简单的jquery
     * @param   {String}    selector    选择器名称
     * @return  {Element}   DOM元素
     */
    var $ = function(selector){
        var patternId = /(^|\W\s+)#.+$/,
            patternClass = /(^|\W\s+)\..+$/,
            patternElement = /(^|\W\s+)\w+$/;
        selector = selector.trim();
        if(patternId.test(selector)){
            return document.getElementById(selector.slice(1));
        }else if(patternClass.test(selector)){
            return document.getElementsByClassName(selector.slice(1))[0];
        }else if(patternElement.test(selector)){
            return document.getElementsByTagName(selector)[0];
        }else{
            return false;
        }
    };

    /**
     * 绑定事件
     * @param   {Element}   element DOM元素
     * @param   {String}    event   事件名称
     * @param   {Function}  listener    绑定的函数
     */
    var addEvent = function(element,event,listener){
        if(element.addEventListener){
            element.addEventListener(event,listener,false);
        }else if(element.attachEvent){
            element.attachEvent("on"+event,listener);
        }else{
            element["on"+event] = listener;
        }
    };

    /**
     * 获取当前事件
     * @param   {String}    event   事件
     * @return  对event对象的引用
     */
    var EventUnit = {
        getEvent: function(event){
            return event ? event : window.event;
        },
        getTarget: function(event){
            return event.target || event.srcElement;
        }
    };

    var getClientSize = function(){
        var clientW,clientH,scrollTop;
        if(document.compatMode == "BackCompat"){
            clientW = document.body.clientWidth;
            clientH = document.body.clientHeight;
            scrollTop = document.body.scrollHeight
        }else{
            clientW = document.documentElement.clientWidth;
            clientH = document.documentElement.clientHeight;
            scrollTop = document.documentElement.scrollHeight;
        }
        return{
            clientW: clientW,
            clientH: clientH,
            scrollTop: scrollTop
        }
    };

    return{
        isObject: isObject,
        uniqueArr: uniqueArr,
        $: $,
        addEvent: addEvent,
        EventUnit: EventUnit,
        getClientSize: getClientSize
    }
});