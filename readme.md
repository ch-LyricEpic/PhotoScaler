# PhotoScaler
一款极简主义小工具, 以便于部署至静态托管网页的HTML形式展示你的照片.

### 使用办法与注意事项
1.Clone该库到本地, 往/assets文件夹下放入你的照片. **请注意:照片文件名默认情况下不允许有```. -```等字符**. 然后将你的照片重命名, 在保留后缀的情况下使用简短的文字描述你的照片.  
2.如果有对照片按序排列的需求, 则重命名照片为```ID-DESCRIPTION.FORMAT```格式. 其中: ID参数为照片编号, 为自然数字. DESCRIPTION参数为照片描述, FORMAT参数即为照片后缀名, 无需更改. 例如, 一张合法可被展示的照片命名应为: ```1-20240101 新年好!.jpg```.而 ```1-2024.01.01 新年好!.jpg```则不被允许, 因为它在DESCRIPTION参数中包含```.```这一字符.  
3.在完成照片操作后确保计算机安装Python 3.x, 并确保```requirements.txt```中所有Python库都已安装.随后运行```main.py```.没有被编号的自然格式图片在此时将被自动编号.  
4.运行正常后即可访问```index.html```.

### 代码说明
**这是我拿来练手的小项目 所以代码很史 见谅哈。**  
· 带下划线的三个程序一般是subprocess内容, 无需独立运行, 已被```main.py```集成  

· ```data.txt```和```script.js```都是由本程序自动生成的必需文件, 其中```data.txt```直接记录```/assets```下所有图片的文件名, ```script.js```即为三件套(```index.html```,```style.css```,```script.js```)之一,由```backup.js```进行填充imageFiles得到(我只是为了规避一个很愚蠢的 CORS 问题,但这样我觉得也是一种很清新脱俗的实现方式,直接隔离开可变数据把js框架单独拎出来维护,算是一种尝试?)  

· ```debugtool-localserver.py```是debugtool.用于快速建立localhost服务器.  

· ```requirements.txt```中存放了本项目所依赖的Python库名称.  

### 待办
1.美化UI    
2.实现DESCRIPTION参数对```.```的支持.  

### LICENSE
MIT
