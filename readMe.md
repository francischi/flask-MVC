# Python flask MVC 架構
###### tags: `python` `MVC` `flask` `router` `ORM`
flask為python語言中能夠快速建立web server的輕量級框架，對於寫一些小型服務來說非常方便，但大部分flask教學中都是將所有程式碼寫在一起，若用於撰寫可能只有幾個API的小型服務來說是夠用的，但當來到需要多人開發的大型專案時，就會有將程式碼拆解的必要了。
此架構為現今較流行的MVC，架構如下(此為純前後端分離，因此少了MVC架構中的V)。

### Router <=> Controller <=> Service <=> Model <=> DB
檔案路徑:

![1](./pic/6-21.png)
