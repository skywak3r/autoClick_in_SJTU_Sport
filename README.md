# autoClick_in_SJTU_Sport
在子衿街值班时时，每次都需要机械的点击鼠标，遂简单学习了下web自动化的selenium库实现简单的网页自动点击，以方便自己以后值班的时候更愉快的摸鱼（bushi


存在的问题：如果正常扫码，可以正常使用。一旦扫到错误的码，就会报错，必须重新运行本程序。（因为扫码成功和扫码失败对应的网页内容修改不同，懒得写错误处理了）

使用说明：
1. 安装python3和selenium库
2. 下载对应浏览器的webdriver，版本号必须一致。
    chrome 浏览器的下载地址：http://chromedriver.storage.googleapis.com/index.html
    
3. 填写登陆的网址和用户名密码，运行此代码即可：

    python autoClick.py
    
### note ：

    本程序仅供本人使用，也仅仅支持特定的系统，登陆网址和用户名密码已经隐去。