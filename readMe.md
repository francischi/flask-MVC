# Python flask MVC 架構
###### tags: `python` `MVC` `flask` `router` `ORM`
flask為python語言中能夠快速建立web server的輕量級框架，對於寫一些小型服務來說非常方便，但大部分flask教學中都是將所有程式碼寫在一起，若用於撰寫可能只有幾個API的小型服務來說是夠用的，但當來到需要多人開發的大型專案時，就會有將程式碼拆解的必要了。
此架構為現今較流行的MVC，架構如下(此為純前後端分離，因此少了MVC架構中的V)。
除了拆分MVC，還導入了clean architecture，使得程式碼分層更加乾淨。

### Router <=> Controller <=> Service <=> Repository <=> Model <=> DB
-------------------------------------
檔案路徑:

![1](https://github.com/francischi/flask-MVC/blob/master/pic/6-22.PNG?raw=true)

## Router
router的部分使用了flask中的Blueprint註冊進app中，將router獨立出一個py檔案可增加程式碼的可維護性及易讀性，當專案越來越大，API越來越多時，也能夠很好的管理與維護。
## Controllers
controller中只做接收前端傳入參數以及打包response的部分，其餘的事情(例如:商業邏輯，取DB資料，改DB資料...)則放到service與repository中實作。
## Services
service顧名思義就是撰寫所有的服務包括商業邏輯以及輸入參數的檢查，並供controller調用。
## Repository
repository負責與資料庫或任何外部連接(mq、db、cache等等...)。
## OrmModels
OrmModels為與資料庫串接部分，使用SQLAlchemy。