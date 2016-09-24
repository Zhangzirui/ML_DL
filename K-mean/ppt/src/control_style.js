/**
 * Created by Administrator on 2016/4/9 0009.
 */
define(['unit'],function(_){

    var secHeight = _.getClientSize().clientH - 80,
        secWidth = _.getClientSize().clientW,
        num = 1,
        n1 = 2,
        n2 = 2,
        y = 0;

    var initAll = function(){
        initPage();
    };


    var initPage = function(){
        initWH("sec1","row1",0);
        initWH("sec2","row2",secHeight);
        initWH("sec3","row3",secHeight*2);
    };
    /**
     * 配置css样式
     *
     * width and height
     */
    var initWH = function(name1,name2,h){
        _.$("."+name1).style.width = secWidth + "px";
        _.$("."+name1).style.height = secHeight + "px";
        _.$("."+name1).style.transform = "translate3d(0," + h + "px,0)";
        for(var j = 0;j<document.getElementsByClassName(name2).length;j++){
            document.getElementsByClassName(name2)[j].style.width = secWidth + "px";
            document.getElementsByClassName(name2)[j].style.height = secHeight + "px";
            document.getElementsByClassName(name2)[j].style.transform = "translate3d(" + j*secWidth +"px," + "0,0)";
        }
    };

    //----------------------------------事件绑定-----------------------------------------//
    _.addEvent(window,"scroll",function(){
        var scrollT = document.body.scrollTop || document.documentElement.scrollTop;
        if(scrollT === 0){
            _.$("header").style.backgroundColor = "#35b558";
            _.$("header").childNodes[1].style.color = "#ffffff";
            _.$("#content").style.color = "#ffffff";
            _.$("#application").style.color = "#ffffff"
        }else{
            _.$("header").style.backgroundColor = "rgba(255,255,255,0.9)";
            _.$("header").childNodes[1].style.color = "#35b558";
            _.$("#content").style.color = "#35b558";
            _.$("#application").style.color = "#35b558"
        }
    });

    _.addEvent(_.$("#content"),"click",function(){
        var i = 0,
            scrollT = document.body.scrollTop || document.documentElement.scrollTop;
        if(scrollT < secHeight){
            i = scrollT;
            var timer = setInterval(function(){
                document.body.scrollTop = document.documentElement.scrollTop = i;
                if(i >= secHeight - 20){
                    document.body.scrollTop = document.documentElement.scrollTop = secHeight;
                    clearInterval(timer);
                }
                i = i + 20;
            },10);
        }else{
            i = scrollT;
            var timer = setInterval(function(){
                document.body.scrollTop = document.documentElement.scrollTop = i;
                if(i <= secHeight + 20){
                    document.body.scrollTop = document.documentElement.scrollTop = secHeight;
                    clearInterval(timer);
                }
                i = i - 20;
            },10);
        }
    });
    _.addEvent(_.$("#application"),"click",function(){
        var i = 0,
            scrollT = document.body.scrollTop || document.documentElement.scrollTop;
        if(scrollT < secHeight*2){
            i = scrollT;
            var timer = setInterval(function(){
                document.body.scrollTop = document.documentElement.scrollTop = i;
                if(i >= secHeight*2 - 20){
                    document.body.scrollTop = document.documentElement.scrollTop = secHeight*2;
                    clearInterval(timer);
                }
                i = i + 20;
            },10);
        }else{
            i = scrollT;
            var timer = setInterval(function(){
                document.body.scrollTop = document.documentElement.scrollTop = i;
                if(i <= secHeight*2 + 20){
                    document.body.scrollTop = document.documentElement.scrollTop = secHeight*2;
                    clearInterval(timer);
                }
                i = i - 20;
            },10);
        }
    });

    _.addEvent(_.$(".r1-col1-1"),"webkitAnimationEnd",function(e){
        var event = _.EventUnit.getEvent(e),
            target = _.EventUnit.getTarget(event);
        target.style.transform = "translate(-50%,-130%)";
        target.style.webkitTransform = "translate(-50%,-130%)";
        target.className = "r1-col1-1";
        _.$(".r1-col1-2").style.display = "block";
    });

    _.addEvent(_.$(".xDrag"),"click",function(){
        dragScreen("row2",1);
        setTimeout(function(){
            _.$(".goR_L").style.display = "inline";
            _.$(".goR_L").style.zIndex = '2';
        },1000);
    });

    _.addEvent(_.$("#goL"),"click",function(){
        if(num>0){
            num = num - 1;
            dragScreen("row2",num);
        }
    });
    _.addEvent(_.$("#goR"),"click",function(){
        if(num < 7){
            num = num + 1;
            dragScreen("row2",num);
        }

    });

    _.addEvent(_.$(".r2-col3-4"),"change",function(){
        _.$(".r2-col3-2").style.transform = "scale(0.85) translate(-27%,0)";
        _.$(".r2-col3-2").style.wekitTransform = "scale(0.85) translate(-27%,0)";
        _.$(".r2-col3-2").style.width = "50%";
        _.$(".r2-col3-3").style.display = "block";
        _.$(".r2-col3-4").style.display = "none";
        _.$(".r2-col3-5").style.display = "block";
    });

    _.addEvent(_.$(".r2-col3-5"),"click",function(){
        _.$(".r2-col3-1").style.transform = "translate(-65%,0)";
        _.$(".r2-col3-1").style.wekitTransform = "translate(-65%,0)";
        _.$(".r2-col3-3").style.display = "none";
        _.$(".r2-col3-6").style.display = "block";
    });

    _.addEvent(_.$(".r2-col5-3"),"click",function(){
        if(_.$(".r2-col5-4").style.display !== "block"){
            _.$(".r2-col5-2").style.transform = "scale(0.85) translate(-20%,0)";
            _.$(".r2-col5-2").style.wekitTransform = "scale(0.85) translate(-20%,0)";
            _.$(".r2-col5-2").style.width = "50%";
            _.$(".r2-col5-1").style.transform = "translate(-80%,0)";
            _.$(".r2-col5-1").style.wekitTransform = "translate(-80%,0)";
            _.$(".r2-col5-4").style.display = "block";
        }else{
            var x =  _.$(".r2-col5-4").childNodes[1].src.slice(-5,-4),
                x1 = _.$(".r2-col5-4").childNodes[1].src.slice(0,-5),
                imgSrc;
            console.log(x1);
            if(x === "2"){
                imgSrc = x1 + "3.png";
            }else if(x === "3"){
                imgSrc = x1 + "4.png";
            }else if(x === "4"){
                imgSrc = x1 + "2.png";
            }
            _.$(".r2-col5-4").childNodes[1].src = imgSrc;
        }
    });

    _.addEvent(_.$(".r2-col6-3"),"click",function(){
        if(_.$(".r2-col6-4").style.display !== "block"){
            _.$(".r2-col6-2").style.transform = "scale(0.85) translate(-20%,0)";
            _.$(".r2-col6-2").style.wekitTransform = "scale(0.85) translate(-20%,0)";
            _.$(".r2-col6-2").style.width = "56%";
            _.$(".r2-col6-1").style.transform = "translate(-80%,0)";
            _.$(".r2-col6-1").style.wekitTransform = "translate(-80%,0)";
            _.$(".r2-col6-4").style.display = "block";
        }else{
            if (n1 <= 8) {
                var x =  _.$(".r2-col6-4").childNodes[1].src.slice(-1),
                    x1 = _.$(".r2-col6-4").childNodes[1].src.slice(0,-5),
                    imgSrc = x1 + n1 + ".png";
                _.$(".r2-col6-4").childNodes[1].src = imgSrc;
                n1++;
            }else {
                _.$(".r2-col6-3").style.width = "250px";
                _.$(".r2-col6-3").innerHTML = "更新质心7次，到达最优";

            }
        }
    });

    _.addEvent(_.$(".r2-col7-3"),"click",function(){
        if(_.$(".r2-col7-4").style.display !== "block"){
            _.$(".r2-col7-2").style.transform = "scale(0.85) translate(-20%,0)";
            _.$(".r2-col7-2").style.wekitTransform = "scale(0.85) translate(-20%,0)";
            _.$(".r2-col7-2").style.width = "56%";
            _.$(".r2-col7-1").style.transform = "translate(-80%,0)";
            _.$(".r2-col7-1").style.wekitTransform = "translate(-80%,0)";
            _.$(".r2-col7-4").style.display = "block";
        }else{
            if (n2 <= 4) {
                var x =  _.$(".r2-col7-4").childNodes[1].src.slice(-1),
                    x1 = _.$(".r2-col7-4").childNodes[1].src.slice(0,-5),
                    imgSrc = x1 + n2 + ".png";
                _.$(".r2-col7-4").childNodes[1].src = imgSrc;
                n2++;
            }else {
                _.$(".r2-col7-3").style.width = "250px";
                _.$(".r2-col7-3").innerHTML = "更新质心4次，到达最优";

            }
        }
    });

    _.addEvent(_.$(".r2-col8-1"),"dblclick",function(){
        _.$(".r2-col8-1").style.left = "6%";
        _.$(".r2-col8-1").style.top = "8%";
        _.$(".r2-col8-1").innerHTML = "<img src='img/figure_box.png' alt='图片好像不见鸟' />"
    });

    _.addEvent(_.$(".r3-col1-1"),"dblclick",function(){
        if(y == 0){
            _.$(".r3-col1-1").innerHTML = "方案：将这些地方进行聚类，这样就可以安排交通工具抵达这些簇的质心，然后步行到簇内每个景点的地址";
        }else if(y == 1){
            _.$(".r3-col1-1").innerHTML = "<img src='img/figure_application.png' alt='图片好像不见鸟'>";
            _.$(".r3-col1-1").style.top = "0%";
            _.$(".r3-col1-1").style.left = "20%";
        }else if(y == 2){
            _.$(".r3-col1-1").innerHTML = "结束！谢谢！";
            _.$(".r3-col1-1").style.top = "36%";
            _.$(".r3-col1-1").style.left = "38%";
            _.$(".r3-col1-1").style.fontSize = "40px";
        }
        y++;
    });











    //-----------------------------------------------------------------------------------//

    function dragScreen(name,i){
        for(var j = 0;j<document.getElementsByClassName(name).length;j++){
            document.getElementsByClassName(name)[j].style.width = secWidth + "px";
            document.getElementsByClassName(name)[j].style.height = secHeight + "px";
            document.getElementsByClassName(name)[j].style.transform = "translate3d(" + (j-i)*secWidth +"px," + "0,0)";
        }
    }

    return{
        initAll: initAll
    }
});