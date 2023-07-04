Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
==================== RESTART: C:/Users/HP/Desktop/allnode.py ===================
共 12 个节点
html head title body div ul li a li a li a 
>>> 
==================== RESTART: C:/Users/HP/Desktop/allnode.py ===================
共 12 个节点
html head title body div ul li a li a li a 
html
 head
  title
 body
  div
   ul
    li
     a
    li
     a
    li
     a
>>> 
==================== RESTART: C:/Users/HP/Desktop/allnode.py ===================
共 12 个节点
html head title body div ul li a li a li a 
html
 head
  title
 body
  div
   ul
    li
     a
    li
     a
    li
     a
共 3 个a节点
123 456 789 
>>> 
================= RESTART: C:/Users/HP/Desktop/childrennode.py =================
共 3 个节点
123 456 789 
>>> 
================= RESTART: C:/Users/HP/Desktop/childrennode.py =================
共 3 个节点
123 456 789 共 3 个节点
123 456 789 
>>> 
================= RESTART: C:/Users/HP/Desktop/childrennode.py =================
共 3 个节点
123 456 789 
共 3 个节点
123 456 789 
>>> 
================== RESTART: C:/Users/HP/Desktop/parentnodes.py =================
Traceback (most recent call last):
  File "C:/Users/HP/Desktop/parentnodes.py", line 4, in <module>
    result = tree.xpath('//a[@href = "123.html"]/../[@class]')
  File "src\lxml\etree.pyx", line 2296, in lxml.etree._ElementTree.xpath
  File "src\lxml\xpath.pxi", line 357, in lxml.etree.XPathDocumentEvaluator.__call__
  File "src\lxml\xpath.pxi", line 225, in lxml.etree._XPathEvaluatorBase._handle_result
lxml.etree.XPathEvalError: Invalid expression
>>> 
================== RESTART: C:/Users/HP/Desktop/parentnodes.py =================
['item1']
>>> 
==================== RESTART: C:/Users/HP/Desktop/propery.py ===================
Traceback (most recent call last):
  File "C:/Users/HP/Desktop/propery.py", line 5, in <module>
    print(result.text)
AttributeError: 'list' object has no attribute 'text'
>>> 
==================== RESTART: C:/Users/HP/Desktop/propery.py ===================
123
>>> 
==================== RESTART: C:/Users/HP/Desktop/propery.py ===================
123
123
>>> 
==================== RESTART: C:/Users/HP/Desktop/propery.py ===================
123
123
['123.html']
>>> 
=================== RESTART: C:/Users/HP/Desktop/xpath 运算符.py ==================
123 123.html
456 456.html
>>> 
=================== RESTART: C:/Users/HP/Desktop/ordernode.py ==================
[<Element a at 0x19d6efb1bc0>, <Element a at 0x19d6efb1b80>, <Element a at 0x19d6efb1a00>] []
>>> 
=================== RESTART: C:/Users/HP/Desktop/ordernode.py ==================
['123', '456', '789'] []
>>> 
=================== RESTART: C:/Users/HP/Desktop/ordernode.py ==================
['123', '456', '789'] []
>>> 
=================== RESTART: C:/Users/HP/Desktop/ordernode.py ==================
[] []
>>> 
=================== RESTART: C:/Users/HP/Desktop/ordernode.py ==================
[] []
>>> 
=================== RESTART: C:/Users/HP/Desktop/ordernode.py ==================
[] []
>>> 
=================== RESTART: C:/Users/HP/Desktop/ordernode.py ==================
[] []
>>> 
=================== RESTART: C:/Users/HP/Desktop/ordernode.py ==================
[] []
>>> 
=================== RESTART: C:/Users/HP/Desktop/ordernode.py ==================
[] []
>>> 
=================== RESTART: C:/Users/HP/Desktop/ordernode.py ==================
[] [] []
>>> 
=================== RESTART: C:/Users/HP/Desktop/ordernode.py ==================
[<Element a at 0x1b340e5fdc0>] [<Element a at 0x1b340e5fd80>] [<Element a at 0x1b340e5fdc0>, <Element a at 0x1b340e5fd80>, <Element a at 0x1b340e5fc00>]
>>> 
=================== RESTART: C:/Users/HP/Desktop/ordernode.py ==================
['123'] [<Element a at 0x20e88d4fe40>] [<Element a at 0x20e88d4fe00>, <Element a at 0x20e88d4fe40>, <Element a at 0x20e88d4fc80>]
>>> 
=================== RESTART: C:/Users/HP/Desktop/ordernode.py ==================
['123'] ['456'] ['123', '456', '789']
>>> 
=================== RESTART: C:/Users/HP/Desktop/ordernode.py ==================
['123'] ['456'] ['123', '456', '789']
['789']
>>> 
=================== RESTART: C:/Users/HP/Desktop/ordernode.py ==================
['123'] ['456'] ['123', '456', '789']
['789']
['456', '789']
>>> 
=================== RESTART: C:/Users/HP/Desktop/ordernode.py ==================
['123'] ['456'] ['123', '456', '789']
['789']
['456', '789']
['123']
>>> 
=================== RESTART: C:/Users/HP/Desktop/autoxpath.py ==================
Traceback (most recent call last):
  File "C:/Users/HP/Desktop/autoxpath.py", line 5, in <module>
    tree = etree.parse(r,etree.HTMLParser())
  File "src\lxml\etree.pyx", line 3521, in lxml.etree.parse
  File "src\lxml\parser.pxi", line 1882, in lxml.etree._parseDocument
TypeError: cannot parse from 'Response'
>>> 
=================== RESTART: C:/Users/HP/Desktop/autoxpath.py ==================
Traceback (most recent call last):
  File "C:/Users/HP/Desktop/autoxpath.py", line 5, in <module>
    tree = etree.parse(r.text(),etree.HTMLParser())
TypeError: 'str' object is not callable
>>> 
=================== RESTART: C:/Users/HP/Desktop/autoxpath.py ==================
Traceback (most recent call last):
  File "C:/Users/HP/Desktop/autoxpath.py", line 5, in <module>
    print(r.text())
TypeError: 'str' object is not callable
>>> 
=================== RESTART: C:/Users/HP/Desktop/autoxpath.py ==================
<Response [200]>
Traceback (most recent call last):
  File "C:/Users/HP/Desktop/autoxpath.py", line 6, in <module>
    tree = etree.parse(r.text(),etree.HTMLParser())
TypeError: 'str' object is not callable
>>> 
=================== RESTART: C:/Users/HP/Desktop/autoxpath.py ==================

Traceback (most recent call last):
  File "C:/Users/HP/Desktop/autoxpath.py", line 6, in <module>
    tree = etree.parse(r.text,etree.HTMLParser())
  File "src\lxml\etree.pyx", line 3521, in lxml.etree.parse
  File "src\lxml\parser.pxi", line 1859, in lxml.etree._parseDocument
  File "src\lxml\parser.pxi", line 1885, in lxml.etree._parseDocumentFromURL
  File "src\lxml\parser.pxi", line 1789, in lxml.etree._parseDocFromFile
  File "src\lxml\parser.pxi", line 1177, in lxml.etree._BaseParser._parseDocFromFile
  File "src\lxml\parser.pxi", line 615, in lxml.etree._ParserContext._handleParseResultDoc
  File "src\lxml\parser.pxi", line 725, in lxml.etree._handleParseResult
  File "src\lxml\parser.pxi", line 652, in lxml.etree._raiseParseError
OSError: Error reading file '<!DOCTYPE html>
<html>

<head>
    <meta charset="utf8" version='1'/>
    <title>京东(JD.COM)-正品低价、品质保障、配送及时、轻松购物！</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=yes"/>
    <meta name="description"
          content="京东JD.COM-专业的综合网上购物商城，为您提供正品低价的购物选择、优质便捷的服务体验。商品来自全球数十万品牌商家，囊括家电、手机、电脑、服装、居家、母婴、美妆、个护、食品、生鲜等丰富品类，满足各种购物需求。"/>
    <meta name="Keywords" content="网上购物,网上商城,家电,手机,电脑,服装,居家,母婴,美妆,个护,食品,生鲜,京东"/>
    <script type="text/javascript">
        window.point = {}
        window.point.start = new Date().getTime()
    </script>
    <link rel="dns-prefetch" href="//static.360buyimg.com"/>
    <link rel="dns-prefetch" href="//misc.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img10.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img11.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img12.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img13.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img14.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img20.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img30.360buyimg.com"/>
    <link rel="dns-prefetch" href="//d.3.cn"/>
    <link rel="dns-prefetch" href="//d.jd.com"/>
    <link rel="icon" href="//www.jd.com/favicon.ico" mce_href="//www.jd.com/favicon.ico" type="image/x-icon"/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>
    <meta name="renderer" content="webkit"/>

    <!--[if lte IE 6]>
    <script src="//misc.360buyimg.com/mtd/pc/index/home/ie6tip.min.js"></script>
    <![endif]-->
    <!--[if IE 8]>
    <script src="//misc.360buyimg.com/mtd/pc/index_2019/1.0.0/static/lib/polyfill/index.js"></script>
    <![endif]-->

    <link href="//misc.360buyimg.com/mtd/pc/index_2019/1.0.0/static/css/first-screen.chunk.css" rel="stylesheet"/>

    <link href="//misc.360buyimg.com/mtd/pc/index_2019/1.0.0/static/css/index.chunk.css" rel="stylesheet"/>
    <script type="text/javascript">
        window.point.css = new Date().getTime()
    </script>
    <script type="text/javascript">
        window.pageConfig = {};
		//灰度区间统一配置
		window.pageConfig.hashList ={"research":[{"start":"0","end":"10000"},{"start":"10000","end":"10000"}],"navitems":[{"start":"0","end":"0"},{"start":"0","end":"10000"}],"treasure":[{"start":"0","end":"10000"},{"start":"10000","end":"10000"}],"floor":[{"start":"0","end":"10000"},{"start":"10000","end":"10000"}],"schoolFloor":[{"start":"0","end":"10000"},{"start":"10000","end":"10000"}],"top":[{"start":"0","end":"10000"},{"start":"10000","end":"10000"}],"recommend":[{"start":"0","end":"10000"},{"start":"10000","end":"10000"}],"channels":[{"start":"0","end":"10000"},{"start":"10000","end":"10000"}]};

        // 大促配置
        window.promotional = {};
        window.promotional.enableShowToolbar = false;

        window.pageConfig.enableShowSpecialTop = false;

        window.promotional.enableShowTop = false;

        window.promotional.actTimeStart = new Date('2022/05/23 14:00:00').getTime();

		window.promotional.actTimeEnd = new Date('2022/06/20 23:59:59').getTime();

		        window.promotional.atmosphere = {};

		window.promotional.atmosphere.background = 'jfs/t1/175008/40/24062/2774/62871bf5E90bce82e/ce484c2ce3c9c8da.png';

		window.promotional.atmosphere.desc = 'jfs/t1/184633/20/25322/3751/6287380eE54718a8e/288c72d11132fb3d.png';

		window.promotional.newEnjoyType = 'S2';

        // 兜底数据
        window.backup = {};
        //logo
         window.pageConfig.logo = {};

        //直通车
        window.pageConfig.treasure = {};

        window.pageConfig.treasureb = {};

        //企业定投直通车
        window.pageConfig.treasureEnterprise  = {};

        //背板
        window.pageConfig.background = {};

        window.pageConfig.shortcutCompanyConfigType="default";
window.pageConfig.headServiceType="default";
window.pageConfig.headSiteNavType="default";
window.pageConfig.headShiLaoHua="true";
window.pageConfig.enableGraySwitch="false";
window.pageConfig.cateType="default";
window.pageConfig.enableJquerySwitch="true";
window.pageConfig.enableFooterConfigSwitch="true";
        //企业背板
        window.pageConfig.backgroundEnterprise = {"bothBgPic":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/109040\/35\/30908\/41245\/62e727caE16216303\/25329f665ad10e38.jpg","href":"https:\/\/pro.jd.com\/mall\/active\/3y1FpcGL5htF5QLw7ShgEZkKV9WQ\/frist.html"};

        // 页面配置
        window.pageConfig.enableActMark = false;

		window.pageConfig.clstagPrefix = 'h|keycount|';

		window.pageConfig.O2_REPORT = 100;

		window.pageConfig.serverTime = new Date('2022/08/01 16:25:02').getTime();

		window.pageConfig.actStart = new Date('2019/10/18 00:00:00').getTime();

		window.pageConfig.actEnd = new Date('2019/11/15 23:59:59').getTime();

        // 手机京东
        window.pageConfig.shortcutMobileData=[{"title":"\u624b\u673a\u4eac\u4e1c","desc":"\u65b0\u4eba\u4e13\u4eab\u5927\u793c\u5305","img":"jfs\/t1\/67481\/15\/565\/28110\/5cec9234E71c47244\/dc4cf353fd96922e.png","url":"","devices":[{"type":"iphone","src":"https:\/\/itunes.apple.com\/cn\/app\/id414245413"},{"type":"android","src":"https:\/\/storage.jd.com\/jdmobile\/JDMALL-PC2.apk"},{"type":"ipad","src":"https:\/\/itunes.apple.com\/cn\/app\/jing-dong-hd\/id434374726"}]},{"title":"\u5173\u6ce8\u4eac\u4e1cJD.COM","desc":"\u62a25\u5143\u7ea2\u5305","img":"jfs\/t1\/133427\/32\/6189\/44062\/5f2a5467Efff804d1\/7cbc252ed5993190.png","url":"","devices":[]},{"title":"\u4eac\u4e1c\u91d1\u878d\u5ba2\u6237\u7aef","desc":"\u65b0\u4eba\u4e13\u4eab\u5927\u793c\u5305","img":"jfs\/t1\/36947\/5\/10895\/15408\/5cec924bE6c038530\/5cf21582b416c186.jpg","url":"https:\/\/m.jr.jd.com\/integrate\/download\/html\/pc.html","devices":[{"type":"iphone","src":"https:\/\/itunes.apple.com\/cn\/app\/jing-dong-jin-rong-hui-li\/id895682747?mt=8"},{"type":"android","src":"http:\/\/211.151.9.66\/downapp\/jrapp_jr188.apk"}]},{"title":"\u4eac\u4e1c\u5065\u5eb7\u5ba2\u6237\u7aef","desc":"","img":"jfs\/t1\/93019\/8\/17752\/28300\/5e8c23b8E4c6c7c13\/9c45c518ad785873.png","url":"","devices":[{"type":"iphone","src":"https:\/\/hlc.m.jd.com\/download\/?downloadSource=jdh_JDcom"},{"type":"android","src":"https:\/\/hlc.m.jd.com\/download\/?downloadSource=jdh_JDcom"}]},{"title":"\u5173\u6ce8\u4eac\u4e1c\u5c0f\u7a0b\u5e8f","desc":"\u65b0\u4eba0.1\u5143\u8d2d","img":"jfs\/t1\/170279\/40\/10824\/19657\/6045bf7dE610d6258\/3e925badd90757a3.jpg","url":"","devices":[]}];

        //今日推荐
        window.backup.today=[{"alt":"\u4f01\u4e1a\u5f00\u5de5\u5b63","ext_columns":{"biclk":"1#a889a3b4cf7bd9198608242923b049cfdec968df-103-619066#43494363","focustype":"s","ap":"K7+n7uMbemcyifAhDdq5Ig==","mcinfo":"03652902-17044221-8101610722-M#0-2-1--59--#1-tb-#102-43494363#pc-home","url":"https:\/\/pro.jd.com\/mall\/active\/33FkET36YNBaCuLwF3GqnCbLr4uT\/frist.html?babelChannel=ttt2","desc":"\u7cbe\u9009\u7206\u6b3e","text":"\u4f01\u4e1a\u5f00\u5de5\u5b63"},"src":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/6851\/13\/21644\/93283\/61f50444Eebe6975f\/03dee49c7825b83d.png","gid":"03652902","href":"https:\/\/pro.jd.com\/mall\/active\/33FkET36YNBaCuLwF3GqnCbLr4uT\/frist.html?babelChannel=ttt2","srcB":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/6851\/13\/21644\/93283\/61f50444Eebe6975f\/03dee49c7825b83d.png","type":"material"},{"alt":"","ext_columns":{"biclk":"1#a889a3b4cf7bd9198608242923b049cfdec968df-103-619066#43494363","focustype":"s","ap":"p7XPj53+XCTIQN3wwN6XDg==","mcinfo":"03652902-17044221-8101611040-M#0-2-1--59--#1-tb-#102-43494363#pc-home","url":"https:\/\/pro.jd.com\/mall\/active\/DMQAamMysqjZ7ZDWHFTBc6ocHAv\/frist.html","desc":"","text":""},"src":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/116864\/1\/21079\/53025\/61ff9962E196a5844\/c1b0bcc5845ad614.jpg","gid":"03652902","href":"https:\/\/pro.jd.com\/mall\/active\/DMQAamMysqjZ7ZDWHFTBc6ocHAv\/frist.html","srcB":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/116864\/1\/21079\/53025\/61ff9962E196a5844\/c1b0bcc5845ad614.jpg","type":"material"},{"ext_columns":{"focustype":"g"},"type":"ad","href":"https:\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9scHMuamQuY29tL3BjL3BzcC81MDE3MDExP2ltdXA9Q2g0S0dPVzV2LVczbnVTN2dlUzRtdVNfb2VhQnItZW5rZWFLZ0JJQUdBQVNHZ2l6bTdJQ0VQT2E2OXdER2dodWEzbDRlWEY0Y3lEQUJpZ0JHTm9oSUFBcUlHbGlMSFZoTEhoblpTeG5hV0VzWTJsbUxHWmZZbUZmWm14ZmJERTJNek00TWdKcFlrcW5BVWw4VTBoVlRsUmZTVUlzU1Y5QlgwWk1YMElzU1Y5QlgxSkZYMElzU1Y5QlgxQk1YMElzU1Y5QlgxTk1YMElzU1Y5QlgwTlRYMElzU1Y5QlgxSlRYMElzU1Y5VlgwWk1YMElzU1Y5VFgwWk1YMElzU1Y5U1gwWk1YMElzU1Y5UVgwWk1YMElzU1Y5SFgxSk1YMElzU1Y5SFgxaEhYMUlzU1Y5Q1gwWk1YMUlzUjBsQkxGaEhSU3hWUVh3N1JueE5TVmhVUVVkZlJsSXNSbDlDUVY5R1RGOU1NVFl6TXpoOA&log=GAzYUXYleBiYx0yi3tCBS_1z9BscamtkMEa4naoSoI8F4fSENdrxcaC38YMbZREFpsXjXNB4_Ypm53RtKSHBrazQvD1ci4f4r3NxR-yU37iCyPP0Nx3Ksdo9hVXBwTt3HNCuZKimPzdqV8DuXlDgrFWcxkJOjuSYNOSTOKruMd5nib6Ke85jPV59_TNBOxLuz40xpc0K52c5pb2BW-CidRAwuvEJ2UV2pu2ACc5TnQYOoIFfvqnq_pjIGT5OzW1vmGodybyGxpjZPg5LOzlzGCmErNpxLG8KmmtZuAHBwJv5a6hRyJMefh3cM2PX42YYmRUhyd1ZWU3KNsK4cmpbU1tiwiDP09sYWdIH1PwB6Xc4YYmcK-kfjde6dbUWd03FaALzdP9hAl1Mlx8Kpt3WxbXQSV6bYzerVLLN7Yxsp7V--fI1C5uABMVtDvu0dVwlkn514XsVQ-PoyMoyTYItSW4k_7U7MrhCBHtupFLJo6EDu1ZZ0r5CUAQ4jUaeQKpwflnnm2IvkrMdtXbxQEmcro5wxUC1XBhINeohtirkRbGkoyIsQ_2tx-EcXDmU7VWrN76AjLom69JO5Dg6bn1Nln7UWlXCXVjkUPnw6VasWvMVFLomIju6G2gv9pJ-6LbxbmwZQQqzSOHa2LENDMNoiw3UcfWYInAXwkzkyyjMV6AOgeUhU_tvmcjpEwiY9a_0KqHNs5Iq2wzhfbwezNb7mEjMJj3tSASBdppSEShPAn2-t9aBir0DnNhKXZNc2Q3-36CF8Lm0n7w34cs61JbOZTY5NkTeTgJ7YHVUMyH_6Srjt7Yu45-S8_bZrM8Bvu59zI8SfGdwY9lOqh6xtVov3aNHrKsb_1t8E0B1qQcJqU7uxoLs8xe8rQbso2IZ_zoomIHHLUBw_jh09gmx_QfALz0KFHgMWW2Y7PUhz-zc9BDl79oyrvk9UWrxdFX9M5hN-QLGcnpTw9U8LpxLP8zWO1NwaoJBvVx1DT4oKx65OQznXSWxxrAyK3lhHjbpUKByLwsS-x94Pj4G6Vh-_D_x-sH_wRLNOgrz11q2hygreZYQaAFP-EdREzDYm5impKFX1zbwTQ1jMLYvsx5a96hOHCRh-pnpPDuJ4H3bFLyPJLnW-B-hsPwNC7zOd4SWlw90&v=404","src":"https:\/\/img1.360buyimg.com\/da\/jfs\/t1\/104009\/20\/18514\/63913\/5e94f1a7Ef66e61f6\/5c41baf664c71c25.png","clog":"https:\/\/im-x.jd.com\/dsp\/np?log=GAzYUXYleBiYx0yi3tCBS_1z9BscamtkMEa4naoSoI8F4fSENdrxcaC38YMbZREFpsXjXNB4_Ypm53RtKSHBrazQvD1ci4f4r3NxR-yU37iCyPP0Nx3Ksdo9hVXBwTt3HNCuZKimPzdqV8DuXlDgrFWcxkJOjuSYNOSTOKruMd5nib6Ke85jPV59_TNBOxLuz40xpc0K52c5pb2BW-CidRAwuvEJ2UV2pu2ACc5TnQYOoIFfvqnq_pjIGT5OzW1vm9wMFMUIdcSqGleQ7DBERpB23DfOdDkfBgrEcyPckgwSOGz6_ea1d3RhiQ0RfaT8i9FfpupZbQSJUJ9Ka-ZQ2JXZbXkKX5LpsFFDBo1MkUcGWMD5MmFmX4YNfWTVijMbXuF6rsUKQept-5qNj1h0EXrt_nLI9-8-yGsh0kOlHbtDPhBImL0D2ATTMocFmNNClp8Ku3y9wAn9b4KEzzGYXr4YxPjmkCP4B4XxXXmxAOba0eudmGHtheAO6ZaHNj9IB9zzoSvFYPCMdVnRI5MiH9PIFalXjQpicQAkHCWzlfutKJYMTUf0EFYwrYr-WKcIWI8fCQ-d7ypUPe-zrC5iTXcF-1uFtusPEFkmLHMQ6YO5XXy6NSO465S11eVyVDf3nsRYE60H9kgrysqWPSW6g50BMlDBQFD2QyDsyXVw-OTWNd6p5QpdLa6nut_x-MaQwmHbMmwajW3cBTIBFRSCZg3i88J0ECjnmNcf-B30FGEGvPGIfyIDzaenYvdaA1DpHsOobR1faNHgJURHZP0Y52sqa0OfdnDpD5D4B0s96YbRfOCCh_UIsEGLtgcT2ohcmLjhJRGhTIDN-GjgFZfURlusSJ-aCA6e_POrD80CCOAkiXeBxZpZV_dgu3P5uEC9JdenLqNEbXcrZnmQCacb9iCg7cCdjDNzN0m57lah9sffuP9uRdA5YOjvQ7e3F-tiihHvIxWVJV5f4LYXHcSq0A8newQoDu59EgWnjC218SmjhtnqPQNMk_Z6vxh3ZuDIM_UhVVwY_YyfNlTCuxQgf4ACHT4j37Frwt8-tLHkwYS0gj6ixux5dEg_0DCIttDOtzrEIAJZgLluCwBxfmc-64AHTHO7IIxC-ic3cG8LiTqVpx239kby0Q6-B-ZLl_kY&v=404&seq=1"},{"ext_columns":{"focustype":"g"},"type":"ad","href":"https:\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9scHMuamQuY29tL3BjL3BzcC85ODQyMjI_aW11cD1DaDRLR09XNXYtVzNudVM3Z2VTNG11U19vZWFCci1lbmtlYUtnQklBR0FBU0ZRaWVpVHdRcE1EcjNBTWFCSGhuWkhvZ3N3VW9BUmphSVNBQUtpQnBZaXgxWVN4NFoyVXNaMmxoTEdOcFppeG1YMkpoWDJac1gyd3hOak16T0RJQ2FXSktwd0ZKZkZOSVZVNVVYMGxDTEVsZlFWOUdURjlDTEVsZlFWOVNSVjlDTEVsZlFWOVFURjlDTEVsZlFWOVRURjlDTEVsZlFWOURVMTlDTEVsZlFWOVNVMTlDTEVsZlZWOUdURjlDTEVsZlUxOUdURjlDTEVsZlVsOUdURjlDTEVsZlVGOUdURjlDTEVsZlIxOVNURjlDTEVsZlIxOVlSMTlTTEVsZlFsOUdURjlTTEVkSlFTeFlSMFVzVlVGOE8wWjhUVWxZVkVGSFgwWlNMRVpmUWtGZlJreGZUREUyTXpNNGZB&log=GAzYUXYleBiYx0yi3tCBS_1z9BscamtkMEa4naoSoI-CJarMJhq6_agQ762Wvx24jWEpt2TB8lW0fsIYlP4Fe-seuZoGZlp6l8wgBEGBCrnpg3X_k-a_n-DwR0gszKeuhP2dFWx5X1KFBBnt2O_11cwDJ8_olKV3TM1s9e43ULmOHGBMHBCwE141418YwuCuujf2Be2NohSbNu1LI8p2y_tLKno3b2dW2MjLtvcLN7vItTry-ohHHcwC7H32MnTQ0WSiuw91rbCrNqpzSl8XWQEqTyusHQDJvQpxzel7FBUwg1nvs5o4wdkl_zLEfRGXmuAv9fXxmsBHvq8SMDZ-XhllnkemJnRwLf0GFTHuQz13m-YRl_Q7Z4TSNxX80LBbr79MC7fbkpFrOWqV3imz0bNkmyZXRvyNUxzK1ZEczJqOH4Y-DZDOsDH8HC_xaYD9zBYZqyMb0HkTLz2E2zMVUECw0sQam5QJ7Fl1Sk3W_G2ZtA3-3D2_HUQm2MBO6pTNknOgp38W3Pk3qzM3Ilvc2sOBaPAcUlCg_12fCdUIs6YTKSMvsKbmQOQUvGMDNX1acDc1m-RYyed9Ws1A_4UljrZCWXXR3awKfg7_1A5RA5OxKusLaF8uAzGBW4GLVyVPp6bzOcGX38F7-pebU6syqF9XTkoTd8S4-oTepaNYwLo89BY1S5y3TwYkDpZPImNJa-XJEEkDI9Ok3iPG0OysFE8rcCoGxGdVQRXIroxef0FbrbbekRb8CfGJUqt8c_4zFIsiESHn5PAqhCpzWsbtCTn-2mCiXskQ9FW_N4T41wR8QU8nqRWbUFlErK5TCjEf_0qZvxrl9BAr_Yc8cLM6Mt--rPpdB9zJ7NprZHwFebNDBGP6dmDpLvSelXhNnUS69xIsA7mJlE_8UcRSLsQlcAoaT9yOmrzoeHwbGwcu7vqTzPq_gaTyzOlXxpiefflWsF5dcxUguhmP9ZmLnwks9jTJVYikn8LTrM-lSAWNb3YuvwyKPI8T1ZJCQWtt0Bg-o4IDoNXiBknLwOhuamnmcfUtt0wpsBSZYyqGv-Nct-Kd2lCuo5IiFh0XXHJV9PVb59EkFL_tcuLaJOIHbuDYBIHpgem8qWqJii2Dl8GoAeg&v=404","src":"https:\/\/img1.360buyimg.com\/da\/jfs\/t1\/65519\/18\/5109\/86986\/5d349331E52fea75f\/5671237d9584131b.png","clog":"https:\/\/im-x.jd.com\/dsp\/np?log=GAzYUXYleBiYx0yi3tCBS_1z9BscamtkMEa4naoSoI-CJarMJhq6_agQ762Wvx24jWEpt2TB8lW0fsIYlP4Fe-seuZoGZlp6l8wgBEGBCrnpg3X_k-a_n-DwR0gszKeuhP2dFWx5X1KFBBnt2O_11cwDJ8_olKV3TM1s9e43ULmOHGBMHBCwE141418YwuCuujf2Be2NohSbNu1LI8p2y_tLKno3b2dW2MjLtvcLN7vItTry-ohHHcwC7H32MnTQbuspoohbCGR5W77K4uX6JU3jKd0rINTxk70lAYmurUFNjb-BvvKvwQjsqHj2iXRVq6LJheU-nCPwUNkRSz7dGGxuyZoTfik4p_r2otcpi-JHG9MhAzFFjThvONi28IfKBCYqM__5Y8KM9FizlxdZrIN7JW_DhewNPz_41pameKPfrFd0FnfsZcy-vvyZCrTvb-4P_TkUt-mnjMVDNx5OJ8DUlUtPv2oA3YNgvzeuo95j8Ql12y7mFXxsg-SilVJMo_s67ZXnW9J9vL88hoSmnPp7Gq1oIVEDzhYY_2SfSEIVp-mE44HPidftXOjI9_KNQc0rTtuOny0-EvG_w4uR45t18GlSvvMDsemVK1_DtnLJ4mh0X7-MCQCGsOUWxMxGLl_-k1lf2K7DMTL6w3RpMf3rSAXRXFXUPPt6D4-Q1pXL4iJ1vU8BYkCOrrnrG5lgy9tA1Ev60tS-1l9M0UI6AEHN415TUVu-V0ZHwSoYbKdYPEoQm6vCNePdJXquM5QHgd_ohcIF97vuTdBX1OZKG1hRhv5Euysm_iK4y9c8AdecjndizrcyS1ix6Qs3lfIEL2uZiy6f9Pye8lwXnnAKy_5Ngc-p8XysQGG6ZzcBftY-E5sw6al9c_5JxJsIgrSza8qVlawtwzjg1Yk4ezNX73xnR7Btd6KpOlIQ8eSTgiPjRelco3rGJlXgU18JAYQPT6Hbhpzp6SWDvyBCjOflyBOgVU2uCRTclhBX2G6TOxPwIHBRarL6JQ-StOPQB6hH3lSlfgEXRFogBwaP9UsRLsovureecA-yWvsP6N5EzA7jhoWO-Rh5NcHJeTpLCDo8SeHboTS23XulEcaNOETdK90EA1X77cbkUpwRHHXrUwY&v=404&seq=2"},{"alt":"","ext_columns":{"biclk":"1#a889a3b4cf7bd9198608242923b049cfdec968df-103-619066#43494363","focustype":"s","ap":"j0Spnb54kus=","mcinfo":"03652902-17044221-8101611202-M#0-2-1--59--#1-tb-#102-43494363#pc-home","url":"https:\/\/prodev.jd.com\/mall\/active\/gi4Pq4ek5494Wu2stU11VwjK9iS\/frist.html","desc":"","text":""},"src":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/94432\/11\/20795\/78385\/62012655Ed228f0b7\/367cca04c2aa3077.jpg","gid":"03652902","href":"https:\/\/prodev.jd.com\/mall\/active\/gi4Pq4ek5494Wu2stU11VwjK9iS\/frist.html","srcB":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/94432\/11\/20795\/78385\/62012655Ed228f0b7\/367cca04c2aa3077.jpg","type":"material"},{"alt":"","ext_columns":{"biclk":"1#a889a3b4cf7bd9198608242923b049cfdec968df-103-619066#43494363","focustype":"s","ap":"z\/ep\/M8C9uoBBlITEyBAiQ==","mcinfo":"03652902-17044221-8101611231-M#0-2-1--59--#1-tb-#102-43494363#pc-home","url":"https:\/\/pro.jd.com\/mall\/active\/kdLV9FcYcKP6s7KdLRVcEPqrUrg\/frist.html?babelChannel=ttt2","desc":"","text":""},"src":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/87414\/17\/21797\/50526\/62010949E99c1a828\/71dc7e61d06f9a36.jpg","gid":"03652902","href":"https:\/\/pro.jd.com\/mall\/active\/kdLV9FcYcKP6s7KdLRVcEPqrUrg\/frist.html?babelChannel=ttt2","srcB":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/87414\/17\/21797\/50526\/62010949E99c1a828\/71dc7e61d06f9a36.jpg","type":"material"},{"ext_columns":{"focustype":"g"},"type":"ad","href":"https:\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9scHMuamQuY29tL3BjL3BzcC83MzAyNDM5P2ltdXA9Q2g0S0dPVzV2LVczbnVTN2dlUzRtdVNfb2VhQnItZW5rZWFLZ0JJQUdBQVNGZ2luMnIwREVPeWM2OXdER2dSa2JHUnpJS3NVS0FFWTJpRWdBQ29nYVdJc2RXRXNlR2RsTEdkcFlTeGphV1lzWmw5aVlWOW1iRjlzTVRZek16Z3lBbWxpU3FjQlNYeFRTRlZPVkY5SlFpeEpYMEZmUmt4ZlFpeEpYMEZmVWtWZlFpeEpYMEZmVUV4ZlFpeEpYMEZmVTB4ZlFpeEpYMEZmUTFOZlFpeEpYMEZmVWxOZlFpeEpYMVZmUmt4ZlFpeEpYMU5mUmt4ZlFpeEpYMUpmUmt4ZlFpeEpYMUJmUmt4ZlFpeEpYMGRmVWt4ZlFpeEpYMGRmV0VkZlVpeEpYMEpmUmt4ZlVpeEhTVUVzV0VkRkxGVkJmRHRHZkUxSldGUkJSMTlHVWl4R1gwSkJYMFpNWDB3eE5qTXpPSHc&log=GAzYUXYleBiYx0yi3tCBS_1z9BscamtkMEa4naoSoI_wQyoHBV5oLDP5wj4Lm6249pyEIshvL3a0kk99Gx7WEB0khRkNhmOPvlXQY7qpYl9u5K23WRZOEmU30WDXW_dlJFxaeh19H7rea1Gf6-JaTYjEhRWP8sjPpHXNVbzhYvVyMAhxWyCgQ5H6opF9C4aW5L0kllYbyAAfSMOgqLqcTDlZilc98ZpZINH6twfJb-haFi9wWch4y3iXjQ8_nEjnZeDvS2v77CDX_IyF-u_td7YRyLbHZadEeSWXKVJQ8CMBDkUvpnPSerEcD2HSdPuiGuqt4b7yTL5jJy_2GrQCxLfjJri6vssxeYnLfm0798OSvj-PA6YhqOPiaSBk3v58eqX1Ofaj9rCjKa5m45DaLQF0e6RggqoMtzrV8-YOCicxVbvrpDfHUmLwC9lKu2oO01ye_aDhMGiEgux6wdiCzjeBz0Q5iJsSVOYzMVFtkKOCfEuptI-azusJcusoGxfmT0L0hnR-XyB0xxnDhQ-XZhKYC-sVqbgmta5UhmKZGtpuPUyXhtvbtvFr2VWW30AHYd-bqB7IhwabIgcCrHzQSQ-8da_KsjpAJIHbQgXdaIRhhDqOxLQHdbuBpQFTcLTs-bRc0cLLfgEG7TlnHCSbPAgonxcZP3HtbtnYJgiVsncfq9YmspTpPR8rqivNflJqERGU5C_f8g07qepu2_xwFB6AS3SCD2MzHxErXDgDthZ-MzZQXLyv9rkIED2_1R_mtCmEHOmL234ie85-ceuPe4ba6gxjNnFJbUDc9lBy98uxle5zBHEGmLMrOgc18wisaNPjEoti3GmPGxTl6CkY-P9RvXUQ75sRU2hJcFmw9ye1Qeo-3ulNHV7Tvmek76J7Tqv-T-QP9a1ALGsMHG0UNxULUtvb0ajs7klneRy0jA_R3W1VZ2mRN9ythOCe_-b-QI_O9TPWHB25DgErWomr6C1JU1NKT69VYHzuEOhz70lOgEXe_-T8AgeLeKpMpaMdiFlkVdZ_3APferq4pwENbUY10anJWgwlpehckGwcsJkzOwa-Rj8eOufOY_u9TPJEHdzmQJ-BKEwGkr9MfqoBDHfl0wly1NRZ_uYRdmyfkqcFCmzbfKqtRhw0j2E9kEBq&v=404","src":"https:\/\/img1.360buyimg.com\/da\/jfs\/t1\/39535\/22\/12149\/77249\/5d337987Ea4fc5f10\/29ba50d1c1eca3bf.png","clog":"https:\/\/im-x.jd.com\/dsp\/np?log=GAzYUXYleBiYx0yi3tCBS_1z9BscamtkMEa4naoSoI_wQyoHBV5oLDP5wj4Lm6249pyEIshvL3a0kk99Gx7WEB0khRkNhmOPvlXQY7qpYl9u5K23WRZOEmU30WDXW_dlJFxaeh19H7rea1Gf6-JaTYjEhRWP8sjPpHXNVbzhYvVyMAhxWyCgQ5H6opF9C4aW5L0kllYbyAAfSMOgqLqcTDlZilc98ZpZINH6twfJb-haFi9wWch4y3iXjQ8_nEjnZANYZSU-C5r6PfQFDsmwPn-SdG2TPy5DFbOQxQios5sxrx9SY1NhtyC0VSEA1ArTsEkHVjPINaIBVv2FJV4pwrkG0XLKK6nqTZdLU_ZaqnkHgfamAniGNJU_bYp7VxS8DH8wLDDVLLexChHhtwkC8fuyx2oH8K_uKH66nE1xfW3yY-S-BFQ7Ol3QRskJ2rRsqVeLIaVEVuaB0Ru-G-guctz5I6zGAGvqsYa8A6iIepr-zm4DXRwmakAh4J_L-BxxZtCi6cGlN99Q7I77LIUrhdyFRPvwfILR0ZY7nAbv6e4zxLlC4LBWVRgfD2A4NWZWs1ailY3EdxKXZV0AF1xuZrTGrkrKuEsJMIEtqYuE1Qgv7Z92cjiGTzBTN58Q-oczXGqHf-aCLlj88lKvAI_-YeHKoAZcJz424cn3LxvFrlQbckkXYWeOQ2fe-xu9qIPuqhmhgg7AQScd1-eyZu8e3_7hvrcRrOM7o9DwxnbDESVLaJPCgElKBCcp8Qzs0Xp4nHNXJKbbU-XI4qwn98nOWfvej2jRfnXGx95Yy8WHzjZH2mcRg4ms-l1EtXhxI7jO1Y6K5sTiLsIyFfNyDD-JE00RPxAEPeXbNJt_-y2nXOid76NI_0XGHC4ReSk6w12_23ltmagvmUKPVmHZzn5omAAWx5CVmCKeEyUHf5XTyxikzJb-V6zkHnnynFw4Niw6Ui9kb6DELV8vh-26qmMefxOmxG59YRvHKa6I0LZRJqSM8prQUT5NhuAfYmwb2gZj3dRpMtA3-LYmVDmkEpWPKQtb17XPcWWSybfXsOxBfdkLnHolwJ0a8QH-EiE7OvrJ9Ay2-wlDlrt8TWV0JJLNXbsh4ZoWggqkBURybN2ZCpb1VgEkIwLvjVDinu2r_iJ_&v=404&seq=3"},{"alt":"\u5546\u7528\u5f00\u5de5\u5b63","ext_columns":{"biclk":"1#a889a3b4cf7bd9198608242923b049cfdec968df-103-619066#43494363","focustype":"s","ap":"9gLGFXP7q4f4h0Arqq\/GuA==","mcinfo":"03652902-17044221-8101610921-M#0-2-1--59--#1-tb-#102-43494363#pc-home","url":"https:\/\/shang.jd.com\/","desc":"\u5546\u7528\u5f00\u5de5\u5b63","text":"\u5546\u7528\u5f00\u5de5\u5b63"},"src":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/120972\/34\/22737\/59798\/61f5468aEcfcd30bd\/3e4c9f12dac8e80b.jpg","gid":"03652902","href":"https:\/\/shang.jd.com\/","srcB":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/120972\/34\/22737\/59798\/61f5468aEcfcd30bd\/3e4c9f12dac8e80b.jpg","type":"material"},{"alt":"","ext_columns":{"biclk":"1#a889a3b4cf7bd9198608242923b049cfdec968df-103-619066#43494363","focustype":"s","ap":"yxgo8R761YABBlITEyBAiQ==","mcinfo":"03652902-17044221-8101611201-M#0-2-1--59--#1-tb-#102-43494363#pc-home","url":"https:\/\/prodev.jd.com\/mall\/active\/34qAaUk6AW39g9BX6me3z2F6pYUG\/frist.html","desc":"","text":""},"src":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/116391\/11\/27363\/76966\/6200d724E4fde75ac\/861537c907516dbf.jpg","gid":"03652902","href":"https:\/\/prodev.jd.com\/mall\/active\/34qAaUk6AW39g9BX6me3z2F6pYUG\/frist.html","srcB":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/116391\/11\/27363\/76966\/6200d724E4fde75ac\/861537c907516dbf.jpg","type":"material"}];

        //首焦兜底(新)
        window.backup.focusbak=[[{"sourceTag":"1","id":"4272","extension_id":"{\"ad\":\"\",\"ch\":\"\",\"shop\":\"\",\"sku\":\"\",\"ts\":\"\",\"uniqid\":\"{\\\"material_id\\\":\\\"7524724277\\\",\\\"pos_id\\\":\\\"4272\\\",\\\"sid\\\":\\\"9d49653d-53db-4d6f-ab0c-2bbf5f35961a\\\",\\\"type\\\":\\\"1\\\"}\"}","ad_billing_type":2,"src":"https:\/\/img1.360buyimg.com\/pop\/jfs\/t1\/40588\/8\/17960\/59407\/62e34ddcE9dbbf4f6\/553bb2b4bf1dbc0c.jpg","ext_columns":{"desc":"2:cpd","focustype":"h"},"href":"https:\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9wcm9kZXYuamQuY29tL21hbGwvYWN0aXZlLzI1aUJxVlFBZFFoQkdLWG16TkFzVkFBS3JnWjcvaW5kZXguaHRtbD9iYWJlbENoYW5uZWw9dHR0MzU&log=sxgVFd7XnnnBm45udPwF6cwXCmE6XtxGUOaO57KRUEc97ymba0k0gfJQRZdv_2NRMbIpKrLKDBWfDuNu77ypx98OTC1MgzrUgfcwzI5sv3UavDj-gJCylIEJuRAmSWTieNYAbd-456xq5qmiytkhhUEFuz8yfEmtbSdXJzBDcdmOWEP_6oCVBYG23KDgbBBiIBW-N0EQHeG-bXdrE5Lgn-kEy0tveUWoaintLhuvIIEpl_mKIcDDr1VIV2KrGKemt6TPbzUf_-_H-j3jD7hsMmkGyxjcG_3zDU-NaaFnDP1rn5Hg-JIfiJyxQB6lEn34kruMLYTIIsVd_Sr3ppPMBrpAACAz9wr6REbpGF1kehXT1MAx8leugf_skv3Pax1-5f_68CePeMf-raUq0-J9isOXNCbb0_-ThkJwbITxBEDqcvZFp4gOCtbT-rOBBTRgZ1VGVlme9314xCmvAt11mu9TsK2mqigqJ8eGTk3OfEtIGpJzJb7EgaOHVKD_T6OLs4kZ1sBjyXVBAJbPpTJfCvZysrBH56M1sVnx0OLfB2qk2FYvnto-5nTilcOM-PSCxx2zWRPkHFjQ8XZk1M1kw-pWH2z38EjwaCbqojDUHO5NcU2zkkTMdg2wTnAJaQ7_3eiHkMaYWFkeFfjfH_7avCN-OioecSonyBJVA2fdb5qM-CYaYBgp4batRTKXo9EjVepg-3ejnpS5e0d5A4Pc2HdjfOAtMNBkyPKrcL01iaHl3X_x2fgMTKjy1WR_1ha5YVP7bTdWT0VUphYW3VwGfgcQizzaAMPPA2GV42F3-h0PM0r5NP3___ntNG5JG7KQr0qcmJiu7ec1LKwUHRplD7c__PA641ktcK2uXTHVjQNvwjL2XmEu8R2ZvqZHdwbwpIPJFO4C1GPJYbB5bArIJJHlHaerbg0B9Sa3viAYh1dO-pEUqCTf385Qw5ZKRzwFfo-K2SBEVbNa3kwTqyLITre1ah58SgPTmpIgy9F_c1_HmKPOmdbnexvwLKkA02UvLf6Fcjn1ZNmb0M8LNnG-CxN421gri3IG6Nz8vFGJo7M&v=404","clog":"https:\/\/im-x.jd.com\/dsp\/np?log=sxgVFd7XnnnBm45udPwF6cwXCmE6XtxGUOaO57KRUEc97ymba0k0gfJQRZdv_2NRMbIpKrLKDBWfDuNu77ypx98OTC1MgzrUgfcwzI5sv3UavDj-gJCylIEJuRAmSWTieNYAbd-456xq5qmiytkhhUEFuz8yfEmtbSdXJzBDcdmOWEP_6oCVBYG23KDgbBBiQ4iussP9JOW3sr2-CKwJnPIOrgqSoAK9cruGP5VEG2_e2-kIV0KzOlABaGeg_XYDcsUgHG14Qhg3QY0q35DQJcDIFRkE6ZJ6o-Xvs486Vqh7bW5drP9P5eYJLmAaDZZ1EQ7vND-e2G9BuC27q77bWQWFiALm1d_ZvCin8PJeo0BkMeBMPCf868qxZb4zRfpupk1J7csTKkK12n4YIKGpK_SVLpwd1oIl07TO-v2rXVbPL1FvAPC0HJSIuirqnSoRiAXdqRjUXbRdjS7P5mi1mwWd4cJPjbOoJDjT2bkl-hC-vadOPekIDYsGwl25MTiaW9NjZjKiW6cbClxSmSmNmIEQMrGMzIbJjamC3w908uu-12FUzzR-ToAWhPifIMwIgPkhT8p27npDnpMO9UxmMz0Ph6-TKZrbwm7v3zH-XNTIUsvtVX33JeIXrjPrAuu2NtwSMHIZXop_C2scUM6LP0vb81sb-lF8QFFRFfyiNR3TTD6WNc3xEhWGmIl8slldgbLi-KZZaY4IhcqPHrWyP4eFAYnhX3MOcXmR9oGcdz_qND9B1cDNfxQtIZcOq2-c17FIKnYm55Nnye3OR7ottLwHoiLDudeSTG2cFXWuBKQHCGf5MziCLskEXG5SW0Le3nbny8k_Ug9UegwChpSXccs7rbHu6T_-aXVMgcJWtEhZr86DYWLVa76PYb2766Rv0FSqLgljYE7RfOfn2JG05zvCPtsxPteczQ8cz_bS9VOM44yvfIA73bcLcQZKO2FMakN-VUNEGhESlqZsdvdZFWCY9WWWUlpp7aqbljlk2Jb8olH5Q6ZrRNEW5sYUxIONeRcsx2O6jZqkB4Kb4WhJPzoJejdujnd74-hlMtvwpQI&v=404&seq=1","type":"ad"}],[{"sourceTag":"0","id":"3503","extension_id":"{\"ad\":\"\",\"ch\":\"\",\"shop\":\"\",\"sku\":\"\",\"ts\":\"\",\"uniqid\":\"{\\\"material_id\\\":\\\"8152277000705173953\\\",\\\"pos_id\\\":\\\"3503\\\",\\\"sid\\\":\\\"2b8c4c03-ca80-4adf-bfc8-4a0b7217ef39\\\"}\"}","ad_billing_type":0,"src":"https:\/\/imgcps.jd.com\/img-cubic\/creative_server_cia\/v2\/2000366\/2174805\/FocusFullshop\/CkNqZnMvdDEvMTE5OTA1LzI3LzE2NjExLzQxMTU1LzYyY2M3Yjk4RWY2NTE3ZjFlL2I1ZGU3NzFmMzRmOTVjMTEucG5nEgk0LXR5XzBfNTUwAjjui3pCGQoV576O5Yqg5YeA5omL6YOo5oqk55CGEAFCEAoM6LSo5LyY5Lu35buJEAJCEAoM56uL5Y2z5oqi6LStEAZCCgoG6LaF5YC8EAdY1d6EAQ\/cr\/s\/q.jpg","ext_columns":{"desc":"0:cpc","focustype":"g"},"href":"https:\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9scHMuamQuY29tL3BjL3BzcC8yMTc0ODA1P2ltdXA9Q2dZS0FCSUFHQUFTR1FqVjNvUUJFTWVHN053REdnWnphR3BvWkhNZ2o0TUJLQUVZcnhzZ0FDb2dhV0VzZFdFc2VHZGhMR2RwWVN4amFXTXNabDlpWVY5bWJGOXNNVFl6TXpReUFtbGhPamNLRDJwaGFIZGhiV1ZwYW1saGFtbHVaeENTNHowWUF5REIwX21NMVpldGtYRW93cU96eUFJd3dhT3p5QUk0RTBDQWdDQmdBbWdCU3RFQlNYeFRTRlZPVkY5SlFTeEpYMEZmUmt4ZlFTeEpYMEZmVWtWZlFTeEpYMEZmVUV4ZlFTeEpYMEZmVTB4ZlFTeEpYMEZmUTFOZlFTeEpYMEZmVWxOZlFTeEpYMVZmUmt4ZlFTeEpYMU5mUmt4ZlFTeEpYMUpmUmt4ZlFTeEpYMUJmUmt4ZlFTeEpYMUJmVGxCTVgwRXNTVjlIWDFKTVgwRXNTVjlIWDFoSFgxSXNTVjlDWDBaTVgweERMRk5lU1Y1YVhrRmZUazVmUmxWZlVpeEhTVUVzV0VkQkxGVkJmRWNxU1Y5VlgwWk1YMHd5TVRNd01qdEdmRTFKV0ZSQlIxOUdVaXhHWDBKQlgwWk1YMHd4TmpNek5Idw&log=juZ3JcClitqWVWdw6CMKKzrTdbRcEaqRCS9UxDH0EZU7eYnNXwlTB9jhJKx0TxCZwfLuGyEYmh8w0uNb7Rk6Jz26-EnMU_qpFYha-pZvi4PGnRT87lRRht2vGdt9BpPkkVzatIEtOkcPEF5GwLbTWu6gZkHsxMXPd_oVQEyxyrS9ATRLsOwjY7Z6meZKYs9VE2_CSky3qneCX7xqIH9lxDT1TAFrvl5rL5P4ucPdCwnizbxeO1hGBiOKZUYElecY6jojeA-vpCbKUhn9WshQBPH-VTh_lLLmQ0xb3ZnJsF8yUutGbGvFtq4rH3QYfqyzSYCbcQfprc6BlubFL8aQdOCrZ8Juo2q_0nk6sQ_r-3Fa8JenWF9ugEfNew10d6MRa0xL1BXySdbJJ2uS48N_oQRbuFtAmUQj-iol4jRIXlhxFSO341FDthFAmTBK6x8rLWRdNW2b8wXBa7c1ttxVoQrmTcuzFjomlNisM1J-CYPlaSsba0CQkw1roW53TnPGRIpXZU0uzFDzU-CRP4FUMimBtwrX9VHHxs72AQwxuJPOI92a3bn1ZdWqdntHUZOBVtQvYLydYlGiFfmOhouqIOPlk-HZAwgrj8RII7nH9mkV7Z786nkttcKnj3Pxdi82tlKOY5meJZHCDbpqsjBT5dPtx5F1Khbi5mpYSnbZltm-n5v7x9c98tuqTzk5DBynrIvVFnRFeFd54V1fVnjDPjg0fWyX_Z2-KsKXSmaXvOrAcfplCkbRbyMixMmmmYs7--ia_iF3wI7QJFLuy8hX9cfmq6ZhmuZvxovQIllmDPxhx2Niv0PoPKktEdxESLsx_xhKfctJEEWp57BaFPLkUGmbVCnoaQQ2Hcy4ZpwN__C7DsdDlz5UiT5JisMDqWnLI12uwnjxsBryMktOZ4w5H5HYVbXU7SUGxEcPE34M37f2zWVJIjotkWKyjuNQtkYz1bT4YdgvK8wxYF5pmbG-SyYSJG1oRAFpwBVh-PxiS2dpwZ2CYeO0oOzn8liIO0QUFsWe2qti83Dw57VkK7_zoSeTc0vk1avuf958y9iYVr5YW25zpJhxJL3gzvTA6WDZIn-77oickMud3R8EfokpbhDAhRVy7Uj-rf7CEF7lMlhtTfXmu_UQIzCDpWvCteCLA6nqHooGCrS3Uvua2Tee4WaXkMG6QL7fZ4zKy2E5Ifg&v=404","clog":"https:\/\/im-x.jd.com\/dsp\/np?log=juZ3JcClitqWVWdw6CMKKzrTdbRcEaqRCS9UxDH0EZU7eYnNXwlTB9jhJKx0TxCZwfLuGyEYmh8w0uNb7Rk6Jz26-EnMU_qpFYha-pZvi4PGnRT87lRRht2vGdt9BpPkkVzatIEtOkcPEF5GwLbTWu6gZkHsxMXPd_oVQEyxyrS9ATRLsOwjY7Z6meZKYs9VE2_CSky3qneCX7xqIH9lxIec7xYpU1OijDeM2KfiPZVqctpQS9wPpQDVt7VifwFhIa0G05beqpKsq22JDDLMQYFUZZ-01foUm2HhVgnsyOVlLJrFBzIHtobI6pwVvsij5MABdtHMWn7rV8WNg9l7fUnHabAycJeaJDAybhxg10ls3iDAtT3I82oeGS0gMiGtJd-JefESDJtzLMgZ5wBrM2Rj49jQS0YTvYpTjIguqcvSqIfIAGRHXHouDQWmg6VPpUKFbT3oZIX8DETdfElZRasKarlV7PFSy8NdtqXL7H8H0dsfCGWnrZ0aMIQKQM1SMUE5pSzszOGk0gr7boB_w3Pw8SmUd6kG0K4TtspuMTtdJHEtmcYgR2RunWJWHGx6p0WSUrbpy8eIy2_FcYw-TYyfl6dDtIDhgpXBas1EqVq1Zl89ulJsrRR017qmE4U-7EdE0CRWitqas9uc58rARDO4rkEk674clD1AMyf2fvaZDgughfC6xd-02SRA9_xJjES0PQV6jvr2RNBd_h-63ueg3itdUbE8upGwsTJc-nRlILGpeRpv8DNtrjUz_Hz_BAXyQ_wNaMwgjtT3WzaRf0PfhisMxI3fmMY4WtuMZnzT5SVi4CrgBVwCvttqfNZ4kNLd_ZrSnK66D1yIdjpMwfMYsj05jNOjCvWtVR1HBIBRtkiSIjBfMrc1Xzi4IGl5z6wSlM2IPUgLQYb26BV9-lflWRa7I4Vw2aPB11BZk_qhOaWki7JNbl4JXOxkpoiS0lzeGfCrsEdMlIRyLmyOB3XudAZBItbY2rej3nm4tm7zxWK4vJ1IPVS6CwPY2gpXKS38UE3hRPZz6vCbGKq2MkBEbvvnJ6IPoDxDhca8NenrWR04a8uYweEzjnHlCID6in0J9_4hMJCkFQVL1NRIRcbTEv8NDMdS_lPvGA8PvgLdpTLZhRLTb0GeaKM9KIKMamKl2lCYRlGqX_1dPpGs4LE2Qi9yRiLj9tWxJBdHbGR4Yd2E636EnUp9497kaSBP&v=404&seq=1","type":"ad"}],[{"sourceTag":"0","id":"3504","extension_id":"{\"ad\":\"3504\",\"ch\":\"2\",\"sku\":\"100015611267\",\"ts\":\"1659342003\",\"uniqid\":\"{\\\"material_id\\\":\\\"5403304408\\\",\\\"pos_id\\\":\\\"3504\\\",\\\"sid\\\":\\\"fd6f77b9-96a1-4610-a565-cbf2025a5bba\\\"}\"}","ad_billing_type":0,"src":"https:\/\/imgcps.jd.com\/img-cubic\/creative_server_cia\/v2\/2000367\/100015611267\/FocusFullshop\/CkJqZnMvdDEvODYwMDEvMTgvMjk2NzkvNzg3NTQvNjJkNzA1NTFFOGU3ZTZkYzUvMWY0ZGUxNGVmMGVkZTQ1OS5wbmcSCTUtdHlfMF81NjACOO-LekIcChjljZrmu7TlhbblroPooaPnianmuIXmtIEQAUIWChLlvIDlkK_ltK3mlrDnlJ_mtLsQAkIQCgznq4vljbPmiqLotK0QBkIHCgPmiqIQB1iDu5TL9AI\/cr\/s\/q.jpg","ext_columns":{"desc":"0:cpc","focustype":"g"},"href":"https:\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS8xMDAwMTU2MTEyNjcuaHRtbA&log=jYzlzMkIvzNR4MdrD5FA7EfWIA6oi6xxvwvKH9qLlu3A21xhkEJwuWlDS_LAn0l3mg2rgNi223-7TSA6cvAvaH5UPnQ1fZCrvNn3EH7zCo8pmNw9quHA_5j7eIg09scZSKtTZM5u4XE6w8sZHcAzCEiU7He8z0adByAMwwegb0U6Jq51Znk3tkGzKqzkHw0bq2h3-vLR61spRZSuSqxvrCl4KB2dA-Ce20r6cIXGTMDdqergWYls6HyTXRRxdarSUH9lGtv5PCfGgY5NtiRKwJIcWxwj0YrEr2TF8HqAojF8VNKqXyZx-XqYo7TZkiuP4sMeu753Ncxf38BstrgYlbm2sdgJQOULzxgH5loBn9eIXkmPtctNpyeh257IcxpADu9-nOV2455-qCYEFgiG8dmeSs_LnO0Fk3dBuoF5m9kICjKal1XVk56zAkjlE9hLeoeKMXHPcs2uu8ciQo-R6xunh5VlxLpytgYx0Uk_KzQJ2LXqrn5X6Pe2d-46L-IlyRVQ77lJzsfnVYAhe6ix8D10_qUQYb-tXiDHQattqWnLWhajGlkLXW6JVIn_7Hbqb-WPzgpy5cVMGVBjnne3YerPuiMLFmBs3Ug_L00JyDHxfaF-ATHtJ7xwDKxDXYFTYyvkDLXzv2fK6O4h-vBOfkaJllGBzJ04HbbKHEcahQ6UPpwavnUCyVw0PLpz-ID6YR1B2fUB7cBlkNzS8VRp8WLWqDYsEuQss98gy-aoNL1wtiY0s-rp2WFb0kWhM7l9D8ojct0Xuu0WJVJZsfvpblnf9_dFNHMHH2tw2qq8wr5YSTbQ-Nf28rQUSfSF6TX_2aYFNBEG7nuiVxTezmI6OjZFXeGOPGhioKU1rkPWDI2HVMZj1N1GgB8tJX_bf7q5qAkRFIHV6si3sMFLNpTBdjOuJXEf9_nGEVBCpP2MSDVRsZk7ebpbXOGvjASJwmJxnGESXKGfw1wTZlWqB9ApsaIkIw0JgyqN_2ujfotfSL41H3t65CjYWpFQCwOQTVSuAKi5vuH7de7VSnLglvIHm2UXtQpC_fxN0pSDEkCFg6YfPz8QDncvUW9ckjBG5yfYtF7bkv1ELneb-uQRdC-RwJTS3lEmgk801mSlBzhKPXlhpPugVsam86SAY-epEo7Eku0DXhSb_9mYZfr1g4clyD3_NgmaQ1dcDqnvtW6CMfw&v=404","clog":"https:\/\/im-x.jd.com\/dsp\/np?log=jYzlzMkIvzNR4MdrD5FA7EfWIA6oi6xxvwvKH9qLlu3A21xhkEJwuWlDS_LAn0l3mg2rgNi223-7TSA6cvAvaH5UPnQ1fZCrvNn3EH7zCo8pmNw9quHA_5j7eIg09scZSKtTZM5u4XE6w8sZHcAzCEiU7He8z0adByAMwwegb0U6Jq51Znk3tkGzKqzkHw0bq2h3-vLR61spRZSuSqxvrMEapee8y0mJ5BVv5mmwKhVKSdy3BFp9Nw1OFqBOWLTH2-OTG29vf9WeIKvzNThiw7CyrXA98EyDdsGlGFTqpbNIR56FfmoScdvMT3N_kK8XesYYL61TId4MlJb21PCPvq9Xy25AxmDZ016QyHZjBdikQqRU7J5CE9V-6FZGps9pgdWmdDUfjncTDVUbKLoWmuoT-JZ3P0Bl4frpDOl0jrBsdnzKfkP2oSntgSM-wNKDSUO2PrOYT0oWuEwLN6anE-vZjx-k6-V4V1JOz5AXBWZgXgPkWt8xSCrwVCdeDvNC1J0QdMafC-M-yWFWWfEFiQUQnkxq0Xlm0TfPWvqgFBsdlOF03XxF7zObf4zTHz7SgX0UHw46_XYu_7ELAL40HOwlrHPTBv5KESdNksGjDDU2GztDjXYpVZit7oObgl-Kyfj7mH3fsvph63-7-NuQmlzi_zkJfhov7f_cNlP8kLka77Hj62qR--nlO1Jf5T7cx6IXAyb6tcYRyFkwFyOIlVy9ZmMolguYUg1tVv8OlMps8oupvDunXy6ZD4K5qj8VK_WtlbnpNXyPyLJjH9ES2JLESqs0W77A5lc38mxh7XJljmpEvtBWBDJVimyRQSgbziYX7gNqZmM-bOJnM7D5VBW1dwMbZmWLs5o6Hac-R65Et97dbjogv3lFtmc6b-zStje_IY5AAmvZgzdPFfxdoLO1cerXF-ny5aNOclOPmNDfMA88BXIDYE-G8Uu5Ap2g_ej_URocygipkdmooiFJY48bMLlhdy4p8rh-OQ8ZU4Gl96QATR7T9EjfnaGTGsVc7IoFIEoL9YOq3gVlKms9j08PEMBhjbclFxXJuQmgKk9W45vMNi0vAH2wDFyVD1LisXoMR_sJVqsDLoUiInyBXRUIcb_s2sfinXlVnHzQ3A1i7hrFgocrkfCcsM6LCL1zsoG4mXRiaEF2qIY1SUs-DbHAjT4yCzCezBL_9xjf5rs&v=404&seq=1","type":"ad"}],[{"sku":"100014546493","did":41,"src":"https:\/\/imgcps.jd.com\/ling4\/100014546493\/5Lqs6YCJ5aW96LSn\/5L2g5YC85b6X5oul5pyJ\/p-5bd8253082acdd181d02f9d0\/6527ebdd\/cr\/s\/q.jpg","href":"https:\/\/pro.jd.com\/mall\/active\/3ZYfZKGRAhbHzJySpRriJoGWo8v6\/frist.html?innerAnchor=100014546493&focus=3","type":"delivery","ext_columns":{"link":"https:\/\/pro.jd.com\/mall\/active\/3ZYfZKGRAhbHzJySpRriJoGWo8v6\/frist.html?innerAnchor=100014546493&focus=3","sku":"100014546493","playImpr":"1#13#100010-d3306b92659940efbf14c780914a9b32___","mcinfo":"null","rt":"0","text":"\u4eac\u9009\u597d\u8d27#100014546493","focustype":"t","desc":"\u4f60\u503c\u5f97\u62e5\u6709","biclk":"1#13#100010-esm:0-esm:0-d3306b92659940efbf14c780914a9b32#379#100014546493#41#5bd8253082acdd181d02f9d0-random--c1:671"}}],[{"sourceTag":"0","id":"3505","extension_id":"{\"ad\":\"3505\",\"ch\":\"2\",\"sku\":\"65972526504\",\"ts\":\"1659342003\",\"uniqid\":\"{\\\"material_id\\\":\\\"8834079630104113484\\\",\\\"pos_id\\\":\\\"3505\\\",\\\"sid\\\":\\\"17704ed9-e19f-4817-bd49-e12f3f17fb3b\\\"}\"}","ad_billing_type":0,"src":"https:\/\/imgcps.jd.com\/img-cubic\/creative_server_cia\/v2\/2000368\/65972526504\/FocusFullshop\/CkJqZnMvdDEvMTI0ODUzLzM3LzE3NjgvNzg5MDEvNWViZjljMmJFNDU1YTM5MDAvMzQ0ZTQ4ZjJhOWM5MDRmOS5qcGcSCjk5OS10eV8wXzEwATjwi3pYqLuT4vUB\/cr\/s\/q.jpg","ext_columns":{"desc":"0:cpc","focustype":"g"},"href":"https:\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9scHMuamQuY29tL3BjL3BzcC82NTk3MjUyNjUwND9pbXVwPUNnWUtBQklBR0FBU0VnaW91NVBpOVFFUXlQNHdHZ0FnczE4b0FSaXhHeUFBS2lCcFlTeDFZU3g0WjJFc1oybGhMR05wWXl4bVgySmhYMlpzWDJ3eE5qTXpORElDYVdGSzBRRkpmRk5JVlU1VVgwbEJMRWxmUVY5R1RGOUJMRWxmUVY5U1JWOUJMRWxmUVY5UVRGOUJMRWxmUVY5VFRGOUJMRWxmUVY5RFUxOUJMRWxmUVY5U1UxOUJMRWxmVlY5R1RGOUJMRWxmVTE5R1RGOUJMRWxmVWw5R1RGOUJMRWxmVUY5R1RGOUJMRWxmVUY5T1VFeGZRU3hKWDBkZlVreGZRU3hKWDBkZldFZGZVaXhKWDBKZlJreGZURU1zVTE1SlhscGVRVjlPVGw5R1ZWOVNMRWRKUVN4WVIwRXNWVUY4UnlwSlgxVmZSa3hmVERJeE16QXlPMFo4VFVsWVZFRkhYMFpTTEVaZlFrRmZSa3hmVERFMk16TTBmQQ&log=ARusfv_XCAKVnOx8AubwZNMORBzR1Tm_FXDk7PoxQlXCw1Cre0fNAw2RKTpkPo6cYMXLM7g454gvXw_xcY-uLw_qiWaeBFzMzERFs9a9iK4DVxLsr8fX0aLDTvsPzd_5RU-TDZkCwhx4sPrkzN1IQ89fmBeZwzF_qmshyd8wBn98eaetlft7Q3HF25opR5lS4kYMEdUkU0AORWKWQ9_wpfhpUl1L4N-48UDR-NAdZrNwZj5fqOJuXRhlyS9XedvlO-RxhoAqSPS3PeoyUub5-Q34nKohaBn43RPE7kpAJmg0BHlJTjFGDrIUw3tTtGlYV35S35zyFu2knIoEO00Qg4GhjU4XXQlPG0ehyZBPmNnhL_GLdf6VIiBJIsMWHQeh5PSX2OcFgcEDurshq2eqB7VqnF3FYO8TWOawV2ea18gSSi_Y-W3ha6LVD2zn1tDfwOOpvXlRAHgiyvRw85a46JI6qK_PfZzJKtuXYUW2ZuDGtogGdRhSXoaIY50G8_8_YL4tIJfBKsifE8Ik3DQ-9onRl7u7ysie5Ob6AXPN9ZAujmlHZMWUcx2AOKF30llGpWF9Bb8qSBl151Sj1nBKwXk7RvldS4yXHPpylZNNFcT33eVPK5nqQtELOE0o9Y64fuWmJSWR2xsTstaIelYtxwN-TdxetIkyQ76YuNh5xO6fTI0v3zj77oxu3a71touEcrzl9O1VIyKevlrNao58OTgMGFpdhGrxJXLtw34RaG8WpOdAEab949dha5G3GxCAhii9srPZttjT82Nex2Aeik4Bqb6pJHwHlWKAdHn1ULtTAAMhq91CKrryveG7CN9gFInzFP4YozBVEAhM7izqztWbRy1nr2Q2rBX_rmrPyUnNW-lhkswwHWT_wXjAJNXeBxGjY4xv7sceWg7RWzmx_DXv5n2WQOjJx4yzpC2yHeTc4_e7evmScGgOfwnk_TM8yTaG7WZNkLtBi_ynginOwLwY7q1nMxvpM33wXr0GAv1VV3X7CuIVSndt9QPnKqPvp25EBfQabCOzeqIXUt3Gs1zvxJm6HG5Gs8gHlzmCpOLfQqNn-EjsI0mvSZrCIngcQBaimdC2YkKG82wBEzIRXzOqVXoRygRqdYzFt_Ay9elOhfZlzFRFj9NSskkqsYqMEh3IGwY5FPZHcPgk7rj6X9QKveEFbMay7sz5CU2vTKg0tkkjHdolow-VMFnK5a6L9rqaFeOl8jz0P8OTK6hbOw&v=404","clog":"https:\/\/im-x.jd.com\/dsp\/np?log=ARusfv_XCAKVnOx8AubwZNMORBzR1Tm_FXDk7PoxQlXCw1Cre0fNAw2RKTpkPo6cYMXLM7g454gvXw_xcY-uLw_qiWaeBFzMzERFs9a9iK4DVxLsr8fX0aLDTvsPzd_5RU-TDZkCwhx4sPrkzN1IQ89fmBeZwzF_qmshyd8wBn98eaetlft7Q3HF25opR5lS4kYMEdUkU0AORWKWQ9_wpcd2oysYHokNbIOeHLk42E1eYSDsfPiGVqwWagAEacvbDrNO3r5UeufT9FPd5ZdBLNYP_DN9Z3Cb0sg-ANeo6r3Im8zAM9WWKOhnUKfkHNZ0zfzTzHy95agYi5QIYl-Iqup_ZEIIeClpp2uck2hrEscn6uQXep37K-tZ_GzSMsLzsjUOGjl0Z-roXBaOI3FWpJDyX6naNewK9zaBGlK8i2EHb6LxxbpjYf4K2JlrBcLywxxKFmB-BHvlqPtaOrP7zS5zU3f3It4awt4KKer0ZkCwxGyUCIo09dI7LSIzEURXtz769k8j04-9RY_uTHK1Xaa9gFrMPF3bNLICQ-yQC2P9k7Kr-ohj5biwVOpOr79JEbkA_jB0EsHJUOh7O2-DZUnApaaJtM-Xgk7DstaWoMGqVi9KMDdipEPlwjxVExuFV1XwwiN8DUdJ1-NMILixcQaBcyZOa2bAMU7zGZLxoiSj2qCVEHXz7EXRjL8TPZEKLHHPKK1oMPwmmyFQKPY3lskaZBXarVMl05OoyOKmilcO7027f2bi8vheju5jIA5jZ26RtkVX8Y6w4SN8H33TwvxP8dcVUBpyUCzaMx53CmltQSBqb44usnsK-2TMEbw9LH3KEc6qwZUNHRDaYnJ6oP6T-GpJiG-2qmcKD1fLXx3PE25zkWOnvHImBFyuIPQgxAxYV4tnRA5jTJ-PsplKVpPWcoLWwGLTCVBTjCE5Rcb6OeFUynpeXFT1Hiny9yZAL-6JNj14mfJrWfyW-R_90lbo1wOun76WkIVK566YIRJhIVf0G4U3V8KqvID3gYaYlJRW6dCcmHldbVp2iYk4hFupv66XZaAhrmZeixXviBn6lBf_RRHPsOyflSJPQN5e868micsxR0bAhdr2L9gaz6gqdZKzlSU-zCM_cQ3Ojqxi8cKn9VLHF3RmE_a9W4MUKPEF7q9S3BIZ5-eilKTGLYCmrlKRf6g49TQ2Lbim6aIY8-j3ZCEdKa84CHyjvRKyhcZadPuHqh6FjBYMhdCgew&v=404&seq=1","type":"ad"}],[{"sku":"100026667878","did":41,"src":"https:\/\/imgcps.jd.com\/ling4\/100026667878\/5Lqs6YCJ5aW96LSn\/5L2g5YC85b6X5oul5pyJ\/p-5bd8253082acdd181d02fa47\/887777d8\/cr\/s\/q.jpg","href":"https:\/\/pro.jd.com\/mall\/active\/3ZYfZKGRAhbHzJySpRriJoGWo8v6\/frist.html?innerAnchor=100026667878&focus=3","type":"delivery","ext_columns":{"link":"https:\/\/pro.jd.com\/mall\/active\/3ZYfZKGRAhbHzJySpRriJoGWo8v6\/frist.html?innerAnchor=100026667878&focus=3","sku":"100026667878","playImpr":"1#13#100010-d3306b92659940efbf14c780914a9b32___","mcinfo":"null","rt":"0","text":"\u4eac\u9009\u597d\u8d27#100026667878","focustype":"t","desc":"\u4f60\u503c\u5f97\u62e5\u6709","biclk":"1#13#100010-esm:4-esm:4-d3306b92659940efbf14c780914a9b32#379#100026667878#41#5bd8253082acdd181d02fa47-random--c1:653"}}],[{"sourceTag":"0","id":"4273","extension_id":"{\"ad\":\"\",\"ch\":\"\",\"shop\":\"\",\"sku\":\"\",\"ts\":\"\",\"uniqid\":\"{\\\"material_id\\\":\\\"7507039422\\\",\\\"pos_id\\\":\\\"4273\\\",\\\"sid\\\":\\\"31b0cd90-186a-4532-b99f-054b7b0069b2\\\",\\\"type\\\":\\\"1\\\"}\"}","ad_billing_type":1,"src":"https:\/\/img1.360buyimg.com\/pop\/jfs\/t1\/67208\/4\/21074\/87040\/62e09ebdE19f9d307\/ce00b54d607416a2.jpg","ext_columns":{"desc":"1:cpm","focustype":"h"},"href":"https:\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9wcm8uamQuY29tL21hbGwvYWN0aXZlLzRKdzVnUnVUS3pOc2RKZlZxTHZyaG1LNWpIQkEvaW5kZXguaHRtbA&log=RPY6maxckdB5MGqYxB4tDb8bsVuK4HSwHUdOSXEy5u5O_xs0hMVnOvwVJ7rIT7Pa7PQFxF1qW7VHy1xrFpLY0eZwA0Y4iUmlV-11qAJGTy4Wd8y11x6M5w0YthIBdQbO-onacdAzGYTGdXzDXiYKrHyeex6KBGZjb-FN4Isw6fKwBf7QdUgiQcKioTPyJiTbavpR73NZqb-R-3Q-DoHIHfK6jXgAXepH4fTQTJfiYZjG8uMEForOhdf9RuW-3Zdw5P_KaE1RhdWhXJXDKWkps-6TVBdHbVAJDa6tKgtXVmB3psiqQ_75F1wvcQtYcDopTCyV9cX-iu-zsKTfmHOtvFcdbHiebu9UuvqPwpZf-VsFRs_2UKuYXXb7JV76f3W1BhgZSVqHZuUvrUHUpWUF8HZEob8-yXITzhMlsfo01azhOAs8ev_wBWdmLhd6S7_uqpD3VngIB1WNjdxUY2_uroiyYYpnR10NEfjf078r4vddTLi1C6hfzE8aO8gvwxOySYqIJWZfH1CRj5280G9e0imS5XgmB6NLhJHGmbEuFRIjtwBBO_eDEsfwP8x9Y_TSpUtRYNtrxPNR5TlPI7vFrMs_diN5n7kzlS4EWpHFaxLcxspPRhtM3dWBkpp95QerjpD9nKndtH63yCaFKpBK0Qj2jJ1S7KqJ0mxAuU3FX6KisQLDTMbdp4VEpoUlZG2Bq67E65_nx9C-E32Om5f5Tjsd4MabEWkL0IUMTN-mqTTCrrQEUIekDp-gbY6qZpFKfxYToSO6SEpQgrsStAdjGpX-ynsHEpyn_ajxCAYIT1R5yyDHJOVPp999NU9vY6oVCFakiIjICiI2kN2uFca1urM8STJNDLtxawkTCnCaAMXfzvly-htIRxRUb7G2L0grWEBqxkIHoaGmv7Ngcp-Ne1jwvj142gav4y9vDDJuv8QHrev3Z-LADnLpZYVPbnlDyw_qLEGJnOEdzCWfUvQjfKyCCYTCxPeMumdh3lnT3FnoAM2MSh3TE862u9fYdf0wGNVtBR3B8mab67pqu9J_sKbFmND6jWJtzi65wqK2OYMB-4kViBQNG-_Gi-7Rxrcf&v=404","clog":"https:\/\/im-x.jd.com\/dsp\/np?log=RPY6maxckdB5MGqYxB4tDb8bsVuK4HSwHUdOSXEy5u5O_xs0hMVnOvwVJ7rIT7Pa7PQFxF1qW7VHy1xrFpLY0eZwA0Y4iUmlV-11qAJGTy4Wd8y11x6M5w0YthIBdQbO-onacdAzGYTGdXzDXiYKrHyeex6KBGZjb-FN4Isw6fKwBf7QdUgiQcKioTPyJiTbavpR73NZqb-R-3Q-DoHIHfK6jXgAXepH4fTQTJfiYZi-XXGh_R6jQFVijvUu8Y6SkR4myIAamYWOC2As2qcgpCyDwgIK0snlbFdcuVpq0hA-ZHhTLNXSBq4XkFZcgvSJNDVFzaGBiGw2nTYxPDD-b6P5iCdyI1zysYcly2-uNjQS4YzTczeYVX8pBXoSdsjKAwJs57uFmy3pKO6BheuafCzUePla-uGCxlHRqH3UzZY-tSGd2Ufav-cmXF2rN4HNrLV4QZT_s4Tb8D3zaFEtxy1TjfKf8Ewl-8MwS6JssDujfOOtm6y4R_iOarrDhQJR5ZnNSe2lNGSLpYCzzMEtcA8kxHxfL1Uhi4DChu9ecKTs7nXZPVdcqyM12DlNYfIH0k6vb3vDSnbj4EDioCqaaxXPTamhH2S71IuJQ6m2VNVLzd8sb53BjadZps71bz2LznZtgecIs1ZgKBwNasSoq5VmYuUPSd5cH7gA_AfLDeRjIIzHnqgVIkunc4Lg8gU-UQGG9wB6PGScG9ErW_92AF6DYjZbdp5V_pl_jRgixiRC-robO1Zg14zt2NO6o1Jt2uHED2EVTNR5HOT6urXBewQO3TZxNruoZFcxAJnZNrRI8QnmtnxBWnhIK9-g6DQ46tXBd59wst9elPsfVZXJIqE8q3MfU_0IYsIrGuum00Q8GtMyBE9MUepHGG4f9CPWiZe2TJU88pD-9DPX2L_UFMnbOxQEuQHCDjyLfVxpnaQjT7DzzzshDl5gIkkweIAbpVmbLbTdVySNkSgItJ1zYcgmrS_06W1ofcdFtvtY2xtWp1jKuJauyW5TbcHGkLOLFo30W4Vbtvm8alFSZ_m7Q2uigDieCwAvZ16A2O2L86nvcRe-gdknVcdWBKXnCtVm&v=404&seq=1","type":"ad"}],[{"sku":"100010728845","did":41,"src":"https:\/\/imgcps.jd.com\/ling4\/100010728845\/5Lqs6YCJ5aW96LSn\/5L2g5YC85b6X5oul5pyJ\/p-5bd8253082acdd181d02f9df\/a169eb96\/cr\/s\/q.jpg","href":"https:\/\/pro.jd.com\/mall\/active\/3ZYfZKGRAhbHzJySpRriJoGWo8v6\/frist.html?innerAnchor=100010728845&focus=3","type":"delivery","ext_columns":{"link":"https:\/\/pro.jd.com\/mall\/active\/3ZYfZKGRAhbHzJySpRriJoGWo8v6\/frist.html?innerAnchor=100010728845&focus=3","sku":"100010728845","playImpr":"1#13#100010-d3306b92659940efbf14c780914a9b32___","mcinfo":"null","rt":"0","text":"\u4eac\u9009\u597d\u8d27#100010728845","focustype":"t","desc":"\u4f60\u503c\u5f97\u62e5\u6709","biclk":"1#13#100010-esm:1-esm:1-d3306b92659940efbf14c780914a9b32#379#100010728845#41#5bd8253082acdd181d02f9df-random--c1:671"}}]];

        //首焦兜底
        window.backup.focus=[{"recommend":[{"alt":"","position":1,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/160427\/8\/216\/44383\/5fea8b3cEa4deb858\/fe57a084e88526f3.jpg","href":"\/\/pro.jd.com\/mall\/active\/26AGXsmM6AChBJXAvFuMKZ8h5T9E\/frist.html?babelChannel=ttt18","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"Zag\/g9b0Dld+fkfVf4Suog==","mcinfo":"03294000-13573946-8801423632-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/26AGXsmM6AChBJXAvFuMKZ8h5T9E\/frist.html?babelChannel=ttt18","desc":"","text":""},"type":"ace"},{"alt":"\u8fd0\u52a8\u6237\u5916","position":2,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/160199\/26\/187\/69636\/5fea04ceE5abe2994\/d12a85889d01cd15.jpg","href":"\/\/prodev.jd.com\/mall\/active\/3X6GiZeEUSw1zfbYxzhVfQpFXbWu\/frist.html?babelChannel=tt9","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"5+Gcq+Ev\/0h5o09w5iB1hQ==","mcinfo":"03294000-13573946-8801423635-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/prodev.jd.com\/mall\/active\/3X6GiZeEUSw1zfbYxzhVfQpFXbWu\/frist.html?babelChannel=tt9","desc":"","text":"\u8fd0\u52a8\u6237\u5916"},"type":"ace"},{"alt":"","position":3,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/151690\/5\/12181\/71606\/5fe9bf3bE80b775d9\/d67be1ff0b8fa2a6.jpg!q90","href":"\/\/pro.jd.com\/mall\/active\/2tRyWk6vGETjF5aPtAZoXxdnddYA\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"gIoMIiWo0D\/LhPR2RJZQ2g==","mcinfo":"03294000-13573946-8801423636-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/2tRyWk6vGETjF5aPtAZoXxdnddYA\/frist.html","desc":"","text":""},"type":"ace"}],"banner":[{"sourceTag":"1","ext_columns":{"desc":"2:cpd","focustype":"h"},"src":"\/\/img1.360buyimg.com\/pop\/jfs\/t1\/40588\/8\/17960\/59407\/62e34ddcE9dbbf4f6\/553bb2b4bf1dbc0c.jpg","href":"\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9wcm9kZXYuamQuY29tL21hbGwvYWN0aXZlLzI1aUJxVlFBZFFoQkdLWG16TkFzVkFBS3JnWjcvaW5kZXguaHRtbD9iYWJlbENoYW5uZWw9dHR0MzU&log=iIiEoULH4trqbeSOIDK8ysI5bQ3OeLayzpB9BXH0FEJn3fAJAQd-SUpG764nxgtV8Fy1OgWXc0qVbPZq1tF3iKp6_kPb8tuyVu8285eSukoOw0Bhb2Mdt1AJRrkPNfC93LFhnHaGju1YWkyaamFkmEdjErmGS7TWHkpCyLDBGR4Ukxo50H55ICLqJ8nc3r8ybNJtaSwtGwfMf50Wp7iKqCigAtLwyZ3J28TYUMzJAtBTRA1mTZWJYHKrg6yqavX55znqTua5c4hhm-4XHMqTWUXnqn--1zMib_u4zDw_J5l3sOuI_e1jXtF-gFVP5qRAzc-B1U0l-yNZoQu52qmZJUT-khFrfP1JOQHTn2Qi1qAJEcf71-dTuCcQKcptKjpagtwxLbfWjs6kPJ8wti1NYvlO9FgtnbutUiCpNWTEsQE03S4xJ2TtxF0wGH2n8T2ygpb2TUhw-N_BE_LFY1nUgXLh-fxwTmxqIAN9efglFR2pLp2WntAmleb2-u5jdRqg4N9hh87tC68QNnIJKqQN01RKniJwe7fdXUU7YWQy1pH1nD6UEJDYM812QgjbKfmc9MWvIZjhq2yI_QUgXchDb8jeoZuGzAq-pQjJcuNmAD-4son4xZMuNGJA8BLUpVHRwM-VxljymUFh7v_3kuOLesmZv85-YNVsVQV7m9OuoWRtWlGzdIMBaMtQ0pyRbSGMNanztoEgvBDozaYoxYFNxEZmumUVOu0wvCQZsT7PJofJkGzAwOCpU-VrqF3jYYXX1JVrpdxUeUCu2WTwFun0CSaC0Mkldngttz_RhEB5xF98m2S_ToTxqguZBW2bncIYT1ZNIMiw0QsbMfsaqabpR_UI79ICvl2w8d8L_w27Bfyr4GjMddVvBjLw-W_k81XEMHlJlL42FMCbmphZrJDPl51gZMgTwyYv2tTzzWkvD_CrHNxCUaKHNQWMbqdF5MOgSn07c7NczCt39M6gwAEpGF2XsHTe3H3hZ1VYmoh3j4xQm3ZZ7f4ExSbhMTO6AwlBwRaBJEFb5Bmk5sL7h5YciQ&v=404","clog":"\/\/im-x.jd.com\/dsp\/np?log=iIiEoULH4trqbeSOIDK8ysI5bQ3OeLayzpB9BXH0FEJn3fAJAQd-SUpG764nxgtV8Fy1OgWXc0qVbPZq1tF3iKp6_kPb8tuyVu8285eSukoOw0Bhb2Mdt1AJRrkPNfC93LFhnHaGju1YWkyaamFkmEdjErmGS7TWHkpCyLDBGR4aZNGc1nnK8kqlmR-xpNmlUM1m3Ccht-c-45Vf3QPXJO7GZjIjCB1qpMBfFDpSRj16h0ERlrKnxsbpK260IzoqaKE8Om2aS3KUsMNOOYEaESeIuSrBKFqtTiiQk2Pu1lgreBzQvUqzRjODLg-qP0bZ0uIPApuGwFa5rivFujdS_OiDEwPO3wYutbBCkDDPYTfarwNBf_jGjdJGwU2chrztrjxycjmaXN_2olzsU1GRQ6MhjK29HBGZlQAgxhj6-_bUUy92eUo3pQLd0RwCbuezq9qN8yqIRjP6EY0jl2ZVENKdIR3pGMiURh7p_-iBILaY5bZEssybJfE5QVk1SVx_m-ZR2n0Ubq0hKExl4YMyUxMHq2v6lvo06IsoAe_ZCEjCfGrPXg-D9h10_OwXXujCxWaopLg_7IRk0enrn-z0OxdaGvRvjFOXpwtJLiKwbJ5YtYI8FU5kpomVXzYPajBLG81peW5A2mE5yAqzBHPflanCWo6KG5q4Cnk2WylHJoi26BdBvbUUpYRqVOe1EyE2xIElK_v_PGPosz21SlvDVp69AEzduI0YR6Vtvprauq_Zb55vLNjXUWHfsJVz6yGG-OCYkEg2b6dwh-8pTMTnEBioHnFFQswOLmWby4uZ-82B66mhMJXE3-CnpC5k2PSLi35sEizLJjVG18MThLKemfkrIYkU8jL8eiq5oM3yCyc4l6nuvmNfZb4jNW-EqPHM1Ml3yWae6V9u_M1VrBKVTALo7j7ihMYVqDobrfot7KX1uDnz7-rX47EAtPQl5ih1TyBigah4j0aR438ZmrLYxOdwx4LtGivGq1mWssn6ne2arAobrLs73r65qtR2r_5OCaBuJZkVhU75Yyt-FsmJGQ&v=404&seq=1","type":"ad"}]},{"recommend":[{"alt":"","position":4,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/151106\/13\/12106\/70958\/5fe5669fEeb4a53c5\/ff4c2841360b1db2.jpg","href":"\/\/prodev.jd.com\/mall\/active\/2KS7qX4VEn8pt5atxK5W1jGAvrc5\/frist.html?babelChannel=ttt32","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"IRwFC2C28awBBlITEyBAiQ==","mcinfo":"03294000-13573946-8801422732-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/prodev.jd.com\/mall\/active\/2KS7qX4VEn8pt5atxK5W1jGAvrc5\/frist.html?babelChannel=ttt32","desc":"","text":""},"type":"ace"},{"alt":"","position":5,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/144093\/37\/19883\/83175\/5fe407c2E1b76b792\/68ed75dabb686375.jpg","href":"\/\/prodev.jd.com\/mall\/active\/37ThKCmK6tFnWd3V8PqwMJ1SE3TK\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"qGh6sTt79QoBBlITEyBAiQ==","mcinfo":"03294000-13573946-8801422298-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/prodev.jd.com\/mall\/active\/37ThKCmK6tFnWd3V8PqwMJ1SE3TK\/frist.html","desc":"","text":""},"type":"ace"},{"alt":"","position":6,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/138772\/31\/20178\/39292\/5fe5cd5fEfce38cdd\/375bf42ad6dedfad.jpg","href":"\/\/pro.jd.com\/mall\/active\/46Vsus7SpKRgDbyAUitFHeBJnthu\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"PMS5koVkFfmNOxwMgDd+Yw==","mcinfo":"03294000-13573946-8801422822-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/46Vsus7SpKRgDbyAUitFHeBJnthu\/frist.html","desc":"","text":""},"type":"ace"}],"banner":[{"sourceTag":"0","ext_columns":{"desc":"0:cpc","focustype":"g"},"src":"\/\/imgcps.jd.com\/img-cubic\/creative_server_cia\/v2\/2000366\/8946845\/FocusFullshop\/CkJqZnMvdDEvMTQ5NzI5LzcvMTA2NDIvODI0MTgvNWY4Njk3MzVFZGE2MDZiYzkvNmFkNjdkZTg1NzUyNGQyOC5qcGcSCjk5OS10eV8wXzEwATjui3pYnYmiBA\/cr\/s\/q.jpg","href":"\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9scHMuamQuY29tL3BjL3BzcC84OTQ2ODQ1P2ltdXA9Q2dZS0FCSUFHQUFTR0FpZGlhSUVFUDJEOE53REdnWm9lbWg1WTJvZ3pUQW9BUml2R3lBQUtpQnBiU3gxWXl4NFoyVXNaMmxoTEdOcFppeG1YMkpoWDJac1gyd3hOak16TURJQ2FXMUswQUZKZkZOSVZVNVVYMGxOTEVsZlFWOUdURjlOTEVsZlFWOVNSVjlOTEVsZlFWOVFURjlOTEVsZlFWOVRURjlOTEVsZlFWOURVMTlOTEVsZlFWOVNVMTlOTEVsZlZWOUdURjlOTEVsZlUxOUdURjlOTEVsZlVsOUdURjlOTEVsZlVGOUdURjlOTEVsZlVGOU9VRXhmVFN4SlgwZGZVa3hmVFN4SlgwZGZXRWRmVWl4SlgwSmZSa3hmVWl4VFhrbGVXbDVCWDA1T1gwWlZYMUlzUjBsQkxGaEhSU3hWUTN4SEtrbGZWVjlHVEY5TU1qRXpNREk3Um54TlNWaFVRVWRmUmxJc1JsOUNRVjlHVEY5TU1UWXpNekI4&log=GQOM1aww1J9z6c7M2Zkh3AW81YMEWWwWtt_KrXJkNMHs_RW9uY7EuDu8ZfbMC5l9Fbrz5LrOOC-ZzbLJ34zgVL9RBA3dhJZWRv0JqOXqZGhKn5aGDuT-5LBPAngyijngv0Edg--lpaa44uBlTack9Bx1L2EBR9bZ4pNl8QXB76lpb-cn1GnSzBtkC5ZuxKcNQw9eJTK8_zbdfiBOYobwMEd86T_xoYmUkZU1zuZltrHMqgo5i1B6UrBBiwCvH5cN_h1rJklRGW2k6N-tLCjfJY1fNDoKsfZO-J7HZc3A9QfuAVXmR7mhPG501IYyqn0iFndGtSen9sGADWvmGzyC-TMgb5Y5iVRTAsgVRYyAtNwFhZ802GPQs3x3wfsD6gm-z1kAIrtThMb12UUy51OX20LWMPxN8u46Z_IWMV8AlVmSrw68cMGyF1KnThZwz_k_sBGZ2rohNfErh9drryi26P2CecuBdS_P90BvveXajr9il_Tnm0_HEnJ5gNd04YRWxI5YOa1MeIzeDDCKWwOQOL5GFIe2xv3Tqp7yW2NX6_xJvnDHeyM-yHJpRRTRTbpPMKndgsMB3M8TWWv9joAANzVW2mava74CGADvdl91vH9Eai0YJA49Uq-2nEzEGL2ah0UX8-L19A4cAwGb9lrmkYo3arpkLbfKspcAvY8tjd6dwgtNM3N8yQOqD-9VaHBw9d8SlEexdf5sqh7JTl0WZmPfwtxfApbclUGuegQPU3dz0OxteRuxWG2vpw3NQ4ECu-45_BinrvUXkrqg5PIRRCx7JyxknWdW9XoJIlBTk1FaBU8e1ScwraNRkhynrDpKdRH69aD0kuqDmic8uwuN4TnkXo6DpiAp56gcwcA6aUhUE0X-QAR-aAxK-sTHzWrRKH0CKB3QrklAhMoSkbiJ8fx8AV_ed_Vy0Nya5FKldPllqlmAKhMXRjRCCrpjZtUMt9o3OrL8uROoSQGKLtCWqb7OfWhl8ApisWROjRSEjVb13YidQ9lsWPqeoevOie4b0EYRVBqtIZ1BHD09_kDP258OeFLZT13kDuSWGg9bB8wj8JywpasmzU9_hB1T_v2yAThPckdrrd8IT1FCiRo9IC1-m7HTXWeOS7ibr-4HwEV8JeD23rNsE9w5j5r717bz&v=404","clog":"\/\/im-x.jd.com\/dsp\/np?log=GQOM1aww1J9z6c7M2Zkh3AW81YMEWWwWtt_KrXJkNMHs_RW9uY7EuDu8ZfbMC5l9Fbrz5LrOOC-ZzbLJ34zgVL9RBA3dhJZWRv0JqOXqZGhKn5aGDuT-5LBPAngyijngv0Edg--lpaa44uBlTack9Bx1L2EBR9bZ4pNl8QXB76mE0xBHW-EXnbPieXcwuZIml58tMmQWpmoUxwZxGLrJeEN7wj_JKJq1kU3GZo27MRxl6aY7-m80vME-v2vlKMZNiQ4Ilake2SYyD0IxSy4xOGA6Tra6iGPHnwftP8fN7CNRVSd2opLCJIoP0RC2KYm-QctcE9n-9y5NS7IAucJuCPtixKG4oj-3UkLMVgydQW_GASkc5N58h4QCwKjrb12Tl3FOvPL6994kw2fs4H2R6M3qr_pm8TzlYk_JlijPXWM_GoyWNiUEYMOqNAfcA94I0pxbeq04JlMn_2xioAbFGmuWHY6xHa3JB0U-1Yo96KQ30mLxIg4G32s_xcTXsC7NjhXtcTzKRKECREAT61Bur82WoWKZrDUE5Aa2zj5CsWTlEL7gip3VdEFDUUPe-Q5GBjw8o-61NUbHDCqfCmamto_n0TtX6hQ90X0UKQkApNNadJRP6bqDArXKai8Dfsz9qmWtuSEQQzuqsgqg2OwQLi_1zepOrVQqvoERhul-SQn_1aS6or-xmJ9GMnYTS8HlwK-EDbMYb-WnlkURiCCO8xx4Bz9KnG4uY67PzelIfeacHshycRTkHeZPGftrdPxJtJJc7sx70xKKKY2-Ilfi7MIYk3trdT8hFSknJGHW6iy0v5HisP_MwAIsCDruB0rIHRAd6hQDBX_6wcj-1Ps1J1x7WJsoBWd4HJJkL5Sg2DeF8kzSh9M5ovRr8OB_h1yvo0Gw7LiDyaiVi3gL3_MPe1J1lfP22zq3eZw2uIiYcVPopwMW6ZGc7mD1xYbUefntiHYsx0l96aZXfF10-tGu_EjJPS0KTX67z9VQX5cJkgtD9fxlHd5AAanDfXYN5S4Uh63FUse2xxBZc3iOHzdPqDg8TJQrFKMM0QDhcFyUDDSp1BIAnwDzCKj5Vw_X1tbLb-Q384XzYCsrILKSPqoPPJRm29cpv3T1TeMTElKNuEhsVJuDmnhJoZ6g3AAK78rCVMRc-uTUKIqbn5LpQkXLYQ&v=404&seq=1","type":"ad"}]},{"recommend":[{"alt":"","position":7,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/129709\/30\/17733\/53433\/5fc20ebaE16d5e08d\/bba7d0a8e8e7fb10.jpg","href":"\/\/prodev.jd.com\/mall\/active\/zGwAUzL3pVGjptBBGeYfpKjYdtX\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"+BuvoFpWY12V+3PXLySUMQ==","mcinfo":"03294000-13573946-8801420745-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/prodev.jd.com\/mall\/active\/zGwAUzL3pVGjptBBGeYfpKjYdtX\/frist.html","desc":"","text":""},"type":"ace"},{"alt":"","position":8,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/153447\/39\/11074\/46465\/5fe2e757E465bdd19\/a3db919bd4cd1490.jpg","href":"\/\/pro.jd.com\/mall\/active\/G6dB2UyBBfwfTVCBp3iMQQQ6GHi\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"rGjgT8k0RWIilVEYymoeQg==","mcinfo":"03294000-13573946-8801422515-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/G6dB2UyBBfwfTVCBp3iMQQQ6GHi\/frist.html","desc":"","text":""},"type":"ace"},{"alt":"","position":9,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/147490\/11\/20231\/58763\/5fe554d2Ed968d82d\/0e749fd6e3e38af1.jpg","href":"\/\/pro.jd.com\/mall\/active\/3XjkyqALMxPUtxHp3VPvPzR2USqK\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"gGIXsI7ZKj4cCPOFSR5xbw==","mcinfo":"03294000-13573946-8801422820-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/3XjkyqALMxPUtxHp3VPvPzR2USqK\/frist.html","desc":"","text":""},"type":"ace"}],"banner":[{"sourceTag":"0","ext_columns":{"desc":"0:cpc","focustype":"g"},"src":"\/\/imgcps.jd.com\/img-cubic\/creative_server_cia\/v2\/2000367\/100004707458\/FocusFullshop\/CkJqZnMvdDEvMjE0MzEvMTIvMTgxMTIvNzU2NDIvNjJkNzA0NDVFNDM4MzQxMGUvZjk5ODk3YmFmMzYzMDExYy5wbmcSCTMtdHlfMF81NDACOO-LekIZChXljY7luJ3nh4PmsJTng63msLTlmagQAUIZChXniannvo7popzpq5jku7fmm7Tlu4kQAkIQCgznq4vljbPmiqLotK0QBkIHCgPmiqIQB1iC-frF9AI\/cr\/s\/q.jpg","href":"\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9scHMuamQuY29tL3BjL3BzcC8xMDAwMDQ3MDc0NTg_aW11cD1DZ1lLQUJJQUdBQVNHUWlDLWZyRjlBSVFvcHZyM0FNYUJYcHpaSEpxSVB0cUtBRVlzQnNnQUNvZ2FXMHNkV0VzZUdkaExHZHBZU3hqYVdZc1psOWlZVjltYkY5c01UWXpNekV5QW1sdFN0QUJTWHhUU0ZWT1ZGOUpUU3hKWDBGZlJreGZUU3hKWDBGZlVrVmZUU3hKWDBGZlVFeGZUU3hKWDBGZlUweGZUU3hKWDBGZlExTmZUU3hKWDBGZlVsTmZUU3hKWDFWZlJreGZUU3hKWDFOZlJreGZUU3hKWDFKZlJreGZUU3hKWDFCZlJreGZUU3hKWDFCZlRsQk1YMDBzU1Y5SFgxSk1YMDBzU1Y5SFgxaEhYMUlzU1Y5Q1gwWk1YMUlzVTE1SlhscGVRVjlPVGw5R1ZWOVNMRWRKUVN4WVIwVXNWVU44UnlwSlgxVmZSa3hmVERJeE16QXlPMFo4VFVsWVZFRkhYMFpTTEVaZlFrRmZSa3hmVERFMk16TXdmQQ&log=lQz90Qa7IfhlbCVKfy67dHXct0Rnm0xURjx0S88iUKUslr2Xq25u3uRsoEJ6IyRVfDMy8Xatkni4lYhj4q4aiyGYjtzgJYs8dF1y3on57Y6iaQB5a2TPvzwVZ95gZQT1M77VjVn5Pl1cuhSrvVdg_YbCPhHX1j2L24J38ULNBc7uqhv_Vq8Oj8EmFoyEj6d_Z19k0anQQnwiHuFeGS4vwkHpG1AaF_9TGhbSDMkO-GUgVDQisI-oC9Gbdl4OXW5gvWpzB1R8jW0_PZD8qwS90eGc32FJXF2N0FHxVpOgTKWO9y9UXMPL13GBdo9w-CCTo0ejJ1CPdH1bbuhVTJBmaNdQU2Tf9vm2wNeO3zVqmHfB4sqSELYyDuPdFcH69y6lmMFdKWeW01-zGA87Uw13-QNOm5MCiXRtDkEntsC7VgGuQsc0Z1Sbeyls7Zo4N8oeAUtBIEQ0x_GWeKpjWuh2BK4YTnaUr5LwZluEuetOTbwqFJbIilXWRRm-EZ1NIxF7pLbrUSYv07t6mhhi0CsFm4Md4wUY5aEMG53ybM1fSAiereVvsB9bX0Ui3VHwnD-4X8JNAW0z9Lve2ckuqt94OMqDgrmF-wh8taMR4H1rHuX3YT6qhfUZ8Aa84i2qcSeS01lVlol1r7aQc_KI8AaS-zpnVpMpHmNxPQiv0RzSCBkzm-UdvgPCJA6FMctKk8EbIz3XBoqvJ5q2H-75jCUgPyn-mnr3GOV4rtqNEmiARvwBgFj7OL1yN7pqp8rTCnIeJYaS1-lmKNfzVdcVZP9sFOw16PRkSD14lzSoAEnVGbxu9fPCjbGzjSMZVrH0Q9e-TnWA1mQU0ZV1U50AOiP_bp2YeAYVcwesK5S3dVK1HyW0na08BnQqx81CnHdny7XjZW6gWrB1x-kpeU5aFOeAEjvt30-NkEnUSjqZHV_3NI0JaC-53YDY-Sr2spieJLg-BjGC5gX-KP9L3uuPc0665w2v5YmAQQoaxM8zFpm-0pZHK_XtvvJxvSqGr0Xto3vR494Ks0GtPJNR3ntOXaOSNgNV3tUcrBHhLlV1YmRR6wSqZ-rxpapOMP-bXztmg2iNu50JNVmC7k_Q96Nh7axw_ddSMY36ivHgJXJGRaS0qz7o_uJmd92CM-lCtBnTrAcp133oF0eo1yKRr-9ttiZOUQ&v=404","clog":"\/\/im-x.jd.com\/dsp\/np?log=lQz90Qa7IfhlbCVKfy67dHXct0Rnm0xURjx0S88iUKUslr2Xq25u3uRsoEJ6IyRVfDMy8Xatkni4lYhj4q4aiyGYjtzgJYs8dF1y3on57Y6iaQB5a2TPvzwVZ95gZQT1M77VjVn5Pl1cuhSrvVdg_YbCPhHX1j2L24J38ULNBc7uqhv_Vq8Oj8EmFoyEj6d_2P65QzK42-S0wW4S7P-zeIIddW3pBafAfbYl8NYq4lajmKfTBrVTcPHm5KIVIbFFjEmgBx4XltWEHDTf-JvYUR8I1rSn6sgQL7Wsg5NFjUAhhfFfCK9Hm5u7KGwQU-0HVx0jAWXB6_lZAvMq5_acRdKMGNKerZrayP-OI-T6zZAGVQxfGtoiokl55TCw2qhzhnFwUtCPjWa__Sxez5Ua-FP8Ek4UYA0aZCmozu4peAx5c0Os7FdUd1f8W2J4yi8SFuB8YBVXINqwIIvLAM3Q8GQf3MdVBtZ-pUq7cEsMestGznY1BnjFf_CAPOeFSOm4ubes5SHo96iEa0VwM05eRAXSkp7W48zKDxdSYEcwwQsuRUSSGIRNqYRDXLur_fY6T6JE9usB_GxThdTCFys4wkcs9N2osJfD83wXKUQOjV6daHkJkctP0AeaB6kU4o2P5scZFKR8CLIR6feUOkMDqwbNCuyzfV8TBMyIN0x3cfGvTeBpegWvMiTdmZAY7hv_CYvSN_1xHKbgFl3I80znAbhozdOo-HAMnKvqsBwUw74gj5OzW-9CkHUrKa6MnFojm2dxvLBlzJbKLJXX3y6nIRbV2Enmy59kHBQgnowaPj5APHErTvAwisyLof5-LgZPV0bY9yW0PP4ZiJ7d0yG3CKQnjQB_OTYoGTd60mwFt8KKJ05otAJzipYLew1Ttyqgnf3qShaCr-arhScQZQ5kZah3ML3V2Ste9N0bN29zgBIEJWUT8xrSMCih0dNXSgT0JELaVvv779FnS8VBw_73bQ1z9mCMTf18H2-HDs761GgEM3U4cMbDDB0F0zeZWUf4qHqRcuh3_oClP9mXmrxGz_e0G8GUQ4i3D1FadBQnxAvnYsZvrMG-Pf4J7LTVI1kaeoFwZiFBHTrmO04vw8FqD3siBt2ozOFgP4NYYKgDznc2ZoFtbH9Ga00BjXyDkFX6mrzxWpB-Kkw8zbpzX0jtDw&v=404&seq=1","type":"ad"}]},{"recommend":[{"alt":"","position":10,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/145833\/33\/17892\/73340\/5fd1f9d8E7ec88331\/4caf9bb9de747f80.jpg","href":"\/\/pro.jd.com\/mall\/active\/37p81TGQS7wcEaHNjA1C1WokKPeT\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"U6gP9cS8gV5xMdJYrWgQ\/Q==","mcinfo":"03294000-13573946-8801420756-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/37p81TGQS7wcEaHNjA1C1WokKPeT\/frist.html","desc":"","text":""},"type":"ace"},{"alt":"","position":11,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/152823\/26\/12012\/68654\/5fe97bc9E430fb6b1\/3f7f6bcef1350531.jpg","href":"\/\/pro.jd.com\/mall\/active\/2i8TdgieNtGwuDqV2yHPSFqRr29t\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"bkSlXW4t4\/oh7WXA5Q6F0w==","mcinfo":"03294000-13573946-8801423369-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/2i8TdgieNtGwuDqV2yHPSFqRr29t\/frist.html","desc":"","text":""},"type":"ace"},{"alt":"","position":12,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/152492\/21\/12040\/52119\/5fe93622E8bc3302f\/67857d409c58d0f9.jpg","href":"\/\/pro.jd.com\/mall\/active\/4AfQf3FkPRGHhtqqKh9tsWyV97sy\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"TteIvHssJv+j1USc28Th3w==","mcinfo":"03294000-13573946-8801423368-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/4AfQf3FkPRGHhtqqKh9tsWyV97sy\/frist.html","desc":"","text":""},"type":"ace"}],"banner":[{"src":"\/\/imgcps.jd.com\/ling\/100003909373\/5a6P56KB5pqX5b2x6aqR5aOr5aiB\/Nuacn-WFjeaBryDmmZLljZXmnInnpLw\/p-5bd8253082acdd181d02fa22\/d4150b6d.jpg","href":"\/\/pro.jd.com\/mall\/active\/qvR5WfiLRi2e9eUKdHCv9eP7Pht\/frist.html?innerAnchor=100003909373","type":"delivery","ext_columns":{"link":"\/\/pro.jd.com\/mall\/active\/qvR5WfiLRi2e9eUKdHCv9eP7Pht\/frist.html?innerAnchor=100003909373","sku":"100003909373","playImpr":"1#13#300002-4___","mcinfo":"null","focustype":"t","biclk":"1#13#acthot-B0036314-0-100003909373-acthot-0#88","desc":"6\u671f\u514d\u606f \u6652\u5355\u6709\u793c","text":"\u5b8f\u7881\u6697\u5f71\u9a91\u58eb\u5a01#100003909373"}}]},{"recommend":[{"alt":"OPPO\u5dc5\u5cf024\u5c0f\u65f6","position":13,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/155218\/21\/11512\/71383\/5fe5532cE2e68cd5a\/d6a736a88863c103.jpg","href":"\/\/pro.jd.com\/mall\/active\/2kr2j6fCYET7LtjRww5vB9DJNfwV\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"w\/Oz53F4tqc=","mcinfo":"03294000-13573946-8801422620-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/2kr2j6fCYET7LtjRww5vB9DJNfwV\/frist.html","desc":"12\u671f\u767d\u6761\u514d\u606f","text":"OPPO\u5dc5\u5cf024\u5c0f\u65f6"},"type":"ace"},{"alt":"\u7f8e\u5986\u7cbe\u9009\u8bd5\u7528","position":14,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/144331\/15\/16230\/75371\/5fc4e20cEce63f6cb\/0148abea8250fc3b.jpg","href":"\/\/pro.jd.com\/mall\/active\/4W2AmqrXWJDtT4t5v5P6Wxe1WTec\/frist.html?babelChannel=pcjinrituijian","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"2CeAlBiVB6aN5qElSwcuOg==","mcinfo":"03294000-13573946-8801420753-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/4W2AmqrXWJDtT4t5v5P6Wxe1WTec\/frist.html?babelChannel=pcjinrituijian","desc":"","text":"\u7f8e\u5986\u7cbe\u9009\u8bd5\u7528"},"type":"ace"},{"alt":"","position":15,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/151220\/8\/11617\/61079\/5fdff6baE0a6f9504\/2dbfdebc8fd79483.jpg","href":"\/\/pro.jd.com\/mall\/active\/myvknjmTQuCsW7kjrnPRLPufSNu\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"bokuLSNDGKYkus93uySCgA==","mcinfo":"03294000-13573946-8801421457-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/myvknjmTQuCsW7kjrnPRLPufSNu\/frist.html","desc":"","text":""},"type":"ace"}],"banner":[{"sourceTag":"0","ext_columns":{"desc":"0:cpc","focustype":"g"},"src":"\/\/imgcps.jd.com\/img-cubic\/creative_server_cia\/v2\/2000368\/701382\/FocusFullshop\/CkNqZnMvdDEvMTQ1MjI1LzM4LzI4MDI1LzcwNzc4LzYyZDcwNmRhRWUzOTdmYzgyLzgyZjRmNDBkMTY1OWFiNTIucG5nEgk1LXR5XzBfNTYwAjjwi3pCEwoP5aaZ5rSB5Z6D5Zy-6KKLEAFCEwoP54mp576O5Lu35pu05LyYEAJCEAoM56uL5Y2z5oqi6LStEAZCCgoG57K-6YCJEAdYxucq\/cr\/s\/q.jpg","href":"\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9scHMuamQuY29tL3BjL3BzcC83MDEzODI_aW11cD1DZ1lLQUJJQUdBQVNGZ2pHNXlvUTI5ZnIzQU1hQkhSd2MzY2drNjRCS0FFWXNSc2dBQ29nYVcwc2RXSXNlR2RuTEdkcFlTeGphV1lzWmw5aVlWOW1iRjlzTVRZek16UXlBbWx0U3RBQlNYeFRTRlZPVkY5SlRTeEpYMEZmUmt4ZlRTeEpYMEZmVWtWZlRTeEpYMEZmVUV4ZlRTeEpYMEZmVTB4ZlRTeEpYMEZmUTFOZlRTeEpYMEZmVWxOZlRTeEpYMVZmUmt4ZlRTeEpYMU5mUmt4ZlRTeEpYMUpmUmt4ZlRTeEpYMUJmUmt4ZlRTeEpYMUJmVGxCTVgwMHNTVjlIWDFKTVgwMHNTVjlIWDFoSFgxSXNTVjlDWDBaTVgxSXNVMTVKWGxwZVFWOU9UbDlHVlY5U0xFZEpRU3hZUjBVc1ZVTjhSeXBKWDFWZlJreGZUREl4TXpBeU8wWjhUVWxZVkVGSFgwWlNMRVpmUWtGZlJreGZUREUyTXpNd2ZB&log=8wrTNOsMGOmz4SfBkEuhnvCc2v_c5iWJm8L4D88NO1JSueLhM4Kkq9TFVqa285KcOK5KY8pGM5tHaAlpFRiKw8wyZqDZMwgV2LFJCnAFxFSpvzmV-AAai1OlifP2pSfXWhjvW2nBEgjEZURlq-OuxdQlrWQGhbTu-SsBEVMwhOiNNZACRcNxGo3efmOvH8x-R7-xtumr0X6ixGfPT0fnKML-Milf4fv9iyV6tePecGbA-pzrCqhCqyVbVMkdJGzSA9yonY4pkdCezAQQM5PpX9_3dI2EcQ4v8k9vi7t_tp2cGQAhLF1mpmpzxSsZPO9T3t4x8MNHvi5PVdO-Avxy11gknbqSzRcpsp33r8PO2eum9MxN5l39ihgowgkpFfPdXuzS4iK6QKvZJcQzyhEnitI9zytc5CzWBRzJxVRtTe8P1fgcwCZtQmCUV-cw4KjqbUeAjibpJBVok3TFe6dhIUAxADrh2HVBoW7ku1fYXEdiycmOmhv0OfOcMEtSJ3Tu93ktsvJYB1-hTlmB3pJfhuTvN-dhohXTNF6Krf8fO0Dxv6DF9_9zNkpLUpcDmNjZrjk-AJHgB3yv8g7IWjSI11a_sxyXcI7O_A_lxAedESyMNArfJdZLeWrhZ8vuz0Q1LIYq-68dr91AAUji2BD9wv1eKLMUs5z3PSPReRBmax7vR1ldw_yLgEMDxXNa7LfRYEHb5fCi1XwHWvZw5MvxnYruNA-fvTKwZGMWq7L_QsNLIZzHhD-b-LN3rdibKppIDHPNcSRfBNcgpZO0B4ch3lB5Z4Wgerq98WR6B4yhDSVsO1CRhOqtwHCJXsxa4NGfYWsAH4Abu-ogMVjL4Km1okSh0Y3rtUxJsbpC4HsqJBcvq9PryNUlnt90_XRCCtKoNbYr761FWUKxqsYeIyppGS-1YUaJsT4cpQ4izUKtuDdW0EAK0l6iz0846FRQ9Zm_WA97TTxgzb8QPIoyK-0zXkXtymWN2fsZrOAen9qghN_iazlr_2xPnEM_rOHdo8Mq5GC8WIRNcJXoiCmdwi2vEoYORNagTgmLzzSj_GjFk8iuBsRUYlto2FQpya18rAkmY88ovPttz8gUAQKaaGs3r0gfu0tdxvRhpTuy6i7UoZ8&v=404","clog":"\/\/im-x.jd.com\/dsp\/np?log=8wrTNOsMGOmz4SfBkEuhnvCc2v_c5iWJm8L4D88NO1JSueLhM4Kkq9TFVqa285KcOK5KY8pGM5tHaAlpFRiKw8wyZqDZMwgV2LFJCnAFxFSpvzmV-AAai1OlifP2pSfXWhjvW2nBEgjEZURlq-OuxdQlrWQGhbTu-SsBEVMwhOhuKYl04UG5IKtd-wIcWfliJUNZ-Cuf8FLAkehkWApbpqzSQ7deWQQWPayOu6UVWjGKeoHAXKNDFqQdRer-SsRWWCcwO2xFKDdllFzW0NWjuOcWqH_Nh7HI2s4facHBPajtJJic33xqtAgh6pJWLc-vA8O9J-aR2lpB7hCGy4GdZ3gXJZIrdq9Ff0c86iGXXTjdib8mJ2tyHTEjZigdAmfH1HV0gf2A0W_Iw3_yBQmRTuKCo7QOuyXv-j4N-j1pGNztFrxZh1m3DN6w-jdLPmV3ralV1QIPN8yTInQMUwkIuvSGPlJOdw0qFtBxSYfdQsFmX6NHPVvckJrpJBg1uoVEm9srJODzSQwN2vBvuWpp7n5JYxETin7JqMq9Y4clSD5ylQYCKBxJ70Td2CFqf0GhtbAQSxMep95MIeUs5Dllb31zLvfGX0NP6nj5TU_ff02FYTAyw3eVVkBAgf1ntfRILODivdd49bgRGbW-6sV34GcXlL7bdFQXAzSdYriByvz6GkhY1JaicFLVlwWqs_Wa9TaAvb5Z7-zr58h9g0ttM6NqLj7nCUHoAa_N7lWok7Spj2obrH1y9q6X8sikq353kYQnP0WgRP_1e4JDol-V7X8wVZEXC36xqYN3S9nQOm3hdKaOsJX0AGxBi2Ld5LWRp4-iC0GWN0V9Q8fsRF61nbRusQF61x5Udb_Pb6E19vWFOxEkPPL2UStWQp8CYG5xPvfrx_eol4IfKYgaGCiSKltYChod4aZkWrF-lQ6FvrvVjbojej9wXUlQCnfXh67CLSuSzc5Sy6Znft-bXsp0XlF9W-osq4bhR45qYIndsk5urS2vU27iL_icvrJBmGJ8A7Ymhh3m3MqCAuWTPWIt0kiUYugCF-PTmIiNU1eG2TNx1K1XjUZxX9EFU0vKxaIKvOvKTTElTq1BRYdguoBGofVuAND6xOCTqzQ3_YshZP8&v=404&seq=1","type":"ad"}]},{"recommend":[{"alt":"\u8fbe\u80fd\u8de8\u5883\u5976\u7c89","position":16,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/142076\/21\/16719\/81798\/5fc755a4E765768a0\/3e35cebd45e72fcf.jpg","href":"\/\/pro.jd.com\/mall\/active\/34G4aLZqete3T2VDrQfwa4z5hdAm\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"QGSzAaCfP34=","mcinfo":"03294000-13573946-8801423371-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/34G4aLZqete3T2VDrQfwa4z5hdAm\/frist.html","desc":"\u65b0\u5ba2\u5165\u4f1a\u7acb\u51cf40","text":"\u8fbe\u80fd\u8de8\u5883\u5976\u7c89"},"type":"ace"},{"alt":"","position":17,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/159465\/15\/15\/54794\/5fe97b93Edc6d2106\/705acb97ee03fa41.jpg","href":"\/\/pro.jd.com\/mall\/active\/SyNEMyANkXQuUmzn5dUef8CQGPA\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"bkSlXW4t4\/oh7WXA5Q6F0w==","mcinfo":"03294000-13573946-8801423370-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/SyNEMyANkXQuUmzn5dUef8CQGPA\/frist.html","desc":"","text":""},"type":"ace"},{"alt":"","position":18,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/143220\/17\/17461\/57750\/5fcd86f8Ef9a8199c\/0f3a18493a9f64ed.jpg","href":"\/\/pro.jd.com\/mall\/active\/3fNa4gg4udob1juiWbWWBp9z9PBs\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"8E9EFljRna9sk5iyH5TJyQ==","mcinfo":"03294000-13573946-8801422413-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/3fNa4gg4udob1juiWbWWBp9z9PBs\/frist.html","desc":"","text":""},"type":"ace"}],"banner":[{"sourceTag":"0","ext_columns":{"desc":"1:cpm","focustype":"h"},"src":"\/\/img1.360buyimg.com\/pop\/jfs\/t1\/67208\/4\/21074\/87040\/62e09ebdE19f9d307\/ce00b54d607416a2.jpg","href":"\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9wcm8uamQuY29tL21hbGwvYWN0aXZlLzRKdzVnUnVUS3pOc2RKZlZxTHZyaG1LNWpIQkEvaW5kZXguaHRtbA&log=-MonR3E0QwjfJpMIQLcePa59uPb6UcjbvO1AHrg5j5f-jMDerx7P1D7i-o4FCIvSbyhQNn1LXxPf65OBwRX21XlZKHNShMKBYqE2zF8W8ZZLhiEmNy3bzX6XY5g0sLZisf2Lugp-vDV8bgwuMZJpEFG0hcHZMIVvKX9rlTJRjGxtzFpRKLCPp7lU3SW-tZzCkaBEI2T5cQfsCKBbhrabyQxOCiw-uoGUp7w0jxNVN9wRfPx9kAdZr2MLy0OWL0TDGofYJBchDedqERV_xwPXllUXKpDpyaSwulxVUvO0_YcyHjd6wKZ49ispi8ZsJv_YtjZ0NL7coZlodCKX46mJ6d6RVcTVyZu0VMOhIgcLU7u2AWBlPmiiXyQxKnxSNMRk_i2eb8yJGRjT-i8Z1ngcq4TMoZqMKUNKmRVCCRr0HGfdTl7PPNN1vMDlO1snprRKSWSKeRRrY3upaB0L4cwIILlPwGhlDxaImSuX_DeP-O3AXnttUpzQ7XbZJ3_uS3kKOfl9I_gfgUkpqxDTdXFTGjPrFTalhyn0jPkHE3MQknrO5UzyPq-svQO8og9NzhM7ZXWASCENVQ14v-WZKHM3YmZW3NQe8X-6arE8z5L10IqnDjG_D2WB-PP7O5VLxX1-ZxGQJReqvgLGelBR6_d3wqNzl0tWVsb9tasA_cvvUd9F3CAwtCgtN8XYmc1kHAbru9-i0uIWb_NmrYFZLYf7Le8dekHvjYqmsw1QLKsEAhTfszJdRtlphpxhOJ1SvCQZA57UB_i1-8sG026YINWIPgUXxIGX07wq6kXmOX0PmUHnZSlGu7cfjdn1UlkY1bLEiYnThF_8QO2egVGRJZIGo-DgTiUET_W48_ULOm3oAHahsEgano2Bp1g7hnO1dFMK3-2isoyuHIB29eXe5JcIS8Mwi-NsuYLKw92fmJSZUkSzRJZhnQjVL8h8cVEdZLLWeZ1_Vmn4ULb7FTPyIDVFQM-dSnSci_S4VOcPuCo2H7mqQiCB62gCK0w12s_BaQnfaZjtxQFaJFdamecVqQr3byq1VmOBYoe2cGmq17eNpKs&v=404","clog":"\/\/im-x.jd.com\/dsp\/np?log=-MonR3E0QwjfJpMIQLcePa59uPb6UcjbvO1AHrg5j5f-jMDerx7P1D7i-o4FCIvSbyhQNn1LXxPf65OBwRX21XlZKHNShMKBYqE2zF8W8ZZLhiEmNy3bzX6XY5g0sLZisf2Lugp-vDV8bgwuMZJpEFG0hcHZMIVvKX9rlTJRjGxtzFpRKLCPp7lU3SW-tZzCw2KBXZMj4ne7KODiKYT2rV3WGQhMQieNkx3SOC8EJRRUrDMK9x0T7Ny4It3nIr5S8t33xpsr3BMXftbBnLp_v7MPSyhCvOousgpLVi7Gjy5H_hsJzRDTvn2TL4pv9XpvRmLSSaYVVz515Nz3fJVUT_P91gdlJAcDnpXD-yJpXvnTgMi2eeogxVNoFKBF4n2UDpSRb-sw6k65MlwYEyFd19iprX-PNBxl6Sc_lErEESKgVW0TzoB7gW63v4kYv4UHu6Yxr6xzRtpa5YHwoVbUNogecMeTSKUaDtUUQCq5dy2qDCFhB5fuqZCtUnT_bczndZzvn1L-sI8EFPUJ8hexE67D2JXKreeMLX2merwy19HouNW-vgM6p1PL7y4uQY4rmv_in349sI8S2EdeyJ8cMXazoRqx6f4AAAbj3m2TyzirPm5CI6HOLEtn3vnrN5i65teypUutACiVi68pIjYx-KiI7yh8a743nnd5KIX9VrdmPFthPVaRlT9TkSei2CjXZhWBXRIUnbWrPftJXQpmWhh-711AZpB69EiWNc8BBPAvQ7yn6Yvxajkm1bLHuHgHtr_4RxqC_8FA9O56sxAVaVaBLfFl-mqSDCfTlYP1RSRAVU0h60K3RP2CXBDnYR-ICMWxMEmHK9BUg7IJEMED2jgj81WBE6z-vyEh0X1_4iCRXNWcVSdBnur8It9U7XSZOga20F9wquwGPCxr8V3NfoAkB_15-wI-Yp-oet1yCqzqc2zpJIL0xeADDrASuGRa1EtJQ6RlxTiVX9XlC8eO4JPHTLJNIOk6zsNUntDoGTOtNQQccmKftD-L-ijuZ7ZR-QIZ5Q1tyTwNzMKAzqthGVAaiKrjARWc2DfNMECAh44&v=404&seq=1","type":"ad"}]},{"recommend":[{"alt":"","position":19,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/154590\/23\/10967\/74195\/5fe2df62E45a142d9\/883e4bda6f5cd278.jpg","href":"\/\/pro.jd.com\/mall\/active\/29aweHKvVWPaPXgJMbtiLsHk9pFR\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"RAv3J0fJGDZCyu6kQERnLQ==","mcinfo":"03294000-13573946-8801422593-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/29aweHKvVWPaPXgJMbtiLsHk9pFR\/frist.html","desc":"","text":""},"type":"ace"},{"alt":"","position":20,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/158239\/17\/80\/59624\/5fe980daEc6af0098\/0b6bcc0f5587720c.jpg","href":"\/\/pro.jd.com\/mall\/active\/31e4RpwAWH66gXmn7UdN9dMGVY7F\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"oWH9E4RbFQwBBlITEyBAiQ==","mcinfo":"03294000-13573946-8801423361-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/31e4RpwAWH66gXmn7UdN9dMGVY7F\/frist.html","desc":"","text":""},"type":"ace"},{"alt":"","position":21,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/139567\/10\/19800\/44582\/5fe46a35E7004831c\/9721fda27a9495ca.jpg","href":"\/\/pro.jd.com\/mall\/active\/2g9n7V52rEtSdKDkPHKMCURGR9aD\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"vTzmnuWTYC1fchOIQe8O+w==","mcinfo":"03294000-13573946-8801422592-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/2g9n7V52rEtSdKDkPHKMCURGR9aD\/frist.html","desc":"","text":""},"type":"ace"}],"banner":[{"src":"\/\/imgcps.jd.com\/ling\/7776792\/5Lyg57uf5bCP6aOf\/6Zu26aOf57OV54K5\/p-5bd8253082acdd181d02fa02\/71ccf55f.jpg","href":"\/\/pro.jd.com\/mall\/active\/2zMKHHhui8H95uEg63v5aSVFLsZ1\/frist.html?innerAnchor=7776792","type":"delivery","ext_columns":{"link":"\/\/pro.jd.com\/mall\/active\/2zMKHHhui8H95uEg63v5aSVFLsZ1\/frist.html?innerAnchor=7776792","sku":"7776792","playImpr":"1#13#300002-4___","mcinfo":"null","focustype":"t","biclk":"1#13#acthot-B0036759-0-7776792-acthot-1#88","desc":"\u96f6\u98df\u7cd5\u70b9","text":"\u4f20\u7edf\u5c0f\u98df#7776792"}}]},{"recommend":[{"alt":"","position":22,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/146800\/33\/20186\/78685\/5fe5c755Ec3a48986\/df7e8df0dd87913d.jpg","href":"\/\/pro.jd.com\/mall\/active\/HkuJmKguhv6jGeEXdrKPR4ygyje\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"0B9WUXoekna8pOynkQjB1g==","mcinfo":"03294000-13573946-8801423360-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/HkuJmKguhv6jGeEXdrKPR4ygyje\/frist.html","desc":"","text":""},"type":"ace"},{"alt":"","position":23,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/140042\/21\/20481\/60091\/5fe7f503Eea69fdd7\/b4b2147f196a9001.jpg!q95","href":"\/\/pro.jd.com\/mall\/active\/3s4A3dfrTy9K6FTXZWd1U67xJ9VR\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"Wbj96fOBwO5Cyu6kQERnLQ==","mcinfo":"03294000-13573946-8801423363-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/3s4A3dfrTy9K6FTXZWd1U67xJ9VR\/frist.html","desc":"","text":""},"type":"ace"},{"alt":"","position":24,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/154709\/15\/12170\/50231\/5fe9a329E1e52a010\/370be07713e5124c.jpg","href":"\/\/pro.jd.com\/mall\/active\/Y7UJeC8KnEb2y5YufTiDrF2zL7J\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"xdy8JnbW2ywFhKBalJKxfA==","mcinfo":"03294000-13573946-8801423362-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/Y7UJeC8KnEb2y5YufTiDrF2zL7J\/frist.html","desc":"","text":""},"type":"ace"}],"banner":[{"src":"\/\/imgcps.jd.com\/ling\/3486678\/6L-Q5Yqo5YGl6Lqr5oyH5Y2X\/6JCl5YW76L-b6Zi256-H\/p-5bd8253082acdd181d02fa5f\/f2af4529.jpg","href":"\/\/pro.jd.com\/mall\/active\/2DPCwovvaBUa7HciiQ2PHCvyECac\/frist.html?innerAnchor=3486678","type":"delivery","ext_columns":{"link":"\/\/pro.jd.com\/mall\/active\/2DPCwovvaBUa7HciiQ2PHCvyECac\/frist.html?innerAnchor=3486678","sku":"3486678","playImpr":"1#13#300002-4___","mcinfo":"null","focustype":"t","biclk":"1#13#acthot-B0007061-0-3486678-acthot-2#88","desc":"\u8425\u517b\u8fdb\u9636\u7bc7","text":"\u8fd0\u52a8\u5065\u8eab\u6307\u5357#3486678"}}]}];        //618大促上报降级配置
        window.pageConfig.handleReportStart=new Date('2020/11/10 22:00:00').getTime();

		window.pageConfig.handleReportEnd=new Date('2020/11/12 10:00:00').getTime();

		    </script>

    <script type="text/javascript">
        !function(e){pageConfig.isWide=function(){var n=e,i=document,o=i.documentElement,t=i.getElementsByTagName("body")[0],a=n.innerWidth||o.clientWidth||t.clientWidth;return a>=1370}();var n=[];pageConfig.isWide?(n.push("root61"),n.push("o2_wide")):n.push("o2_mini");var i=document.getElementsByTagName("html")[0];i.className=n.join(" ")}(window,void 0);
    </script>

    <script type="text/javascript">
        !function (n) {
            function o(n) {
                for (var o = n + "=", t = document.cookie.split(";"), e = 0; e < t.length; e++) {
                    for (var i = t[e]; " " == i.charAt(0);) i = i.substring(1, i.length);
                    if (0 == i.indexOf(o)) return i.substring(o.length, i.length)
                }
                return null
            }

            var t = o("pcm"), e = n.navigator.userAgent.toLocaleLowerCase(), i = "//m.jd.com",
                r = /iphone|android|symbianos|windows\sphone/g, c = /micromessenger|qq\/[\d.]+/i;
            return c.test(e) ? (n.location.href = "//wqs.jd.com/?from=jdindex", !1) : r.test(e) && "1" != t ? (n.location.href = i, !1) : void 0
        }(window);
    </script>

    <script type="text/javascript">
        window.search = function (a) {
            var b, c = "//search.jd.com/Search?keyword={keyword}&enc={enc}{additional}";
            var d = search.additinal || "";
            var e = document.getElementById(a);
            var f = e.value;
            if (f = f.replace(/^\s*(.*?)\s*$/, "$1"), f.length > 100 && (f = f.substring(0, 100)), "" == f) return void (window.location.href = window.location.href);
            var g = 0;
            "undefined" != typeof window.pageConfig && "undefined" != typeof window.pageConfig.searchType && (g = window.pageConfig.searchType);
            var h = "&cid{level}={cid}";
            var i = "string" == typeof search.cid ? search.cid : "";
            var j = "string" == typeof search.cLevel ? search.cLevel : "";
            var k = "string" == typeof search.ev_val ? search.ev_val : "";
            switch (g) {
                case 0:
                    break;
                case 1:
                    j = "-1", d += "&book=y";
                    break;
                case 2:
                    j = "-1", d += "&mvd=music";
                    break;
                case 3:
                    j = "-1", d += "&mvd=movie";
                    break;
                case 4:
                    j = "-1", d += "&mvd=education";
                    break;
                case 5:
                    var l = "&other_filters=%3Bcid1%2CL{cid1}M{cid1}[cid2]";
                    switch (j) {
                        case "51":
                            h = l.replace(/\[cid2]/, ""), h = h.replace(/\{cid1}/g, "5272");
                            break;
                        case "52":
                            h = l.replace(/\{cid1}/g, "5272"), h = h.replace(/\[cid2]/, "%3Bcid2%2CL{cid}M{cid}");
                            break;
                        case "61":
                            h = l.replace(/\[cid2]/, ""), h = h.replace(/\{cid1}/g, "5273");
                            break;
                        case "62":
                            h = l.replace(/\{cid1}/g, "5273"), h = h.replace(/\[cid2]/, "%3Bcid2%2CL{cid}M{cid}");
                            break;
                        case "71":
                            h = l.replace(/\[cid2]/, ""), h = h.replace(/\{cid1}/g, "5274");
                            break;
                        case "72":
                            h = l.replace(/\{cid1}/g, "5274"), h = h.replace(/\[cid2]/, "%3Bcid2%2CL{cid}M{cid}");
                            break;
                        case "81":
                            h = l.replace(/\[cid2]/, ""), h = h.replace(/\{cid1}/g, "5275");
                            break;
                        case "82":
                            h = l.replace(/\{cid1}/g, "5275"), h = h.replace(/\[cid2]/, "%3Bcid2%2CL{cid}M{cid}")
                    }
                    c = "//search-e.jd.com/searchDigitalBook?ajaxSearch=0&enc=utf-8&key={keyword}&page=1{additional}";
                    break;
                case 6:
                    j = "-1", c = "//music.jd.com/8_0_desc_0_0_1_15.html?key={keyword}";
                    break;
                case 7:
                    c = "//s-e.jd.com/Search?key={keyword}&enc=utf-8";
                    break;
                case 8:
                    c = "//search.jd.hk/Search?keyword={keyword}&enc=utf-8";
                    break;
                case 9:
                    d += "&market=1"
            }
            if ("string" == typeof i && "" != i && "string" == typeof j) {
                var m = /^(?:[1-8])?([1-3])$/;
                j = "-1" == j ? "" : m.test(j) ? RegExp.$1 : "";
                var n = h.replace(/\{level}/, j);
                n = n.replace(/\{cid}/g, i), d += n
            }
            if ("string" == typeof k && "" != k && (d += "&ev=" + k), f = encodeURIComponent(f), b = c.replace(/\{keyword}/, f), b = b.replace(/\{enc}/, "utf-8"), b = b.replace(/\{additional}/, d), "object" == typeof $o && ("string" == typeof $o.lastKeyword && (b += "&wq=" + encodeURIComponent($o.lastKeyword)), "string" == typeof $o.pvid && (b += "&pvid=" + $o.pvid)), b.indexOf("/search.jd.com/") > 0) try {
                JA.tracker.ngloader("search.000009", {key: f, posid: a, target: b})
            } catch (o) {
            }
            ("undefined" == typeof search.isSubmitted || 0 == search.isSubmitted) && (setTimeout(function () {
                window.location.href = b
            }, 50), search.isSubmitted = !0)
        };
    </script>


</head>

<body class="index">
<div class="mod_container">
    <!--无障碍占位-->
    <div id="J_accessibility"></div>
    <!--顶通占位 -->
    <div id="J_promotional-top">
    </div>
    <div id="shortcut">
        <div class="w">
            <ul class="fl" clstag="h|keycount|head|topbar_01">
                <li class="dropdown" id="ttbar-mycity"></li>
            </ul>

            <ul class="fr">
                <li class="fore1 dropdown" id="ttbar-login" clstag="h|keycount|head|topbar_02">
					<a href="//passport.jd.com/uc/login?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F" class="link-login">你好，请登录</a>&nbsp;&nbsp;<a
					href="//reg.jd.com/reg/person?ReturnUrl=https%3A//www.jd.com/" class="link-regist style-red">免费注册</a>
                </li>
                <li class="spacer"></li>
                <li class="fore2" clstag="h|keycount|head|topbar_03">
                    <div class="dt"><a target="_blank" href="//order.jd.com/center/list.action">我的订单</a></div>
                </li>
                <li class="spacer"></li>
                <li class="fore3 dropdown" id="ttbar-myjd" clstag="h|keycount|head|topbar_04">
                    <div class="dt cw-icon"><a target="_blank" href="//home.jd.com/">我的京东</a><i class="iconfont">&#xe610;</i><i
                            class="ci-right"><s>◇</s></i></div>
                    <div class="dd dropdown-layer"></div>
                </li>
                <li class="spacer"></li>
                <li class="fore4" clstag="h|keycount|head|topbar_05">
                    <div class="dt"><a target="_blank" href="//vip.jd.com/">京东会员</a></div>
                </li>
                <li class="spacer"></li>
                <li class="fore5" clstag="h|keycount|head|topbar_06">
                    <div class="dt"><a target="_blank" href="//b.jd.com/">企业采购</a></div>
                </li>
                <li class="spacer"></li>
                <li class="fore8 dropdown" id="ttbar-serv" clstag="h|keycount|head|topbar_07">
                    <div class="dt cw-icon">客户服务<i class="iconfont">&#xe610;</i><i class="ci-right"><s>◇</s></i></div>
                    <div class="dd dropdown-layer"></div>
                </li>
                <li class="spacer"></li>
                <li class="fore9 dropdown" id="ttbar-navs" clstag="h|keycount|head|topbar_08">
                    <div class="dt cw-icon">网站导航<i class="iconfont">&#xe610;</i><i class="ci-right"><s>◇</s></i></div>
                    <div class="dd dropdown-layer"></div>
                </li>
                <li class="spacer"></li>
                <li class="fore10 mobile" id="J_mobile" clstag="h|keycount|head|topbar_09">
                    <div class="dt mobile_txt">手机京东</div>
                    <div class="mobile_static">
                        <div class="mobile_static_qrcode"></div>
                    </div>
                    <div id='J_mobile_pop' class='mod_loading mobile_pop'>
                    </div>
                </li>
            </ul>
        </div>
    </div>


    <div id="header">
        <div class="w">
            <div id="logo" class="logo">
                <h1 class="logo_tit">
                    <a href="//www.jd.com" class="logo_tit_lk" clstag="h|keycount|head|logo_01">京东</a>
                </h1>
                <h2 class="logo_subtit">京东,多快好省</h2>
                <div class="logo_extend" clstag="h|keycount|head|logo_02"></div>
            </div>

            <div id="search">
                <div class="search-m">
                    <div class="search_logo">
                        <a href="//www.jd.com" class="search_logo_lk" clstag="h|keycount|head|logo_01" tabindex="-1">京东，多快好省</a>
                    </div>

                    <div class="form" role="serachbox">
                        <ul id="shelper" class="search-helper" style="display: none"></ul>
                        <input clstag="h|keycount|head|search_c" type="text"
                               onkeydown="javascript:if(event.keyCode==13) search('key');" autocomplete="off" id="key"
                               accesskey="s"
                               class="text"
                               aria-label="搜索"/>
                        <button clstag="h|keycount|head|search_a" onclick="search('key');return false;" class="button" aria-label="搜索">
                            <i
                                    class="iconfont">&#xe60b;</i></button>
                    </div>

                    <div id="settleup" class="dropdown" clstag="h|keycount|head|cart_null">
                        <div class="cw-icon">
                            <i class="iconfont">&#xe60c;</i>
                            <a target="_blank" href="//cart.jd.com/cart.action">我的购物车</a>
                            <i class="ci-count" id="shopping-amount"></i>
                        </div>
                        <div class="dropdown-layer">
                            <div id="J_cart_pop">
                                <span class="loading"></span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div id="hotwords" clstag="h|keycount|head|search_d" role=""></div>

            <div id="navitems" role="navigation">
                <div class="spacer"></div>
                                                            <ul id="navitems-group1">
                                        <li clstag="h|keycount|head|navi_01" class="fore1">
                                                    <a class="navitems-lk"
                               target="_blank"
                               href="https://miaosha.jd.com/"
                               aria-lable="秒杀">秒杀                                                            </a>
                                            </li>
                                                                            <li clstag="h|keycount|head|navi_02" class="fore2">
                                                    <a class="navitems-lk"
                               target="_blank"
                               href="https://a.jd.com/"
                               aria-lable="优惠券">优惠券                                                            </a>
                                            </li>
                                                                            <li clstag="h|keycount|head|navi_03" class="fore3">
                                                    <a class="navitems-lk"
                               target="_blank"
                               href="https://plus.jd.com/index?flow_system=appicon&flow_entrance=appicon11&flow_channel=pc"
                               aria-lable="PLUS会员">PLUS会员                                                            </a>
                                            </li>
                                                                            <li clstag="h|keycount|head|navi_04" class="fore4">
                                                    <a class="navitems-lk"
                               target="_blank"
                               href="https://red.jd.com/"
                               aria-lable="品牌闪购">品牌闪购                                                            </a>
                                            </li>
                                            </ul>
                        <div class="spacer"></div>
                                                                                <ul id="navitems-group2">
                                        <li clstag="h|keycount|head|navi_05" class="fore5">
                                                    <a class="navitems-lk"
                               target="_blank"
                               href="https://paimai.jd.com/"
                               aria-lable="拍卖">拍卖                                                            </a>
                                            </li>
                                                                            <li clstag="h|keycount|head|navi_06" class="fore6">
                                                    <a class="navitems-lk"
                               target="_blank"
                               href="https://jiadian.jd.com/"
                               aria-lable="京东家电">京东家电                                                            </a>
                                            </li>
                                                                            <li clstag="h|keycount|head|navi_07" class="fore7">
                                                    <a class="navitems-lk"
                               target="_blank"
                               href="https://chaoshi.jd.com/"
                               aria-lable="京东超市">京东超市                                                            </a>
                                            </li>
                                                                            <li clstag="h|keycount|head|navi_08" class="fore8">
                                                    <a class="navitems-lk"
                               target="_blank"
                               href="https://fresh.jd.com/"
                               aria-lable="京东生鲜">京东生鲜                                                            </a>
                                            </li>
                                            </ul>
                        <div class="spacer"></div>
                                                                                <ul id="navitems-group3">
                                        <li clstag="h|keycount|head|navi_09" class="fore9">
                                                    <a class="navitems-lk"
                               target="_blank"
                               href="https://www.jd.hk/"
                               aria-lable="京东国际">京东国际                                                            </a>
                                            </li>
                                                                            <li clstag="h|keycount|head|navi_10" class="fore10">
                                                    <a class="navitems-lk"
                               target="_blank"
                               href="https://www.jdcloud.com/cn/?utm_source=DMT_jdcom&utm_medium=title&utm_campaign=regular&utm_term=NA"
                               aria-lable="京东云">京东云                                                            </a>
                                            </li>
                                            </ul>
                        <div class="spacer"></div>
                                    
            </div>

            <div id="treasure"></div>
        </div>
    </div>
    <div class="fs">
        <div class="grid_c1 fs_inner">
            <div class="fs_col1">
                <div id='J_cate' class="cate J_cate" role="navigation" aria-label="左侧导航">
                    <ul class="JS_navCtn cate_menu">
                                                    <li class="cate_menu_item" data-index="1" clstag="h|keycount|head|category_01a">
                                                                <a target="_blank" class="cate_menu_lk" href="//jiadian.jd.com">家用电器</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="2" clstag="h|keycount|head|category_02a">
                                                                <a target="_blank" class="cate_menu_lk" href="//search.jd.com&#47;Search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;wq=%E6%89%8B%E6%9C%BA&amp;pvid=8858151673f941e9b1a4d2c7214b2b52">手机</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//wt.jd.com">运营商</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//shuma.jd.com&#47;">数码</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="3" clstag="h|keycount|head|category_03a">
                                                                <a target="_blank" class="cate_menu_lk" href="//diannao.jd.com&#47;">电脑</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//bg.jd.com">办公</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="4" clstag="h|keycount|head|category_04a">
                                                                <a target="_blank" class="cate_menu_lk" href="//channel.jd.com&#47;home.html">家居</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//channel.jd.com&#47;furniture.html">家具</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//jzjc.jd.com&#47;">家装</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//channel.jd.com&#47;kitchenware.html">厨具</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="5" clstag="h|keycount|head|category_05a">
                                                                <a target="_blank" class="cate_menu_lk" href="//phat.jd.com&#47;10-603.html">男装</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//phat.jd.com&#47;10-507.html">女装</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//phat.jd.com&#47;10-156.html">童装</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//channel.jd.com&#47;1315-1345.html">内衣</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="6" clstag="h|keycount|head|category_06a">
                                                                <a target="_blank" class="cate_menu_lk" href="//beauty.jd.com&#47;">美妆</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//phat.jd.com&#47;10-816.html">个护清洁</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//channel.jd.com&#47;pet.html">宠物</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="7" clstag="h|keycount|head|category_07a">
                                                                <a target="_blank" class="cate_menu_lk" href="//phat.jd.com&#47;10-184.html">女鞋</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//phat.jd.com&#47;10-183.html">箱包</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//pro.jd.com&#47;mall&#47;active&#47;2BcJPCVVzMEtMUynXkPscCSsx68W&#47;frist.html">钟表</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//channel.jd.com&#47;jewellery.html">珠宝</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="8" clstag="h|keycount|head|category_08a">
                                                                <a target="_blank" class="cate_menu_lk" href="//phat.jd.com&#47;10-185.html">男鞋</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//phat.jd.com&#47;10-109.html">运动</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//phat.jd.com&#47;10-272.html">户外</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="9" clstag="h|keycount|head|category_09a">
                                                                <a target="_blank" class="cate_menu_lk" href="//xinfang.jd.com&#47;">房产</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//car.jd.com&#47;">汽车</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//che.jd.com&#47;">汽车用品</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="10" clstag="h|keycount|head|category_10a">
                                                                <a target="_blank" class="cate_menu_lk" href="//search.jd.com&#47;Search?keyword=%E6%AF%8D%E5%A9%B4&amp;enc=utf-8&amp;wq=%E6%AF%8D%E5%A9%B4&amp;pvid=3e86f063795740d594b1bb1187e02063">母婴</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//toy.jd.com&#47;">玩具乐器</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="11" clstag="h|keycount|head|category_11a">
                                                                <a target="_blank" class="cate_menu_lk" href="//food.jd.com&#47;">食品</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//jiu.jd.com">酒类</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//fresh.jd.com">生鲜</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//prodev.jd.com&#47;mall&#47;active&#47;41YdRWconKueXwVVnLLM6YY4x4wU&#47;frist.html">特产</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="12" clstag="h|keycount|head|category_12a">
                                                                <a target="_blank" class="cate_menu_lk" href="//art.jd.com">艺术</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//channel.jd.com&#47;1672-2599.html">礼品鲜花</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//nong.jd.com">农资绿植</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="13" clstag="h|keycount|head|category_13a">
                                                                <a target="_blank" class="cate_menu_lk" href="//phat.jd.com&#47;10-925.html">医药保健</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//channel.jd.com&#47;9192-9196.html">计生情趣</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="14" clstag="h|keycount|head|category_14a">
                                                                <a target="_blank" class="cate_menu_lk" href="//pro.jd.com&#47;mall&#47;active&#47;3sAaxodHF7kfo3s95cjxo2UZUxu2&#47;frist.html">图书</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//pro.jd.com&#47;mall&#47;active&#47;2TxxbZnqAm7M8tkDpTN3VJNtoSKo&#47;frist.html">文娱</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//education.jd.com">教育</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//e.jd.com&#47;ebook.html">电子书</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="15" clstag="h|keycount|head|category_15a">
                                                                <a target="_blank" class="cate_menu_lk" href="//jipiao.jd.com&#47;">机票</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//hotel.jd.com&#47;">酒店</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//trip.jd.com&#47;">旅游</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//ish.jd.com&#47;">生活</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="16" clstag="h|keycount|head|category_16a">
                                                                <a target="_blank" class="cate_menu_lk" href="//licai.jd.com&#47;">理财</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//pro.jd.com&#47;mall&#47;active&#47;4EYjXQ6xjnM9TgeSjuMRE8ACEk6q&#47;frist.html">众筹</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//baitiao.jd.com">白条</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//pro.jd.com&#47;mall&#47;active&#47;4NuyHPocGdSDUzmSVosXjVwvEGdG&#47;frist.html">保险</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="17" clstag="h|keycount|head|category_17a">
                                                                <a target="_blank" class="cate_menu_lk" href="//anzhuang.jd.com">安装</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//search.jd.com&#47;Search?keyword=维修&amp;enc=utf-8&amp;wq=维修&amp;pvid=eba9b7454da0494c960f074db37be847">维修</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//cleanclean.jd.com">清洗</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//2.jd.com&#47;">二手</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="18" clstag="h|keycount|head|category_18a">
                                                                <a target="_blank" class="cate_menu_lk" href="//mro.jd.com&#47;">工业品</a>
                                                                                                </li>
                                            </ul>
                    <div id="J_popCtn" class="JS_popCtn cate_pop mod_loading" style="display: none;"></div>
                </div>
            </div>

            <div class="fs_col2">
                <div id='J_focus' class="focus">
                    <div class="focus__loading focus__main skeleton-wrapper">
                        <div class="focus-slider">
                        <div class="focus-item__core skeleton-elementDark mod_lazyload"></div>
                        <div class="focus-item__recommend">
                            <div class="recommend-item skeleton-elementDark"></div>
                            <div class="recommend-item skeleton-elementDark"></div>
                            <div class="recommend-item skeleton-elementDark"></div>
                        </div>
                        </div>
                    </div>
                </div>
            </div>

            <div id="J_fs_col3" class="fs_col3">
                <div id='J_user' class="J_user user mod_loading">
                    <div class="user__loading user_inner">
                    <div class="user_avatar">
                        <div class="user_avatar_lk skeleton-element"></div>
                    </div>
                    <div class="user_show skeleton-element">
                        <p></p><p></p>
                    </div>
                    <div class="user_profit_placeholder skeleton-element"></div>
                </div>
                </div>
                <div id='J_news' class="news J_news">
                    <div class="news__loading news2">
                        <div class="news_hd">
                        <div class="news_hd_placeholder skeleton-element"></div>
                        </div>
                        <div class="news_list"><div class="news_item skeleton-element"></div><div class="news_item skeleton-element"></div><div class="news_item skeleton-element"></div><div class="news_item skeleton-element"></div></div>
                    </div>
                </div>
                <div id="J_service" class="service">
                    <div class="service_entry">
                        <ul class="J_tab_head service_list">
                            <li class="service_item service_frame mod_tab_head_item">
                                <a href="//chongzhi.jd.com/" class="service_lk"
                                   target="_blank" clstag="h|keycount|head|shortcut_01" aria-label="话费">
                                                                                                                                                    <i class="service_ico service_ico_huafei">
                                        <img class="service_ico_img"
                                             src="//m.360buyimg.com/babel/jfs/t1/30057/19/14881/720/5cbf064aE187b8361/eed6f6cbf1de3aaa.png"/>
                                        <img class="service_ico_img_hover"
                                             src="//m.360buyimg.com/babel/jfs/t1/45423/33/385/778/5cd4f265E442a9342/0aff0a42cece09ee.png"/>
                                    </i>
                                    <span class="service_txt">话费</span>
                                </a>
                            </li>
                            <li class="service_item service_frame mod_tab_head_item">
                                <a href="//jipiao.jd.com/" class="service_lk" target="_blank"
                                   clstag="h|keycount|head|shortcut_02" aria-label="机票">
                                                                                                                                                    <i class="service_ico service_ico_jipiao">
                                        <img class="service_ico_img"
                                             src="//m.360buyimg.com/babel/jfs/t1/36478/38/5384/2901/5cbf065aEb0c60a12/afb4399323fe3b76.png"/>
                                        <img class="service_ico_img_hover"
                                             src="//m.360buyimg.com/babel/jfs/t1/34261/15/10242/3120/5cd4f256E10257aba/8f3f63ae04ff19af.png"/>
                                    </i>
                                    <span class="service_txt">机票</span>
                                </a>
                            </li>
                            <li class="service_item service_frame mod_tab_head_item">
                                <a href="//hotel.jd.com/" class="service_lk" target="_blank"
                                   clstag="h|keycount|head|shortcut_03" aria-label="酒店">
                                                                                                                                                    <i class="service_ico service_ico_jiudian">
                                        <img class="service_ico_img"
                                             src="//m.360buyimg.com/babel/jfs/t1/31069/34/14642/979/5cbf0665Ec7dc8223/5fee386254dd2ebc.png"/>
                                        <img class="service_ico_img_hover"
                                             src="//m.360buyimg.com/babel/jfs/t1/44601/19/915/1039/5cd4f1cfE2e46473c/b61f083872a7a1de.png"/>
                                    </i>
                                    <span class="service_txt">酒店</span>
                                </a>
                            </li>
                            <li class="service_item service_frame service_frame2 mod_tab_head_item" data-row="2">
                                <a href="//game.jd.com/" class="service_lk" target="_blank"
                                   clstag="h|keycount|head|shortcut_04" aria-label="游戏">
                                                                                                                                                    <i class="service_ico service_ico_youxi">
                                        <img class="service_ico_img"
                                             src="//m.360buyimg.com/babel/jfs/t1/32403/22/14829/3699/5cbf0674E04723693/caa83ce9b881cd24.png"/>
                                        <img class="service_ico_img_hover"
                                             src="//m.360buyimg.com/babel/jfs/t1/57520/8/375/4092/5cd4f1d8Ea1266047/1c590322ece537ba.png"/>
                                    </i>
                                    <span class="service_txt">游戏</span>
                                </a>
                            </li>
                                                                                                                                                                                                                                                                                                                                                <li class="service_item service_noframe">
                                        <a href="https:&#47;&#47;jiayouka.jd.com&#47;" class="service_lk" target="_blank"
                                           clstag="h|keycount|head|shortcut_05" aria-label="加油卡">
                                                                                        <i class="service_ico">
                                                <!-- 常态 icon -->
                                                <img class="service_ico_img"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;71890&#47;14&#47;9897&#47;3048&#47;5d7739ddE93eb94f8&#47;f1f6dc5c207329f9.png"/>
                                                <!-- hover 态 icon -->
                                                <img class="service_ico_img_hover"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;36002&#47;35&#47;9106&#47;3311&#47;5cd4f1bdE06ff07ed&#47;9570fdd46ecd3a76.png"/>
                                            </i>
                                            <span class="service_txt">加油卡</span>
                                        </a>
                                    </li>
                                                                                                                                <li class="service_item service_noframe">
                                        <a href="https:&#47;&#47;train.jd.com&#47;" class="service_lk" target="_blank"
                                           clstag="h|keycount|head|shortcut_06" aria-label="火车票">
                                                                                        <i class="service_ico">
                                                <!-- 常态 icon -->
                                                <img class="service_ico_img"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;45761&#47;32&#47;10307&#47;1581&#47;5d7739e2Ece4b6671&#47;0004c1b85fbf7bde.png"/>
                                                <!-- hover 态 icon -->
                                                <img class="service_ico_img_hover"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;58891&#47;36&#47;278&#47;1745&#47;5cd4f1e0Ef4cc50a7&#47;f12276b17e5dcf3b.png"/>
                                            </i>
                                            <span class="service_txt">火车票</span>
                                        </a>
                                    </li>
                                                                                                                                <li class="service_item service_noframe">
                                        <a href="https:&#47;&#47;pro.jd.com&#47;mall&#47;active&#47;4EYjXQ6xjnM9TgeSjuMRE8ACEk6q&#47;frist.html" class="service_lk" target="_blank"
                                           clstag="h|keycount|head|shortcut_07" aria-label="众筹">
                                                                                        <i class="service_ico">
                                                <!-- 常态 icon -->
                                                <img class="service_ico_img"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;51584&#47;31&#47;10221&#47;1685&#47;5d7739e7E1adb25cd&#47;1d0957d7f2ae01a2.png"/>
                                                <!-- hover 态 icon -->
                                                <img class="service_ico_img_hover"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;50929&#47;1&#47;374&#47;1847&#47;5cd4f1eaE5daf90db&#47;cebbff76b25dc22e.png"/>
                                            </i>
                                            <span class="service_txt">众筹</span>
                                        </a>
                                    </li>
                                                                                                                                <li class="service_item service_noframe">
                                        <a href="https:&#47;&#47;jr.jd.com&#47;" class="service_lk" target="_blank"
                                           clstag="h|keycount|head|shortcut_08" aria-label="理财">
                                                                                        <i class="service_ico">
                                                <!-- 常态 icon -->
                                                <img class="service_ico_img"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;52683&#47;35&#47;10394&#47;3447&#47;5d7739edE270aa7b3&#47;d4d1151b09b5553b.png"/>
                                                <!-- hover 态 icon -->
                                                <img class="service_ico_img_hover"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;47544&#47;23&#47;372&#47;3943&#47;5cd4f24eE92fbcf79&#47;4b49b55af25a7bdf.png"/>
                                            </i>
                                            <span class="service_txt">理财</span>
                                        </a>
                                    </li>
                                                                                                                                <li class="service_item service_noframe">
                                        <a href="https:&#47;&#47;baitiao.jd.com&#47;?from=jrscyn_20160" class="service_lk" target="_blank"
                                           clstag="h|keycount|head|shortcut_09" aria-label="白条">
                                                                                        <i class="service_ico">
                                                <!-- 常态 icon -->
                                                <img class="service_ico_img"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;56296&#47;3&#47;10260&#47;1443&#47;5d7739f3E233abc53&#47;e6976f3cb30c9a8a.png"/>
                                                <!-- hover 态 icon -->
                                                <img class="service_ico_img_hover"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;39983&#47;24&#47;6834&#47;1596&#47;5cd4f247E8cf89f1e&#47;b8a8418d5418f471.png"/>
                                            </i>
                                            <span class="service_txt">白条</span>
                                        </a>
                                    </li>
                                                                                                                                <li class="service_item service_noframe">
                                        <a href="https:&#47;&#47;movie.jd.com&#47;frist.html" class="service_lk" target="_blank"
                                           clstag="h|keycount|head|shortcut_10" aria-label="电影票">
                                                                                        <i class="service_ico">
                                                <!-- 常态 icon -->
                                                <img class="service_ico_img"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;60778&#47;37&#47;9838&#47;3066&#47;5d7739faEd3b7dbb9&#47;dd4d9ef7ce8fc169.png"/>
                                                <!-- hover 态 icon -->
                                                <img class="service_ico_img_hover"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;41106&#47;15&#47;4551&#47;3300&#47;5cd4f1c7E507148c7&#47;90a218f053e903d2.png"/>
                                            </i>
                                            <span class="service_txt">电影票</span>
                                        </a>
                                    </li>
                                                                                                                                <li class="service_item service_noframe">
                                        <a href="https:&#47;&#47;b.jd.com&#47;" class="service_lk" target="_blank"
                                           clstag="h|keycount|head|shortcut_11" aria-label="企业购">
                                                                                        <i class="service_ico">
                                                <!-- 常态 icon -->
                                                <img class="service_ico_img"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;40738&#47;20&#47;14562&#47;826&#47;5d773a01E09eb8121&#47;d6f3909618c6307a.png"/>
                                                <!-- hover 态 icon -->
                                                <img class="service_ico_img_hover"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;45316&#47;3&#47;388&#47;884&#47;5cd4f25eEea4c67ed&#47;671f7c186c5e9b01.png"/>
                                            </i>
                                            <span class="service_txt">企业购</span>
                                        </a>
                                    </li>
                                                                                                                                <li class="service_item service_noframe">
                                        <a href="https:&#47;&#47;o.jd.com" class="service_lk" target="_blank"
                                           clstag="h|keycount|head|shortcut_12" aria-label="礼品卡">
                                                                                        <i class="service_ico">
                                                <!-- 常态 icon -->
                                                <img class="service_ico_img"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;57014&#47;6&#47;10297&#47;815&#47;5d773a07Ec7a61fc9&#47;97917a2daa34be0f.png"/>
                                                <!-- hover 态 icon -->
                                                <img class="service_ico_img_hover"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;55911&#47;31&#47;402&#47;858&#47;5cd4f23eE6f536460&#47;5da079255c6dfabe.png"/>
                                            </i>
                                            <span class="service_txt">礼品卡</span>
                                        </a>
                                    </li>
                                                                                    </ul>
                    </div>
                    <div class="J_tab_content service_pop" tabindex="-1" aria-hidden="true">
                        <div class="mod_tab_content_item service_pop_item mod_loading"></div>
                        <div class="mod_tab_content_item service_pop_item mod_loading"></div>
                        <div class="mod_tab_content_item service_pop_item mod_loading"></div>
                        <div class="mod_tab_content_item service_pop_item mod_loading"></div>
                        <a class="J_service_pop_close service_pop_close iconfont" href="javascript:;" tabindex="-1"></a>
                    </div>
                </div>
            </div>
        </div>
        <div id="J_fs_act" class="fs_act"></div>
    </div>
    <!-- CLUB_LINK start seo  -->
    <div style="display:none">
                <a href="//itb2b.jd.com/">京采汇</a>
                <a href="//pro.m.jd.com/mall/active/2ukQm4T7b9utHWDn2cXGH2KEnUYV/frist.html">电动车十大排行榜</a>
                <a href="//pro.m.jd.com/mall/active/pVc2ZtPRvzzCuAE8eRSfXFvan1d/frist.html">电动车价钱</a>
                <a href="//jzt.m.jd.com/school/market/2021/11/11">京准通11.11</a>
                <a href="//pro.m.jd.com/mall/active/wcvrZNcfWbUV6spvqoY17CXwny1/frist.html">电动车十大名牌排名</a>
                <a href="//pro.m.jd.com/mall/active/2GYft5Ph4ZAAAQKWxJyHtsFun1ef/frist.html">十大名牌电动车</a>
                <a href="//pro.m.jd.com/mall/active/2GL7sRxRYrRSE6Zk7DesxmQ5JDvc/frist.html">电动车三轮车</a>
                <a href="//pro.m.jd.com/mall/active/22ADrLDeC31kzfT171t8UYDcRf23/frist.html">电动车排行</a>
                <a href="//union.jd.com">网络赚钱</a>
                <a href="//pro.m.jd.com/mall/active/1X36PoLQQ6JYgrLusHZpfowpxpc/frist.html">电动车十大品牌排行榜</a>
                <a href="//pro.m.jd.com/mall/active/3VLqBaQBjR3XxwDBNdDYMMAAX1wc/frist.html">电动车十大排行</a>
                <a href="//pro.m.jd.com/mall/active/3ERkqhxNQozbNJ3BQCxUX3p1sFEC/frist.html">电动车十佳品牌排行榜</a>
                <a href="//pro.m.jd.com/mall/active/TU6auzpj8HDPAqumWMZ35uML4HB/frist.html">电动车电池十大排名</a>
                <a href="//pro.m.jd.com/mall/active/3uxWVvqh2dmwN2eLbqDfGj6BBoAk/frist.html">台铃电动车</a>
                <a href="//www.jd.com/sptopic/117296ca19d46b24dfeb3.html">女士鞋</a>
                <a href="//www.jd.com/cppf/9847333cd3d99d6886d9.html">实木沙发</a>
                <a href="//www.jd.com/book/737280eea8ac7dfea03.html">索尼电视</a>
                <a href="//www.jd.com/hotitem/9855fbd5a67b591890f1.html">卫浴品牌</a>
                <a href="//www.jd.com/zuozhe/7378d855fa5f85d59a5.html">奥克斯空调</a>
                <a href="//fresh.jd.com/shengxian/12218e48f879c700b44c1.html">百香果</a>
                <a href="https://yp.jd.com/7377f27b3c0f467edec.html">美的变频冰箱</a>
                <a href="https://www.jd.com/phb/737233c1fef6369a2bf.html">常熟世茂交家电</a>
                <a href="https://www.jd.com/phb/key_7371d629ebd8e0e7ebf.html">美菱冰箱50l</a>
                <a href="https://www.jd.com/jiage/737f87f679b386c1f8d.html">美的冰箱460</a>
                <a href="https://www.jd.com/tupian/7373998da2215062bc1.html">BCD-190KHM</a>
                <a href="https://www.jd.com/xinkuan/7379796bcc56db1167c.html">LG电脑控温冰箱</a>
                <a href="https://www.jd.com/book/737b2da90cad920c0a6.html">京东自营两门冰箱</a>
                <a href="https://www.jd.com/zuozhe/7378662bdf37a93c98d.html">松下多开门冰箱</a>
                <a href="https://www.jd.com/brand/737d61085e52d17ec27.html">牛杂冰箱</a>
                <a href="https://www.jd.com/xinghao/737cf5605204fd39733.html">康佳108升冰箱</a>
                <a href="https://www.jd.com/cppf/73795eb5841a4d45096.html">康佳bcd一102s</a>
                <a href="https://www.jd.com/hprm/7374c1e52c92c299244.html">海尔269-wdgb</a>
                <a href="https://www.jd.com/sptopic/737233aa6b3e8634592.html">BOSCH 冰箱</a>
                <a href="https://www.jd.com/hotitem/7373fb21b27f07855b5.html">百安居冰箱</a>
                <a href="https://www.jd.com/nrjs/271ba3c18480be81.html">海尔智能冰箱哪款好？海尔智能冰箱怎么样好用吗？</a>
                <a href="https://www.jd.com/zxnews/0a4175d0080c3523.html">晶弘600冰箱哪款好？晶弘600冰箱怎么样好用吗？</a>
                <a href="https://www.jd.com/phb/zhishi/6f930f8c085ff1b3.html">冰箱门冰箱排行榜，冰箱门冰箱十大排名推荐</a>
                <a href="https://www.jd.com/phb/zhishi/753594fa35fe5b90.html">博世kaf96a46ti排行榜，博世kaf96a46ti十大排名推荐</a>
                <a href="https://www.jd.com/jxinfo/0a07c3d9e866eae4.html">海尔（Haier） . 十字对开门 冰箱</a>
                <a href="https://www.jd.com/jxinfo/99413aaca6ae2b7e.html">卡萨帝（Casarte） BCD-627WDCLU1 对开门 冰箱</a>
            </div>
    <!-- CLUB_LINK end -->
    <script type="text/javascript">
        window.point.fs = new Date().getTime();
    </script>
    <!-- E ad2 -->

</div>

<script src="//storage.360buyimg.com/pc-pre-tmp/jquery.js"></script>
<script src="//misc.360buyimg.com/??mtd/pc/common/js/o2_ua.js,mtd/pc/base/1.0.0/event.js"></script>
<script src="//wl.jd.com/wl.js"></script>

<script>

</script>

<style>

.o2_ie8 .more2_international {

    filter: progid:dximagetransform.microsoft.alphaimageloader(src='//storage.360buyimg.com/mtd/home/more_international1575014601797.png',sizingMethod='scale');

    background: none;

}

.mod_help_cover {

    background-image: none;

}

#settleup:hover .cw-icon {

    border-bottom: 1px solid #c81623;

}

.o2_mini .company .feed-tab {

    margin: 0 auto;

}

.company .feed-tab {

    margin: 0 auto;

}

.channelsB .channels_block_1 .channels_item_1 .channels_item_link {

    height: 370px;

    width: 290px;

}

.channelsB .channels_block_1 .channels_item_2 .channels_item_link {

    height: 370px;

    width: 290px;

}

.JD_close-button--square {

  z-index: 1;

}

</style>
<div id="app"></div>
<script type="text/javascript">
    window.point.dom = new Date().getTime();
</script>

<style type="text/css">
.mod_footer {
  height: 500px;
  background-color: #eaeaea;
}

/* 服务承诺 */
.mod_service {
  padding: 30px 0;
  border-bottom: 1px solid #dedede;
}

.mod_service_list {
  overflow: hidden;
  height: 42px;
}

.mod_service_item {
  float: left;
  width: 297px;
}

.mod_service_unit {
  position: relative;
  margin: 0 auto;
  padding-left: 45px;
  width: 180px;
}

.mod_service_tit {
  overflow: hidden;
  position: absolute;
  left: 0;
  top: 0;
  width: 36px;
  height: 42px;
  text-indent: -999px;
}

.mod_service_txt {
  overflow: hidden;
  width: 100%;
  height: 42px;
  line-height: 42px;
  font-size: 18px;
  font-weight: 700;
  text-overflow: ellipsis;
  white-space: nowrap;
  color: #444;
}

/* 多快好省的图标 */
.mod_service_duo {
  background-repeat: no-repeat;
  background-position: 0 -192px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_service_kuai {
  background-repeat: no-repeat;
  background-position: -41px -192px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_service_hao {
  background-repeat: no-repeat;
  background-position: -82px -192px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_service_sheng {
  background-repeat: no-repeat;
  background-position: -123px -192px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

/* 帮助清单 */
.mod_help {
  padding: 20px 0;
}

.mod_help_list {
  overflow: hidden;
  height: 160px;
}

.mod_help_nav {
  float: left;
  width: 198px;
  line-height: 22px;
}

.mod_help_nav_tit {
  margin-bottom: 5px;
  font-size: 14px;
}

.mod_help_cover {
  background-repeat: no-repeat;
  background-position: 0 0;
  float: right;
  width: 200px;
  height: 150px;
}

.mod_help_cover_tit {
  margin-bottom: 15px;
  font-size: 14px;
  text-align: center;
}

.mod_help_cover_con {
  padding: 0 10px;
}

.mod_help_cover_more {
  text-align: right;
}

/* 版权信息 */
.mod_copyright_inner {
  padding: 15px 0;
  border-top: 1px solid #e1e1e1;
  text-align: center;
}

.mod_copyright_split {
  margin: 0 7px;
  color: #ccc;
}

.mod_copyright_info {
  padding: 10px 0;
  line-height: 22px;
  color: #999;
}

.mod_copyright_info a {
  color: #999;
}

.mod_copyright_info a:hover {
  color: #c81623;
}

.mod_copyright_inter_ico {
  display: inline-block;
  width: 15px;
  height: 10px;
  vertical-align: -1px;
  margin-right: 10px;
  background-repeat: no-repeat;
}

.mod_copyright_inter_ico_global {
  background-repeat: no-repeat;
  background-position: -108px -155px;
  width: 15px;
  height: 12px;
  margin-top: -1px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_copyright_inter_ico_rissia {
  background-repeat: no-repeat;
  background-position: -168px -155px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_copyright_inter_ico_indonesia {
  background-repeat: no-repeat;
  background-position: -148px -155px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_copyright_inter_ico_thailand {
  background-repeat: no-repeat;
  background-position: -108px -172px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_copyright_inter_ico_spain {
  background-repeat: no-repeat;
  background-position: -128px -155px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_copyright_auth {
  margin: 25px 0;
}

.mod_copyright_auth_ico {
  overflow: hidden;
  display: inline-block;
  margin: 0 3px;
  width: 103px;
  height: 32px;
  line-height: 1000px;
}

.mod_copyright_auth_ico_1 {
  background-repeat: no-repeat;
  background-position: -205px -148px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_copyright_auth_ico_2 {
  background-repeat: no-repeat;
  background-position: -205px -111px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_copyright_auth_ico_3 {
  background-repeat: no-repeat;
  background-position: -205px -74px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_copyright_auth_ico_4 {
  background-repeat: no-repeat;
  background-position: -205px -37px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_copyright_auth_ico_5 {
  background-repeat: no-repeat;
  background-position: 0 -66px;
  background-image: url(//img13.360buyimg.com/imagetools/jfs/t1/108497/17/22418/15570/6215e0d0E01387603/81e883d9e15cebb7.png);
}

.mod_copyright_auth_ico_6 {
  background-repeat: no-repeat;
  background-position: 0 -155px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_copyright_auth_ico_7 {
  background-repeat: no-repeat;
  background-position: 0 -99px;
  background-image: url(//img13.360buyimg.com/imagetools/jfs/t1/108497/17/22418/15570/6215e0d0E01387603/81e883d9e15cebb7.png);
}

.mod_copyright_auth_ico_8 {
  width: 70px;
  background-repeat: no-repeat;
  background-position: -104px -99px;
  background-image: url(//img13.360buyimg.com/imagetools/jfs/t1/108497/17/22418/15570/6215e0d0E01387603/81e883d9e15cebb7.png);
}

.mod_copyright_auth_ico_9 {
  width: 88px;
  background-repeat: no-repeat;
  background-position: -104px -131px;
  background-image: url(//img13.360buyimg.com/imagetools/jfs/t1/108497/17/22418/15570/6215e0d0E01387603/81e883d9e15cebb7.png);
}

// .mod_copyright_license {
//   margin-left: 16px;
// }

/* 适配高清屏 */

@media only screen and (-webkit-min-device-pixel-ratio: 1.5),
  only screen and (min--moz-device-pixel-ratio: 1.5),
  only screen and (-o-min-device-pixel-ratio: 3/2),
  only screen and (min-device-pixel-ratio: 1.5) {

  .mod_service_duo {
    background-repeat: no-repeat;
    background-size: 113px 86.5px;
    background-position: 0 0;
    background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211722/38/13035/9322/6215e10cEa9918ac1/7f8686ee76e42123.png);
  }

  .mod_service_kuai {
    background-repeat: no-repeat;
    background-size: 113px 86.5px;
    background-position: -38.5px 0;
    background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211722/38/13035/9322/6215e10cEa9918ac1/7f8686ee76e42123.png);
  }

  .mod_service_hao {
    background-repeat: no-repeat;
    background-size: 113px 86.5px;
    background-position: -77px 0;
    background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211722/38/13035/9322/6215e10cEa9918ac1/7f8686ee76e42123.png);
  }

  .mod_service_sheng {
    background-repeat: no-repeat;
    background-size: 113px 86.5px;
    background-position: 0 -44.5px;
    background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211722/38/13035/9322/6215e10cEa9918ac1/7f8686ee76e42123.png);
  }

  .mod_copyright_inter_ico_global {
    background-repeat: no-repeat;
    background-size: 113px 86.5px;
    background-position: -38.5px -44.5px;
    background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211722/38/13035/9322/6215e10cEa9918ac1/7f8686ee76e42123.png);
  }

  .mod_copyright_inter_ico_rissia {
    background-repeat: no-repeat;
    background-size: 113px 86.5px;
    background-position: -56px -44.5px;
    background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211722/38/13035/9322/6215e10cEa9918ac1/7f8686ee76e42123.png);
  }

  .mod_copyright_inter_ico_indonesia {
    background-repeat: no-repeat;
    background-size: 113px 86.5px;
    background-position: -73.5px -44.5px;
    background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211722/38/13035/9322/6215e10cEa9918ac1/7f8686ee76e42123.png);
  }

  .mod_copyright_inter_ico_thailand {
    background-repeat: no-repeat;
    background-size: 113px 86.5px;
    background-position: -91px -44.5px;
    background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211722/38/13035/9322/6215e10cEa9918ac1/7f8686ee76e42123.png);
  }

  .mod_copyright_inter_ico_spain {
    background-repeat: no-repeat;
    background-size: 113px 86.5px;
    background-position: -38.5px -59px;
    background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211722/38/13035/9322/6215e10cEa9918ac1/7f8686ee76e42123.png);
  }

  .mod_copyright_inter_lk {
    font-family: initial;
  }
}

/* 窄版 */
.o2_mini .mod_service_item {
  width: 247px;
}

.o2_mini .mod_help_nav {
  width: 158px;
}

.o2_mini .mod_copyright_links .mod_copyright_split {
  margin: 0 6px;
}
</style>
<script type="text/javascript">
  function clickReport(){
    $("body").delegate("[poi]", "click", function(e){
        let $current = $(e.target)
        let tagName = $current.prop("tagName")

        if(tagName === 'A' || tagName === 'a'){
          let fullpoi = $current.attr('poi') ? $current.attr('poi') : $current.parents('[poi]').attr('poi')
          let url = $current.attr('href')
          let text = $.trim($current.text())

          window.footerGetOnClick && window.footerGetOnClick(fullpoi, url, text)
        }
    })
  }
  clickReport()
</script>
<div id="J_footer" class="footer">
  <div class="mod_service" clstag="btm|btmnavi_null01" poi="btm|btmnavi|null01">
    <div class="grid_c1 mod_service_inner">
      <ul class="mod_service_list">
        <li class="mod_service_item">
          <div class="mod_service_unit">
            <h5 class="mod_service_tit mod_service_duo">多</h5>
            <p class="mod_service_txt">品类齐全，轻松购物</p>
          </div>
        </li>
        <li class="mod_service_item">
          <div class="mod_service_unit">
            <h5 class="mod_service_tit mod_service_kuai">快</h5>
            <p class="mod_service_txt">多仓直发，极速配送</p>
          </div>
        </li>
        <li class="mod_service_item">
          <div class="mod_service_unit">
            <h5 class="mod_service_tit mod_service_hao">好</h5>
            <p class="mod_service_txt">正品行货，精致服务</p>
          </div>
        </li>
        <li class="mod_service_item">
          <div class="mod_service_unit">
            <h5 class="mod_service_tit mod_service_sheng">省</h5>
            <p class="mod_service_txt">天天低价，畅选无忧</p>
          </div>
        </li>
      </ul>
    </div>
  </div>

  <div class="mod_help" clstag="btm|btmnavi_null02" poi="btm|btmnavi|null02">
    <div class="grid_c1 mod_help_inner">
      <div class="mod_help_list">
        <div class="mod_help_nav">
          <h5 class="mod_help_nav_tit">购物指南</h5>
          <ul class="mod_help_nav_con">
            <li>
              <a href="//help.jd.com/user/issue/list-29.html" target="_blank" rel="noopener noreferrer">
                购物流程
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/list-151.html" target="_blank" rel="noopener noreferrer">
                会员介绍
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/list-297.html" target="_blank" rel="noopener noreferrer">
                生活旅行
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue.html" target="_blank" rel="noopener noreferrer">
                常见问题
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/list-136.html" target="_blank" rel="noopener noreferrer">
                大家电
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/custom.html" target="_blank" rel="noopener noreferrer">
                联系客服
              </a>
            </li>
          </ul>
        </div>
        <div class="mod_help_nav">
          <h5 class="mod_help_nav_tit">配送方式</h5>
          <ul class="mod_help_nav_con">
            <li>
              <a href="//help.jd.com/user/issue/list-81-100.html" target="_blank" rel="noopener noreferrer">
                上门自提
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/list-81.html" target="_blank" rel="noopener noreferrer">
                211限时达
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/103-983.html" target="_blank" rel="noopener noreferrer">
                配送服务查询
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/109-188.html" target="_blank" rel="noopener noreferrer">
                配送费收取标准
              </a>
            </li>
            <li>
              <a href="//help.joybuy.com/help/question-list-201.html" target="_blank" rel="noopener noreferrer">
                海外配送
              </a>
            </li>
          </ul>
        </div>
        <div class="mod_help_nav">
          <h5 class="mod_help_nav_tit">支付方式</h5>
          <ul class="mod_help_nav_con">
            <li>
              <a href="//help.jd.com/user/issue/list-172.html" target="_blank" rel="noopener noreferrer">
                货到付款
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/list-173.html" target="_blank" rel="noopener noreferrer">
                在线支付
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/list-176.html" target="_blank" rel="noopener noreferrer">
                分期付款
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/list-175.html" target="_blank" rel="noopener noreferrer">
                公司转账
              </a>
            </li>
          </ul>
        </div>
        <div class="mod_help_nav">
          <h5 class="mod_help_nav_tit">售后服务</h5>
          <ul class="mod_help_nav_con">
            <li>
              <a href="//help.jd.com/user/issue/list-112.html" target="_blank" rel="noopener noreferrer">
                售后政策
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/list-132.html" target="_blank" rel="noopener noreferrer">
                价格保护
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/130-978.html" target="_blank" rel="noopener noreferrer">
                退款说明
              </a>
            </li>
            <li>
              <a href="//myjd.jd.com/repair/repairs.action" target="_blank" rel="noopener noreferrer">
                返修/退换货
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/list-50.html" target="_blank" rel="noopener noreferrer">
                取消订单
              </a>
            </li>
          </ul>
        </div>
        <div class="mod_help_nav">
          <h5 class="mod_help_nav_tit">特色服务</h5>
          <ul class="mod_help_nav_con">
            <li>
              <a href="//1paipai.jd.com/" target="_blank" rel="noopener noreferrer">
                夺宝岛
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/list-134.html" target="_blank" rel="noopener noreferrer">
                DIY装机
              </a>
            </li>
            <li>
              <a href="//fuwu.jd.com/" target="_blank" rel="noopener noreferrer">
                延保服务
              </a>
            </li>
            <li>
              <a href="//o.jd.com/market/index.action" target="_blank" rel="noopener noreferrer">
                京东E卡
              </a>
            </li>
            <li>
              <a href="//mobile.jd.com/" target="_blank" rel="noopener noreferrer">
                京东通信
              </a>
            </li>
            <li>
              <a href="//smart.jd.com/" target="_blank" rel="noopener noreferrer">
                京鱼座智能
              </a>
            </li>
          </ul>
        </div>
        <div class="mod_help_cover">
          <h5 class="mod_help_cover_tit">京东自营覆盖区县</h5>
          <div class="mod_help_cover_con">
            <p class="mod_help_cover_info">
              京东已向全国2661个区县提供自营配送服务，支持货到付款、POS机刷卡和售后上门服务。
            </p>
            <p class="mod_help_cover_more">
              <a href="//help.jd.com/user/issue/103-983.html" target="_blank" rel="noopener noreferrer">
                查看详情
                <i class="iconfont">&#xe60d;</i>
              </a>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="mod_copyright">
    <div class="grid_c1 mod_copyright_inner">
      <p
        class="mod_copyright_links"
        clstag="btm|btmnavi_null03"
        poi="btm|btmnavi|null03"
      >
        <a href="//about.jd.com" target="_blank" rel="noopener noreferrer">关于我们</a>
        <span class="mod_copyright_split">|</span>
        <a href="//about.jd.com/contact" target="_blank" rel="noopener noreferrer">联系我们</a>
        <span class="mod_copyright_split">|</span>
        <a href="//help.jd.com/user/custom.html" target="_blank" rel="noopener noreferrer">联系客服</a>
        <span class="mod_copyright_split">|</span>
        <a href="//lai.jd.com" target="_blank" rel="noopener noreferrer">合作招商</a>
        <span class="mod_copyright_split">|</span>
        <a href="//helpcenter.jd.com/venderportal/frist.html" target="_blank" rel="noopener noreferrer">商家帮助</a>
        <span class="mod_copyright_split">|</span>
        <a href="//jzt.jd.com" target="_blank" rel="noopener noreferrer">营销中心</a>
        <span class="mod_copyright_split">|</span>
        <a href="//app.jd.com/" target="_blank" rel="noopener noreferrer">手机京东</a>
        <span class="mod_copyright_split">|</span>
        <a href="//club.jd.com/links.aspx" target="_blank" rel="noopener noreferrer">友情链接</a>
        <span class="mod_copyright_split">|</span>
        <a href="//union.jd.com/index" target="_blank" rel="noopener noreferrer">销售联盟</a>
        <span class="mod_copyright_split">|</span>
        <a href="//pro.jd.com/mall/active/3WA2zN8wkwc9fL9TxAJXHh5Nj79u/frist.html" target="_blank" rel="noopener noreferrer">京东社区</a>
        <span class="mod_copyright_split">|</span>
        <a href="//pro.jd.com/mall/active/3TF25tMdrnURET8Ez1cW9hzfg3Jt/frist.html" target="_blank" rel="noopener noreferrer">风险监测</a>
        <span class="mod_copyright_split">|</span>
        <a href="//about.jd.com/privacy/" target="_blank" rel="noopener noreferrer">隐私政策</a>
        <span class="mod_copyright_split">|</span>
        <a href="//gongyi.jd.com" target="_blank" rel="noopener noreferrer">京东公益</a>
        <span class="mod_copyright_split">|</span>
        <a href="//www.joybuy.com/" target="_blank" rel="noopener noreferrer">English Site</a>
        <span class="mod_copyright_split">|</span>
        <a href="//corporate.jd.com" target="_blank" rel="noopener noreferrer">Media & IR</a>
      </p>


      <div class="mod_copyright_info">
        <div
          class="mod_copyright_cert"
          clstag="btm|btmnavi_null04"
          poi="btm|btmnavi|null04"
        >
          <p>
            <a
              href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11000002000088"
              target="_blank"
              rel="noopener noreferrer"
            >
              京公网安备 11000002000088号
            </a>
            <span class="mod_copyright_split">|</span>
            <a href="http://beian.miit.gov.cn" target="_blank" rel="noopener noreferrer">
              京ICP备11041704号
            </a>
            <span class="mod_copyright_split">|</span>
            <a
              href="//h5.m.jd.com/pc/dev/3T3No18XR8k8rpLGLGhgbJ1StAFq/frist.html"
              target="_blank"
              rel="noopener noreferrer"
            >
              ICP
            </a>
            <span class="mod_copyright_split">|</span>
            <a href="//jdwp.jd.com/544-2927.html" target="_blank" rel="noopener noreferrer">
              互联网药品信息服务资格证编号(京)-经营性-2014-0008
            </a>
            <span class="mod_copyright_split">|</span>
            <span>新出发京零&nbsp;字第大120007号</span>
          </p>
          <p>
            <span>互联网出版许可证编号新出网证(京)字150号</span>
            <span class="mod_copyright_split">|</span>
            <a
              href="//pro.jd.com/mall/active/3bVDLXHdwVmdQksGF8TtS7ocq1NY/frist.html"
              target="_blank"
              rel="noopener noreferrer"
            >
              出版物经营许可证
            </a>
            <span class="mod_copyright_split">|</span>
            <a
              href="//img10.360buyimg.com/ling/jfs/t1/164806/19/5070/567736/6017d6d6Eab06ec9c/d8ca6e029f495447.jpg"
              target="_blank"
              rel="noopener noreferrer"
            >
              网络文化经营许可证京网文[2020]6112-1201号
            </a>
            <span class="mod_copyright_split">|</span>
            <span>违法和不良信息举报电话：4006561155</span>
          </p>
          <p>
            <span class="copyright_txt"></span>
            <span class="mod_copyright_split">|</span>
            <span>消费者维权热线：4006067733</span>
            <span class="mod_copyright_split">|</span>
            <a
              href="//pro.jd.com/mall/active/38PitHBfR7ZopNHRSHnuuWR5AMDL/frist.html"
              target="_blank"
              rel="noopener noreferrer"
              class="mod_copyright_license"
            >
              经营证照
            </a>
            <span class="mod_copyright_split">|</span>
            <span>(京)网械平台备字(2018)第00003号</span>
            <span class="mod_copyright_split">|</span>
            <a
              href="//h5.m.jd.com/babelDiy/Zeus/ARcYnJ8coUdUecn6UQAN6TDaVmH/frist.html"
              target="_blank"
              rel="noopener noreferrer"
              class="mod_business_license"
            >
              营业执照
            </a>
            <span class="mod_copyright_split">|</span>
            <a
              href="//img11.360buyimg.com/imagetools/jfs/t1/148412/19/20641/1513871/6204e24aEd9434d24/b11d1cd7d1d36976.png"
              target="_blank"
              rel="noopener noreferrer"
              class="mod_business_license"
            >
              增值电信业务经营许可证
            </a>
          </p>
        </div>

        <div class="mod_copyright_inter">
          <p>
            <a
              class="mod_copyright_inter_lk"
              href="//www.joybuy.com/?source=1&visitor_from=3"
              target="_blank"
              rel="noopener noreferrer"
              clstag="btm|btmnavi_null0501"
              poi="btm|btmnavi|null0501"
            >
              <i class="mod_copyright_inter_ico mod_copyright_inter_ico_global"></i>
              Global Site
            </a>
            <span class="mod_copyright_split">|</span>
            <a
              class="mod_copyright_inter_lk"
              href="//www.jd.ru/?source=1&visitor_from=3"
              target="_blank"
              rel="noopener noreferrer"
              clstag="btm|btmnavi_null0502"
              poi="btm|btmnavi|null0502"
            >
              <i class="mod_copyright_inter_ico mod_copyright_inter_ico_rissia"></i>
              Сайт России
            </a>
            <span class="mod_copyright_split">|</span>
            <a
              class="mod_copyright_inter_lk"
              href="//www.jd.id/?source=1&visitor_from=3"
              target="_blank"
              rel="noopener noreferrer"
              clstag="btm|btmnavi_null0503"
              poi="btm|btmnavi|null0503"
            >
              <i class="mod_copyright_inter_ico mod_copyright_inter_ico_indonesia"></i>
              Situs Indonesia
            </a>
            <span class="mod_copyright_split">|</span>
            <a
              class="mod_copyright_inter_lk"
              href="//www.joybuy.es/?source=1&visitor_from=3"
              target="_blank"
              rel="noopener noreferrer"
              clstag="btm|btmnavi_null0504"
              poi="btm|btmnavi|null0504"
            >
              <i class="mod_copyright_inter_ico mod_copyright_inter_ico_spain"></i>
              Sitio de España
            </a>
            <span class="mod_copyright_split">|</span>
            <a
              class="mod_copyright_inter_lk"
              href="//www.jd.co.th/?source=1&visitor_from=3"
              target="_blank"
              rel="noopener noreferrer"
              clstag="btm|btmnavi_null0505"
              poi="btm|btmnavi|null0505"
            >
              <i class="mod_copyright_inter_ico mod_copyright_inter_ico_thailand"></i>
              เว็บไซต์ประเทศไทย
            </a>
          </p>
        </div>

        <div
          class="mod_copyright_subsites"
          clstag="btm|btmnavi_null06"
          poi="btm|btmnavi|null06"
        >
          <p>
            <span>京东旗下网站：</span>
            <a href="https://www.jdpay.com/" target="_blank" rel="noopener noreferrer">
              京东钱包
            </a>
            <span class="mod_copyright_split">|</span>
            <a href="http://www.jdcloud.com" target="_blank" rel="noopener noreferrer">
              京东云
            </a>
            <span class="mod_copyright_split">|</span>
            <span>网络内容从业人员违法违规行为举报电话：4006561155-3</span>
          </p>
        </div>
      </div>

      <p
        class="mod_copyright_auth"
        clstag="btm|btmnavi_null07"
        poi="btm|btmnavi|null07"
      >
        <a
          class="mod_copyright_auth_ico mod_copyright_auth_ico_2"
          href="https://ss.knet.cn/verifyseal.dll?sn=2008070300100000031&ampct=df&amppa=294005"
          target="_blank"
          rel="noopener noreferrer"
        >
          可信网站信用评估
        </a>
        <a
          class="mod_copyright_auth_ico mod_copyright_auth_ico_3"
          href="http://www.cyberpolice.cn"
          target="_blank"
          rel="noopener noreferrer"
        >
          网络警察提醒你
        </a>
        <a
          class="mod_copyright_auth_ico mod_copyright_auth_ico_4"
          href="https://search.szfw.org/cert/l/CX20120111001803001836"
          target="_blank"
          rel="noopener noreferrer"
        >
          诚信网站
        </a>
        <a
          class="mod_copyright_auth_ico mod_copyright_auth_ico_5"
          href="http://www.12377.cn/"
          target="_blank"
          rel="noopener noreferrer"
        >
          中国互联网举报中心
        </a>
        <a
          class="mod_copyright_auth_ico mod_copyright_auth_ico_6"
          href="http://www.12377.cn/node_548446.htm"
          target="_blank"
          rel="noopener noreferrer"
        >
          网络举报APP下载
        </a>
        <a
          class="mod_copyright_auth_ico mod_copyright_auth_ico_7"
          href="http://www.shdf.gov.cn/shdf/channels/740.html"
          target="_blank"
          rel="noopener noreferrer"
        >
          扫黄打非网举报专区
        </a>
        <a
          class="mod_copyright_auth_ico mod_copyright_auth_ico_8"
          href="javascript:;"
          target="_self"
          rel="noopener noreferrer"
        >
          适老化无障碍服务
        </a>
        <a
          class="mod_copyright_auth_ico mod_copyright_auth_ico_9"
          href="http://ggfw.cnipa.gov.cn:8010/PatentCMS_Center?fromsite=www.jd.com"
          target="_blank"
          rel="noopener noreferrer"
        >
          国家知识产权公共服务网
        </a>
      </p>
    </div>
  </div>
</div>

<script type="text/javascript">
function footerRender (){
  function getClstagPrefix(){
      var $clstagEles = $('[clstag]');
      $clstagEles.each(function(){
          var fullpoi = $(this).attr('clstag')
          $(this).attr('clstag', pageConfig.clstagPrefix+fullpoi)
      });
  }

  function getCopyrightTxt(){
    var $copyrightEles = $('.copyright_txt');
    $copyrightEles.html("Copyright&nbsp;©&nbsp;2004&nbsp;-&nbsp;"+ new Date().getFullYear() + "&nbsp;&nbsp;京东JD.com&nbsp;版权所有")
  }

  getClstagPrefix()
  getCopyrightTxt()
}

footerRender()
</script>

</body>


<script type="text/javascript" src="//misc.360buyimg.com/mtd/pc/index_2019/1.0.0/static/js/runtime.js"></script>

<script type="text/javascript" src="//misc.360buyimg.com/mtd/pc/index_2019/1.0.0/static/js/index.chunk.js"></script>

<script type="text/javascript">
    window.point.js = new Date().getTime();
</script>
<script defer="defer" async type="text/javascript" src="//static.360buyimg.com/item/assets/oldman/wza1/aria.js?appid=bfeaebea192374ec1f220455f8d5f952"></script>
</html>
': failed to load external entity "<!DOCTYPE html>
<html>

<head>
    <meta charset="utf8" version='1'/>
    <title>京东(JD.COM)-正品低价、品质
>>> 
=================== RESTART: C:/Users/HP/Desktop/autoxpath.py ==================

Traceback (most recent call last):
  File "C:/Users/HP/Desktop/autoxpath.py", line 6, in <module>
    tree = etree.parse(r.text,etree.HTMLParser())
  File "src\lxml\etree.pyx", line 3521, in lxml.etree.parse
  File "src\lxml\parser.pxi", line 1859, in lxml.etree._parseDocument
  File "src\lxml\parser.pxi", line 1885, in lxml.etree._parseDocumentFromURL
  File "src\lxml\parser.pxi", line 1789, in lxml.etree._parseDocFromFile
  File "src\lxml\parser.pxi", line 1177, in lxml.etree._BaseParser._parseDocFromFile
  File "src\lxml\parser.pxi", line 615, in lxml.etree._ParserContext._handleParseResultDoc
  File "src\lxml\parser.pxi", line 725, in lxml.etree._handleParseResult
  File "src\lxml\parser.pxi", line 652, in lxml.etree._raiseParseError
OSError: Error reading file '<!DOCTYPE html>
<html>

<head>
    <meta charset="utf8" version='1'/>
    <title>京东(JD.COM)-正品低价、品质保障、配送及时、轻松购物！</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=yes"/>
    <meta name="description"
          content="京东JD.COM-专业的综合网上购物商城，为您提供正品低价的购物选择、优质便捷的服务体验。商品来自全球数十万品牌商家，囊括家电、手机、电脑、服装、居家、母婴、美妆、个护、食品、生鲜等丰富品类，满足各种购物需求。"/>
    <meta name="Keywords" content="网上购物,网上商城,家电,手机,电脑,服装,居家,母婴,美妆,个护,食品,生鲜,京东"/>
    <script type="text/javascript">
        window.point = {}
        window.point.start = new Date().getTime()
    </script>
    <link rel="dns-prefetch" href="//static.360buyimg.com"/>
    <link rel="dns-prefetch" href="//misc.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img10.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img11.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img12.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img13.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img14.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img20.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img30.360buyimg.com"/>
    <link rel="dns-prefetch" href="//d.3.cn"/>
    <link rel="dns-prefetch" href="//d.jd.com"/>
    <link rel="icon" href="//www.jd.com/favicon.ico" mce_href="//www.jd.com/favicon.ico" type="image/x-icon"/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>
    <meta name="renderer" content="webkit"/>

    <!--[if lte IE 6]>
    <script src="//misc.360buyimg.com/mtd/pc/index/home/ie6tip.min.js"></script>
    <![endif]-->
    <!--[if IE 8]>
    <script src="//misc.360buyimg.com/mtd/pc/index_2019/1.0.0/static/lib/polyfill/index.js"></script>
    <![endif]-->

    <link href="//misc.360buyimg.com/mtd/pc/index_2019/1.0.0/static/css/first-screen.chunk.css" rel="stylesheet"/>

    <link href="//misc.360buyimg.com/mtd/pc/index_2019/1.0.0/static/css/index.chunk.css" rel="stylesheet"/>
    <script type="text/javascript">
        window.point.css = new Date().getTime()
    </script>
    <script type="text/javascript">
        window.pageConfig = {};
		//灰度区间统一配置
		window.pageConfig.hashList ={"research":[{"start":"0","end":"10000"},{"start":"10000","end":"10000"}],"navitems":[{"start":"0","end":"0"},{"start":"0","end":"10000"}],"treasure":[{"start":"0","end":"10000"},{"start":"10000","end":"10000"}],"floor":[{"start":"0","end":"10000"},{"start":"10000","end":"10000"}],"schoolFloor":[{"start":"0","end":"10000"},{"start":"10000","end":"10000"}],"top":[{"start":"0","end":"10000"},{"start":"10000","end":"10000"}],"recommend":[{"start":"0","end":"10000"},{"start":"10000","end":"10000"}],"channels":[{"start":"0","end":"10000"},{"start":"10000","end":"10000"}]};

        // 大促配置
        window.promotional = {};
        window.promotional.enableShowToolbar = false;

        window.pageConfig.enableShowSpecialTop = false;

        window.promotional.enableShowTop = false;

        window.promotional.actTimeStart = new Date('2022/05/23 14:00:00').getTime();

		window.promotional.actTimeEnd = new Date('2022/06/20 23:59:59').getTime();

		        window.promotional.atmosphere = {};

		window.promotional.atmosphere.background = 'jfs/t1/175008/40/24062/2774/62871bf5E90bce82e/ce484c2ce3c9c8da.png';

		window.promotional.atmosphere.desc = 'jfs/t1/184633/20/25322/3751/6287380eE54718a8e/288c72d11132fb3d.png';

		window.promotional.newEnjoyType = 'S2';

        // 兜底数据
        window.backup = {};
        //logo
         window.pageConfig.logo = {};

        //直通车
        window.pageConfig.treasure = {};

        window.pageConfig.treasureb = {};

        //企业定投直通车
        window.pageConfig.treasureEnterprise  = {};

        //背板
        window.pageConfig.background = {};

        window.pageConfig.shortcutCompanyConfigType="default";
window.pageConfig.headServiceType="default";
window.pageConfig.headSiteNavType="default";
window.pageConfig.headShiLaoHua="true";
window.pageConfig.enableGraySwitch="false";
window.pageConfig.cateType="default";
window.pageConfig.enableJquerySwitch="true";
window.pageConfig.enableFooterConfigSwitch="true";
        //企业背板
        window.pageConfig.backgroundEnterprise = {"bothBgPic":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/109040\/35\/30908\/41245\/62e727caE16216303\/25329f665ad10e38.jpg","href":"https:\/\/pro.jd.com\/mall\/active\/3y1FpcGL5htF5QLw7ShgEZkKV9WQ\/frist.html"};

        // 页面配置
        window.pageConfig.enableActMark = false;

		window.pageConfig.clstagPrefix = 'h|keycount|';

		window.pageConfig.O2_REPORT = 100;

		window.pageConfig.serverTime = new Date('2022/08/01 16:30:02').getTime();

		window.pageConfig.actStart = new Date('2019/10/18 00:00:00').getTime();

		window.pageConfig.actEnd = new Date('2019/11/15 23:59:59').getTime();

        // 手机京东
        window.pageConfig.shortcutMobileData=[{"title":"\u624b\u673a\u4eac\u4e1c","desc":"\u65b0\u4eba\u4e13\u4eab\u5927\u793c\u5305","img":"jfs\/t1\/67481\/15\/565\/28110\/5cec9234E71c47244\/dc4cf353fd96922e.png","url":"","devices":[{"type":"iphone","src":"https:\/\/itunes.apple.com\/cn\/app\/id414245413"},{"type":"android","src":"https:\/\/storage.jd.com\/jdmobile\/JDMALL-PC2.apk"},{"type":"ipad","src":"https:\/\/itunes.apple.com\/cn\/app\/jing-dong-hd\/id434374726"}]},{"title":"\u5173\u6ce8\u4eac\u4e1cJD.COM","desc":"\u62a25\u5143\u7ea2\u5305","img":"jfs\/t1\/133427\/32\/6189\/44062\/5f2a5467Efff804d1\/7cbc252ed5993190.png","url":"","devices":[]},{"title":"\u4eac\u4e1c\u91d1\u878d\u5ba2\u6237\u7aef","desc":"\u65b0\u4eba\u4e13\u4eab\u5927\u793c\u5305","img":"jfs\/t1\/36947\/5\/10895\/15408\/5cec924bE6c038530\/5cf21582b416c186.jpg","url":"https:\/\/m.jr.jd.com\/integrate\/download\/html\/pc.html","devices":[{"type":"iphone","src":"https:\/\/itunes.apple.com\/cn\/app\/jing-dong-jin-rong-hui-li\/id895682747?mt=8"},{"type":"android","src":"http:\/\/211.151.9.66\/downapp\/jrapp_jr188.apk"}]},{"title":"\u4eac\u4e1c\u5065\u5eb7\u5ba2\u6237\u7aef","desc":"","img":"jfs\/t1\/93019\/8\/17752\/28300\/5e8c23b8E4c6c7c13\/9c45c518ad785873.png","url":"","devices":[{"type":"iphone","src":"https:\/\/hlc.m.jd.com\/download\/?downloadSource=jdh_JDcom"},{"type":"android","src":"https:\/\/hlc.m.jd.com\/download\/?downloadSource=jdh_JDcom"}]},{"title":"\u5173\u6ce8\u4eac\u4e1c\u5c0f\u7a0b\u5e8f","desc":"\u65b0\u4eba0.1\u5143\u8d2d","img":"jfs\/t1\/170279\/40\/10824\/19657\/6045bf7dE610d6258\/3e925badd90757a3.jpg","url":"","devices":[]}];

        //今日推荐
        window.backup.today=[{"alt":"\u4f01\u4e1a\u5f00\u5de5\u5b63","ext_columns":{"biclk":"1#a889a3b4cf7bd9198608242923b049cfdec968df-103-619066#43494363","focustype":"s","ap":"K7+n7uMbemcyifAhDdq5Ig==","mcinfo":"03652902-17044221-8101610722-M#0-2-1--59--#1-tb-#102-43494363#pc-home","url":"https:\/\/pro.jd.com\/mall\/active\/33FkET36YNBaCuLwF3GqnCbLr4uT\/frist.html?babelChannel=ttt2","desc":"\u7cbe\u9009\u7206\u6b3e","text":"\u4f01\u4e1a\u5f00\u5de5\u5b63"},"src":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/6851\/13\/21644\/93283\/61f50444Eebe6975f\/03dee49c7825b83d.png","gid":"03652902","href":"https:\/\/pro.jd.com\/mall\/active\/33FkET36YNBaCuLwF3GqnCbLr4uT\/frist.html?babelChannel=ttt2","srcB":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/6851\/13\/21644\/93283\/61f50444Eebe6975f\/03dee49c7825b83d.png","type":"material"},{"alt":"","ext_columns":{"biclk":"1#a889a3b4cf7bd9198608242923b049cfdec968df-103-619066#43494363","focustype":"s","ap":"p7XPj53+XCTIQN3wwN6XDg==","mcinfo":"03652902-17044221-8101611040-M#0-2-1--59--#1-tb-#102-43494363#pc-home","url":"https:\/\/pro.jd.com\/mall\/active\/DMQAamMysqjZ7ZDWHFTBc6ocHAv\/frist.html","desc":"","text":""},"src":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/116864\/1\/21079\/53025\/61ff9962E196a5844\/c1b0bcc5845ad614.jpg","gid":"03652902","href":"https:\/\/pro.jd.com\/mall\/active\/DMQAamMysqjZ7ZDWHFTBc6ocHAv\/frist.html","srcB":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/116864\/1\/21079\/53025\/61ff9962E196a5844\/c1b0bcc5845ad614.jpg","type":"material"},{"ext_columns":{"focustype":"g"},"type":"ad","href":"https:\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9scHMuamQuY29tL3BjL3BzcC81MDE3MDExP2ltdXA9Q2g0S0dPVzV2LVczbnVTN2dlUzRtdVNfb2VhQnItZW5rZWFLZ0JJQUdBQVNHZ2l6bTdJQ0VQT2E2OXdER2dodWEzbDRlWEY0Y3lEQUJpZ0JHTm9oSUFBcUlHbGlMSFZoTEhoblpTeG5hV0VzWTJsbUxHWmZZbUZmWm14ZmJERTJNek00TWdKcFlrcW5BVWw4VTBoVlRsUmZTVUlzU1Y5QlgwWk1YMElzU1Y5QlgxSkZYMElzU1Y5QlgxQk1YMElzU1Y5QlgxTk1YMElzU1Y5QlgwTlRYMElzU1Y5QlgxSlRYMElzU1Y5VlgwWk1YMElzU1Y5VFgwWk1YMElzU1Y5U1gwWk1YMElzU1Y5UVgwWk1YMElzU1Y5SFgxSk1YMElzU1Y5SFgxaEhYMUlzU1Y5Q1gwWk1YMUlzUjBsQkxGaEhSU3hWUVh3N1JueE5TVmhVUVVkZlJsSXNSbDlDUVY5R1RGOU1NVFl6TXpoOA&log=GAzYUXYleBiYx0yi3tCBS_1z9BscamtkMEa4naoSoI8F4fSENdrxcaC38YMbZREFpsXjXNB4_Ypm53RtKSHBrazQvD1ci4f4r3NxR-yU37iCyPP0Nx3Ksdo9hVXBwTt3HNCuZKimPzdqV8DuXlDgrFWcxkJOjuSYNOSTOKruMd5nib6Ke85jPV59_TNBOxLuz40xpc0K52c5pb2BW-CidRAwuvEJ2UV2pu2ACc5TnQYOoIFfvqnq_pjIGT5OzW1vmGodybyGxpjZPg5LOzlzGCmErNpxLG8KmmtZuAHBwJv5a6hRyJMefh3cM2PX42YYmRUhyd1ZWU3KNsK4cmpbU1tiwiDP09sYWdIH1PwB6Xc4YYmcK-kfjde6dbUWd03FaALzdP9hAl1Mlx8Kpt3WxbXQSV6bYzerVLLN7Yxsp7V--fI1C5uABMVtDvu0dVwlkn514XsVQ-PoyMoyTYItSW4k_7U7MrhCBHtupFLJo6EDu1ZZ0r5CUAQ4jUaeQKpwflnnm2IvkrMdtXbxQEmcro5wxUC1XBhINeohtirkRbGkoyIsQ_2tx-EcXDmU7VWrN76AjLom69JO5Dg6bn1Nln7UWlXCXVjkUPnw6VasWvMVFLomIju6G2gv9pJ-6LbxbmwZQQqzSOHa2LENDMNoiw3UcfWYInAXwkzkyyjMV6AOgeUhU_tvmcjpEwiY9a_0KqHNs5Iq2wzhfbwezNb7mEjMJj3tSASBdppSEShPAn2-t9aBir0DnNhKXZNc2Q3-36CF8Lm0n7w34cs61JbOZTY5NkTeTgJ7YHVUMyH_6Srjt7Yu45-S8_bZrM8Bvu59zI8SfGdwY9lOqh6xtVov3aNHrKsb_1t8E0B1qQcJqU7uxoLs8xe8rQbso2IZ_zoomIHHLUBw_jh09gmx_QfALz0KFHgMWW2Y7PUhz-zc9BDl79oyrvk9UWrxdFX9M5hN-QLGcnpTw9U8LpxLP8zWO1NwaoJBvVx1DT4oKx65OQznXSWxxrAyK3lhHjbpUKByLwsS-x94Pj4G6Vh-_D_x-sH_wRLNOgrz11q2hygreZYQaAFP-EdREzDYm5impKFX1zbwTQ1jMLYvsx5a96hOHCRh-pnpPDuJ4H3bFLyPJLnW-B-hsPwNC7zOd4SWlw90&v=404","src":"https:\/\/img1.360buyimg.com\/da\/jfs\/t1\/104009\/20\/18514\/63913\/5e94f1a7Ef66e61f6\/5c41baf664c71c25.png","clog":"https:\/\/im-x.jd.com\/dsp\/np?log=GAzYUXYleBiYx0yi3tCBS_1z9BscamtkMEa4naoSoI8F4fSENdrxcaC38YMbZREFpsXjXNB4_Ypm53RtKSHBrazQvD1ci4f4r3NxR-yU37iCyPP0Nx3Ksdo9hVXBwTt3HNCuZKimPzdqV8DuXlDgrFWcxkJOjuSYNOSTOKruMd5nib6Ke85jPV59_TNBOxLuz40xpc0K52c5pb2BW-CidRAwuvEJ2UV2pu2ACc5TnQYOoIFfvqnq_pjIGT5OzW1vm9wMFMUIdcSqGleQ7DBERpB23DfOdDkfBgrEcyPckgwSOGz6_ea1d3RhiQ0RfaT8i9FfpupZbQSJUJ9Ka-ZQ2JXZbXkKX5LpsFFDBo1MkUcGWMD5MmFmX4YNfWTVijMbXuF6rsUKQept-5qNj1h0EXrt_nLI9-8-yGsh0kOlHbtDPhBImL0D2ATTMocFmNNClp8Ku3y9wAn9b4KEzzGYXr4YxPjmkCP4B4XxXXmxAOba0eudmGHtheAO6ZaHNj9IB9zzoSvFYPCMdVnRI5MiH9PIFalXjQpicQAkHCWzlfutKJYMTUf0EFYwrYr-WKcIWI8fCQ-d7ypUPe-zrC5iTXcF-1uFtusPEFkmLHMQ6YO5XXy6NSO465S11eVyVDf3nsRYE60H9kgrysqWPSW6g50BMlDBQFD2QyDsyXVw-OTWNd6p5QpdLa6nut_x-MaQwmHbMmwajW3cBTIBFRSCZg3i88J0ECjnmNcf-B30FGEGvPGIfyIDzaenYvdaA1DpHsOobR1faNHgJURHZP0Y52sqa0OfdnDpD5D4B0s96YbRfOCCh_UIsEGLtgcT2ohcmLjhJRGhTIDN-GjgFZfURlusSJ-aCA6e_POrD80CCOAkiXeBxZpZV_dgu3P5uEC9JdenLqNEbXcrZnmQCacb9iCg7cCdjDNzN0m57lah9sffuP9uRdA5YOjvQ7e3F-tiihHvIxWVJV5f4LYXHcSq0A8newQoDu59EgWnjC218SmjhtnqPQNMk_Z6vxh3ZuDIM_UhVVwY_YyfNlTCuxQgf4ACHT4j37Frwt8-tLHkwYS0gj6ixux5dEg_0DCIttDOtzrEIAJZgLluCwBxfmc-64AHTHO7IIxC-ic3cG8LiTqVpx239kby0Q6-B-ZLl_kY&v=404&seq=1"},{"ext_columns":{"focustype":"g"},"type":"ad","href":"https:\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9scHMuamQuY29tL3BjL3BzcC85ODQyMjI_aW11cD1DaDRLR09XNXYtVzNudVM3Z2VTNG11U19vZWFCci1lbmtlYUtnQklBR0FBU0ZRaWVpVHdRcE1EcjNBTWFCSGhuWkhvZ3N3VW9BUmphSVNBQUtpQnBZaXgxWVN4NFoyVXNaMmxoTEdOcFppeG1YMkpoWDJac1gyd3hOak16T0RJQ2FXSktwd0ZKZkZOSVZVNVVYMGxDTEVsZlFWOUdURjlDTEVsZlFWOVNSVjlDTEVsZlFWOVFURjlDTEVsZlFWOVRURjlDTEVsZlFWOURVMTlDTEVsZlFWOVNVMTlDTEVsZlZWOUdURjlDTEVsZlUxOUdURjlDTEVsZlVsOUdURjlDTEVsZlVGOUdURjlDTEVsZlIxOVNURjlDTEVsZlIxOVlSMTlTTEVsZlFsOUdURjlTTEVkSlFTeFlSMFVzVlVGOE8wWjhUVWxZVkVGSFgwWlNMRVpmUWtGZlJreGZUREUyTXpNNGZB&log=GAzYUXYleBiYx0yi3tCBS_1z9BscamtkMEa4naoSoI-CJarMJhq6_agQ762Wvx24jWEpt2TB8lW0fsIYlP4Fe-seuZoGZlp6l8wgBEGBCrnpg3X_k-a_n-DwR0gszKeuhP2dFWx5X1KFBBnt2O_11cwDJ8_olKV3TM1s9e43ULmOHGBMHBCwE141418YwuCuujf2Be2NohSbNu1LI8p2y_tLKno3b2dW2MjLtvcLN7vItTry-ohHHcwC7H32MnTQ0WSiuw91rbCrNqpzSl8XWQEqTyusHQDJvQpxzel7FBUwg1nvs5o4wdkl_zLEfRGXmuAv9fXxmsBHvq8SMDZ-XhllnkemJnRwLf0GFTHuQz13m-YRl_Q7Z4TSNxX80LBbr79MC7fbkpFrOWqV3imz0bNkmyZXRvyNUxzK1ZEczJqOH4Y-DZDOsDH8HC_xaYD9zBYZqyMb0HkTLz2E2zMVUECw0sQam5QJ7Fl1Sk3W_G2ZtA3-3D2_HUQm2MBO6pTNknOgp38W3Pk3qzM3Ilvc2sOBaPAcUlCg_12fCdUIs6YTKSMvsKbmQOQUvGMDNX1acDc1m-RYyed9Ws1A_4UljrZCWXXR3awKfg7_1A5RA5OxKusLaF8uAzGBW4GLVyVPp6bzOcGX38F7-pebU6syqF9XTkoTd8S4-oTepaNYwLo89BY1S5y3TwYkDpZPImNJa-XJEEkDI9Ok3iPG0OysFE8rcCoGxGdVQRXIroxef0FbrbbekRb8CfGJUqt8c_4zFIsiESHn5PAqhCpzWsbtCTn-2mCiXskQ9FW_N4T41wR8QU8nqRWbUFlErK5TCjEf_0qZvxrl9BAr_Yc8cLM6Mt--rPpdB9zJ7NprZHwFebNDBGP6dmDpLvSelXhNnUS69xIsA7mJlE_8UcRSLsQlcAoaT9yOmrzoeHwbGwcu7vqTzPq_gaTyzOlXxpiefflWsF5dcxUguhmP9ZmLnwks9jTJVYikn8LTrM-lSAWNb3YuvwyKPI8T1ZJCQWtt0Bg-o4IDoNXiBknLwOhuamnmcfUtt0wpsBSZYyqGv-Nct-Kd2lCuo5IiFh0XXHJV9PVb59EkFL_tcuLaJOIHbuDYBIHpgem8qWqJii2Dl8GoAeg&v=404","src":"https:\/\/img1.360buyimg.com\/da\/jfs\/t1\/65519\/18\/5109\/86986\/5d349331E52fea75f\/5671237d9584131b.png","clog":"https:\/\/im-x.jd.com\/dsp\/np?log=GAzYUXYleBiYx0yi3tCBS_1z9BscamtkMEa4naoSoI-CJarMJhq6_agQ762Wvx24jWEpt2TB8lW0fsIYlP4Fe-seuZoGZlp6l8wgBEGBCrnpg3X_k-a_n-DwR0gszKeuhP2dFWx5X1KFBBnt2O_11cwDJ8_olKV3TM1s9e43ULmOHGBMHBCwE141418YwuCuujf2Be2NohSbNu1LI8p2y_tLKno3b2dW2MjLtvcLN7vItTry-ohHHcwC7H32MnTQbuspoohbCGR5W77K4uX6JU3jKd0rINTxk70lAYmurUFNjb-BvvKvwQjsqHj2iXRVq6LJheU-nCPwUNkRSz7dGGxuyZoTfik4p_r2otcpi-JHG9MhAzFFjThvONi28IfKBCYqM__5Y8KM9FizlxdZrIN7JW_DhewNPz_41pameKPfrFd0FnfsZcy-vvyZCrTvb-4P_TkUt-mnjMVDNx5OJ8DUlUtPv2oA3YNgvzeuo95j8Ql12y7mFXxsg-SilVJMo_s67ZXnW9J9vL88hoSmnPp7Gq1oIVEDzhYY_2SfSEIVp-mE44HPidftXOjI9_KNQc0rTtuOny0-EvG_w4uR45t18GlSvvMDsemVK1_DtnLJ4mh0X7-MCQCGsOUWxMxGLl_-k1lf2K7DMTL6w3RpMf3rSAXRXFXUPPt6D4-Q1pXL4iJ1vU8BYkCOrrnrG5lgy9tA1Ev60tS-1l9M0UI6AEHN415TUVu-V0ZHwSoYbKdYPEoQm6vCNePdJXquM5QHgd_ohcIF97vuTdBX1OZKG1hRhv5Euysm_iK4y9c8AdecjndizrcyS1ix6Qs3lfIEL2uZiy6f9Pye8lwXnnAKy_5Ngc-p8XysQGG6ZzcBftY-E5sw6al9c_5JxJsIgrSza8qVlawtwzjg1Yk4ezNX73xnR7Btd6KpOlIQ8eSTgiPjRelco3rGJlXgU18JAYQPT6Hbhpzp6SWDvyBCjOflyBOgVU2uCRTclhBX2G6TOxPwIHBRarL6JQ-StOPQB6hH3lSlfgEXRFogBwaP9UsRLsovureecA-yWvsP6N5EzA7jhoWO-Rh5NcHJeTpLCDo8SeHboTS23XulEcaNOETdK90EA1X77cbkUpwRHHXrUwY&v=404&seq=2"},{"alt":"","ext_columns":{"biclk":"1#a889a3b4cf7bd9198608242923b049cfdec968df-103-619066#43494363","focustype":"s","ap":"j0Spnb54kus=","mcinfo":"03652902-17044221-8101611202-M#0-2-1--59--#1-tb-#102-43494363#pc-home","url":"https:\/\/prodev.jd.com\/mall\/active\/gi4Pq4ek5494Wu2stU11VwjK9iS\/frist.html","desc":"","text":""},"src":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/94432\/11\/20795\/78385\/62012655Ed228f0b7\/367cca04c2aa3077.jpg","gid":"03652902","href":"https:\/\/prodev.jd.com\/mall\/active\/gi4Pq4ek5494Wu2stU11VwjK9iS\/frist.html","srcB":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/94432\/11\/20795\/78385\/62012655Ed228f0b7\/367cca04c2aa3077.jpg","type":"material"},{"alt":"","ext_columns":{"biclk":"1#a889a3b4cf7bd9198608242923b049cfdec968df-103-619066#43494363","focustype":"s","ap":"z\/ep\/M8C9uoBBlITEyBAiQ==","mcinfo":"03652902-17044221-8101611231-M#0-2-1--59--#1-tb-#102-43494363#pc-home","url":"https:\/\/pro.jd.com\/mall\/active\/kdLV9FcYcKP6s7KdLRVcEPqrUrg\/frist.html?babelChannel=ttt2","desc":"","text":""},"src":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/87414\/17\/21797\/50526\/62010949E99c1a828\/71dc7e61d06f9a36.jpg","gid":"03652902","href":"https:\/\/pro.jd.com\/mall\/active\/kdLV9FcYcKP6s7KdLRVcEPqrUrg\/frist.html?babelChannel=ttt2","srcB":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/87414\/17\/21797\/50526\/62010949E99c1a828\/71dc7e61d06f9a36.jpg","type":"material"},{"ext_columns":{"focustype":"g"},"type":"ad","href":"https:\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9scHMuamQuY29tL3BjL3BzcC83MzAyNDM5P2ltdXA9Q2g0S0dPVzV2LVczbnVTN2dlUzRtdVNfb2VhQnItZW5rZWFLZ0JJQUdBQVNGZ2luMnIwREVPeWM2OXdER2dSa2JHUnpJS3NVS0FFWTJpRWdBQ29nYVdJc2RXRXNlR2RsTEdkcFlTeGphV1lzWmw5aVlWOW1iRjlzTVRZek16Z3lBbWxpU3FjQlNYeFRTRlZPVkY5SlFpeEpYMEZmUmt4ZlFpeEpYMEZmVWtWZlFpeEpYMEZmVUV4ZlFpeEpYMEZmVTB4ZlFpeEpYMEZmUTFOZlFpeEpYMEZmVWxOZlFpeEpYMVZmUmt4ZlFpeEpYMU5mUmt4ZlFpeEpYMUpmUmt4ZlFpeEpYMUJmUmt4ZlFpeEpYMGRmVWt4ZlFpeEpYMGRmV0VkZlVpeEpYMEpmUmt4ZlVpeEhTVUVzV0VkRkxGVkJmRHRHZkUxSldGUkJSMTlHVWl4R1gwSkJYMFpNWDB3eE5qTXpPSHc&log=GAzYUXYleBiYx0yi3tCBS_1z9BscamtkMEa4naoSoI_wQyoHBV5oLDP5wj4Lm6249pyEIshvL3a0kk99Gx7WEB0khRkNhmOPvlXQY7qpYl9u5K23WRZOEmU30WDXW_dlJFxaeh19H7rea1Gf6-JaTYjEhRWP8sjPpHXNVbzhYvVyMAhxWyCgQ5H6opF9C4aW5L0kllYbyAAfSMOgqLqcTDlZilc98ZpZINH6twfJb-haFi9wWch4y3iXjQ8_nEjnZeDvS2v77CDX_IyF-u_td7YRyLbHZadEeSWXKVJQ8CMBDkUvpnPSerEcD2HSdPuiGuqt4b7yTL5jJy_2GrQCxLfjJri6vssxeYnLfm0798OSvj-PA6YhqOPiaSBk3v58eqX1Ofaj9rCjKa5m45DaLQF0e6RggqoMtzrV8-YOCicxVbvrpDfHUmLwC9lKu2oO01ye_aDhMGiEgux6wdiCzjeBz0Q5iJsSVOYzMVFtkKOCfEuptI-azusJcusoGxfmT0L0hnR-XyB0xxnDhQ-XZhKYC-sVqbgmta5UhmKZGtpuPUyXhtvbtvFr2VWW30AHYd-bqB7IhwabIgcCrHzQSQ-8da_KsjpAJIHbQgXdaIRhhDqOxLQHdbuBpQFTcLTs-bRc0cLLfgEG7TlnHCSbPAgonxcZP3HtbtnYJgiVsncfq9YmspTpPR8rqivNflJqERGU5C_f8g07qepu2_xwFB6AS3SCD2MzHxErXDgDthZ-MzZQXLyv9rkIED2_1R_mtCmEHOmL234ie85-ceuPe4ba6gxjNnFJbUDc9lBy98uxle5zBHEGmLMrOgc18wisaNPjEoti3GmPGxTl6CkY-P9RvXUQ75sRU2hJcFmw9ye1Qeo-3ulNHV7Tvmek76J7Tqv-T-QP9a1ALGsMHG0UNxULUtvb0ajs7klneRy0jA_R3W1VZ2mRN9ythOCe_-b-QI_O9TPWHB25DgErWomr6C1JU1NKT69VYHzuEOhz70lOgEXe_-T8AgeLeKpMpaMdiFlkVdZ_3APferq4pwENbUY10anJWgwlpehckGwcsJkzOwa-Rj8eOufOY_u9TPJEHdzmQJ-BKEwGkr9MfqoBDHfl0wly1NRZ_uYRdmyfkqcFCmzbfKqtRhw0j2E9kEBq&v=404","src":"https:\/\/img1.360buyimg.com\/da\/jfs\/t1\/39535\/22\/12149\/77249\/5d337987Ea4fc5f10\/29ba50d1c1eca3bf.png","clog":"https:\/\/im-x.jd.com\/dsp\/np?log=GAzYUXYleBiYx0yi3tCBS_1z9BscamtkMEa4naoSoI_wQyoHBV5oLDP5wj4Lm6249pyEIshvL3a0kk99Gx7WEB0khRkNhmOPvlXQY7qpYl9u5K23WRZOEmU30WDXW_dlJFxaeh19H7rea1Gf6-JaTYjEhRWP8sjPpHXNVbzhYvVyMAhxWyCgQ5H6opF9C4aW5L0kllYbyAAfSMOgqLqcTDlZilc98ZpZINH6twfJb-haFi9wWch4y3iXjQ8_nEjnZANYZSU-C5r6PfQFDsmwPn-SdG2TPy5DFbOQxQios5sxrx9SY1NhtyC0VSEA1ArTsEkHVjPINaIBVv2FJV4pwrkG0XLKK6nqTZdLU_ZaqnkHgfamAniGNJU_bYp7VxS8DH8wLDDVLLexChHhtwkC8fuyx2oH8K_uKH66nE1xfW3yY-S-BFQ7Ol3QRskJ2rRsqVeLIaVEVuaB0Ru-G-guctz5I6zGAGvqsYa8A6iIepr-zm4DXRwmakAh4J_L-BxxZtCi6cGlN99Q7I77LIUrhdyFRPvwfILR0ZY7nAbv6e4zxLlC4LBWVRgfD2A4NWZWs1ailY3EdxKXZV0AF1xuZrTGrkrKuEsJMIEtqYuE1Qgv7Z92cjiGTzBTN58Q-oczXGqHf-aCLlj88lKvAI_-YeHKoAZcJz424cn3LxvFrlQbckkXYWeOQ2fe-xu9qIPuqhmhgg7AQScd1-eyZu8e3_7hvrcRrOM7o9DwxnbDESVLaJPCgElKBCcp8Qzs0Xp4nHNXJKbbU-XI4qwn98nOWfvej2jRfnXGx95Yy8WHzjZH2mcRg4ms-l1EtXhxI7jO1Y6K5sTiLsIyFfNyDD-JE00RPxAEPeXbNJt_-y2nXOid76NI_0XGHC4ReSk6w12_23ltmagvmUKPVmHZzn5omAAWx5CVmCKeEyUHf5XTyxikzJb-V6zkHnnynFw4Niw6Ui9kb6DELV8vh-26qmMefxOmxG59YRvHKa6I0LZRJqSM8prQUT5NhuAfYmwb2gZj3dRpMtA3-LYmVDmkEpWPKQtb17XPcWWSybfXsOxBfdkLnHolwJ0a8QH-EiE7OvrJ9Ay2-wlDlrt8TWV0JJLNXbsh4ZoWggqkBURybN2ZCpb1VgEkIwLvjVDinu2r_iJ_&v=404&seq=3"},{"alt":"\u5546\u7528\u5f00\u5de5\u5b63","ext_columns":{"biclk":"1#a889a3b4cf7bd9198608242923b049cfdec968df-103-619066#43494363","focustype":"s","ap":"9gLGFXP7q4f4h0Arqq\/GuA==","mcinfo":"03652902-17044221-8101610921-M#0-2-1--59--#1-tb-#102-43494363#pc-home","url":"https:\/\/shang.jd.com\/","desc":"\u5546\u7528\u5f00\u5de5\u5b63","text":"\u5546\u7528\u5f00\u5de5\u5b63"},"src":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/120972\/34\/22737\/59798\/61f5468aEcfcd30bd\/3e4c9f12dac8e80b.jpg","gid":"03652902","href":"https:\/\/shang.jd.com\/","srcB":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/120972\/34\/22737\/59798\/61f5468aEcfcd30bd\/3e4c9f12dac8e80b.jpg","type":"material"},{"alt":"","ext_columns":{"biclk":"1#a889a3b4cf7bd9198608242923b049cfdec968df-103-619066#43494363","focustype":"s","ap":"yxgo8R761YABBlITEyBAiQ==","mcinfo":"03652902-17044221-8101611201-M#0-2-1--59--#1-tb-#102-43494363#pc-home","url":"https:\/\/prodev.jd.com\/mall\/active\/34qAaUk6AW39g9BX6me3z2F6pYUG\/frist.html","desc":"","text":""},"src":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/116391\/11\/27363\/76966\/6200d724E4fde75ac\/861537c907516dbf.jpg","gid":"03652902","href":"https:\/\/prodev.jd.com\/mall\/active\/34qAaUk6AW39g9BX6me3z2F6pYUG\/frist.html","srcB":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/116391\/11\/27363\/76966\/6200d724E4fde75ac\/861537c907516dbf.jpg","type":"material"}];

        //首焦兜底(新)
        window.backup.focusbak=[[{"sourceTag":"1","id":"4272","extension_id":"{\"ad\":\"\",\"ch\":\"\",\"shop\":\"\",\"sku\":\"\",\"ts\":\"\",\"uniqid\":\"{\\\"material_id\\\":\\\"7524724277\\\",\\\"pos_id\\\":\\\"4272\\\",\\\"sid\\\":\\\"b185b1de-6027-445b-88d8-7fe77d6c9d71\\\",\\\"type\\\":\\\"1\\\"}\"}","ad_billing_type":2,"src":"https:\/\/img1.360buyimg.com\/pop\/jfs\/t1\/40588\/8\/17960\/59407\/62e34ddcE9dbbf4f6\/553bb2b4bf1dbc0c.jpg","ext_columns":{"desc":"2:cpd","focustype":"h"},"href":"https:\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9wcm9kZXYuamQuY29tL21hbGwvYWN0aXZlLzI1aUJxVlFBZFFoQkdLWG16TkFzVkFBS3JnWjcvaW5kZXguaHRtbD9iYWJlbENoYW5uZWw9dHR0MzU&log=RhICBfqE7JFtl65rdz17dniaPVdI0ZLZMnMIp2p_LRAk65a_ARoIN9zPFz7LoLrffm7CQgTs5mWf4glrfboMabF4K0MOOj1lrB3c2F6feTDPRantG99NhFfPHb8AjVpBgvvWET1OK8IDQxhS_B2An9TEbddYb9OWKH7WT92o8MCsJryMVjuLf987VbUHG9UeZAn6NwsOl2S1l0PCrcmIRbwVvHS6s94aqdynuyOSaWdmr0mYPmRug-CGgT22GAlQCDehvnMwZByVjLtZFzM5FBmdAX3QzzFg7LPqbcRcNmuLoYp1xF_uitE-19THzUEmhbJHKi8LzkLUiUV3O2V24_aPyRB8eK5tgAS1KTidXuAOui5lvi0B2LtBWV-cN5ETE16gnCc_HnDNqL6lsFhDEE-1lVhVZgO-2P58vQE3TIueoJZxd7jm_R0YAL3-Er3G9WfM98jFKzm975PKrm3F_cuKSmlbcgXotkphgim84JL3VLHst_ap4Xfy4dNzKLZ2PAvDxYTEp3Z4Bnnb98P1XKAXq6Tab9st2MA9DLI4MnTmGG7i8XXgyVCH7IvjB7Yg-Znle29d0Hs9DNqScKw7cCuIOwg_TyDYwUF-aj4n93rsm34QuaccvWEQWk4GDWkZGnk0ZTQGoeVO9t6QIrMETwGN-H5O-Jts294svypO6vTbqHlwMA-FUHi_I5cQSPSDbi3oBFQND2sS68zgSeSbwzOupFQDLZHkTnoHkTeKL_TknxSER6n_y1tmOA4EqAoVOgwx4dp0EJjRlWjUENHAn7OJ_ZDJ8YkgGKds-fJIul0EQat8t0thACLG3xTlUnETZ-X5RyVjIbZzi3eGszrZsOz9XiNcg7viwXH950jsgTKKg65wJAThgRKeldFijBs0IE7IYwlVSI7TYCBMdD9cIhjq_EigDkmd5j4f-ep2VTerwGNAopywe7B-HRS9JhCLPGFr3Io64xeNXD2pl0nDEFycjLUgBLdw7svesyBHsHDSIIsBW19o-o9SvkcMZ1exiU3u56X9WOYsgcr-uQta4hySdQtLO0iJxTm6H9TbzS1UmyzrWqRHwCCqc8zE0-7sRpK5QwLmjcbDX64z7vUZRVbJqIbWX3dAyo0TTIxaUjee-LHBUyKxyjFz7DjbbCejgtsgI4hjGrfkpLSX6pazddWK5f0T21xnVY5kpJJQhXw&v=404","clog":"https:\/\/im-x.jd.com\/dsp\/np?log=RhICBfqE7JFtl65rdz17dniaPVdI0ZLZMnMIp2p_LRAk65a_ARoIN9zPFz7LoLrffm7CQgTs5mWf4glrfboMabF4K0MOOj1lrB3c2F6feTDPRantG99NhFfPHb8AjVpBgvvWET1OK8IDQxhS_B2An9TEbddYb9OWKH7WT92o8MCsJryMVjuLf987VbUHG9UeZAn6NwsOl2S1l0PCrcmIRRt6CCMCcpzcZwMLDo1jTJc1W4G_gCCaU4R--IDct2-wcjhphlrL3LTPrTKCa9YAcJgNmz-QkdfQQLQEBKln8dyfcK55yijjsHd_iBEhwc9LOwUF1CeR5h5jF9IxwoYq1XofLCG8xNAL81GyK8an36u2VBvPLRBrF2_YzsmPNTA2ev78rp1mX2mcpEdp-MXpKBUQPJ9tPG5WkhBZQkBTnxtcjcsS1Yt2xch7XAp2IqA4qKLMB86CbfwdRXy8bGclw9N1IRgToCqh4kzA9LfDILyF8uEwBpaqjEB8RUzcmLF2D1qKdTGt0B0-tSnt8bWDtNy1CvQ_09san9EXJLk990RdoXXpBTM235f9AwmQcd-rh7tmdJCHvzC3RqRpSp_ppYCytV4WnFTh6l9qDzEQcgoBCYkR4cHNgRHuW3Tl3FE9RC2u5adbVL8kOylcW7a7JamhFMdH8nVq6kDaaJYu6YxNud-o3Ohj4DCuX6LeEye4t3CcnucadQL0nHrs3IPYs0ackZrLVCHRLFB9C_sToDhAbPnFV0FbGJ_IAb3BQyRNeGt5hiYXgDn-am1IAdAD7iJ1ujY0GIl-LgMLweDUJ-yjKDCnr0dQe4LuXiEHn-zyRo4dWOMPUb7ybcF3j23ZPBy4RybfQRvFLgCkiErMsiAmvaMrmjobwbJhMXEOUbFJoh3E-DbO7QaIG6750hFsK3FNmP6YyRWfeYI4acTWVw7-CIWSnNH_tCGrlCqC5ijKg97JEm3gl3NJGdGJQamUXn-zYRnG4uNyPQ4HOevrhu13-oc-ai859ap3T_r6cacjNloTksxCpc70kbIlWkSsiiyqH7VVneJObg5hU50WGKnS3FA2hpNT9_KRD9pytxslKWuSkQ_FeWj_onsVaDt5l0J2vFXLdW1-ptEwGe-ul26hmICXOgXhcLOkd3tSvEq3BF5pgaw41s4nuW8q6U43gipcEYMBgo2yDkPCao8-uMI&v=404&seq=1","type":"ad"}],[{"sourceTag":"0","id":"3503","extension_id":"{\"ad\":\"\",\"ch\":\"\",\"shop\":\"\",\"sku\":\"\",\"ts\":\"\",\"uniqid\":\"{\\\"material_id\\\":\\\"9047627284137476637\\\",\\\"pos_id\\\":\\\"3503\\\",\\\"sid\\\":\\\"5e4529ba-f05f-46b8-a7a9-0832933a7372\\\"}\"}","ad_billing_type":0,"src":"https:\/\/img1.360buyimg.com\/pop\/jfs\/t1\/97340\/25\/28363\/100793\/6259ef9eEe79ba93e\/74319dfe09fac8f0.jpg","ext_columns":{"desc":"0:cpc","focustype":"g"},"href":"https:\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9scHMuamQuY29tL3BjL3BzcC8xMDAyNDEwMTMyNjQ4NT9pbXVwPUNoVUtEMnBrWDB0QlRWWjVhVkZYY1dGcWFCSUFHQUFTRkFpVjNmN1gzcU1DRUtPNjlnUWFBQ0RsQlNnQkdLOGJJQUFxSm0xcGVIUmhaMTlwTEhWbUxIaG5aaXhuYVdFc1kybGlMR1pmWW1GZlpteGZiREUyTXpNMU1naHRhWGgwWVdkZmFUb19DaHZtaTV6bHNKVGxycGptbHJub2g2cm9rS1htbDVmb2lMRGx1cGNRd0tSNkdBSWduWVNXMmNHaTZNZDlLSzY5NExNQk1LMjk0TE1CT0JOQWdJQWdTdG9CU1h4TlNWaFVRVWRmU1ZJc1NWOUJYMFpNWDFJc1NWOUJYMUpGWDB4RExFbGZRVjlRVEY5U0xFbGZRVjlUVEY5U0xFbGZRVjlEVTE5TU1qSXpNVFVzU1Y5QlgxSlRYMUlzU1Y5VlgwWk1YMHhETEVsZlUxOUdURjlTTEVsZlVsOUdURjlNUXl4SlgxQmZSa3hmVWl4SlgxQmZUbEJNWDB4RExFbGZSMTlZUjE5U0xFbGZSMTlTVEY5U0xFbGZRbDlHVEY5U0xGTmVTVjVhWGtGZlRrNWZSbFZmVWl4SFNVRXNXRWRHTEZWR2ZFY3FTVjlWWDBaTVgwd3lNVE13TWp0R2ZFMUpXRlJCUjE5R1VpeEdYMEpCWDBaTVgwd3hOak16Tlh3&log=dZAuGmySPn01aZFL0ziMXwZRG7HRyHlyCgQUj1FRIHn9T9YalGjPs6cppWPsb2rS0Ev0tzNp6ebXxH-KcpoEWGNoXprgYvLHu0tBmUjaXEnFDvfqLvj2tenoP-ri9kfarJLtkdcr5jREVZwU8Pt18xyPjstVnunRFuHihToKvxn9eIq15-RSDEF0NuS9hfxSmwVw_i9z0oQmtVIw5QxNYSkYEwzpHZxU3HAGRyCpe5QYgL7gZ5-tdZqdP27Xj3ZQ4lsZzmxFGfsJ-5tKZh8yLzxuIaMe2-qQH_Qtdt882-hIlTUfCbs_bLy-xt-EigdJPw0PfPf4ltB2igTKT8DawzcwWKDLilkSWEaclWjDvoXhU_-d8zJoD0LxyQO5Zt2Q6SZ4TRdS7B_h_zlHOReFMIfJJNAFagdyky7EBUH2gNWrJzU0roPQpPGsWUHBNX10qvJ3dq9iC26QjvW183RrOp2Ry2e1Vqtl07DwKkgZO6C_nJZPZPGQ2K95pMWI7rbhDagE9lcLR0MRcdf3-0vBIp88pxI0_3YNJ-FPEzS7RZiefuOZ3bYFL7Xo3Heh1AbIiMBh9zvjI0JUyxOWftJrhybJpHyVwnT8Hy-HFwMM3Dd10ZVLoi1scmtF5cc4UwRIlReULplr2Mtf6A8iACUjh8vMU_NMH-PWr1AXzqnGIzVvRmXa3oiK7CV966otzfA72436BnSo-4r7jFKH0yE_J_q1nSfSTiM7xu5dDTUO_e6bBa0XDwEkhwfwMR8_XBvng_oaJQ_oXV3hquuRherUI92NafqEvrmY6uR-zB-gN8qKiJuqlm1bXqohxFA9hEExb6Aq1wkLgak1uqToVB--ooNPE-ataLL9jh8c87-ubjoKU4gQIi-eVbBlWtKn7lPmOP-omkQqlpimDkzPx9prtCGd8GSID85Hr87Yvd2oPjkLOzlkivpsns323vKazC49hb_hI77wOcM7wCMW9plEoLZJf1nrS0heIWXUREIZuQW52sErzEqgAMN2xx_5cAw9xMWxJ7iZWhmuwzMBuwKkqAAytFBTHdbTxxv0xwS0ISdUxodsbvuWQc6J7O2fly2sMG55j94K-Hnd-CMtxaxylg_ypsSlhkTATURZ9p44ioYtwPd_6imPc7vlrGRkkwMHvR-SKCzOqEcJb1lPHfBE7CaxxYmIBmchXYcEDIs5c-mkTl_ZaPfxy-kasfYKyDO9t_5TdSAwIP6We4izDc0IqoYPshTudBiKHvIPquPjsoGEuKXIwNF8TTUgr4IVejRVXsKIRE5xYSgHcsEtNR-jjY7zHMsEiXfRmDvtiQoveyE&v=404","clog":"https:\/\/im-x.jd.com\/dsp\/np?log=dZAuGmySPn01aZFL0ziMXwZRG7HRyHlyCgQUj1FRIHn9T9YalGjPs6cppWPsb2rS0Ev0tzNp6ebXxH-KcpoEWGNoXprgYvLHu0tBmUjaXEnFDvfqLvj2tenoP-ri9kfarJLtkdcr5jREVZwU8Pt18xyPjstVnunRFuHihToKvxn9eIq15-RSDEF0NuS9hfxSmwVw_i9z0oQmtVIw5QxNYSkYEwzpHZxU3HAGRyCpe5QYgL7gZ5-tdZqdP27Xj3ZQ-khdtKnEcYLdFPeyAbfNqyX_wR5QLvepLSKwYaFj3kT7waCjuG_jhpc8awGGmXZ6zZUR3dy1Sf6Ptzgc1UQhFUangy6Za0RRduTVPlAPPtDzqjzLq39v7VZredbglRLRqd5-M2VqB-sKyvAjfgC2K34yeXnmYATzVoJdO_IfmVCKJVYcr81AiSzK7bDEJYYFGtZFUBszx4Uwz9JXj456JklXCDHHZO5E6UQmgy0X6hrdZuwrvtFWEt6NQrghqLfjaEDAmc7iYfRWjKiAcZOQoEBsmvjD48KBNqWh3ajeg4hgqE5NwNcDSS76DwPKSUBCgy000ybXfrFPMOlTrVD8xRSy-ISHP_vwX36F-4Ih48yZwRB_3GUhRlSBGqM3cXHkKq98DH1MEBUVnvGffY4v__NZBekjOoDMK-gw79wBiXF7QCs0BXl3hjYfpGhDEcIl_ZVKhNWEd_m6SK23ybpfseUqnHnAFnbQVoIm0bHNo_WtMmFohb0tT0PrJbMfQDQvznZsUPXGLRpDM2XNfhoLUg2DrVRm5Wo7xBL-Q39v23JQD3hkHT5s6eeczibt_gg4R0ZTgD1lRi0fO_Ue0ZElVlg1YEGeCGyKlGuJrpcBOvoGwRAHOuXbWSizfLsLmC7ItP3XeGhThHzMNZK4stIRBgDlm5SNE2F4aM_IvzwDxNlDMc0yIiY4-W16ghoxwqNqmvYQYMvtqY-6v7tQYRL6EHZb5FNk2cr1lAD026tEV_c_56WaJYi0z6PmNSfEBie58Gv_t7yBvWEckl-Vcc2B_7hYJUcThEAfuuemQCuoFjXaoe929FB4P78D9JXcKnqjCpnJhkUsWeiFuIahkV30NcdwJ_nC8rS9HBAsewE2jCWUPq-N7d_BSUvTlJjxiNM-Hw9um0Z8ahudT15no54OL0GdS0bTzNMrT62-S3nAnZ55zXlFb02soGC9DPeiFjucZxDpXsc_vgLBAAL42GVBVbnPBfN4tmq2kFgYo-H3MKdH6EeVE0gWYauqwxBSk7nnPWcKJbKocmNP6CJVDQbBfFN84fX9Pw1ehvDwbWhWHVs&v=404&seq=1","type":"ad"}],[{"sourceTag":"0","id":"3504","extension_id":"{\"ad\":\"3504\",\"ch\":\"2\",\"sku\":\"10040709678123\",\"ts\":\"1659342568\",\"uniqid\":\"{\\\"material_id\\\":\\\"8600628069413434965\\\",\\\"pos_id\\\":\\\"3504\\\",\\\"sid\\\":\\\"bad2b803-c88c-499c-917c-29c8122b7621\\\"}\"}","ad_billing_type":0,"src":"https:\/\/imgcps.jd.com\/img-cubic\/creative_server_cib\/v2\/2000367\/10040709678123\/FocusFullshop\/CkFqZnMvdDEvMzIzMS8zNy8xOTUzNC80NzU5MS82MmNkY2IyOUViNmU4OTIxYS81NGQ1YjQ0M2I1MWQ2OGY2LnBuZxIJMi10eV8wXzUzMAI474t6QhMKD-WNjuS4uueslOiusOacrBABQhEKDeenkuadgOS7tzU0ODgQAkIQCgznq4vljbPmiqLotK0QBkIKCgbkvJjpgIkQB1iriLzHnKQC\/cr\/s\/q.jpg","ext_columns":{"desc":"0:cpc","focustype":"g"},"href":"https:\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9scHMuamQuY29tL3BjL3BzcC8xMDA0MDcwOTY3ODEyMz9pbXVwPUNoVUtEMnBrWDB0QlRWWjVhVkZYY1dGcWFCSUFHQUFTRXdpcmlMekhuS1FDRUxqaU1ob0FJS0FGS0FFWXNCc2dBQ29tYldsNGRHRm5YMmtzZFdZc2VHZG1MR2RwWVN4amFXSXNabDlpWVY5bWJGOXNNVFl6TXpVeUNHMXBlSFJoWjE5cFN0b0JTWHhOU1ZoVVFVZGZTVklzU1Y5QlgwWk1YMUlzU1Y5QlgxSkZYMHhETEVsZlFWOVFURjlTTEVsZlFWOVRURjlTTEVsZlFWOURVMTlNTWpJek1UVXNTVjlCWDFKVFgxSXNTVjlWWDBaTVgweERMRWxmVTE5R1RGOVNMRWxmVWw5R1RGOU1ReXhKWDFCZlJreGZVaXhKWDFCZlRsQk1YMHhETEVsZlIxOVlSMTlTTEVsZlIxOVNURjlTTEVsZlFsOUdURjlTTEZOZVNWNWFYa0ZmVGs1ZlJsVmZVaXhIU1VFc1dFZEdMRlZHZkVjcVNWOVZYMFpNWDB3eU1UTXdNanRHZkUxSldGUkJSMTlHVWl4R1gwSkJYMFpNWDB3eE5qTXpOWHc&log=dXvPepIj-qyFY0d87t9bRJsZvO7LvDm1ODXmg9hbq5Di3VRn_u6cvwAe_vQaicdRKgARpNsYUmY18H3vqs_5S6F4mvhp4eTZzutUF2gcg-j1xZALc0q5F0ITP0lIGKUMG7AuvK4IKCgEB4v8FFPDmEX3f18TCjSr_s36yg28tw6xJhrzLeUmdDZP7dWejRD27fqygNvZYHAiJsOcpZD7cRsmmPut2UmUKlWLlyfphkxQBwwwnr92rCRyhRPdnEBZARgH5y6zihjF_ZtqCxFAcrsr-PsCVQ12SzYnaPP7zkNxzwiNbOnBGxL0WoKrrsEN_sRPHkNEDdcU71sYUIRLozh-qsY-tekNU7RLCH_eH00oFO21lJYwofV8YF6JW6JhzprhzBG9n3yJ0OMZZyQKKDiR_lcJlqR4qIYFzxQe2FdGV-_9fIL5DxBzdw_DP4h4wZKMEMQLnRkdReQncI6OeQdmxi0rACSZWvQ83MVPAwRVVb3ScYA6ysGf4IA2vDIPFNSWNzcgezjN48-yRlVs46hXs6W_HfHh5XzjyUJzJSt0uFjlStwj5mpqkLuFMXfWY_K30E6BQixWmh01I4sBo8tHPO8FOu7FwWQtzowh-e_LJfl1dnRBljEAYvL7ZMOc45jrwYId5MnFAsywKhAHMCB5hjsIT8a-jS6-RC_Q6k-G-9EoCcZUAkgGdtTTXE-p7g2DOFKVy4s_WTa4gSXvL-WRPVKe8TGmFnoZdmZj948Inx7vTxpTWVoLKE77OCipUA2EhI4tBGzxHxiN2mWgljKYoMN2By-FstXtFund98DkODKfbRfCPzCyxzlNQPtJKco_MUpVdKGMGDkWjHvhz-LpXTsSTHawAcCgxzejOyXkAeP2e4iQvXqdfjzzDsaxxJdVOfJmqM63ChhXPPrAmHPY6y-ObLNoOeYsLWr0HpznpK1vSpkwVOwe7UbBYgryOC7gqnDaIdGI_TBjD7IYgW1jlKN_5RyXs3_O2kRBGT1rgttYC8lY1c59Z1ZwtH5lOjd3kkrWBXyGp3FtZysS2OVcm1l3aZ9OECNUd5HX-hNrH1WyVw_yLu6VWJvmSrqnbjLslYlMcb_vvUbF7z9ArKIJBpjIBZpblzkAyKy8gmFpTxjLX1-YoMD9rXgRa1fiOKTkAllWM7OvuEEOvMxhiicN8ude6dhuvmkFstON_a76PGPdvcJobDIjI9__sAJPVtXRfYi6IHBUeb9LEevgSKJ_VLQ1vO01vWheG9m1fiCQYALFdknIUuEnXE_Bw_iIuIiu7GcIQImLmNqmv7p3d2X8NcMztZKkRX1gQtfPoc8&v=404","clog":"https:\/\/im-x.jd.com\/dsp\/np?log=dXvPepIj-qyFY0d87t9bRJsZvO7LvDm1ODXmg9hbq5Di3VRn_u6cvwAe_vQaicdRKgARpNsYUmY18H3vqs_5S6F4mvhp4eTZzutUF2gcg-j1xZALc0q5F0ITP0lIGKUMG7AuvK4IKCgEB4v8FFPDmEX3f18TCjSr_s36yg28tw6xJhrzLeUmdDZP7dWejRD27fqygNvZYHAiJsOcpZD7cRsmmPut2UmUKlWLlyfphkwKAYjSvnauyLYYadzaoGTk8dkMEb664GOn9oR_kM5NyQAN8Z3vQ6LMtJqs6CjjepV9kttv54_MEbICuupLTrabT95RVbofYO9_B2AtM45H_0USqIvq5x5xSY8SnxWuyY0nuY_yiVXfWQv93UFC-W2iiTXkXpgIx_POlfF5ji7-QB1qLFXj8euvoGUixwaNaOi3MFo20GLem6Xhxaz7DUvuYCY3oxsJ9ago9wjQzvi77Fz8TE-9L857yQ6KrSWeSxltui6E_Tk9mJmTc5mvd7IfHbRRBaOf-Wlu3hmOZRcuhVyqEIo5ibD2TwRcA2OHgZocPI2-NN6eRhV_g0h0M29dxH1S-xUIgFUIv0PHEOo-a2wrs1hvmkLeEHm_TilI9DZkxXrBCIwGQjo9E36IjM_O_hjdC2rEJ2zxv4gvj8BwIKiYOTAl74dNjcakdTTi35pg0MRQKKGlLJnLFRYRWAf9c2mJSzyeAwK4bxNJ6Hz1DgBh4Q6615u1qUtKLSdkfJ6UfMWecU1lLKg4QcIUbmaE6VUgGorOIfkajyNLGXXAKPG1D_m5xDvxzzs2k6cVD2DgSy4ox5NAnqYFsJYGxiWBi21W0iTHY9PN2enRjX_2ArxE19p9IYzP-a04dqYBGlZiHEi94bLI0RRH0WOzvp4ZCbaV-YInOQ3n1ELhZEthw-3j9b5cKW9z4w4goJ4feZ9xYmjygj0V2bfwP9CyGeYjVtr70crx44zG23jWdUCi2bDO5ktG2fvnn7Hsub5xV5WSmG6dzErKueD9sTXTVCUWDcPT9nZI0sHyBZR0tYm86Ps815gXvDJM-7R6YdUELwAT-e0s8IUoOgLdUb9SNtNSm8nYAVCBcUHKPwJqeUPJwqtAOGf7Mrl350P87HTchgj8sZrETuZ9pkXjL8b7pS0UaicJN6tTldjiMyIcmKlm1sjiEizjLIhj5cdWL44SSiN24eSz9jOo07PbwCjT7RPQeQfEvz7EWK9YLp-5PVHa3xpec7UOiUCU69p8W6KVNKGyufER71NERKC1qr_ZYwDoDyDa3ZqMQOery0FWMxynxc9zdIp9L7-yNYBZOWMJcvM&v=404&seq=1","type":"ad"}],[{"sku":"100014546493","did":41,"ext_columns":{"link":"https:\/\/pro.jd.com\/mall\/active\/3ZYfZKGRAhbHzJySpRriJoGWo8v6\/frist.html?innerAnchor=100014546493&focus=3","sku":"100014546493","playImpr":"1#13#100010-fc9a8e1d44f14d3495ece9d0ae958481___","mcinfo":"null","rt":"0","text":"\u4eac\u9009\u597d\u8d27#100014546493","biclk":"1#13#100010-esm:0-esm:0-fc9a8e1d44f14d3495ece9d0ae958481#388#100014546493#41#5f3a47329785549f6bc7a6e0-random--c1:671","desc":"\u4f60\u503c\u5f97\u62e5\u6709","focustype":"t"},"href":"https:\/\/pro.jd.com\/mall\/active\/3ZYfZKGRAhbHzJySpRriJoGWo8v6\/frist.html?innerAnchor=100014546493&focus=3","type":"delivery","src":"https:\/\/imgcps.jd.com\/ling4\/100014546493\/5Lqs6YCJ5aW96LSn\/5L2g5YC85b6X5oul5pyJ\/p-5f3a47329785549f6bc7a6e0\/2d18a66d\/cr\/s\/q.jpg"}],[{"sourceTag":"0","id":"3505","extension_id":"{\"ad\":\"3505\",\"ch\":\"2\",\"sku\":\"100018458255\",\"ts\":\"1659342568\",\"uniqid\":\"{\\\"material_id\\\":\\\"9028155012850330959\\\",\\\"pos_id\\\":\\\"3505\\\",\\\"sid\\\":\\\"4e677c59-69d2-4bed-a30e-5091d31e9f2b\\\"}\"}","ad_billing_type":0,"src":"https:\/\/imgcps.jd.com\/img-cubic\/creative_server_cib\/v2\/2000368\/100018458255\/FocusFullshop\/Cj9qZnMvdDEvNTMvMjEvMTc2NjMvNDIxMDkvNjJkZDliOGFFMjAyNGE4OTEvMGFjYzhlNWY1ZjE1YWNhOS5wbmcSCTMtdHlfMF81NDACOPCLekIcChjnp5HmsoPmlq_miavlnLDmnLrlmajkuroQAUITCg_ni4LmrKLkuI3lgZzmrYcQAkIQCgznq4vljbPmiqLotK0QBkIKCgblipvojZAQB1iPncLM9AI\/cr\/s\/q.jpg","ext_columns":{"desc":"0:cpc","focustype":"g"},"href":"https:\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9scHMuamQuY29tL3BjL3BzcC8xMDAwMTg0NTgyNTU_aW11cD1DaFVLRDJwa1gwdEJUVlo1YVZGWGNXRnFhQklBR0FBU0dRaVBuY0xNOUFJUXJhdnIzQU1hQld0M2MyUnhJT3BnS0FFWXNSc2dBQ29tYldsNGRHRm5YMmtzZFdJc2VHZG1MR2RwWVN4amFXSXNabDlpWVY5bWJGOXNNVFl6TXpVeUNHMXBlSFJoWjE5cFN0b0JTWHhOU1ZoVVFVZGZTVklzU1Y5QlgwWk1YMUlzU1Y5QlgxSkZYMHhETEVsZlFWOVFURjlTTEVsZlFWOVRURjlTTEVsZlFWOURVMTlNTWpJek1UVXNTVjlCWDFKVFgxSXNTVjlWWDBaTVgweERMRWxmVTE5R1RGOVNMRWxmVWw5R1RGOU1ReXhKWDFCZlJreGZVaXhKWDFCZlRsQk1YMHhETEVsZlIxOVlSMTlTTEVsZlIxOVNURjlTTEVsZlFsOUdURjlTTEZOZVNWNWFYa0ZmVGs1ZlJsVmZVaXhIU1VFc1dFZEdMRlZHZkVjcVNWOVZYMFpNWDB3eU1UTXdNanRHZkUxSldGUkJSMTlHVWl4R1gwSkJYMFpNWDB3eE5qTXpOWHc&log=vU1pKTizGZj5Su8ko_7dgjwf758NaCcRHcs4Tj25e2zxBN4PsREBgKu5Clmh2hqORt2c_6Bce0-eTSbH81O9EQcT84JnqzfXJCI5Ea_1F12cIIep6ExtNzSXA7mlbyPA9wE8qnsqrhBjMsX4dPcsGXmLg1RvxP-7UccpYk9ktNlME79uMD5NMcsecxDe46wxNLfhinz4_HQBQ_jUtWIZ59PcLBJrwKx9Mjq-cyg_4WNVyEa0o9bihP6JV2mDvPaWmC99dVF0B4dhxRazDgE73hBj-c8uAaFxg6ew7nBUxSVw5EJ-i84Hj9x535tmp9Lkl4OzpaQGFCeTNmmBS8SIIomeSA8Ds72s34wggbO2XujsNHB43n2-nmaW8KS2a_bjjWsc5GaHjWOYRYzbmNwkkW7P-M2bcnJz2gf6yakLQ2tfJP-kVFtxP10gcMudmqhz4l9FdnOidjlkN5ehwtTBUSzTWni1m3v5fiBhCfmgUKmSFe0sbWpltXSX0HW2qC5vtfDWg_HJRgLvRcnc86OjQWBE_YI9BJFz8dN_IGplfNJjsuIM8_RnRvSddRw77h2BtbmU0v0qvqktgPZVXXH-6BPBtDh1ZRAYLVq-SpqVXdYB_6P9lHfoJ0RkWZbZEFwwmn9Z9uq0JPHLIFrWIMMnHjmdEUlpszh14E1p737ZzEte1GeSaP3MhBm1EskDjZoUruPMH_vZ5vFXs1oM4-hrrfH7Kiw5fpXzsTEFVoY3-3O4_-eDAnCiSxPEE-FltLjRizWuli8CLGONoGTZzG0mNICH4Po3GAlkm7ld-yYNm1yobEsW3tD-XIE0BHxl4lD-dyH9iPo8qWOcj6QC73UYl6Qy8O3o_Inm1J-mcvJBDKltTaNi6S_ugaGB4aDmdgzsitGuJnj_86vt5t8K1m5Pi8sPEnvMI7QdgdUGsKrXZlhXpaAgM0vzEzWxi4RMBX1a5hVRw8ZOtrduLAnd4glPClo9j9lsmW1YBOYObqY0HWXfArnyeY_XFCkzgYDdUtbzKHv1bzSzq8pShtQzDj3Fv4JyhRMeTsykQhJh-FirMTF15f5HrRUi9adf5IQIFynGUuBJ0W0v_0Pv91KOtW6Ln4rbK6fy4XAbagaLSHU_hZn9-4V2454of7SvQePFIBbbh2vRURkhAWbcLnHDUNP13XOxrQxF3V_hQdCVdHkFH8eYPWEAGt6AV1ixT6gmXh1lJOdrQYLlGQtP2CsaOFxy-nvjkCKUlf9XkJgcKwAiDy5H55Xto0SDgC85e3SMUThWpHGe56GXlpZEjt1bOrEniw&v=404","clog":"https:\/\/im-x.jd.com\/dsp\/np?log=vU1pKTizGZj5Su8ko_7dgjwf758NaCcRHcs4Tj25e2zxBN4PsREBgKu5Clmh2hqORt2c_6Bce0-eTSbH81O9EQcT84JnqzfXJCI5Ea_1F12cIIep6ExtNzSXA7mlbyPA9wE8qnsqrhBjMsX4dPcsGXmLg1RvxP-7UccpYk9ktNlME79uMD5NMcsecxDe46wxNLfhinz4_HQBQ_jUtWIZ556MbOwZblQF1B8mZxLazMxB5T9XGiaiaDxR9n8Z-ib4MKfSIgIX7xbLa64YxBbFqyOG2SGfHQlqpyt9zg4RAuf8IMscJ35ywhrfTFdkPrN12fyyqT6OS6BYLF3s5LpQzS48kx18lQN92QJZ0e-gj0QhTipllZDr_XVf8qu7nr8jY2QW_koeJDZl4wd6iCzs4Y-xUkae8W3CTFi6fGcfPjFl4Hz5mrgwILdNu5OAJilaE5KN4rN8h9FRG-fZ14KhLwg2yMnhNTylwzbtzn4ZKuLwRq2dzMiWeotqk42Ih_t8-3lcJR2p9GPLZdpeLc11siUoUSlemT13be9aHMnfCoZZIZ9kMpVov3Np0SMyH33YXecjvLn8orgPbhMJl2SdCNbP4f2kBjrmkIJnq2Xk3b56T_VRy_cTv-uDPgNMihiqcqu2uNQcBISt_I5AkGAGbBft40gKtNIC-2SrJox3HuYymyanSefkw3cg3hDkZVrD6ki5enP7Yh9kLQNhalH8VSUPfDfCPWPUevCivkWfOVin6r-kbDRESvFStdFp-yRCfxUDqAa_QeBMPNorMBZj9bSoUPFaa9ho-K-dTBFj7rm8y3xN6tnPBzI4fRy7rWCSBOFq0k6EYh_bvwaWSgxbpthnWxyzNuPtfXa1aYe7audqID5BKrm_BRPO9HDfcSJkVCCwkKXVWJKOx-flfXADZJyV_uSwuEKcwzLua1hQeO9NOxm1ZFx9SmlIAR1CXJtH26gEICHDRgLYTPxSu5DN7kjamIC2faXg6erggosQKZcquYAhsaOHjW1NLnYD0V_bcZKTWlB9jY8PM1gfo5eUPbPFbe2V8OkMX6HY2Cm8NqJ3UncW5e-vOHUqflBUX8itAv_m1_mI488A7kr8gk26xfV7QEt47MlNRE7dYyR6WO5ojRSffAzFh65mZqzLiU-jKgQtwuMeiCZ8Kss8rVgc4iVZL2ao4rbBuOw6nsjWujwFJKdWFG4Yjt8pugqaeCkLRnx2zuhkXyMm_-5DCihTrlyw2ND5_EVwUImKyWb7fo7vRKcVEluPletFyxiS5bxNE85c9gzxEZr4tN9yY_rZ9A&v=404&seq=1","type":"ad"}],[{"sku":"100026667878","did":41,"ext_columns":{"link":"https:\/\/pro.jd.com\/mall\/active\/3ZYfZKGRAhbHzJySpRriJoGWo8v6\/frist.html?innerAnchor=100026667878&focus=3","sku":"100026667878","playImpr":"1#13#100010-fc9a8e1d44f14d3495ece9d0ae958481___","mcinfo":"null","rt":"0","text":"\u4eac\u9009\u597d\u8d27#100026667878","biclk":"1#13#100010-esm:4-esm:4-fc9a8e1d44f14d3495ece9d0ae958481#388#100026667878#41#5f3a47329785549f6bc7a6e9-random--c1:653","desc":"\u4f60\u503c\u5f97\u62e5\u6709","focustype":"t"},"href":"https:\/\/pro.jd.com\/mall\/active\/3ZYfZKGRAhbHzJySpRriJoGWo8v6\/frist.html?innerAnchor=100026667878&focus=3","type":"delivery","src":"https:\/\/imgcps.jd.com\/ling4\/100026667878\/5Lqs6YCJ5aW96LSn\/5L2g5YC85b6X5oul5pyJ\/p-5f3a47329785549f6bc7a6e9\/ffe43533\/cr\/s\/q.jpg"}],[{"sourceTag":"0","id":"4273","extension_id":"{\"ad\":\"\",\"ch\":\"\",\"shop\":\"\",\"sku\":\"\",\"ts\":\"\",\"uniqid\":\"{\\\"material_id\\\":\\\"7507039422\\\",\\\"pos_id\\\":\\\"4273\\\",\\\"sid\\\":\\\"751feb0c-43e3-4f83-ba18-c9814490075f\\\",\\\"type\\\":\\\"1\\\"}\"}","ad_billing_type":1,"src":"https:\/\/img1.360buyimg.com\/pop\/jfs\/t1\/67208\/4\/21074\/87040\/62e09ebdE19f9d307\/ce00b54d607416a2.jpg","ext_columns":{"desc":"1:cpm","focustype":"h"},"href":"https:\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9wcm8uamQuY29tL21hbGwvYWN0aXZlLzRKdzVnUnVUS3pOc2RKZlZxTHZyaG1LNWpIQkEvaW5kZXguaHRtbA&log=SkYObA61MG-Nl0uQseUgUOPTmT5KYXDV_pmHdTVNqHYO20fJXw3IXaXMBj4xsyom5DGXje4XFV2XeZlc4BJED8fnSjZZ8LyxPnFTfWk5kCEHdYwdVsWjSJZdlJ9_FanGAXXSqzNe8V12xHkS2ldOEuzYVQlQH-DfM85D1CvrXZT7I8qF5bCbhXdxCEzDV0RjJQTexggxFYhzNrcPcIUDGdnsRCy9sQygSqjI47XXDb0klALK59G9iwGo9Cjkc2uKxbmdhkf6Bmj3JWqDDVicLLm9GtaWANEZ2OhgoiCsDcThCfoO-gD5tUIq3HuXPRrFAYPow7ugOKICQgskW8jpXXVsTLCjlDPWtnpjK3tB4IlHFmZl9NOIF-aa2J7HoZnz3BWe9wM-HZq61HBxIegmwZy3Iwv53UlcDYu0Bv5-RZqcrmvLiu7Aex2GYEToIP59mE2_F-yvm4V92octx50ay7H5riyCUcSVYjYcHwjh0priZd0EldfUXlO4zUuBzjP7dqGktRtusd-4g7UEAlNO-kk3Kw4OfkWcsR_Qr_kRZL_D_kHHJIn04dYX7w32JraWFvv_1zY35i4lqAfp3BabOGvQ0QI6BenanrMwcUA6gYKQi5fWc0eCwc8nnpyNtTBYWfL1PpERPpCwmNknlLxjh3QlCmCbyg7CQE-2Fm-N5MCAaqLOQuoI6Q1rMFx_Fk2T-0xv6incA7dHzHSyIjVxrlFBce7PZFhovXL-j-cWyob5xh6ekERepb-5TD4WERNiiVhR_kU11VUPgeK71OsnHeVYpmIUkEQym4zZ30KX8Mamx8cvV5fralNWSUJc2zu39tvB35jgqoC-DsFosO9jR8-CVr7RUax2GzbfVdM-ML416yvElJBZ9cXHJSrQrP0ORl_gBtRgO_VQ11zpHKMsMxBCd1ckvVlWRbkkeojuU1pOGK5nABrOaMJBE3CIRC3n-CYIshk7adgeXYQB6i_Kh_cyObcoYdWBccie0-KmSYZJbVAmBbH750C8U7zK3X8hwDeBsHi4bovTWFXb4jQCSMvaz4xA3-L5qB4vEJqb_L1XxauBTQtxhjVzrF7cZesubASHqXMPeux7c8k2JWyrbLXhbDxwjDPsscrWWJoQYtPW-I2ab9S-RwCDdg2v-01xszWgyf4RAHRhsZHNuVtcnVwLRTzi3RaKPTnuxRM8zStAI-yRtMt86epDe0ToLOWw&v=404","clog":"https:\/\/im-x.jd.com\/dsp\/np?log=SkYObA61MG-Nl0uQseUgUOPTmT5KYXDV_pmHdTVNqHYO20fJXw3IXaXMBj4xsyom5DGXje4XFV2XeZlc4BJED8fnSjZZ8LyxPnFTfWk5kCEHdYwdVsWjSJZdlJ9_FanGAXXSqzNe8V12xHkS2ldOEuzYVQlQH-DfM85D1CvrXZT7I8qF5bCbhXdxCEzDV0RjJQTexggxFYhzNrcPcIUDGdnsRCy9sQygSqjI47XXDb27daQUfCySuuSRxZuMK8SdhiXAwtOIs0z91V3VsmSWGpz_vvzNTRztW-g8I0Zc8cTwMjMhMB-bvx0OgEGee6Sd0CM_Yh5e_qG7S3N45GaUA_qQN3W5Wnw19DkQsaCf7vCw-J6USqrJDjQ6DLoszgVgThRZndOz1L_TocVKkouoCDgSwwulCBFFSlBHu7E9Ui4div1XWu8J7cfsYPiOTXJyWtG7JZIMBb1Pq20Tz1GnpUmJdtvTmg_pRX30ZTKZGaAED8udeGqHRFuujg3iVJ4otIlZLRV27UUmM9oMpogbnf88a_Aw_M3JYXwttAX1NwJvnY5ByB3EioXDisYmE4AsdQ63lUPl-wugsNer0KeftyBYfopWPo9pNJtlXtrStKkn60sCzaNSrkYFyKTu0QQ5wV9YE64QUikeQixqFgLId9lma4dvdvf8OnepZHmzBc_Scy307W2dTRZAjQNvaF4JqDDNaHRen27WHw6dPpmSuZDtCNaWhERfXwbtAWIhYi_7WG6d4roaFhYIQaLcoHNT-CNxns_PinhsGpdQxs6GK97UWcqlPzXxFBk8ORlDgHcELCGUvhHqXxXl6EFSOCF2jzGtXtgJsjJDpcd4z4sR2Xp1886nhdvP7tVR-2ZFabXqlXC0BZdGhxPnv9d1F-zMyfRWof-kC0kaY_DujwBQ3NfNb7BMA_hW9NIKoaIJ2n97Ro-R4mWZrhy8rdrsP73lCPdA6W9V2lp8YXH1IdGpktP80oKzOj6q9ZWiiHnzRF7pimiFGLgRfS3CVtMNnF0AZQaQwfJR3QIRgr-vt2b_fZZF8zmqu80hfzqc5FkNXnM_QTnikvl44sFXz30RB3hBq11DEpUqsbxhaW70x4RqyY5iw5Sha1t3Y3egBKQ-lSnt9aCGs4fA7pcunCtR3BBkslJjroPJKbGmubZNidG0bjo-KR5XK3_0CTAOdruHHJJk0fEzTvXtEljO6WbuoBxm&v=404&seq=1","type":"ad"}],[{"sku":"100010728845","did":41,"ext_columns":{"link":"https:\/\/pro.jd.com\/mall\/active\/3ZYfZKGRAhbHzJySpRriJoGWo8v6\/frist.html?innerAnchor=100010728845&focus=3","sku":"100010728845","playImpr":"1#13#100010-fc9a8e1d44f14d3495ece9d0ae958481___","mcinfo":"null","rt":"0","text":"\u4eac\u9009\u597d\u8d27#100010728845","biclk":"1#13#100010-esm:1-esm:1-fc9a8e1d44f14d3495ece9d0ae958481#388#100010728845#41#5f3a47329785549f6bc7a6e3-random--c1:671","desc":"\u4f60\u503c\u5f97\u62e5\u6709","focustype":"t"},"href":"https:\/\/pro.jd.com\/mall\/active\/3ZYfZKGRAhbHzJySpRriJoGWo8v6\/frist.html?innerAnchor=100010728845&focus=3","type":"delivery","src":"https:\/\/imgcps.jd.com\/ling4\/100010728845\/5Lqs6YCJ5aW96LSn\/5L2g5YC85b6X5oul5pyJ\/p-5f3a47329785549f6bc7a6e3\/f257035d\/cr\/s\/q.jpg"}]];

        //首焦兜底
        window.backup.focus=[{"recommend":[{"alt":"","position":1,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/160427\/8\/216\/44383\/5fea8b3cEa4deb858\/fe57a084e88526f3.jpg","href":"\/\/pro.jd.com\/mall\/active\/26AGXsmM6AChBJXAvFuMKZ8h5T9E\/frist.html?babelChannel=ttt18","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"Zag\/g9b0Dld+fkfVf4Suog==","mcinfo":"03294000-13573946-8801423632-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/26AGXsmM6AChBJXAvFuMKZ8h5T9E\/frist.html?babelChannel=ttt18","desc":"","text":""},"type":"ace"},{"alt":"\u8fd0\u52a8\u6237\u5916","position":2,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/160199\/26\/187\/69636\/5fea04ceE5abe2994\/d12a85889d01cd15.jpg","href":"\/\/prodev.jd.com\/mall\/active\/3X6GiZeEUSw1zfbYxzhVfQpFXbWu\/frist.html?babelChannel=tt9","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"5+Gcq+Ev\/0h5o09w5iB1hQ==","mcinfo":"03294000-13573946-8801423635-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/prodev.jd.com\/mall\/active\/3X6GiZeEUSw1zfbYxzhVfQpFXbWu\/frist.html?babelChannel=tt9","desc":"","text":"\u8fd0\u52a8\u6237\u5916"},"type":"ace"},{"alt":"","position":3,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/151690\/5\/12181\/71606\/5fe9bf3bE80b775d9\/d67be1ff0b8fa2a6.jpg!q90","href":"\/\/pro.jd.com\/mall\/active\/2tRyWk6vGETjF5aPtAZoXxdnddYA\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"gIoMIiWo0D\/LhPR2RJZQ2g==","mcinfo":"03294000-13573946-8801423636-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/2tRyWk6vGETjF5aPtAZoXxdnddYA\/frist.html","desc":"","text":""},"type":"ace"}],"banner":[{"sourceTag":"1","ext_columns":{"desc":"2:cpd","focustype":"h"},"src":"\/\/img1.360buyimg.com\/pop\/jfs\/t1\/40588\/8\/17960\/59407\/62e34ddcE9dbbf4f6\/553bb2b4bf1dbc0c.jpg","href":"\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9wcm9kZXYuamQuY29tL21hbGwvYWN0aXZlLzI1aUJxVlFBZFFoQkdLWG16TkFzVkFBS3JnWjcvaW5kZXguaHRtbD9iYWJlbENoYW5uZWw9dHR0MzU&log=P9s65AycpQwmQ8oTNGBvBCb8PbOu6yGsYtDodHHur78q18US_CB-t3ZQzt_oKgb3ERufj1NP8Cw4IqHraGDB9PCMD5XM84mLVWmm1dl_vrvKx6V7lK9xbuwEmCIhyfMkYNc16yR1l2k-kifemIMb1h0uqqLTywjVsxzaxn93pBD3RNcnNZYtPzYSOwOyw29fhPhIzGFuXE_-k9-0iWt57_nWcxdKCZ6RGeh10VIeJepthed0-GgMw87m3jfu9R7woX_7WSbodG2y7_BiGYPHAixXBxpxGlWLkReuuab9vMdeK0_TmFyN74yNiTpWk8W_KX7W9r5BYEIM0152kVH7oFTY4xrtirtTVjy4ewIOjMh_QJXbd6i9UkIJh8iBpTCH25Bd5ZB6aBrH6MMwTAlZvZ3iH3p_jwYy1xET57bH_3aG7WwOc-eZ1P8Zqw_kEOKfxo3hAWcq4aQBIrcax0yc6CtnrZ88qcjOR8HI02Ce3R_Kx9HPBWIF3rrbQZWUoy8sgick3ibdoxaMn3zRQDqkB3ZM1FyDTuHHENBNXeUz1To-kjFRUSzoEKx5sPeknTgZoqxlMfdifAD75iXStbLFltH8GW9vQCzFMi3uek56NbXKZeRGRcij2jYn4iS2aRCunrgm2szOiMmNZ9vPCCOsTZtSHHIyvzoqBjHQSh70-XwsysmOeFesRsZKhFO41qUiWJr32DiW0HuyJhx3EAJgTMg1wNxyJzfviLdoiC6_mFASvG5R-FGcqmbbH2-fpTkZkfiHVBp_laIxKnpQZINqgZd58fhobQJw-2AH6c5ZITYPxNzBLGTBs_ZgrpV2AOVkI4B0pCYjpk5tv_I9fpnwC4sWUYrqEAxARIlqg17NkGOk0GxDLnRvHmol4ac7YaN8cMzpUbqwU475CgTJGkEvpLlEJ0kHTRzfMi0FUDwZBblpASoVAzCBxnfoqMqa2yb0TZQYBxgoVhb8tQfzylZM-Csi0HEt55ojNQEv7A002qt4EE7SdJ8FAKVEtjF9g-A5BHjt6Zc8Edird6eWKnz3zA&v=404","clog":"\/\/im-x.jd.com\/dsp\/np?log=P9s65AycpQwmQ8oTNGBvBCb8PbOu6yGsYtDodHHur78q18US_CB-t3ZQzt_oKgb3ERufj1NP8Cw4IqHraGDB9PCMD5XM84mLVWmm1dl_vrvKx6V7lK9xbuwEmCIhyfMkYNc16yR1l2k-kifemIMb1h0uqqLTywjVsxzaxn93pBDtM75wunO3xG72Twi4hdO-nmpEE0xo3owkcyfkVxi9C7Y06mdCSmE0kYcjgKNIckUXq8DlvNRt882uFN8ZdWGAvxjjkQVNoRQT5BVEWKMsmePx4sz_2pf7cvRj04Kt-E0rnacY9G7TiRVZg68oSH2vaQAm8tqqCxUUYl2qwE1NdTV0N49rGrolNVkGXtG4YpGnckszA2CZ4KaSKFnYtZ9LAcN2VTlgN9mm1xwG7JkWdVK_8iO0pAFedCUn2ZoBVm6Dp4KIB4wzjyy6-UawcE7pPGxknkIFCxiVWbZFaoKeOzKXAGXVgOoPmCZg-xQ85z-uPJt6xFdpWd4LOW5nrbRY-DvIY_a0qaD0mOLPrw9_x7oubR0FwWKBTnGhQ0k1b61KjcH9M-bZ6uyMlz6qh4oMpbh9VQEGWA_LzudJRtWiQdg1c69f7M-rOt2o3AMa_6QPJ-2djY4DpYrYVwSUyfb1I7T5COZ-QDaPoWieo7feJWHtdiPrKeExTOFzCow-OQD0juydip9z2vrSLKlJZ2wsuA7eCkyiFRhhtogSARPqL4Le3TT00S9w9MFlSmoX72g3RCBFZUv1b3G21lAQx4071R6vNvOhEcjNYejoKRU66mpcDvW86BDRXNJpEAkwx1Om1vOXKxr-o7MwvpKpNKtS-wgvGa4R8yj8Bq3fWcVI-aKLd-1hh1xhc9B7yuzfs5oRr4uy_CuaUgojWkCf7ZxlAS-oOZkhaKLM8aZoZqLTWaqxioqqzqtr_tbxZdxRhSWgI6blB2nnMShoujP24EFK6ZcrIFlXIthPr-O-6Xvtor4NbFbcJY3GOFLQZNCaRwMsZ410TDq6O9apY5m3PtjC5oHFtS28QC9Q3ZkalQToxA&v=404&seq=1","type":"ad"}]},{"recommend":[{"alt":"","position":4,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/151106\/13\/12106\/70958\/5fe5669fEeb4a53c5\/ff4c2841360b1db2.jpg","href":"\/\/prodev.jd.com\/mall\/active\/2KS7qX4VEn8pt5atxK5W1jGAvrc5\/frist.html?babelChannel=ttt32","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"IRwFC2C28awBBlITEyBAiQ==","mcinfo":"03294000-13573946-8801422732-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/prodev.jd.com\/mall\/active\/2KS7qX4VEn8pt5atxK5W1jGAvrc5\/frist.html?babelChannel=ttt32","desc":"","text":""},"type":"ace"},{"alt":"","position":5,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/144093\/37\/19883\/83175\/5fe407c2E1b76b792\/68ed75dabb686375.jpg","href":"\/\/prodev.jd.com\/mall\/active\/37ThKCmK6tFnWd3V8PqwMJ1SE3TK\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"qGh6sTt79QoBBlITEyBAiQ==","mcinfo":"03294000-13573946-8801422298-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/prodev.jd.com\/mall\/active\/37ThKCmK6tFnWd3V8PqwMJ1SE3TK\/frist.html","desc":"","text":""},"type":"ace"},{"alt":"","position":6,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/138772\/31\/20178\/39292\/5fe5cd5fEfce38cdd\/375bf42ad6dedfad.jpg","href":"\/\/pro.jd.com\/mall\/active\/46Vsus7SpKRgDbyAUitFHeBJnthu\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"PMS5koVkFfmNOxwMgDd+Yw==","mcinfo":"03294000-13573946-8801422822-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/46Vsus7SpKRgDbyAUitFHeBJnthu\/frist.html","desc":"","text":""},"type":"ace"}],"banner":[{"sourceTag":"0","ext_columns":{"desc":"0:cpc","focustype":"g"},"src":"\/\/imgcps.jd.com\/img-cubic\/creative_server_cia\/v2\/2000366\/100014261500\/FocusFullshop\/CkNqZnMvdDEvMTI1NTI5LzM3LzI5MzQyLzgxNDI2LzYyZDcwNTlkRWZjYWU1MDJjLzg3ZGIzNWY2NzNmMTVkNzQucG5nEgkzLXR5XzBfNTQwAjjui3pCFAoQRlJBTlpJQeiRoeiQhOmFkhABQhIKDuenkuadgOS7tzExNy45EAJCEAoM56uL5Y2z5oqi6LStEAZCCgoG5LyY6LSoEAdY_InCyvQC\/cr\/s\/q.jpg","href":"\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9scHMuamQuY29tL3BjL3BzcC8xMDAwMTQyNjE1MDA_aW11cD1DZ1lLQUJJQUdBQVNIQWo4aWNMSzlBSVFuZG1BM1FNYUNHaDZaR3hrZW5OM0lQRjVLQUVZcnhzZ0FDb21iV2w0ZEdGblgya3NkV01zZUdkaUxHZHBZU3hqYVdNc1psOWlZVjltYkY5c01UWXpNemt5Q0cxcGVIUmhaMTlwU3RvQlNYeE5TVmhVUVVkZlNWSXNTVjlCWDBaTVgxSXNTVjlCWDFKRlgweERMRWxmUVY5UVRGOVNMRWxmUVY5VFRGOVNMRWxmUVY5RFUxOVNMRWxmUVY5U1UxOVNMRWxmVlY5R1RGOU1ReXhKWDFOZlJreGZURU1zU1Y5U1gwWk1YMUlzU1Y5UVgwWk1YMHd5TVRjME9DeEpYMUJmVGxCTVgxSXNTVjlIWDFoSFgweERMRWxmUjE5U1RGOVNMRWxmUWw5R1RGOVNMRk5lU1Y1YVhrRmZUazVmUmxWZlVpeEhTVUVzV0VkQ0xGVkRmRWNxU1Y5VlgwWk1YMHd5TVRNd01qdEdmRTFKV0ZSQlIxOUdVaXhHWDBKQlgwWk1YMHd4TmpNek9Ydw&log=N7Q5XzUN2Cb_YoGCoJq6vzLzKWoaHqJYT9dBPmihk8ifMbdO82NLAkVaUWuABVjDwT9xodtp9-xFbqIay3yGOHc4eTR26zECbqclk4QkUqCM1bKB1L-5u56bXdJ4qitXRuprxCJdC3MgPWwx4vXcDcU-za9ya0DaXnN3Y2E4nckrigvZXdSIgMGeWkeUQZCnvnUMJYXkLN8Bue-iFlIq-39pBm3gSJohTILt4_IL7e27mrwa8Oncd0-QbLixTGIZt83nCHZTyqXpvKHT1wq3s4WhlvASf4azz7rDQT7i7XinK5BjYRq-o4sgGh_tiBWsHt5xjzRdqpauehdmgAJ8FsYk3ulm-A28u6y_nSgPFIrhxLaAJCflN00zQgjrkNBcPn15CnlPkJhY3HHMghHhuEPQKA0UrTc0deCD2mzONnvaw-dUK_wfbZ8tYzOjcB5kFaTF6IaKVD1X7B6sYEbdVgLxU5zN5UEY-4y1QbT5icb4ubwvsYOpH9TG7rq2qggBGenpd8xGCmedn-VJgWmSEC6m1_gc0Sq8OCXRZA4HTNCyRnAwqOLx4haAAWrjqoumEBwi8okE8axBeKzSLcBjYgftabGzC_jZJK8ZY2Wj7FdtThF9au3LlVOxFAiRYFQMrWZty8SamSjdUu1AKNWSdfYfhh3RUWMxZprFuAwwLjCJBeKGNV-ujvyxwNLg_lQvKWOdZ5jYj8DSvGSQASYiOAd-qkpe0px8uFR9_NXSv3fyDrB9Hb_0pNUbSHzpyG4wUlmVuPltMu6Idi6c3KxA9k27Ol6gLBfqUJqJ6UOTPYkSdBSvwGG078zHZDP53zEVLCev8zJa47VG7Z9KSI6KTbpmLBV7oAndjLSv6D6UAnBCFUyJSkFjPPMVfbtNNvN_V2pSSOm2ddaAkYc5zfCKuhCJqVKcYlzXbzytJ484GkXKmCE2iCrJMQMFdeSW03uRwzA1v-giinN7ROSl2fzWbfbsWK_UEw2rncoN7Sh6wDt1n79qznLqt1U5vTZkiuV9bMok8usl6xDm4v4-Wnf7pOeDcWnIYuLA3QTKIhKexmt5Tl-E4r8jE9D9dI66rN0SAW38OKVFPNMtWBhe6HQnVQ99xXg8ewwqvyYtAi-T3ufPjCfZIEXbHqFLoXYE01UxIsuymgGIaa_JU_X9hGt5x702qN2h8lOV1rz6WJtKNsY&v=404","clog":"\/\/im-x.jd.com\/dsp\/np?log=N7Q5XzUN2Cb_YoGCoJq6vzLzKWoaHqJYT9dBPmihk8ifMbdO82NLAkVaUWuABVjDwT9xodtp9-xFbqIay3yGOHc4eTR26zECbqclk4QkUqCM1bKB1L-5u56bXdJ4qitXRuprxCJdC3MgPWwx4vXcDcU-za9ya0DaXnN3Y2E4nckrigvZXdSIgMGeWkeUQZCn1bp84qc288gUHsPs6evYQbw72r5XFyq42OOWiYCjMcapDPmG_IRop_LyOVlO7Y6RrpZD1vZep7JzctWByGJQAyOJ84ToqR6l6H8CWoONVsrkLD_BIDMGAJ3NpT33IUQo9mv7gDvmz1j0lly0F67b6iDQj0zq977gr250-D9IDSOYCf8hTFxdHFi7wozhlRjQmizZjd6RnyvCfFpZuV7PKONpHWfk46rHCTRZPnrSZZbDX0m5fKRboINXllfp-2iUGNh2nItLfXKaFP-Kd0gNDLnrJKwvr8KC-saL7gNAoorsWYIzPOXbk6sNLPGid4RSurZhpQSGujsb3jNxltLTe_uXJfHyGHoVw9_8Ks3PJqTFfRqXFAVhTMjezHuuiSkG0qi2xAr_hPVRYhNlKe5ao9uOf-lOenw0h59JzlDOWFqelISnQ4LXhNFB-ksY3drnPGKGj_nHhWisDtPywPJJpRqu-qKL-uZJLETU59RRrTUw9NSSvjlBIvaDq2x_CGVnExpsdOBvMy02-mwXeuLyC0PymXBrCVUMKIBooy33DFOgjaafuNO1JeW0rGuY8HE1EqB5JAVW6g-iaQcoEBC1RWaxkhOfAnYIq4Kvgmhbm_DvBKxDY404oWr8w3ry15gSIMJ1og9EVr-ZZhJfX08MDAM7FRxeWddnYXhB6Lsn3AYkkIXhquop0IlYWeFkDO60v3Lf5WnQyXnFmuNdPxBJDN6UDSvvvlGlV16y2EvpF7wI-2g_zS0mWLBHgct8T3FCLhk1U1CdhZBAsNcGCchs-U-ceopAI_VcZNGMGvlDfKugtwayP7e0gL_M4S3Mnq6LCrksmf4B8wyx9ahEhMw-u2kkimnJQdM5t3BuH8LmCbFst0mIDK-vrDZA87XK7rQyTivt4h6zl6lEh06IuC7ZpPqB2J2jLBSElJ35nXnXlyKXuSAO82Tq7blKXOpXppHZpVpmAhxai2mm6jr9ghFyRKTnx878gD0f8bNcqQw5yvyzmPfxvCLb-YI_M-wVDrfM&v=404&seq=1","type":"ad"}]},{"recommend":[{"alt":"","position":7,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/129709\/30\/17733\/53433\/5fc20ebaE16d5e08d\/bba7d0a8e8e7fb10.jpg","href":"\/\/prodev.jd.com\/mall\/active\/zGwAUzL3pVGjptBBGeYfpKjYdtX\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"+BuvoFpWY12V+3PXLySUMQ==","mcinfo":"03294000-13573946-8801420745-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/prodev.jd.com\/mall\/active\/zGwAUzL3pVGjptBBGeYfpKjYdtX\/frist.html","desc":"","text":""},"type":"ace"},{"alt":"","position":8,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/153447\/39\/11074\/46465\/5fe2e757E465bdd19\/a3db919bd4cd1490.jpg","href":"\/\/pro.jd.com\/mall\/active\/G6dB2UyBBfwfTVCBp3iMQQQ6GHi\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"rGjgT8k0RWIilVEYymoeQg==","mcinfo":"03294000-13573946-8801422515-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/G6dB2UyBBfwfTVCBp3iMQQQ6GHi\/frist.html","desc":"","text":""},"type":"ace"},{"alt":"","position":9,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/147490\/11\/20231\/58763\/5fe554d2Ed968d82d\/0e749fd6e3e38af1.jpg","href":"\/\/pro.jd.com\/mall\/active\/3XjkyqALMxPUtxHp3VPvPzR2USqK\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"gGIXsI7ZKj4cCPOFSR5xbw==","mcinfo":"03294000-13573946-8801422820-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/3XjkyqALMxPUtxHp3VPvPzR2USqK\/frist.html","desc":"","text":""},"type":"ace"}],"banner":[{"sourceTag":"0","ext_columns":{"desc":"0:cpc","focustype":"g"},"src":"\/\/imgcps.jd.com\/img-cubic\/creative_server_cia\/v2\/2000367\/100036482164\/FocusFullshop\/CkJqZnMvdDEvNjc1OTYvMTIvMjA1NTcvMzc2NzAvNjJkNDYzYWRFYmI1ZDY1ZjIvODg5N2EwMDgyNjMzODJlOS5wbmcSCTQtdHlfMF81NTACOO-LekIQCgxiMnbmiqTlj5HntKAQAUITCg_lrp7mg6DkuZDkuI3lgZwQAkIQCgznq4vljbPmiqLotK0QBkIKCgblipvojZAQB1j0qI7V9AI\/cr\/s\/q.jpg","href":"\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9scHMuamQuY29tL3BjL3BzcC8xMDAwMzY0ODIxNjQ_aW11cD1DZ1lLQUJJQUdBQVNHd2owcUk3VjlBSVFpY1NCM1FNYUJtZDZlblJvYkNEMWdnRW9BUml3R3lBQUtpWnRhWGgwWVdkZmFTeDFZaXg0WjJFc1oybGhMR05wWXl4bVgySmhYMlpzWDJ3eE5qTXpOeklJYldsNGRHRm5YMmxLMmdGSmZFMUpXRlJCUjE5SlVpeEpYMEZmUmt4ZlVpeEpYMEZmVWtWZlRFTXNTVjlCWDFCTVgxSXNTVjlCWDFOTVgxSXNTVjlCWDBOVFgxSXNTVjlCWDFKVFgxSXNTVjlWWDBaTVgweERMRWxmVTE5R1RGOU1ReXhKWDFKZlJreGZVaXhKWDFCZlJreGZUREl4TnpRNExFbGZVRjlPVUV4ZlVpeEpYMGRmV0VkZlRFTXNTVjlIWDFKTVgxSXNTVjlDWDBaTVgxSXNVMTVKWGxwZVFWOU9UbDlHVlY5U0xFZEpRU3hZUjBJc1ZVTjhSeXBKWDFWZlJreGZUREl4TXpBeU8wWjhUVWxZVkVGSFgwWlNMRVpmUWtGZlJreGZUREUyTXpNNWZB&log=6Uo0sKMWJfprY08fuFy5BTIM22OtG18V2X2QAd6TT_cvrESgIIeZou4zdxGpYEuhcMiDEo6hRWQUdyD6f759_MV4ShmMfOO9koS1T6zZjCHEwdF20HS-Yh3U_kOniHwpiRQOaOR8z4wM2NgEk5oJQIjybhZjdCoo8sP2454IuaTivdBf1ieIjwz-asiaABB9GI6ghQuK3JMRhrBKLeDk0strre8G6Abkzi5K3Th0YnwmRyB85Ov9Y-P2U489NrmUh1mR8aV1pSV2DIRQMX00I7S5IfkLsdlokmtVdiIKD14dAmFg5ItK-mj6jYDL5kyGCdPTuDIydNhQT22yF8TYfdAgxqD8_PopxPS2gpfP5uhwU5X01NgoWPgWwJVS-oUILUnMrbC0j7SD6BKvFp8XN3EHQnkCLu2Zuv9PrQBuIBJswsjoZdWqNpPTpItQDtaapDN6gUNsbMa6sA0jHp_FrhLypDy7KAn-afcSXLwp6Cq2hDoZBRMaE6xVlf2SPxVfksiu2TT9GEml4IFDVDNEm0SbBNWbqBEt4t3EGV1XhkDkPbyboejFh_mqAfMO6u0WgW264ziCkAUCv9sl_EYBNAakBKQvELol1fOQG8NbQ8hw2S1sI0R_Q4hU0l2aJuXh0sIHG8jdCETZvbMvbfVOOc86_1Fz302wuDEcZfDp2sVzG7BShqgh893c1mUavMqKhxU1c4fMxmRwa6IRh5zZuHELGnacqq_YhXCicDkq5Hqjun5Xu66TP_MQQQ6eLs0vX2sUgtqTlBdoTc-80HqaWjomhSkkfa3aFLdSxCaUEiIxxc_nJvPB7Wt5bALh7gmvJV7waO9j0ObwZVsp_ACgK7MHw83nUQnXWo119AxHK4bcqH8PxT84Pzl5NvPTo1hk_dr7B7C3NeIae_rH3Q5sK9Q_onkKXMJE2JSjZGdmLppCzpCywX7bEJ4lXmf6ABNo-7E7Ob-fBytcB_otiApQVc0j91NsIBfy5eiGbm7CxO-4A8YRKcFunSoECP09AXabuDprPjI-Bg7HpGagxOcQMGJE2tnu1FLFCM_xejbQKcPcGw8Ud-llIa1hylqPqlOPx3D6AN1rHU8-JjOwdKhCnAYOdhqMN50R46VBQkD1EYX9ddIrFA8oYZQDJUvgie4vCvg528WF6W237R1tjt7xlDpyx15b0Y3Ks_TSYbbJ0sTmQypZ__Agr9dYmR3wRAcxpQ4oL5ZdWyNZNAANmo1e1r1DxSsA46ScURbJ6RCZeLs&v=404","clog":"\/\/im-x.jd.com\/dsp\/np?log=6Uo0sKMWJfprY08fuFy5BTIM22OtG18V2X2QAd6TT_cvrESgIIeZou4zdxGpYEuhcMiDEo6hRWQUdyD6f759_MV4ShmMfOO9koS1T6zZjCHEwdF20HS-Yh3U_kOniHwpiRQOaOR8z4wM2NgEk5oJQIjybhZjdCoo8sP2454IuaS_MYaClv52ldokpkrTmN7iVOuUrZWjeVzO7HUoD32eExo3y_tBsA8gV-Bq9j6YSr7MiGVnu2hJCRwYHa4lttIxwlt40FY8NXRu7xXUxbUeNnEwdeE3Ikj7_GwBn0vTDx75MMCbk3yWLnSO1wiOOtIqqQJ9thWfSchcC9_UhQf_PkvE03NU-LCDCdoCz9eMPNqquU3S04nu7ABa8SWNBwkHq_-BaXfJIk0qyuEE8Lr4rU2kDsqOEBq0rZh0kBszxTwMI4fuBcpT8GXlbh4h3lZ9spZKjUEjmO4QXPRoFpr7JxwWinntUY08ViAMZEbTBXJR7JutDtnk9mjpB2JfuVMXRGMMgNAIFOfagTjUToZokFyCmkVSokVTmFcUNpFARu9DkBlZzlUBKUSxnTUQwNr5MyuYmmsN4EqKPUV_wcizjAVLXbEn8Jj8rzTjGR1Jz8AmkR3wHtNRyqoip-s4Ke_gCWcA8kxvrS37YHKrcn9DiqbV29JenQAjW6wXA2Jv17SXcU3CJION6BgZMIE3zbvtVU-3gY4582bKgG8AItz6zF_xB7SSHUnlJHFOfd1jagC3BzjGB8My4mkg1H2yo5F-rochWYcKKVFTqubNj1D0kpESJThBD7Kb00_DONN35VfOUVZB0JjQvC9FAy-FNbKyxeueosk013sIVQym5999srjHX8uiGDQu17k24I7F4xK9QfkjtlqpWKOXG84x9Vyae0Z2I5-nCxHQaVSqRUGGw_K6oyShuU9bWj-7tbI3PVftx6_JHRFdKC95vW1lzD7aw7EEJXqfYYR16JQekiY9lPMPsr0O1iB1Mib8tukMDzngQNyAcKxoMpdgWSQlIkz84ucZCxU0yFJIVBOAje7rNKfDFWKgRZ3fETMa9X_pmj2JhI4gGMinjVuEcFAy9ANmjXs-rxvsID_8FB2UKoKhvA6sVaQJmW1r_UHTG9neiWCHu1ElHomyYCjPpGhYR0pN_W-KN1GcAhV4elJLkZP73f78cUy_Hawwy-CXi0V7HXz7Sei-BDak0erkfEsOGwmS1o6bjcl6GOYwfOQxeDf_nqPIvhHP4gGskQyAMn9uR9M&v=404&seq=1","type":"ad"}]},{"recommend":[{"alt":"","position":10,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/145833\/33\/17892\/73340\/5fd1f9d8E7ec88331\/4caf9bb9de747f80.jpg","href":"\/\/pro.jd.com\/mall\/active\/37p81TGQS7wcEaHNjA1C1WokKPeT\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"U6gP9cS8gV5xMdJYrWgQ\/Q==","mcinfo":"03294000-13573946-8801420756-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/37p81TGQS7wcEaHNjA1C1WokKPeT\/frist.html","desc":"","text":""},"type":"ace"},{"alt":"","position":11,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/152823\/26\/12012\/68654\/5fe97bc9E430fb6b1\/3f7f6bcef1350531.jpg","href":"\/\/pro.jd.com\/mall\/active\/2i8TdgieNtGwuDqV2yHPSFqRr29t\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"bkSlXW4t4\/oh7WXA5Q6F0w==","mcinfo":"03294000-13573946-8801423369-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/2i8TdgieNtGwuDqV2yHPSFqRr29t\/frist.html","desc":"","text":""},"type":"ace"},{"alt":"","position":12,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/152492\/21\/12040\/52119\/5fe93622E8bc3302f\/67857d409c58d0f9.jpg","href":"\/\/pro.jd.com\/mall\/active\/4AfQf3FkPRGHhtqqKh9tsWyV97sy\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"TteIvHssJv+j1USc28Th3w==","mcinfo":"03294000-13573946-8801423368-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/4AfQf3FkPRGHhtqqKh9tsWyV97sy\/frist.html","desc":"","text":""},"type":"ace"}],"banner":[{"src":"\/\/imgcps.jd.com\/ling\/100003909373\/5a6P56KB5pqX5b2x6aqR5aOr5aiB\/Nuacn-WFjeaBryDmmZLljZXmnInnpLw\/p-5bd8253082acdd181d02fa22\/d4150b6d.jpg","href":"\/\/pro.jd.com\/mall\/active\/qvR5WfiLRi2e9eUKdHCv9eP7Pht\/frist.html?innerAnchor=100003909373","type":"delivery","ext_columns":{"link":"\/\/pro.jd.com\/mall\/active\/qvR5WfiLRi2e9eUKdHCv9eP7Pht\/frist.html?innerAnchor=100003909373","sku":"100003909373","playImpr":"1#13#300002-4___","mcinfo":"null","focustype":"t","biclk":"1#13#acthot-B0036314-0-100003909373-acthot-0#88","desc":"6\u671f\u514d\u606f \u6652\u5355\u6709\u793c","text":"\u5b8f\u7881\u6697\u5f71\u9a91\u58eb\u5a01#100003909373"}}]},{"recommend":[{"alt":"OPPO\u5dc5\u5cf024\u5c0f\u65f6","position":13,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/155218\/21\/11512\/71383\/5fe5532cE2e68cd5a\/d6a736a88863c103.jpg","href":"\/\/pro.jd.com\/mall\/active\/2kr2j6fCYET7LtjRww5vB9DJNfwV\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"w\/Oz53F4tqc=","mcinfo":"03294000-13573946-8801422620-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/2kr2j6fCYET7LtjRww5vB9DJNfwV\/frist.html","desc":"12\u671f\u767d\u6761\u514d\u606f","text":"OPPO\u5dc5\u5cf024\u5c0f\u65f6"},"type":"ace"},{"alt":"\u7f8e\u5986\u7cbe\u9009\u8bd5\u7528","position":14,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/144331\/15\/16230\/75371\/5fc4e20cEce63f6cb\/0148abea8250fc3b.jpg","href":"\/\/pro.jd.com\/mall\/active\/4W2AmqrXWJDtT4t5v5P6Wxe1WTec\/frist.html?babelChannel=pcjinrituijian","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"2CeAlBiVB6aN5qElSwcuOg==","mcinfo":"03294000-13573946-8801420753-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/4W2AmqrXWJDtT4t5v5P6Wxe1WTec\/frist.html?babelChannel=pcjinrituijian","desc":"","text":"\u7f8e\u5986\u7cbe\u9009\u8bd5\u7528"},"type":"ace"},{"alt":"","position":15,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/151220\/8\/11617\/61079\/5fdff6baE0a6f9504\/2dbfdebc8fd79483.jpg","href":"\/\/pro.jd.com\/mall\/active\/myvknjmTQuCsW7kjrnPRLPufSNu\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"bokuLSNDGKYkus93uySCgA==","mcinfo":"03294000-13573946-8801421457-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/myvknjmTQuCsW7kjrnPRLPufSNu\/frist.html","desc":"","text":""},"type":"ace"}],"banner":[{"sourceTag":"0","ext_columns":{"desc":"0:cpc","focustype":"g"},"src":"\/\/imgcps.jd.com\/img-cubic\/creative_server_cia\/v2\/2000368\/701382\/FocusFullshop\/CkNqZnMvdDEvMTQ1MjI1LzM4LzI4MDI1LzcwNzc4LzYyZDcwNmRhRWUzOTdmYzgyLzgyZjRmNDBkMTY1OWFiNTIucG5nEgk1LXR5XzBfNTYwAjjwi3pCEwoP5aaZ5rSB5Z6D5Zy-6KKLEAFCEwoP5L2g5YC85b6X5oul5pyJEAJCEAoM56uL5Y2z5oqi6LStEAZCCgoG57K-6YCJEAdYxucq\/cr\/s\/q.jpg","href":"\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9scHMuamQuY29tL3BjL3BzcC83MDEzODI_aW11cD1DZ1lLQUJJQUdBQVNGZ2pHNXlvUTI5ZnIzQU1hQkhSd2MzY2drNjRCS0FFWXNSc2dBQ29tYldsNGRHRm5YMmtzZFdZc2VHZGhMR2RwWVN4amFXTXNabDlpWVY5bWJGOXNNVFl6TXpJeUNHMXBlSFJoWjE5cFN0b0JTWHhOU1ZoVVFVZGZTVklzU1Y5QlgwWk1YMUlzU1Y5QlgxSkZYMHhETEVsZlFWOVFURjlTTEVsZlFWOVRURjlTTEVsZlFWOURVMTlTTEVsZlFWOVNVMTlTTEVsZlZWOUdURjlNUXl4SlgxTmZSa3hmVEVNc1NWOVNYMFpNWDFJc1NWOVFYMFpNWDB3eU1UYzBPQ3hKWDFCZlRsQk1YMUlzU1Y5SFgxaEhYMHhETEVsZlIxOVNURjlTTEVsZlFsOUdURjlTTEZOZVNWNWFYa0ZmVGs1ZlJsVmZVaXhIU1VFc1dFZENMRlZEZkVjcVNWOVZYMFpNWDB3eU1UTXdNanRHZkUxSldGUkJSMTlHVWl4R1gwSkJYMFpNWDB3eE5qTXpPWHc&log=TGIp2IDHTqoHmM4V77x_GTcT3olzF3XafEGxUEB4nTtYv9DGDoW5_lgLk5E4wZOtJNVzDqX31g5uZtz3_a4ppC4ol8aSGQxTYqayWpp7jWlcl_BIsyjHgbuECkWY9CrpAUUQVJiAL3-rQ0fRBgMdnutDxxiZ24MLjifaxyaR69l_1Y3uElR3bwM_0nwur2hhuLOOj23e-OYGzzUjmWproSr_cMOVF5WoFBTY1mBIaXG5GlW3zvxSjzkx93t3zbpgRdTMt3Lau0jJy-3Y9u7cf4LPFKcRcQFGyFYuuU4trmjjjPjkxiGndevGWku2wFQh8VHI6G6YaPWnZ6_2eBTPo8zsJ94tZT5f267tx1BQZMygQwr4rCBj3qgbhr5ZjovgZI45VYaQLeX1X8Frx6GeycWxAKScvfJ2-f9DwvKe-SLT_tsfQ_ZHJXBBatuI2jkM2y2K6nwDaWAvFJ0KGwlb9HOSpeVQXrSo8TovB5Kjj3FhjijgonQE3CAowZ63sRxKhaB7LbviRNA7jzbHvhIUvQmQ1Dbgqd81RxSo9Oks0tQGXiRNah2SONPTtuae12vISCjyO1fppp-f4DB_EmuYHUa9TwbKoqnWNvb_W1e-oBrc8n6bpe2B_TyJwKbrP9nj_JTb1ZwAaYf3JE26gM8JDBq0M-cfOl11esuAcsXagRzKhVsD5Zut13vk8AfgLh1H32YYSrPvDi9OD4AxPGg0LYrmjLk9_BcpA96miU7KA6GpLEQrY_ABuyUq6_R5jhtPeu0OKYWQL7u9VdJmkH--V0TdMTB6tN0t1JzKB8R66iOz8N7Jnts1bV-BaiJg27zEIs3f4GdpAAZUAR0NLry5qAwmDIyq9PPkq_QCmSwi5PAgspeW18_Mty9H5A6-Zt1sCAIWkze2mrdHtOoMK1_QL7rpZzHAEVV6VI5tQm3Cfh8uhrCMy-k-pe9Y_LgdrUSMnWlsngx9YTbfiG4laAIEGhhCRAik0L-F3B8SLNH6vR_tzbb6N9qjpk5vac3OqsHUiY4WhWwj2JBo_GIQgv4ey3U5sPXx3s0cTIA_4FQ_i7Ob9a9schjHtLESXEqrJRGA873DQcHckfC-NbTp3NC-fd9YSER5yhI5lCPkgKSKmxQeu1NdilUyXFtvFTI8Arw-&v=404","clog":"\/\/im-x.jd.com\/dsp\/np?log=TGIp2IDHTqoHmM4V77x_GTcT3olzF3XafEGxUEB4nTtYv9DGDoW5_lgLk5E4wZOtJNVzDqX31g5uZtz3_a4ppC4ol8aSGQxTYqayWpp7jWlcl_BIsyjHgbuECkWY9CrpAUUQVJiAL3-rQ0fRBgMdnutDxxiZ24MLjifaxyaR69kvjxxDNrRNhrSVMKzEvChlsahQsN4iUBEl5ypa2QEk12VKCAhJbd8I-v_Ls6miJCK3jfmRCTM5ZPIYOYTuW5E4iXSverfsxLpWNTDZhSjKWHcjB9xD7suaA70NuDL34DRBTXKFw2U6cPtNp0xVHwvD2Aa_gshgZ3Cek2O1ZIfycoe7Ql-hZRGFHLhBj35CAJoGmv_MHazkbhRWH12ICYM_r4mzr2EAEvnSJMwdqV-4q_ovR4dxaVRpVkZU0PzWIAZ4GmpGcS8Hcxc9QIdEisVHNndkymjrt_7kiJpNQTxwRcZy0f_37yuNeTU6WLG71iBvk1HN249CzVdSDMM925sAr8IXJ0boaOO6Esh0zPtMBnBfBRYuUk28Knm3va3pjH7VHrxftlNsahUsO5D9Kq7BNvln390Etu_M6EvVmsNB7HLth7LscxzJtC0tTQiRyQWMfZq4uAW0dy_Nc_5xXnTfLBeaGL8NwgevtW3JgFMdLvF0G6waVeh_R6Be2ib6RO-ccXfkL0f1KmvnnReG_VyRy-zIJwkFHMP6rMNwwWZTr-YSjAIgJgcOTji9ROlNcaJZ9PGwie7spnwpGn2OQ4ZNnqxGcLAZDLcYDFx-mJuNs_5xjgAOAh2f8T6RhIxKHhxw9I4WhCipIw65gXmc2euDkaTS0ie3FUQfcpjx75Wi2kLrm0knuX7EdHfCh0PhgPIfZu1a8fRvfwh71sqGH_rUPdsjvy2mAikhmIZN-Uf4GcCmDB29goIiSnBZIBXUU1vo13IkPhc6hRzbePk0HuKY_miXf8qIUKKBZ0syeAlaK4ooTt8c7QeI5SPUUjdeii4O35ATvo7dzdygM_Dn1JbZiBDjTX5paCJqlNkbLKChD9GGDlYNrh4TEZs3OBeO1iGxLGL6pskAcUekiaZrKHosjEjWufQZwD9cW_zdqQ5ACloT_WO8c9oXZebXuETOUOMwLfIe2lUx1SgewrXEEutp5DStvXessADMRAs6CJfFrA&v=404&seq=1","type":"ad"}]},{"recommend":[{"alt":"\u8fbe\u80fd\u8de8\u5883\u5976\u7c89","position":16,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/142076\/21\/16719\/81798\/5fc755a4E765768a0\/3e35cebd45e72fcf.jpg","href":"\/\/pro.jd.com\/mall\/active\/34G4aLZqete3T2VDrQfwa4z5hdAm\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"QGSzAaCfP34=","mcinfo":"03294000-13573946-8801423371-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/34G4aLZqete3T2VDrQfwa4z5hdAm\/frist.html","desc":"\u65b0\u5ba2\u5165\u4f1a\u7acb\u51cf40","text":"\u8fbe\u80fd\u8de8\u5883\u5976\u7c89"},"type":"ace"},{"alt":"","position":17,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/159465\/15\/15\/54794\/5fe97b93Edc6d2106\/705acb97ee03fa41.jpg","href":"\/\/pro.jd.com\/mall\/active\/SyNEMyANkXQuUmzn5dUef8CQGPA\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"bkSlXW4t4\/oh7WXA5Q6F0w==","mcinfo":"03294000-13573946-8801423370-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/SyNEMyANkXQuUmzn5dUef8CQGPA\/frist.html","desc":"","text":""},"type":"ace"},{"alt":"","position":18,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/143220\/17\/17461\/57750\/5fcd86f8Ef9a8199c\/0f3a18493a9f64ed.jpg","href":"\/\/pro.jd.com\/mall\/active\/3fNa4gg4udob1juiWbWWBp9z9PBs\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"8E9EFljRna9sk5iyH5TJyQ==","mcinfo":"03294000-13573946-8801422413-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/3fNa4gg4udob1juiWbWWBp9z9PBs\/frist.html","desc":"","text":""},"type":"ace"}],"banner":[{"sourceTag":"0","ext_columns":{"desc":"1:cpm","focustype":"h"},"src":"\/\/img1.360buyimg.com\/pop\/jfs\/t1\/67208\/4\/21074\/87040\/62e09ebdE19f9d307\/ce00b54d607416a2.jpg","href":"\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9wcm8uamQuY29tL21hbGwvYWN0aXZlLzRKdzVnUnVUS3pOc2RKZlZxTHZyaG1LNWpIQkEvaW5kZXguaHRtbA&log=zurm1T5gNMWpFd-44N3u5M77sRyyco1JsEHBNclss6UwLAHSKZTC00QUa1j9q3ee_cHwYj_pXtQ8jgR35kqUd67xgRxQvxBzCGl03ZqfjJlrs0XMEbluM24WhEgzTUeK9TDV0trONqu2KlkQtAOHsk5_Q5ky8X0Kyi_gK2qggwdO1c83mn9QyPDSOk5wm5Vm0zGTNBfwDnJhIKhRBF9vzf7SMIdKsaqbcIiwWGmUCQFClCMXbVazAEI6ijvWPHSdaa_Rx2EBc20PiHAzhISp3C68XrQPjpOQF-h509YupqG3PXEMWEBak4KsxhPJ9wIcqt8k3_NsiXBU9QMqrVeCY1D6Yv2M9DyzbhE945VbdWvkaCW1C5HD5cOMlDocBr5mp7yqRSeNmlpTVCL46SwNp9uFV5aqRGNH7538akWZHxRP2zSqYG0mtgC4VaNEZ6-tVaFZL_KJsL9vNvLFgzZfseh0A1vlVqlcARs1Ep6Y7hiXYaGHDf0w0vtphEkPlU05HSKpHSMgM236PXS5k-XgBItHQgchRfyWLJuFupb_FsFqbloifoLxr-eoy3oqkotxMZcknQNdJJ9ALZTwb4z-65zaFIbGQrfr_CoPCOHzOMYrKW46YXQls4tgiIXR8Pmek81HrvslaDhUeOfOGOrNBIW5kkqAQ0-eNLc_mBSXPyheoxHD_NVkAafxgo9lgXRwVTx3vS63HMahsgtYH5Os5lF-JOifUex2pwLJynwZhsbUC0EGcyGk7_rFe0QRUrEdT9EE-HgWMCaOzd8-c5bkzw20a9c1zayWDFzzlj1mBTLY3rPTC9-y7w2Q59LdVFgUuK21V0upPo3-pi6e4YIwF-bNhpsoch-T8j_eDHTDtg-VMOFO-WcFPIRmtrBXgjT6rceZjZX6_eGgJR0IH5FPtauPlG6KQmBzH5ckXIq7di9rC5Fr3kgjOkRYzB6JmVQil3US4_Xx071vLU8q-4ay_JrliiCtTuJOephcvNKce0ZL8HZn_zUBK972G7yoLn2frhc2nscNyXcarsHuGfMhIU8zQwCN2Gv2VhNcEzpsvuc&v=404","clog":"\/\/im-x.jd.com\/dsp\/np?log=zurm1T5gNMWpFd-44N3u5M77sRyyco1JsEHBNclss6UwLAHSKZTC00QUa1j9q3ee_cHwYj_pXtQ8jgR35kqUd67xgRxQvxBzCGl03ZqfjJlrs0XMEbluM24WhEgzTUeK9TDV0trONqu2KlkQtAOHsk5_Q5ky8X0Kyi_gK2qggwdO1c83mn9QyPDSOk5wm5Vmy-tFMKi3L2GiizMl3ZcP6lHItyyelsy__ChNDliXomSvwKVLQF6jOOIfqGEr8sFp9-3ZlI_XC1gAAXwO8G1fV38Zl3Ej2cKEpd-bCfcCZ4p3lKUnyRwnLreQZdIsa__HmwcOXsojTfvzGQnbP5H0OpSnom77TJTcPz8lNbPZ3Ij2AECsfABQ3ptAmpJUrVzYn8_eouwEAY7eGA3GyjreLVdJvL8O2etvczjAU6UN8W79OtQEhOrYyCYQlwubXVld_Zuw19erVEtX_0NuJXYLTlVtuXTivJQ_MDF8rHbzZ3HMH7H3KYpz5dxAsjiAJHICFht95iBk2GXnmYoq0-Z9uZtWWA0u47kJptrQrcbiiIoxPt4LLy9iGF1YWEN9v71wvVn6jDXOdnq6z69NrHTr2mqEszU0Ck8iDNZ9qksORTE6vHEaAYfWxpLkteqFSNHPXzwRApffMCtVunMTMlJW_zf0YP28VUyKg20PbK-jF-TITrhtmWhK3aYm8HnjQJUgUv8ZEWb8wlWufZ693S1RjnibFktFtStIO393JHM9A0obR31BnoqikY3l6GUDwn5vunHQXyFIZbmfE17peWRD-i8N4dAQTKgmkh3_sd60NUqr5oGSYlpayYuTG0T5YqoOKvSxE4YwDrXAwPfZW5b6P5xhmcHciP4xCdz1HGg82XvAFL1DSLrGaTAqp2Y2LZ9GzfCKtj9grt31Kaf_ISLoDaYv0NFGTU71GHSqbtXLcUAg5R0vHhHRWmeXbjANLE4Qxl3_VYHbRRySTcR1lWq_67wW48SVh2T0OcRwc7J2eI8ipc_Oq3Bsz-tWmscYeCpvifAVjcYfgZ_6JQKKTkW_YLsQpOvj2nodfhXi-eZqeJg&v=404&seq=1","type":"ad"}]},{"recommend":[{"alt":"","position":19,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/154590\/23\/10967\/74195\/5fe2df62E45a142d9\/883e4bda6f5cd278.jpg","href":"\/\/pro.jd.com\/mall\/active\/29aweHKvVWPaPXgJMbtiLsHk9pFR\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"RAv3J0fJGDZCyu6kQERnLQ==","mcinfo":"03294000-13573946-8801422593-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/29aweHKvVWPaPXgJMbtiLsHk9pFR\/frist.html","desc":"","text":""},"type":"ace"},{"alt":"","position":20,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/158239\/17\/80\/59624\/5fe980daEc6af0098\/0b6bcc0f5587720c.jpg","href":"\/\/pro.jd.com\/mall\/active\/31e4RpwAWH66gXmn7UdN9dMGVY7F\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"oWH9E4RbFQwBBlITEyBAiQ==","mcinfo":"03294000-13573946-8801423361-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/31e4RpwAWH66gXmn7UdN9dMGVY7F\/frist.html","desc":"","text":""},"type":"ace"},{"alt":"","position":21,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/139567\/10\/19800\/44582\/5fe46a35E7004831c\/9721fda27a9495ca.jpg","href":"\/\/pro.jd.com\/mall\/active\/2g9n7V52rEtSdKDkPHKMCURGR9aD\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"vTzmnuWTYC1fchOIQe8O+w==","mcinfo":"03294000-13573946-8801422592-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/2g9n7V52rEtSdKDkPHKMCURGR9aD\/frist.html","desc":"","text":""},"type":"ace"}],"banner":[{"src":"\/\/imgcps.jd.com\/ling\/7776792\/5Lyg57uf5bCP6aOf\/6Zu26aOf57OV54K5\/p-5bd8253082acdd181d02fa02\/71ccf55f.jpg","href":"\/\/pro.jd.com\/mall\/active\/2zMKHHhui8H95uEg63v5aSVFLsZ1\/frist.html?innerAnchor=7776792","type":"delivery","ext_columns":{"link":"\/\/pro.jd.com\/mall\/active\/2zMKHHhui8H95uEg63v5aSVFLsZ1\/frist.html?innerAnchor=7776792","sku":"7776792","playImpr":"1#13#300002-4___","mcinfo":"null","focustype":"t","biclk":"1#13#acthot-B0036759-0-7776792-acthot-1#88","desc":"\u96f6\u98df\u7cd5\u70b9","text":"\u4f20\u7edf\u5c0f\u98df#7776792"}}]},{"recommend":[{"alt":"","position":22,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/146800\/33\/20186\/78685\/5fe5c755Ec3a48986\/df7e8df0dd87913d.jpg","href":"\/\/pro.jd.com\/mall\/active\/HkuJmKguhv6jGeEXdrKPR4ygyje\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"0B9WUXoekna8pOynkQjB1g==","mcinfo":"03294000-13573946-8801423360-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/HkuJmKguhv6jGeEXdrKPR4ygyje\/frist.html","desc":"","text":""},"type":"ace"},{"alt":"","position":23,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/140042\/21\/20481\/60091\/5fe7f503Eea69fdd7\/b4b2147f196a9001.jpg!q95","href":"\/\/pro.jd.com\/mall\/active\/3s4A3dfrTy9K6FTXZWd1U67xJ9VR\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"Wbj96fOBwO5Cyu6kQERnLQ==","mcinfo":"03294000-13573946-8801423363-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/3s4A3dfrTy9K6FTXZWd1U67xJ9VR\/frist.html","desc":"","text":""},"type":"ace"},{"alt":"","position":24,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/154709\/15\/12170\/50231\/5fe9a329E1e52a010\/370be07713e5124c.jpg","href":"\/\/pro.jd.com\/mall\/active\/Y7UJeC8KnEb2y5YufTiDrF2zL7J\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"xdy8JnbW2ywFhKBalJKxfA==","mcinfo":"03294000-13573946-8801423362-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/Y7UJeC8KnEb2y5YufTiDrF2zL7J\/frist.html","desc":"","text":""},"type":"ace"}],"banner":[{"src":"\/\/imgcps.jd.com\/ling\/3486678\/6L-Q5Yqo5YGl6Lqr5oyH5Y2X\/6JCl5YW76L-b6Zi256-H\/p-5bd8253082acdd181d02fa5f\/f2af4529.jpg","href":"\/\/pro.jd.com\/mall\/active\/2DPCwovvaBUa7HciiQ2PHCvyECac\/frist.html?innerAnchor=3486678","type":"delivery","ext_columns":{"link":"\/\/pro.jd.com\/mall\/active\/2DPCwovvaBUa7HciiQ2PHCvyECac\/frist.html?innerAnchor=3486678","sku":"3486678","playImpr":"1#13#300002-4___","mcinfo":"null","focustype":"t","biclk":"1#13#acthot-B0007061-0-3486678-acthot-2#88","desc":"\u8425\u517b\u8fdb\u9636\u7bc7","text":"\u8fd0\u52a8\u5065\u8eab\u6307\u5357#3486678"}}]}];        //618大促上报降级配置
        window.pageConfig.handleReportStart=new Date('2020/11/10 22:00:00').getTime();

		window.pageConfig.handleReportEnd=new Date('2020/11/12 10:00:00').getTime();

		    </script>

    <script type="text/javascript">
        !function(e){pageConfig.isWide=function(){var n=e,i=document,o=i.documentElement,t=i.getElementsByTagName("body")[0],a=n.innerWidth||o.clientWidth||t.clientWidth;return a>=1370}();var n=[];pageConfig.isWide?(n.push("root61"),n.push("o2_wide")):n.push("o2_mini");var i=document.getElementsByTagName("html")[0];i.className=n.join(" ")}(window,void 0);
    </script>

    <script type="text/javascript">
        !function (n) {
            function o(n) {
                for (var o = n + "=", t = document.cookie.split(";"), e = 0; e < t.length; e++) {
                    for (var i = t[e]; " " == i.charAt(0);) i = i.substring(1, i.length);
                    if (0 == i.indexOf(o)) return i.substring(o.length, i.length)
                }
                return null
            }

            var t = o("pcm"), e = n.navigator.userAgent.toLocaleLowerCase(), i = "//m.jd.com",
                r = /iphone|android|symbianos|windows\sphone/g, c = /micromessenger|qq\/[\d.]+/i;
            return c.test(e) ? (n.location.href = "//wqs.jd.com/?from=jdindex", !1) : r.test(e) && "1" != t ? (n.location.href = i, !1) : void 0
        }(window);
    </script>

    <script type="text/javascript">
        window.search = function (a) {
            var b, c = "//search.jd.com/Search?keyword={keyword}&enc={enc}{additional}";
            var d = search.additinal || "";
            var e = document.getElementById(a);
            var f = e.value;
            if (f = f.replace(/^\s*(.*?)\s*$/, "$1"), f.length > 100 && (f = f.substring(0, 100)), "" == f) return void (window.location.href = window.location.href);
            var g = 0;
            "undefined" != typeof window.pageConfig && "undefined" != typeof window.pageConfig.searchType && (g = window.pageConfig.searchType);
            var h = "&cid{level}={cid}";
            var i = "string" == typeof search.cid ? search.cid : "";
            var j = "string" == typeof search.cLevel ? search.cLevel : "";
            var k = "string" == typeof search.ev_val ? search.ev_val : "";
            switch (g) {
                case 0:
                    break;
                case 1:
                    j = "-1", d += "&book=y";
                    break;
                case 2:
                    j = "-1", d += "&mvd=music";
                    break;
                case 3:
                    j = "-1", d += "&mvd=movie";
                    break;
                case 4:
                    j = "-1", d += "&mvd=education";
                    break;
                case 5:
                    var l = "&other_filters=%3Bcid1%2CL{cid1}M{cid1}[cid2]";
                    switch (j) {
                        case "51":
                            h = l.replace(/\[cid2]/, ""), h = h.replace(/\{cid1}/g, "5272");
                            break;
                        case "52":
                            h = l.replace(/\{cid1}/g, "5272"), h = h.replace(/\[cid2]/, "%3Bcid2%2CL{cid}M{cid}");
                            break;
                        case "61":
                            h = l.replace(/\[cid2]/, ""), h = h.replace(/\{cid1}/g, "5273");
                            break;
                        case "62":
                            h = l.replace(/\{cid1}/g, "5273"), h = h.replace(/\[cid2]/, "%3Bcid2%2CL{cid}M{cid}");
                            break;
                        case "71":
                            h = l.replace(/\[cid2]/, ""), h = h.replace(/\{cid1}/g, "5274");
                            break;
                        case "72":
                            h = l.replace(/\{cid1}/g, "5274"), h = h.replace(/\[cid2]/, "%3Bcid2%2CL{cid}M{cid}");
                            break;
                        case "81":
                            h = l.replace(/\[cid2]/, ""), h = h.replace(/\{cid1}/g, "5275");
                            break;
                        case "82":
                            h = l.replace(/\{cid1}/g, "5275"), h = h.replace(/\[cid2]/, "%3Bcid2%2CL{cid}M{cid}")
                    }
                    c = "//search-e.jd.com/searchDigitalBook?ajaxSearch=0&enc=utf-8&key={keyword}&page=1{additional}";
                    break;
                case 6:
                    j = "-1", c = "//music.jd.com/8_0_desc_0_0_1_15.html?key={keyword}";
                    break;
                case 7:
                    c = "//s-e.jd.com/Search?key={keyword}&enc=utf-8";
                    break;
                case 8:
                    c = "//search.jd.hk/Search?keyword={keyword}&enc=utf-8";
                    break;
                case 9:
                    d += "&market=1"
            }
            if ("string" == typeof i && "" != i && "string" == typeof j) {
                var m = /^(?:[1-8])?([1-3])$/;
                j = "-1" == j ? "" : m.test(j) ? RegExp.$1 : "";
                var n = h.replace(/\{level}/, j);
                n = n.replace(/\{cid}/g, i), d += n
            }
            if ("string" == typeof k && "" != k && (d += "&ev=" + k), f = encodeURIComponent(f), b = c.replace(/\{keyword}/, f), b = b.replace(/\{enc}/, "utf-8"), b = b.replace(/\{additional}/, d), "object" == typeof $o && ("string" == typeof $o.lastKeyword && (b += "&wq=" + encodeURIComponent($o.lastKeyword)), "string" == typeof $o.pvid && (b += "&pvid=" + $o.pvid)), b.indexOf("/search.jd.com/") > 0) try {
                JA.tracker.ngloader("search.000009", {key: f, posid: a, target: b})
            } catch (o) {
            }
            ("undefined" == typeof search.isSubmitted || 0 == search.isSubmitted) && (setTimeout(function () {
                window.location.href = b
            }, 50), search.isSubmitted = !0)
        };
    </script>


</head>

<body class="index">
<div class="mod_container">
    <!--无障碍占位-->
    <div id="J_accessibility"></div>
    <!--顶通占位 -->
    <div id="J_promotional-top">
    </div>
    <div id="shortcut">
        <div class="w">
            <ul class="fl" clstag="h|keycount|head|topbar_01">
                <li class="dropdown" id="ttbar-mycity"></li>
            </ul>

            <ul class="fr">
                <li class="fore1 dropdown" id="ttbar-login" clstag="h|keycount|head|topbar_02">
					<a href="//passport.jd.com/uc/login?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F" class="link-login">你好，请登录</a>&nbsp;&nbsp;<a
					href="//reg.jd.com/reg/person?ReturnUrl=https%3A//www.jd.com/" class="link-regist style-red">免费注册</a>
                </li>
                <li class="spacer"></li>
                <li class="fore2" clstag="h|keycount|head|topbar_03">
                    <div class="dt"><a target="_blank" href="//order.jd.com/center/list.action">我的订单</a></div>
                </li>
                <li class="spacer"></li>
                <li class="fore3 dropdown" id="ttbar-myjd" clstag="h|keycount|head|topbar_04">
                    <div class="dt cw-icon"><a target="_blank" href="//home.jd.com/">我的京东</a><i class="iconfont">&#xe610;</i><i
                            class="ci-right"><s>◇</s></i></div>
                    <div class="dd dropdown-layer"></div>
                </li>
                <li class="spacer"></li>
                <li class="fore4" clstag="h|keycount|head|topbar_05">
                    <div class="dt"><a target="_blank" href="//vip.jd.com/">京东会员</a></div>
                </li>
                <li class="spacer"></li>
                <li class="fore5" clstag="h|keycount|head|topbar_06">
                    <div class="dt"><a target="_blank" href="//b.jd.com/">企业采购</a></div>
                </li>
                <li class="spacer"></li>
                <li class="fore8 dropdown" id="ttbar-serv" clstag="h|keycount|head|topbar_07">
                    <div class="dt cw-icon">客户服务<i class="iconfont">&#xe610;</i><i class="ci-right"><s>◇</s></i></div>
                    <div class="dd dropdown-layer"></div>
                </li>
                <li class="spacer"></li>
                <li class="fore9 dropdown" id="ttbar-navs" clstag="h|keycount|head|topbar_08">
                    <div class="dt cw-icon">网站导航<i class="iconfont">&#xe610;</i><i class="ci-right"><s>◇</s></i></div>
                    <div class="dd dropdown-layer"></div>
                </li>
                <li class="spacer"></li>
                <li class="fore10 mobile" id="J_mobile" clstag="h|keycount|head|topbar_09">
                    <div class="dt mobile_txt">手机京东</div>
                    <div class="mobile_static">
                        <div class="mobile_static_qrcode"></div>
                    </div>
                    <div id='J_mobile_pop' class='mod_loading mobile_pop'>
                    </div>
                </li>
            </ul>
        </div>
    </div>


    <div id="header">
        <div class="w">
            <div id="logo" class="logo">
                <h1 class="logo_tit">
                    <a href="//www.jd.com" class="logo_tit_lk" clstag="h|keycount|head|logo_01">京东</a>
                </h1>
                <h2 class="logo_subtit">京东,多快好省</h2>
                <div class="logo_extend" clstag="h|keycount|head|logo_02"></div>
            </div>

            <div id="search">
                <div class="search-m">
                    <div class="search_logo">
                        <a href="//www.jd.com" class="search_logo_lk" clstag="h|keycount|head|logo_01" tabindex="-1">京东，多快好省</a>
                    </div>

                    <div class="form" role="serachbox">
                        <ul id="shelper" class="search-helper" style="display: none"></ul>
                        <input clstag="h|keycount|head|search_c" type="text"
                               onkeydown="javascript:if(event.keyCode==13) search('key');" autocomplete="off" id="key"
                               accesskey="s"
                               class="text"
                               aria-label="搜索"/>
                        <button clstag="h|keycount|head|search_a" onclick="search('key');return false;" class="button" aria-label="搜索">
                            <i
                                    class="iconfont">&#xe60b;</i></button>
                    </div>

                    <div id="settleup" class="dropdown" clstag="h|keycount|head|cart_null">
                        <div class="cw-icon">
                            <i class="iconfont">&#xe60c;</i>
                            <a target="_blank" href="//cart.jd.com/cart.action">我的购物车</a>
                            <i class="ci-count" id="shopping-amount"></i>
                        </div>
                        <div class="dropdown-layer">
                            <div id="J_cart_pop">
                                <span class="loading"></span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div id="hotwords" clstag="h|keycount|head|search_d" role=""></div>

            <div id="navitems" role="navigation">
                <div class="spacer"></div>
                                                            <ul id="navitems-group1">
                                        <li clstag="h|keycount|head|navi_01" class="fore1">
                                                    <a class="navitems-lk"
                               target="_blank"
                               href="https://miaosha.jd.com/"
                               aria-lable="秒杀">秒杀                                                            </a>
                                            </li>
                                                                            <li clstag="h|keycount|head|navi_02" class="fore2">
                                                    <a class="navitems-lk"
                               target="_blank"
                               href="https://a.jd.com/"
                               aria-lable="优惠券">优惠券                                                            </a>
                                            </li>
                                                                            <li clstag="h|keycount|head|navi_03" class="fore3">
                                                    <a class="navitems-lk"
                               target="_blank"
                               href="https://plus.jd.com/index?flow_system=appicon&flow_entrance=appicon11&flow_channel=pc"
                               aria-lable="PLUS会员">PLUS会员                                                            </a>
                                            </li>
                                                                            <li clstag="h|keycount|head|navi_04" class="fore4">
                                                    <a class="navitems-lk"
                               target="_blank"
                               href="https://red.jd.com/"
                               aria-lable="品牌闪购">品牌闪购                                                            </a>
                                            </li>
                                            </ul>
                        <div class="spacer"></div>
                                                                                <ul id="navitems-group2">
                                        <li clstag="h|keycount|head|navi_05" class="fore5">
                                                    <a class="navitems-lk"
                               target="_blank"
                               href="https://paimai.jd.com/"
                               aria-lable="拍卖">拍卖                                                            </a>
                                            </li>
                                                                            <li clstag="h|keycount|head|navi_06" class="fore6">
                                                    <a class="navitems-lk"
                               target="_blank"
                               href="https://jiadian.jd.com/"
                               aria-lable="京东家电">京东家电                                                            </a>
                                            </li>
                                                                            <li clstag="h|keycount|head|navi_07" class="fore7">
                                                    <a class="navitems-lk"
                               target="_blank"
                               href="https://chaoshi.jd.com/"
                               aria-lable="京东超市">京东超市                                                            </a>
                                            </li>
                                                                            <li clstag="h|keycount|head|navi_08" class="fore8">
                                                    <a class="navitems-lk"
                               target="_blank"
                               href="https://fresh.jd.com/"
                               aria-lable="京东生鲜">京东生鲜                                                            </a>
                                            </li>
                                            </ul>
                        <div class="spacer"></div>
                                                                                <ul id="navitems-group3">
                                        <li clstag="h|keycount|head|navi_09" class="fore9">
                                                    <a class="navitems-lk"
                               target="_blank"
                               href="https://www.jd.hk/"
                               aria-lable="京东国际">京东国际                                                            </a>
                                            </li>
                                                                            <li clstag="h|keycount|head|navi_10" class="fore10">
                                                    <a class="navitems-lk"
                               target="_blank"
                               href="https://www.jdcloud.com/cn/?utm_source=DMT_jdcom&utm_medium=title&utm_campaign=regular&utm_term=NA"
                               aria-lable="京东云">京东云                                                            </a>
                                            </li>
                                            </ul>
                        <div class="spacer"></div>
                                    
            </div>

            <div id="treasure"></div>
        </div>
    </div>
    <div class="fs">
        <div class="grid_c1 fs_inner">
            <div class="fs_col1">
                <div id='J_cate' class="cate J_cate" role="navigation" aria-label="左侧导航">
                    <ul class="JS_navCtn cate_menu">
                                                    <li class="cate_menu_item" data-index="1" clstag="h|keycount|head|category_01a">
                                                                <a target="_blank" class="cate_menu_lk" href="//jiadian.jd.com">家用电器</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="2" clstag="h|keycount|head|category_02a">
                                                                <a target="_blank" class="cate_menu_lk" href="//search.jd.com&#47;Search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;wq=%E6%89%8B%E6%9C%BA&amp;pvid=8858151673f941e9b1a4d2c7214b2b52">手机</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//wt.jd.com">运营商</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//shuma.jd.com&#47;">数码</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="3" clstag="h|keycount|head|category_03a">
                                                                <a target="_blank" class="cate_menu_lk" href="//diannao.jd.com&#47;">电脑</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//bg.jd.com">办公</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="4" clstag="h|keycount|head|category_04a">
                                                                <a target="_blank" class="cate_menu_lk" href="//channel.jd.com&#47;home.html">家居</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//channel.jd.com&#47;furniture.html">家具</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//jzjc.jd.com&#47;">家装</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//channel.jd.com&#47;kitchenware.html">厨具</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="5" clstag="h|keycount|head|category_05a">
                                                                <a target="_blank" class="cate_menu_lk" href="//phat.jd.com&#47;10-603.html">男装</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//phat.jd.com&#47;10-507.html">女装</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//phat.jd.com&#47;10-156.html">童装</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//channel.jd.com&#47;1315-1345.html">内衣</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="6" clstag="h|keycount|head|category_06a">
                                                                <a target="_blank" class="cate_menu_lk" href="//beauty.jd.com&#47;">美妆</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//phat.jd.com&#47;10-816.html">个护清洁</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//channel.jd.com&#47;pet.html">宠物</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="7" clstag="h|keycount|head|category_07a">
                                                                <a target="_blank" class="cate_menu_lk" href="//phat.jd.com&#47;10-184.html">女鞋</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//phat.jd.com&#47;10-183.html">箱包</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//pro.jd.com&#47;mall&#47;active&#47;2BcJPCVVzMEtMUynXkPscCSsx68W&#47;frist.html">钟表</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//channel.jd.com&#47;jewellery.html">珠宝</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="8" clstag="h|keycount|head|category_08a">
                                                                <a target="_blank" class="cate_menu_lk" href="//phat.jd.com&#47;10-185.html">男鞋</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//phat.jd.com&#47;10-109.html">运动</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//phat.jd.com&#47;10-272.html">户外</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="9" clstag="h|keycount|head|category_09a">
                                                                <a target="_blank" class="cate_menu_lk" href="//xinfang.jd.com&#47;">房产</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//car.jd.com&#47;">汽车</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//che.jd.com&#47;">汽车用品</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="10" clstag="h|keycount|head|category_10a">
                                                                <a target="_blank" class="cate_menu_lk" href="//search.jd.com&#47;Search?keyword=%E6%AF%8D%E5%A9%B4&amp;enc=utf-8&amp;wq=%E6%AF%8D%E5%A9%B4&amp;pvid=3e86f063795740d594b1bb1187e02063">母婴</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//toy.jd.com&#47;">玩具乐器</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="11" clstag="h|keycount|head|category_11a">
                                                                <a target="_blank" class="cate_menu_lk" href="//food.jd.com&#47;">食品</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//jiu.jd.com">酒类</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//fresh.jd.com">生鲜</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//prodev.jd.com&#47;mall&#47;active&#47;41YdRWconKueXwVVnLLM6YY4x4wU&#47;frist.html">特产</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="12" clstag="h|keycount|head|category_12a">
                                                                <a target="_blank" class="cate_menu_lk" href="//art.jd.com">艺术</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//channel.jd.com&#47;1672-2599.html">礼品鲜花</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//nong.jd.com">农资绿植</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="13" clstag="h|keycount|head|category_13a">
                                                                <a target="_blank" class="cate_menu_lk" href="//phat.jd.com&#47;10-925.html">医药保健</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//channel.jd.com&#47;9192-9196.html">计生情趣</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="14" clstag="h|keycount|head|category_14a">
                                                                <a target="_blank" class="cate_menu_lk" href="//pro.jd.com&#47;mall&#47;active&#47;3sAaxodHF7kfo3s95cjxo2UZUxu2&#47;frist.html">图书</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//pro.jd.com&#47;mall&#47;active&#47;2TxxbZnqAm7M8tkDpTN3VJNtoSKo&#47;frist.html">文娱</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//education.jd.com">教育</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//e.jd.com&#47;ebook.html">电子书</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="15" clstag="h|keycount|head|category_15a">
                                                                <a target="_blank" class="cate_menu_lk" href="//jipiao.jd.com&#47;">机票</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//hotel.jd.com&#47;">酒店</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//trip.jd.com&#47;">旅游</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//ish.jd.com&#47;">生活</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="16" clstag="h|keycount|head|category_16a">
                                                                <a target="_blank" class="cate_menu_lk" href="//licai.jd.com&#47;">理财</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//pro.jd.com&#47;mall&#47;active&#47;4EYjXQ6xjnM9TgeSjuMRE8ACEk6q&#47;frist.html">众筹</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//baitiao.jd.com">白条</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//pro.jd.com&#47;mall&#47;active&#47;4NuyHPocGdSDUzmSVosXjVwvEGdG&#47;frist.html">保险</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="17" clstag="h|keycount|head|category_17a">
                                                                <a target="_blank" class="cate_menu_lk" href="//anzhuang.jd.com">安装</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//search.jd.com&#47;Search?keyword=维修&amp;enc=utf-8&amp;wq=维修&amp;pvid=eba9b7454da0494c960f074db37be847">维修</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//cleanclean.jd.com">清洗</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//2.jd.com&#47;">二手</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="18" clstag="h|keycount|head|category_18a">
                                                                <a target="_blank" class="cate_menu_lk" href="//mro.jd.com&#47;">工业品</a>
                                                                                                </li>
                                            </ul>
                    <div id="J_popCtn" class="JS_popCtn cate_pop mod_loading" style="display: none;"></div>
                </div>
            </div>

            <div class="fs_col2">
                <div id='J_focus' class="focus">
                    <div class="focus__loading focus__main skeleton-wrapper">
                        <div class="focus-slider">
                        <div class="focus-item__core skeleton-elementDark mod_lazyload"></div>
                        <div class="focus-item__recommend">
                            <div class="recommend-item skeleton-elementDark"></div>
                            <div class="recommend-item skeleton-elementDark"></div>
                            <div class="recommend-item skeleton-elementDark"></div>
                        </div>
                        </div>
                    </div>
                </div>
            </div>

            <div id="J_fs_col3" class="fs_col3">
                <div id='J_user' class="J_user user mod_loading">
                    <div class="user__loading user_inner">
                    <div class="user_avatar">
                        <div class="user_avatar_lk skeleton-element"></div>
                    </div>
                    <div class="user_show skeleton-element">
                        <p></p><p></p>
                    </div>
                    <div class="user_profit_placeholder skeleton-element"></div>
                </div>
                </div>
                <div id='J_news' class="news J_news">
                    <div class="news__loading news2">
                        <div class="news_hd">
                        <div class="news_hd_placeholder skeleton-element"></div>
                        </div>
                        <div class="news_list"><div class="news_item skeleton-element"></div><div class="news_item skeleton-element"></div><div class="news_item skeleton-element"></div><div class="news_item skeleton-element"></div></div>
                    </div>
                </div>
                <div id="J_service" class="service">
                    <div class="service_entry">
                        <ul class="J_tab_head service_list">
                            <li class="service_item service_frame mod_tab_head_item">
                                <a href="//chongzhi.jd.com/" class="service_lk"
                                   target="_blank" clstag="h|keycount|head|shortcut_01" aria-label="话费">
                                                                                                                                                    <i class="service_ico service_ico_huafei">
                                        <img class="service_ico_img"
                                             src="//m.360buyimg.com/babel/jfs/t1/30057/19/14881/720/5cbf064aE187b8361/eed6f6cbf1de3aaa.png"/>
                                        <img class="service_ico_img_hover"
                                             src="//m.360buyimg.com/babel/jfs/t1/45423/33/385/778/5cd4f265E442a9342/0aff0a42cece09ee.png"/>
                                    </i>
                                    <span class="service_txt">话费</span>
                                </a>
                            </li>
                            <li class="service_item service_frame mod_tab_head_item">
                                <a href="//jipiao.jd.com/" class="service_lk" target="_blank"
                                   clstag="h|keycount|head|shortcut_02" aria-label="机票">
                                                                                                                                                    <i class="service_ico service_ico_jipiao">
                                        <img class="service_ico_img"
                                             src="//m.360buyimg.com/babel/jfs/t1/36478/38/5384/2901/5cbf065aEb0c60a12/afb4399323fe3b76.png"/>
                                        <img class="service_ico_img_hover"
                                             src="//m.360buyimg.com/babel/jfs/t1/34261/15/10242/3120/5cd4f256E10257aba/8f3f63ae04ff19af.png"/>
                                    </i>
                                    <span class="service_txt">机票</span>
                                </a>
                            </li>
                            <li class="service_item service_frame mod_tab_head_item">
                                <a href="//hotel.jd.com/" class="service_lk" target="_blank"
                                   clstag="h|keycount|head|shortcut_03" aria-label="酒店">
                                                                                                                                                    <i class="service_ico service_ico_jiudian">
                                        <img class="service_ico_img"
                                             src="//m.360buyimg.com/babel/jfs/t1/31069/34/14642/979/5cbf0665Ec7dc8223/5fee386254dd2ebc.png"/>
                                        <img class="service_ico_img_hover"
                                             src="//m.360buyimg.com/babel/jfs/t1/44601/19/915/1039/5cd4f1cfE2e46473c/b61f083872a7a1de.png"/>
                                    </i>
                                    <span class="service_txt">酒店</span>
                                </a>
                            </li>
                            <li class="service_item service_frame service_frame2 mod_tab_head_item" data-row="2">
                                <a href="//game.jd.com/" class="service_lk" target="_blank"
                                   clstag="h|keycount|head|shortcut_04" aria-label="游戏">
                                                                                                                                                    <i class="service_ico service_ico_youxi">
                                        <img class="service_ico_img"
                                             src="//m.360buyimg.com/babel/jfs/t1/32403/22/14829/3699/5cbf0674E04723693/caa83ce9b881cd24.png"/>
                                        <img class="service_ico_img_hover"
                                             src="//m.360buyimg.com/babel/jfs/t1/57520/8/375/4092/5cd4f1d8Ea1266047/1c590322ece537ba.png"/>
                                    </i>
                                    <span class="service_txt">游戏</span>
                                </a>
                            </li>
                                                                                                                                                                                                                                                                                                                                                <li class="service_item service_noframe">
                                        <a href="https:&#47;&#47;jiayouka.jd.com&#47;" class="service_lk" target="_blank"
                                           clstag="h|keycount|head|shortcut_05" aria-label="加油卡">
                                                                                        <i class="service_ico">
                                                <!-- 常态 icon -->
                                                <img class="service_ico_img"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;71890&#47;14&#47;9897&#47;3048&#47;5d7739ddE93eb94f8&#47;f1f6dc5c207329f9.png"/>
                                                <!-- hover 态 icon -->
                                                <img class="service_ico_img_hover"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;36002&#47;35&#47;9106&#47;3311&#47;5cd4f1bdE06ff07ed&#47;9570fdd46ecd3a76.png"/>
                                            </i>
                                            <span class="service_txt">加油卡</span>
                                        </a>
                                    </li>
                                                                                                                                <li class="service_item service_noframe">
                                        <a href="https:&#47;&#47;train.jd.com&#47;" class="service_lk" target="_blank"
                                           clstag="h|keycount|head|shortcut_06" aria-label="火车票">
                                                                                        <i class="service_ico">
                                                <!-- 常态 icon -->
                                                <img class="service_ico_img"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;45761&#47;32&#47;10307&#47;1581&#47;5d7739e2Ece4b6671&#47;0004c1b85fbf7bde.png"/>
                                                <!-- hover 态 icon -->
                                                <img class="service_ico_img_hover"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;58891&#47;36&#47;278&#47;1745&#47;5cd4f1e0Ef4cc50a7&#47;f12276b17e5dcf3b.png"/>
                                            </i>
                                            <span class="service_txt">火车票</span>
                                        </a>
                                    </li>
                                                                                                                                <li class="service_item service_noframe">
                                        <a href="https:&#47;&#47;pro.jd.com&#47;mall&#47;active&#47;4EYjXQ6xjnM9TgeSjuMRE8ACEk6q&#47;frist.html" class="service_lk" target="_blank"
                                           clstag="h|keycount|head|shortcut_07" aria-label="众筹">
                                                                                        <i class="service_ico">
                                                <!-- 常态 icon -->
                                                <img class="service_ico_img"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;51584&#47;31&#47;10221&#47;1685&#47;5d7739e7E1adb25cd&#47;1d0957d7f2ae01a2.png"/>
                                                <!-- hover 态 icon -->
                                                <img class="service_ico_img_hover"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;50929&#47;1&#47;374&#47;1847&#47;5cd4f1eaE5daf90db&#47;cebbff76b25dc22e.png"/>
                                            </i>
                                            <span class="service_txt">众筹</span>
                                        </a>
                                    </li>
                                                                                                                                <li class="service_item service_noframe">
                                        <a href="https:&#47;&#47;jr.jd.com&#47;" class="service_lk" target="_blank"
                                           clstag="h|keycount|head|shortcut_08" aria-label="理财">
                                                                                        <i class="service_ico">
                                                <!-- 常态 icon -->
                                                <img class="service_ico_img"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;52683&#47;35&#47;10394&#47;3447&#47;5d7739edE270aa7b3&#47;d4d1151b09b5553b.png"/>
                                                <!-- hover 态 icon -->
                                                <img class="service_ico_img_hover"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;47544&#47;23&#47;372&#47;3943&#47;5cd4f24eE92fbcf79&#47;4b49b55af25a7bdf.png"/>
                                            </i>
                                            <span class="service_txt">理财</span>
                                        </a>
                                    </li>
                                                                                                                                <li class="service_item service_noframe">
                                        <a href="https:&#47;&#47;baitiao.jd.com&#47;?from=jrscyn_20160" class="service_lk" target="_blank"
                                           clstag="h|keycount|head|shortcut_09" aria-label="白条">
                                                                                        <i class="service_ico">
                                                <!-- 常态 icon -->
                                                <img class="service_ico_img"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;56296&#47;3&#47;10260&#47;1443&#47;5d7739f3E233abc53&#47;e6976f3cb30c9a8a.png"/>
                                                <!-- hover 态 icon -->
                                                <img class="service_ico_img_hover"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;39983&#47;24&#47;6834&#47;1596&#47;5cd4f247E8cf89f1e&#47;b8a8418d5418f471.png"/>
                                            </i>
                                            <span class="service_txt">白条</span>
                                        </a>
                                    </li>
                                                                                                                                <li class="service_item service_noframe">
                                        <a href="https:&#47;&#47;movie.jd.com&#47;frist.html" class="service_lk" target="_blank"
                                           clstag="h|keycount|head|shortcut_10" aria-label="电影票">
                                                                                        <i class="service_ico">
                                                <!-- 常态 icon -->
                                                <img class="service_ico_img"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;60778&#47;37&#47;9838&#47;3066&#47;5d7739faEd3b7dbb9&#47;dd4d9ef7ce8fc169.png"/>
                                                <!-- hover 态 icon -->
                                                <img class="service_ico_img_hover"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;41106&#47;15&#47;4551&#47;3300&#47;5cd4f1c7E507148c7&#47;90a218f053e903d2.png"/>
                                            </i>
                                            <span class="service_txt">电影票</span>
                                        </a>
                                    </li>
                                                                                                                                <li class="service_item service_noframe">
                                        <a href="https:&#47;&#47;b.jd.com&#47;" class="service_lk" target="_blank"
                                           clstag="h|keycount|head|shortcut_11" aria-label="企业购">
                                                                                        <i class="service_ico">
                                                <!-- 常态 icon -->
                                                <img class="service_ico_img"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;40738&#47;20&#47;14562&#47;826&#47;5d773a01E09eb8121&#47;d6f3909618c6307a.png"/>
                                                <!-- hover 态 icon -->
                                                <img class="service_ico_img_hover"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;45316&#47;3&#47;388&#47;884&#47;5cd4f25eEea4c67ed&#47;671f7c186c5e9b01.png"/>
                                            </i>
                                            <span class="service_txt">企业购</span>
                                        </a>
                                    </li>
                                                                                                                                <li class="service_item service_noframe">
                                        <a href="https:&#47;&#47;o.jd.com" class="service_lk" target="_blank"
                                           clstag="h|keycount|head|shortcut_12" aria-label="礼品卡">
                                                                                        <i class="service_ico">
                                                <!-- 常态 icon -->
                                                <img class="service_ico_img"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;57014&#47;6&#47;10297&#47;815&#47;5d773a07Ec7a61fc9&#47;97917a2daa34be0f.png"/>
                                                <!-- hover 态 icon -->
                                                <img class="service_ico_img_hover"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;55911&#47;31&#47;402&#47;858&#47;5cd4f23eE6f536460&#47;5da079255c6dfabe.png"/>
                                            </i>
                                            <span class="service_txt">礼品卡</span>
                                        </a>
                                    </li>
                                                                                    </ul>
                    </div>
                    <div class="J_tab_content service_pop" tabindex="-1" aria-hidden="true">
                        <div class="mod_tab_content_item service_pop_item mod_loading"></div>
                        <div class="mod_tab_content_item service_pop_item mod_loading"></div>
                        <div class="mod_tab_content_item service_pop_item mod_loading"></div>
                        <div class="mod_tab_content_item service_pop_item mod_loading"></div>
                        <a class="J_service_pop_close service_pop_close iconfont" href="javascript:;" tabindex="-1"></a>
                    </div>
                </div>
            </div>
        </div>
        <div id="J_fs_act" class="fs_act"></div>
    </div>
    <!-- CLUB_LINK start seo  -->
    <div style="display:none">
                <a href="//itb2b.jd.com/">京采汇</a>
                <a href="//pro.m.jd.com/mall/active/2ukQm4T7b9utHWDn2cXGH2KEnUYV/frist.html">电动车十大排行榜</a>
                <a href="//pro.m.jd.com/mall/active/pVc2ZtPRvzzCuAE8eRSfXFvan1d/frist.html">电动车价钱</a>
                <a href="//jzt.m.jd.com/school/market/2021/11/11">京准通11.11</a>
                <a href="//pro.m.jd.com/mall/active/wcvrZNcfWbUV6spvqoY17CXwny1/frist.html">电动车十大名牌排名</a>
                <a href="//pro.m.jd.com/mall/active/2GYft5Ph4ZAAAQKWxJyHtsFun1ef/frist.html">十大名牌电动车</a>
                <a href="//pro.m.jd.com/mall/active/2GL7sRxRYrRSE6Zk7DesxmQ5JDvc/frist.html">电动车三轮车</a>
                <a href="//pro.m.jd.com/mall/active/22ADrLDeC31kzfT171t8UYDcRf23/frist.html">电动车排行</a>
                <a href="//union.jd.com">网络赚钱</a>
                <a href="//pro.m.jd.com/mall/active/1X36PoLQQ6JYgrLusHZpfowpxpc/frist.html">电动车十大品牌排行榜</a>
                <a href="//pro.m.jd.com/mall/active/3VLqBaQBjR3XxwDBNdDYMMAAX1wc/frist.html">电动车十大排行</a>
                <a href="//pro.m.jd.com/mall/active/3ERkqhxNQozbNJ3BQCxUX3p1sFEC/frist.html">电动车十佳品牌排行榜</a>
                <a href="//pro.m.jd.com/mall/active/TU6auzpj8HDPAqumWMZ35uML4HB/frist.html">电动车电池十大排名</a>
                <a href="//pro.m.jd.com/mall/active/3uxWVvqh2dmwN2eLbqDfGj6BBoAk/frist.html">台铃电动车</a>
                <a href="//www.jd.com/sptopic/117296ca19d46b24dfeb3.html">女士鞋</a>
                <a href="//www.jd.com/cppf/9847333cd3d99d6886d9.html">实木沙发</a>
                <a href="//www.jd.com/book/737280eea8ac7dfea03.html">索尼电视</a>
                <a href="//www.jd.com/hotitem/9855fbd5a67b591890f1.html">卫浴品牌</a>
                <a href="//www.jd.com/zuozhe/7378d855fa5f85d59a5.html">奥克斯空调</a>
                <a href="//fresh.jd.com/shengxian/12218e48f879c700b44c1.html">百香果</a>
                <a href="https://yp.jd.com/737b36a4184d54f29a0.html">富信十字对开门直冷冰箱</a>
                <a href="https://www.jd.com/phb/73720f146e36377c660.html">大冷藏冰箱</a>
                <a href="https://www.jd.com/phb/key_737a166c7819e49073e.html">lg冰箱2078dkd</a>
                <a href="https://www.jd.com/jiage/7374057d6f1e5b4d2e3.html">惠而浦定频冰箱</a>
                <a href="https://www.jd.com/tupian/737f959cecec45ca6d8.html">哈士奇BC-130RDA</a>
                <a href="https://www.jd.com/xinkuan/7376335ed73fe7bd781.html">冰箱博世</a>
                <a href="https://www.jd.com/book/737f47babdf1c493dc3.html">bcd238zip3ck</a>
                <a href="https://www.jd.com/zuozhe/737275eff2d5153d3c2.html">海信KFR26GWA8Q100NA11N23制热</a>
                <a href="https://www.jd.com/brand/7379a1e5052d079d2f2.html">M45PKVM</a>
                <a href="https://www.jd.com/xinghao/7378311b714a7328d8d.html">松下c32wp2</a>
                <a href="https://www.jd.com/cppf/737a87040e74d6e4dc1.html">541WDPJ</a>
                <a href="https://www.jd.com/hprm/7378dc4973dcb247273.html">复古冰箱Misha bear</a>
                <a href="https://www.jd.com/sptopic/73705eed7ddb8397df4.html">西门孑冰箱</a>
                <a href="https://www.jd.com/hotitem/7377956c9078fb98d22.html">欧立多门变频冰箱</a>
                <a href="https://www.jd.com/nrjs/889716b196350a23.html">海尔冰箱201无霜排行榜，海尔冰箱201无霜十大排名推荐</a>
                <a href="https://www.jd.com/zxnews/26b309e098b65571.html">樱花（SAKURA）不锈钢冰箱排行榜，樱花（SAKURA）不锈钢冰箱十大排名推荐</a>
                <a href="https://www.jd.com/phb/zhishi/8240bd3ce86c027e.html">bcd201l排行榜，bcd201l十大排名推荐</a>
                <a href="https://www.jd.com/phb/zhishi/c436f14ce3bb3520.html">容声冰箱176哪款好？容声冰箱176怎么样好用吗？</a>
                <a href="https://www.jd.com/jxinfo/8006720b566b9f88.html">风冷无霜冰箱，给你的健康生活</a>
                <a href="https://www.jd.com/jxinfo/6ac5cddd6f57391f.html">海尔冰箱206stpa排行榜，海尔冰箱206stpa十大排名推荐</a>
            </div>
    <!-- CLUB_LINK end -->
    <script type="text/javascript">
        window.point.fs = new Date().getTime();
    </script>
    <!-- E ad2 -->

</div>

<script src="//storage.360buyimg.com/pc-pre-tmp/jquery.js"></script>
<script src="//misc.360buyimg.com/??mtd/pc/common/js/o2_ua.js,mtd/pc/base/1.0.0/event.js"></script>
<script src="//wl.jd.com/wl.js"></script>

<script>

</script>

<style>

.o2_ie8 .more2_international {

    filter: progid:dximagetransform.microsoft.alphaimageloader(src='//storage.360buyimg.com/mtd/home/more_international1575014601797.png',sizingMethod='scale');

    background: none;

}

.mod_help_cover {

    background-image: none;

}

#settleup:hover .cw-icon {

    border-bottom: 1px solid #c81623;

}

.o2_mini .company .feed-tab {

    margin: 0 auto;

}

.company .feed-tab {

    margin: 0 auto;

}

.channelsB .channels_block_1 .channels_item_1 .channels_item_link {

    height: 370px;

    width: 290px;

}

.channelsB .channels_block_1 .channels_item_2 .channels_item_link {

    height: 370px;

    width: 290px;

}

.JD_close-button--square {

  z-index: 1;

}

</style>
<div id="app"></div>
<script type="text/javascript">
    window.point.dom = new Date().getTime();
</script>

<style type="text/css">
.mod_footer {
  height: 500px;
  background-color: #eaeaea;
}

/* 服务承诺 */
.mod_service {
  padding: 30px 0;
  border-bottom: 1px solid #dedede;
}

.mod_service_list {
  overflow: hidden;
  height: 42px;
}

.mod_service_item {
  float: left;
  width: 297px;
}

.mod_service_unit {
  position: relative;
  margin: 0 auto;
  padding-left: 45px;
  width: 180px;
}

.mod_service_tit {
  overflow: hidden;
  position: absolute;
  left: 0;
  top: 0;
  width: 36px;
  height: 42px;
  text-indent: -999px;
}

.mod_service_txt {
  overflow: hidden;
  width: 100%;
  height: 42px;
  line-height: 42px;
  font-size: 18px;
  font-weight: 700;
  text-overflow: ellipsis;
  white-space: nowrap;
  color: #444;
}

/* 多快好省的图标 */
.mod_service_duo {
  background-repeat: no-repeat;
  background-position: 0 -192px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_service_kuai {
  background-repeat: no-repeat;
  background-position: -41px -192px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_service_hao {
  background-repeat: no-repeat;
  background-position: -82px -192px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_service_sheng {
  background-repeat: no-repeat;
  background-position: -123px -192px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

/* 帮助清单 */
.mod_help {
  padding: 20px 0;
}

.mod_help_list {
  overflow: hidden;
  height: 160px;
}

.mod_help_nav {
  float: left;
  width: 198px;
  line-height: 22px;
}

.mod_help_nav_tit {
  margin-bottom: 5px;
  font-size: 14px;
}

.mod_help_cover {
  background-repeat: no-repeat;
  background-position: 0 0;
  float: right;
  width: 200px;
  height: 150px;
}

.mod_help_cover_tit {
  margin-bottom: 15px;
  font-size: 14px;
  text-align: center;
}

.mod_help_cover_con {
  padding: 0 10px;
}

.mod_help_cover_more {
  text-align: right;
}

/* 版权信息 */
.mod_copyright_inner {
  padding: 15px 0;
  border-top: 1px solid #e1e1e1;
  text-align: center;
}

.mod_copyright_split {
  margin: 0 7px;
  color: #ccc;
}

.mod_copyright_info {
  padding: 10px 0;
  line-height: 22px;
  color: #999;
}

.mod_copyright_info a {
  color: #999;
}

.mod_copyright_info a:hover {
  color: #c81623;
}

.mod_copyright_inter_ico {
  display: inline-block;
  width: 15px;
  height: 10px;
  vertical-align: -1px;
  margin-right: 10px;
  background-repeat: no-repeat;
}

.mod_copyright_inter_ico_global {
  background-repeat: no-repeat;
  background-position: -108px -155px;
  width: 15px;
  height: 12px;
  margin-top: -1px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_copyright_inter_ico_rissia {
  background-repeat: no-repeat;
  background-position: -168px -155px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_copyright_inter_ico_indonesia {
  background-repeat: no-repeat;
  background-position: -148px -155px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_copyright_inter_ico_thailand {
  background-repeat: no-repeat;
  background-position: -108px -172px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_copyright_inter_ico_spain {
  background-repeat: no-repeat;
  background-position: -128px -155px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_copyright_auth {
  margin: 25px 0;
}

.mod_copyright_auth_ico {
  overflow: hidden;
  display: inline-block;
  margin: 0 3px;
  width: 103px;
  height: 32px;
  line-height: 1000px;
}

.mod_copyright_auth_ico_1 {
  background-repeat: no-repeat;
  background-position: -205px -148px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_copyright_auth_ico_2 {
  background-repeat: no-repeat;
  background-position: -205px -111px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_copyright_auth_ico_3 {
  background-repeat: no-repeat;
  background-position: -205px -74px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_copyright_auth_ico_4 {
  background-repeat: no-repeat;
  background-position: -205px -37px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_copyright_auth_ico_5 {
  background-repeat: no-repeat;
  background-position: 0 -66px;
  background-image: url(//img13.360buyimg.com/imagetools/jfs/t1/108497/17/22418/15570/6215e0d0E01387603/81e883d9e15cebb7.png);
}

.mod_copyright_auth_ico_6 {
  background-repeat: no-repeat;
  background-position: 0 -155px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_copyright_auth_ico_7 {
  background-repeat: no-repeat;
  background-position: 0 -99px;
  background-image: url(//img13.360buyimg.com/imagetools/jfs/t1/108497/17/22418/15570/6215e0d0E01387603/81e883d9e15cebb7.png);
}

.mod_copyright_auth_ico_8 {
  width: 70px;
  background-repeat: no-repeat;
  background-position: -104px -99px;
  background-image: url(//img13.360buyimg.com/imagetools/jfs/t1/108497/17/22418/15570/6215e0d0E01387603/81e883d9e15cebb7.png);
}

.mod_copyright_auth_ico_9 {
  width: 88px;
  background-repeat: no-repeat;
  background-position: -104px -131px;
  background-image: url(//img13.360buyimg.com/imagetools/jfs/t1/108497/17/22418/15570/6215e0d0E01387603/81e883d9e15cebb7.png);
}

// .mod_copyright_license {
//   margin-left: 16px;
// }

/* 适配高清屏 */

@media only screen and (-webkit-min-device-pixel-ratio: 1.5),
  only screen and (min--moz-device-pixel-ratio: 1.5),
  only screen and (-o-min-device-pixel-ratio: 3/2),
  only screen and (min-device-pixel-ratio: 1.5) {

  .mod_service_duo {
    background-repeat: no-repeat;
    background-size: 113px 86.5px;
    background-position: 0 0;
    background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211722/38/13035/9322/6215e10cEa9918ac1/7f8686ee76e42123.png);
  }

  .mod_service_kuai {
    background-repeat: no-repeat;
    background-size: 113px 86.5px;
    background-position: -38.5px 0;
    background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211722/38/13035/9322/6215e10cEa9918ac1/7f8686ee76e42123.png);
  }

  .mod_service_hao {
    background-repeat: no-repeat;
    background-size: 113px 86.5px;
    background-position: -77px 0;
    background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211722/38/13035/9322/6215e10cEa9918ac1/7f8686ee76e42123.png);
  }

  .mod_service_sheng {
    background-repeat: no-repeat;
    background-size: 113px 86.5px;
    background-position: 0 -44.5px;
    background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211722/38/13035/9322/6215e10cEa9918ac1/7f8686ee76e42123.png);
  }

  .mod_copyright_inter_ico_global {
    background-repeat: no-repeat;
    background-size: 113px 86.5px;
    background-position: -38.5px -44.5px;
    background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211722/38/13035/9322/6215e10cEa9918ac1/7f8686ee76e42123.png);
  }

  .mod_copyright_inter_ico_rissia {
    background-repeat: no-repeat;
    background-size: 113px 86.5px;
    background-position: -56px -44.5px;
    background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211722/38/13035/9322/6215e10cEa9918ac1/7f8686ee76e42123.png);
  }

  .mod_copyright_inter_ico_indonesia {
    background-repeat: no-repeat;
    background-size: 113px 86.5px;
    background-position: -73.5px -44.5px;
    background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211722/38/13035/9322/6215e10cEa9918ac1/7f8686ee76e42123.png);
  }

  .mod_copyright_inter_ico_thailand {
    background-repeat: no-repeat;
    background-size: 113px 86.5px;
    background-position: -91px -44.5px;
    background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211722/38/13035/9322/6215e10cEa9918ac1/7f8686ee76e42123.png);
  }

  .mod_copyright_inter_ico_spain {
    background-repeat: no-repeat;
    background-size: 113px 86.5px;
    background-position: -38.5px -59px;
    background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211722/38/13035/9322/6215e10cEa9918ac1/7f8686ee76e42123.png);
  }

  .mod_copyright_inter_lk {
    font-family: initial;
  }
}

/* 窄版 */
.o2_mini .mod_service_item {
  width: 247px;
}

.o2_mini .mod_help_nav {
  width: 158px;
}

.o2_mini .mod_copyright_links .mod_copyright_split {
  margin: 0 6px;
}
</style>
<script type="text/javascript">
  function clickReport(){
    $("body").delegate("[poi]", "click", function(e){
        let $current = $(e.target)
        let tagName = $current.prop("tagName")

        if(tagName === 'A' || tagName === 'a'){
          let fullpoi = $current.attr('poi') ? $current.attr('poi') : $current.parents('[poi]').attr('poi')
          let url = $current.attr('href')
          let text = $.trim($current.text())

          window.footerGetOnClick && window.footerGetOnClick(fullpoi, url, text)
        }
    })
  }
  clickReport()
</script>
<div id="J_footer" class="footer">
  <div class="mod_service" clstag="btm|btmnavi_null01" poi="btm|btmnavi|null01">
    <div class="grid_c1 mod_service_inner">
      <ul class="mod_service_list">
        <li class="mod_service_item">
          <div class="mod_service_unit">
            <h5 class="mod_service_tit mod_service_duo">多</h5>
            <p class="mod_service_txt">品类齐全，轻松购物</p>
          </div>
        </li>
        <li class="mod_service_item">
          <div class="mod_service_unit">
            <h5 class="mod_service_tit mod_service_kuai">快</h5>
            <p class="mod_service_txt">多仓直发，极速配送</p>
          </div>
        </li>
        <li class="mod_service_item">
          <div class="mod_service_unit">
            <h5 class="mod_service_tit mod_service_hao">好</h5>
            <p class="mod_service_txt">正品行货，精致服务</p>
          </div>
        </li>
        <li class="mod_service_item">
          <div class="mod_service_unit">
            <h5 class="mod_service_tit mod_service_sheng">省</h5>
            <p class="mod_service_txt">天天低价，畅选无忧</p>
          </div>
        </li>
      </ul>
    </div>
  </div>

  <div class="mod_help" clstag="btm|btmnavi_null02" poi="btm|btmnavi|null02">
    <div class="grid_c1 mod_help_inner">
      <div class="mod_help_list">
        <div class="mod_help_nav">
          <h5 class="mod_help_nav_tit">购物指南</h5>
          <ul class="mod_help_nav_con">
            <li>
              <a href="//help.jd.com/user/issue/list-29.html" target="_blank" rel="noopener noreferrer">
                购物流程
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/list-151.html" target="_blank" rel="noopener noreferrer">
                会员介绍
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/list-297.html" target="_blank" rel="noopener noreferrer">
                生活旅行
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue.html" target="_blank" rel="noopener noreferrer">
                常见问题
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/list-136.html" target="_blank" rel="noopener noreferrer">
                大家电
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/custom.html" target="_blank" rel="noopener noreferrer">
                联系客服
              </a>
            </li>
          </ul>
        </div>
        <div class="mod_help_nav">
          <h5 class="mod_help_nav_tit">配送方式</h5>
          <ul class="mod_help_nav_con">
            <li>
              <a href="//help.jd.com/user/issue/list-81-100.html" target="_blank" rel="noopener noreferrer">
                上门自提
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/list-81.html" target="_blank" rel="noopener noreferrer">
                211限时达
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/103-983.html" target="_blank" rel="noopener noreferrer">
                配送服务查询
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/109-188.html" target="_blank" rel="noopener noreferrer">
                配送费收取标准
              </a>
            </li>
            <li>
              <a href="//help.joybuy.com/help/question-list-201.html" target="_blank" rel="noopener noreferrer">
                海外配送
              </a>
            </li>
          </ul>
        </div>
        <div class="mod_help_nav">
          <h5 class="mod_help_nav_tit">支付方式</h5>
          <ul class="mod_help_nav_con">
            <li>
              <a href="//help.jd.com/user/issue/list-172.html" target="_blank" rel="noopener noreferrer">
                货到付款
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/list-173.html" target="_blank" rel="noopener noreferrer">
                在线支付
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/list-176.html" target="_blank" rel="noopener noreferrer">
                分期付款
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/list-175.html" target="_blank" rel="noopener noreferrer">
                公司转账
              </a>
            </li>
          </ul>
        </div>
        <div class="mod_help_nav">
          <h5 class="mod_help_nav_tit">售后服务</h5>
          <ul class="mod_help_nav_con">
            <li>
              <a href="//help.jd.com/user/issue/list-112.html" target="_blank" rel="noopener noreferrer">
                售后政策
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/list-132.html" target="_blank" rel="noopener noreferrer">
                价格保护
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/130-978.html" target="_blank" rel="noopener noreferrer">
                退款说明
              </a>
            </li>
            <li>
              <a href="//myjd.jd.com/repair/repairs.action" target="_blank" rel="noopener noreferrer">
                返修/退换货
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/list-50.html" target="_blank" rel="noopener noreferrer">
                取消订单
              </a>
            </li>
          </ul>
        </div>
        <div class="mod_help_nav">
          <h5 class="mod_help_nav_tit">特色服务</h5>
          <ul class="mod_help_nav_con">
            <li>
              <a href="//1paipai.jd.com/" target="_blank" rel="noopener noreferrer">
                夺宝岛
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/list-134.html" target="_blank" rel="noopener noreferrer">
                DIY装机
              </a>
            </li>
            <li>
              <a href="//fuwu.jd.com/" target="_blank" rel="noopener noreferrer">
                延保服务
              </a>
            </li>
            <li>
              <a href="//o.jd.com/market/index.action" target="_blank" rel="noopener noreferrer">
                京东E卡
              </a>
            </li>
            <li>
              <a href="//mobile.jd.com/" target="_blank" rel="noopener noreferrer">
                京东通信
              </a>
            </li>
            <li>
              <a href="//smart.jd.com/" target="_blank" rel="noopener noreferrer">
                京鱼座智能
              </a>
            </li>
          </ul>
        </div>
        <div class="mod_help_cover">
          <h5 class="mod_help_cover_tit">京东自营覆盖区县</h5>
          <div class="mod_help_cover_con">
            <p class="mod_help_cover_info">
              京东已向全国2661个区县提供自营配送服务，支持货到付款、POS机刷卡和售后上门服务。
            </p>
            <p class="mod_help_cover_more">
              <a href="//help.jd.com/user/issue/103-983.html" target="_blank" rel="noopener noreferrer">
                查看详情
                <i class="iconfont">&#xe60d;</i>
              </a>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="mod_copyright">
    <div class="grid_c1 mod_copyright_inner">
      <p
        class="mod_copyright_links"
        clstag="btm|btmnavi_null03"
        poi="btm|btmnavi|null03"
      >
        <a href="//about.jd.com" target="_blank" rel="noopener noreferrer">关于我们</a>
        <span class="mod_copyright_split">|</span>
        <a href="//about.jd.com/contact" target="_blank" rel="noopener noreferrer">联系我们</a>
        <span class="mod_copyright_split">|</span>
        <a href="//help.jd.com/user/custom.html" target="_blank" rel="noopener noreferrer">联系客服</a>
        <span class="mod_copyright_split">|</span>
        <a href="//lai.jd.com" target="_blank" rel="noopener noreferrer">合作招商</a>
        <span class="mod_copyright_split">|</span>
        <a href="//helpcenter.jd.com/venderportal/frist.html" target="_blank" rel="noopener noreferrer">商家帮助</a>
        <span class="mod_copyright_split">|</span>
        <a href="//jzt.jd.com" target="_blank" rel="noopener noreferrer">营销中心</a>
        <span class="mod_copyright_split">|</span>
        <a href="//app.jd.com/" target="_blank" rel="noopener noreferrer">手机京东</a>
        <span class="mod_copyright_split">|</span>
        <a href="//club.jd.com/links.aspx" target="_blank" rel="noopener noreferrer">友情链接</a>
        <span class="mod_copyright_split">|</span>
        <a href="//union.jd.com/index" target="_blank" rel="noopener noreferrer">销售联盟</a>
        <span class="mod_copyright_split">|</span>
        <a href="//pro.jd.com/mall/active/3WA2zN8wkwc9fL9TxAJXHh5Nj79u/frist.html" target="_blank" rel="noopener noreferrer">京东社区</a>
        <span class="mod_copyright_split">|</span>
        <a href="//pro.jd.com/mall/active/3TF25tMdrnURET8Ez1cW9hzfg3Jt/frist.html" target="_blank" rel="noopener noreferrer">风险监测</a>
        <span class="mod_copyright_split">|</span>
        <a href="//about.jd.com/privacy/" target="_blank" rel="noopener noreferrer">隐私政策</a>
        <span class="mod_copyright_split">|</span>
        <a href="//gongyi.jd.com" target="_blank" rel="noopener noreferrer">京东公益</a>
        <span class="mod_copyright_split">|</span>
        <a href="//www.joybuy.com/" target="_blank" rel="noopener noreferrer">English Site</a>
        <span class="mod_copyright_split">|</span>
        <a href="//corporate.jd.com" target="_blank" rel="noopener noreferrer">Media & IR</a>
      </p>


      <div class="mod_copyright_info">
        <div
          class="mod_copyright_cert"
          clstag="btm|btmnavi_null04"
          poi="btm|btmnavi|null04"
        >
          <p>
            <a
              href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11000002000088"
              target="_blank"
              rel="noopener noreferrer"
            >
              京公网安备 11000002000088号
            </a>
            <span class="mod_copyright_split">|</span>
            <a href="http://beian.miit.gov.cn" target="_blank" rel="noopener noreferrer">
              京ICP备11041704号
            </a>
            <span class="mod_copyright_split">|</span>
            <a
              href="//h5.m.jd.com/pc/dev/3T3No18XR8k8rpLGLGhgbJ1StAFq/frist.html"
              target="_blank"
              rel="noopener noreferrer"
            >
              ICP
            </a>
            <span class="mod_copyright_split">|</span>
            <a href="//jdwp.jd.com/544-2927.html" target="_blank" rel="noopener noreferrer">
              互联网药品信息服务资格证编号(京)-经营性-2014-0008
            </a>
            <span class="mod_copyright_split">|</span>
            <span>新出发京零&nbsp;字第大120007号</span>
          </p>
          <p>
            <span>互联网出版许可证编号新出网证(京)字150号</span>
            <span class="mod_copyright_split">|</span>
            <a
              href="//pro.jd.com/mall/active/3bVDLXHdwVmdQksGF8TtS7ocq1NY/frist.html"
              target="_blank"
              rel="noopener noreferrer"
            >
              出版物经营许可证
            </a>
            <span class="mod_copyright_split">|</span>
            <a
              href="//img10.360buyimg.com/ling/jfs/t1/164806/19/5070/567736/6017d6d6Eab06ec9c/d8ca6e029f495447.jpg"
              target="_blank"
              rel="noopener noreferrer"
            >
              网络文化经营许可证京网文[2020]6112-1201号
            </a>
            <span class="mod_copyright_split">|</span>
            <span>违法和不良信息举报电话：4006561155</span>
          </p>
          <p>
            <span class="copyright_txt"></span>
            <span class="mod_copyright_split">|</span>
            <span>消费者维权热线：4006067733</span>
            <span class="mod_copyright_split">|</span>
            <a
              href="//pro.jd.com/mall/active/38PitHBfR7ZopNHRSHnuuWR5AMDL/frist.html"
              target="_blank"
              rel="noopener noreferrer"
              class="mod_copyright_license"
            >
              经营证照
            </a>
            <span class="mod_copyright_split">|</span>
            <span>(京)网械平台备字(2018)第00003号</span>
            <span class="mod_copyright_split">|</span>
            <a
              href="//h5.m.jd.com/babelDiy/Zeus/ARcYnJ8coUdUecn6UQAN6TDaVmH/frist.html"
              target="_blank"
              rel="noopener noreferrer"
              class="mod_business_license"
            >
              营业执照
            </a>
            <span class="mod_copyright_split">|</span>
            <a
              href="//img11.360buyimg.com/imagetools/jfs/t1/148412/19/20641/1513871/6204e24aEd9434d24/b11d1cd7d1d36976.png"
              target="_blank"
              rel="noopener noreferrer"
              class="mod_business_license"
            >
              增值电信业务经营许可证
            </a>
          </p>
        </div>

        <div class="mod_copyright_inter">
          <p>
            <a
              class="mod_copyright_inter_lk"
              href="//www.joybuy.com/?source=1&visitor_from=3"
              target="_blank"
              rel="noopener noreferrer"
              clstag="btm|btmnavi_null0501"
              poi="btm|btmnavi|null0501"
            >
              <i class="mod_copyright_inter_ico mod_copyright_inter_ico_global"></i>
              Global Site
            </a>
            <span class="mod_copyright_split">|</span>
            <a
              class="mod_copyright_inter_lk"
              href="//www.jd.ru/?source=1&visitor_from=3"
              target="_blank"
              rel="noopener noreferrer"
              clstag="btm|btmnavi_null0502"
              poi="btm|btmnavi|null0502"
            >
              <i class="mod_copyright_inter_ico mod_copyright_inter_ico_rissia"></i>
              Сайт России
            </a>
            <span class="mod_copyright_split">|</span>
            <a
              class="mod_copyright_inter_lk"
              href="//www.jd.id/?source=1&visitor_from=3"
              target="_blank"
              rel="noopener noreferrer"
              clstag="btm|btmnavi_null0503"
              poi="btm|btmnavi|null0503"
            >
              <i class="mod_copyright_inter_ico mod_copyright_inter_ico_indonesia"></i>
              Situs Indonesia
            </a>
            <span class="mod_copyright_split">|</span>
            <a
              class="mod_copyright_inter_lk"
              href="//www.joybuy.es/?source=1&visitor_from=3"
              target="_blank"
              rel="noopener noreferrer"
              clstag="btm|btmnavi_null0504"
              poi="btm|btmnavi|null0504"
            >
              <i class="mod_copyright_inter_ico mod_copyright_inter_ico_spain"></i>
              Sitio de España
            </a>
            <span class="mod_copyright_split">|</span>
            <a
              class="mod_copyright_inter_lk"
              href="//www.jd.co.th/?source=1&visitor_from=3"
              target="_blank"
              rel="noopener noreferrer"
              clstag="btm|btmnavi_null0505"
              poi="btm|btmnavi|null0505"
            >
              <i class="mod_copyright_inter_ico mod_copyright_inter_ico_thailand"></i>
              เว็บไซต์ประเทศไทย
            </a>
          </p>
        </div>

        <div
          class="mod_copyright_subsites"
          clstag="btm|btmnavi_null06"
          poi="btm|btmnavi|null06"
        >
          <p>
            <span>京东旗下网站：</span>
            <a href="https://www.jdpay.com/" target="_blank" rel="noopener noreferrer">
              京东钱包
            </a>
            <span class="mod_copyright_split">|</span>
            <a href="http://www.jdcloud.com" target="_blank" rel="noopener noreferrer">
              京东云
            </a>
            <span class="mod_copyright_split">|</span>
            <span>网络内容从业人员违法违规行为举报电话：4006561155-3</span>
          </p>
        </div>
      </div>

      <p
        class="mod_copyright_auth"
        clstag="btm|btmnavi_null07"
        poi="btm|btmnavi|null07"
      >
        <a
          class="mod_copyright_auth_ico mod_copyright_auth_ico_2"
          href="https://ss.knet.cn/verifyseal.dll?sn=2008070300100000031&ampct=df&amppa=294005"
          target="_blank"
          rel="noopener noreferrer"
        >
          可信网站信用评估
        </a>
        <a
          class="mod_copyright_auth_ico mod_copyright_auth_ico_3"
          href="http://www.cyberpolice.cn"
          target="_blank"
          rel="noopener noreferrer"
        >
          网络警察提醒你
        </a>
        <a
          class="mod_copyright_auth_ico mod_copyright_auth_ico_4"
          href="https://search.szfw.org/cert/l/CX20120111001803001836"
          target="_blank"
          rel="noopener noreferrer"
        >
          诚信网站
        </a>
        <a
          class="mod_copyright_auth_ico mod_copyright_auth_ico_5"
          href="http://www.12377.cn/"
          target="_blank"
          rel="noopener noreferrer"
        >
          中国互联网举报中心
        </a>
        <a
          class="mod_copyright_auth_ico mod_copyright_auth_ico_6"
          href="http://www.12377.cn/node_548446.htm"
          target="_blank"
          rel="noopener noreferrer"
        >
          网络举报APP下载
        </a>
        <a
          class="mod_copyright_auth_ico mod_copyright_auth_ico_7"
          href="http://www.shdf.gov.cn/shdf/channels/740.html"
          target="_blank"
          rel="noopener noreferrer"
        >
          扫黄打非网举报专区
        </a>
        <a
          class="mod_copyright_auth_ico mod_copyright_auth_ico_8"
          href="javascript:;"
          target="_self"
          rel="noopener noreferrer"
        >
          适老化无障碍服务
        </a>
        <a
          class="mod_copyright_auth_ico mod_copyright_auth_ico_9"
          href="http://ggfw.cnipa.gov.cn:8010/PatentCMS_Center?fromsite=www.jd.com"
          target="_blank"
          rel="noopener noreferrer"
        >
          国家知识产权公共服务网
        </a>
      </p>
    </div>
  </div>
</div>

<script type="text/javascript">
function footerRender (){
  function getClstagPrefix(){
      var $clstagEles = $('[clstag]');
      $clstagEles.each(function(){
          var fullpoi = $(this).attr('clstag')
          $(this).attr('clstag', pageConfig.clstagPrefix+fullpoi)
      });
  }

  function getCopyrightTxt(){
    var $copyrightEles = $('.copyright_txt');
    $copyrightEles.html("Copyright&nbsp;©&nbsp;2004&nbsp;-&nbsp;"+ new Date().getFullYear() + "&nbsp;&nbsp;京东JD.com&nbsp;版权所有")
  }

  getClstagPrefix()
  getCopyrightTxt()
}

footerRender()
</script>

</body>


<script type="text/javascript" src="//misc.360buyimg.com/mtd/pc/index_2019/1.0.0/static/js/runtime.js"></script>

<script type="text/javascript" src="//misc.360buyimg.com/mtd/pc/index_2019/1.0.0/static/js/index.chunk.js"></script>

<script type="text/javascript">
    window.point.js = new Date().getTime();
</script>
<script defer="defer" async type="text/javascript" src="//static.360buyimg.com/item/assets/oldman/wza1/aria.js?appid=bfeaebea192374ec1f220455f8d5f952"></script>
</html>
': failed to load external entity "<!DOCTYPE html>
<html>

<head>
    <meta charset="utf8" version='1'/>
    <title>京东(JD.COM)-正品低价、品质
>>> 
=================== RESTART: C:/Users/HP/Desktop/autoxpath.py ==================
Traceback (most recent call last):
  File "C:/Users/HP/Desktop/autoxpath.py", line 6, in <module>
    tree = etree.parse(r.text,etree.HTMLParser())
  File "src\lxml\etree.pyx", line 3521, in lxml.etree.parse
  File "src\lxml\parser.pxi", line 1859, in lxml.etree._parseDocument
  File "src\lxml\parser.pxi", line 1885, in lxml.etree._parseDocumentFromURL
  File "src\lxml\parser.pxi", line 1789, in lxml.etree._parseDocFromFile
  File "src\lxml\parser.pxi", line 1177, in lxml.etree._BaseParser._parseDocFromFile
  File "src\lxml\parser.pxi", line 615, in lxml.etree._ParserContext._handleParseResultDoc
  File "src\lxml\parser.pxi", line 725, in lxml.etree._handleParseResult
  File "src\lxml\parser.pxi", line 652, in lxml.etree._raiseParseError
OSError: Error reading file '<!DOCTYPE html>
<html>

<head>
    <meta charset="utf8" version='1'/>
    <title>京东(JD.COM)-正品低价、品质保障、配送及时、轻松购物！</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=yes"/>
    <meta name="description"
          content="京东JD.COM-专业的综合网上购物商城，为您提供正品低价的购物选择、优质便捷的服务体验。商品来自全球数十万品牌商家，囊括家电、手机、电脑、服装、居家、母婴、美妆、个护、食品、生鲜等丰富品类，满足各种购物需求。"/>
    <meta name="Keywords" content="网上购物,网上商城,家电,手机,电脑,服装,居家,母婴,美妆,个护,食品,生鲜,京东"/>
    <script type="text/javascript">
        window.point = {}
        window.point.start = new Date().getTime()
    </script>
    <link rel="dns-prefetch" href="//static.360buyimg.com"/>
    <link rel="dns-prefetch" href="//misc.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img10.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img11.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img12.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img13.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img14.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img20.360buyimg.com"/>
    <link rel="dns-prefetch" href="//img30.360buyimg.com"/>
    <link rel="dns-prefetch" href="//d.3.cn"/>
    <link rel="dns-prefetch" href="//d.jd.com"/>
    <link rel="icon" href="//www.jd.com/favicon.ico" mce_href="//www.jd.com/favicon.ico" type="image/x-icon"/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>
    <meta name="renderer" content="webkit"/>

    <!--[if lte IE 6]>
    <script src="//misc.360buyimg.com/mtd/pc/index/home/ie6tip.min.js"></script>
    <![endif]-->
    <!--[if IE 8]>
    <script src="//misc.360buyimg.com/mtd/pc/index_2019/1.0.0/static/lib/polyfill/index.js"></script>
    <![endif]-->

    <link href="//misc.360buyimg.com/mtd/pc/index_2019/1.0.0/static/css/first-screen.chunk.css" rel="stylesheet"/>

    <link href="//misc.360buyimg.com/mtd/pc/index_2019/1.0.0/static/css/index.chunk.css" rel="stylesheet"/>
    <script type="text/javascript">
        window.point.css = new Date().getTime()
    </script>
    <script type="text/javascript">
        window.pageConfig = {};
		//灰度区间统一配置
		window.pageConfig.hashList ={"research":[{"start":"0","end":"10000"},{"start":"10000","end":"10000"}],"navitems":[{"start":"0","end":"0"},{"start":"0","end":"10000"}],"treasure":[{"start":"0","end":"10000"},{"start":"10000","end":"10000"}],"floor":[{"start":"0","end":"10000"},{"start":"10000","end":"10000"}],"schoolFloor":[{"start":"0","end":"10000"},{"start":"10000","end":"10000"}],"top":[{"start":"0","end":"10000"},{"start":"10000","end":"10000"}],"recommend":[{"start":"0","end":"10000"},{"start":"10000","end":"10000"}],"channels":[{"start":"0","end":"10000"},{"start":"10000","end":"10000"}]};

        // 大促配置
        window.promotional = {};
        window.promotional.enableShowToolbar = false;

        window.pageConfig.enableShowSpecialTop = false;

        window.promotional.enableShowTop = false;

        window.promotional.actTimeStart = new Date('2022/05/23 14:00:00').getTime();

		window.promotional.actTimeEnd = new Date('2022/06/20 23:59:59').getTime();

		        window.promotional.atmosphere = {};

		window.promotional.atmosphere.background = 'jfs/t1/175008/40/24062/2774/62871bf5E90bce82e/ce484c2ce3c9c8da.png';

		window.promotional.atmosphere.desc = 'jfs/t1/184633/20/25322/3751/6287380eE54718a8e/288c72d11132fb3d.png';

		window.promotional.newEnjoyType = 'S2';

        // 兜底数据
        window.backup = {};
        //logo
         window.pageConfig.logo = {};

        //直通车
        window.pageConfig.treasure = {};

        window.pageConfig.treasureb = {};

        //企业定投直通车
        window.pageConfig.treasureEnterprise  = {};

        //背板
        window.pageConfig.background = {};

        window.pageConfig.shortcutCompanyConfigType="default";
window.pageConfig.headServiceType="default";
window.pageConfig.headSiteNavType="default";
window.pageConfig.headShiLaoHua="true";
window.pageConfig.enableGraySwitch="false";
window.pageConfig.cateType="default";
window.pageConfig.enableJquerySwitch="true";
window.pageConfig.enableFooterConfigSwitch="true";
        //企业背板
        window.pageConfig.backgroundEnterprise = {"bothBgPic":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/109040\/35\/30908\/41245\/62e727caE16216303\/25329f665ad10e38.jpg","href":"https:\/\/pro.jd.com\/mall\/active\/3y1FpcGL5htF5QLw7ShgEZkKV9WQ\/frist.html"};

        // 页面配置
        window.pageConfig.enableActMark = false;

		window.pageConfig.clstagPrefix = 'h|keycount|';

		window.pageConfig.O2_REPORT = 100;

		window.pageConfig.serverTime = new Date('2022/08/01 16:29:02').getTime();

		window.pageConfig.actStart = new Date('2019/10/18 00:00:00').getTime();

		window.pageConfig.actEnd = new Date('2019/11/15 23:59:59').getTime();

        // 手机京东
        window.pageConfig.shortcutMobileData=[{"title":"\u624b\u673a\u4eac\u4e1c","desc":"\u65b0\u4eba\u4e13\u4eab\u5927\u793c\u5305","img":"jfs\/t1\/67481\/15\/565\/28110\/5cec9234E71c47244\/dc4cf353fd96922e.png","url":"","devices":[{"type":"iphone","src":"https:\/\/itunes.apple.com\/cn\/app\/id414245413"},{"type":"android","src":"https:\/\/storage.jd.com\/jdmobile\/JDMALL-PC2.apk"},{"type":"ipad","src":"https:\/\/itunes.apple.com\/cn\/app\/jing-dong-hd\/id434374726"}]},{"title":"\u5173\u6ce8\u4eac\u4e1cJD.COM","desc":"\u62a25\u5143\u7ea2\u5305","img":"jfs\/t1\/133427\/32\/6189\/44062\/5f2a5467Efff804d1\/7cbc252ed5993190.png","url":"","devices":[]},{"title":"\u4eac\u4e1c\u91d1\u878d\u5ba2\u6237\u7aef","desc":"\u65b0\u4eba\u4e13\u4eab\u5927\u793c\u5305","img":"jfs\/t1\/36947\/5\/10895\/15408\/5cec924bE6c038530\/5cf21582b416c186.jpg","url":"https:\/\/m.jr.jd.com\/integrate\/download\/html\/pc.html","devices":[{"type":"iphone","src":"https:\/\/itunes.apple.com\/cn\/app\/jing-dong-jin-rong-hui-li\/id895682747?mt=8"},{"type":"android","src":"http:\/\/211.151.9.66\/downapp\/jrapp_jr188.apk"}]},{"title":"\u4eac\u4e1c\u5065\u5eb7\u5ba2\u6237\u7aef","desc":"","img":"jfs\/t1\/93019\/8\/17752\/28300\/5e8c23b8E4c6c7c13\/9c45c518ad785873.png","url":"","devices":[{"type":"iphone","src":"https:\/\/hlc.m.jd.com\/download\/?downloadSource=jdh_JDcom"},{"type":"android","src":"https:\/\/hlc.m.jd.com\/download\/?downloadSource=jdh_JDcom"}]},{"title":"\u5173\u6ce8\u4eac\u4e1c\u5c0f\u7a0b\u5e8f","desc":"\u65b0\u4eba0.1\u5143\u8d2d","img":"jfs\/t1\/170279\/40\/10824\/19657\/6045bf7dE610d6258\/3e925badd90757a3.jpg","url":"","devices":[]}];

        //今日推荐
        window.backup.today=[{"alt":"\u4f01\u4e1a\u5f00\u5de5\u5b63","ext_columns":{"biclk":"1#a889a3b4cf7bd9198608242923b049cfdec968df-103-619066#43494363","focustype":"s","ap":"K7+n7uMbemcyifAhDdq5Ig==","mcinfo":"03652902-17044221-8101610722-M#0-2-1--59--#1-tb-#102-43494363#pc-home","url":"https:\/\/pro.jd.com\/mall\/active\/33FkET36YNBaCuLwF3GqnCbLr4uT\/frist.html?babelChannel=ttt2","desc":"\u7cbe\u9009\u7206\u6b3e","text":"\u4f01\u4e1a\u5f00\u5de5\u5b63"},"src":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/6851\/13\/21644\/93283\/61f50444Eebe6975f\/03dee49c7825b83d.png","gid":"03652902","href":"https:\/\/pro.jd.com\/mall\/active\/33FkET36YNBaCuLwF3GqnCbLr4uT\/frist.html?babelChannel=ttt2","srcB":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/6851\/13\/21644\/93283\/61f50444Eebe6975f\/03dee49c7825b83d.png","type":"material"},{"alt":"","ext_columns":{"biclk":"1#a889a3b4cf7bd9198608242923b049cfdec968df-103-619066#43494363","focustype":"s","ap":"p7XPj53+XCTIQN3wwN6XDg==","mcinfo":"03652902-17044221-8101611040-M#0-2-1--59--#1-tb-#102-43494363#pc-home","url":"https:\/\/pro.jd.com\/mall\/active\/DMQAamMysqjZ7ZDWHFTBc6ocHAv\/frist.html","desc":"","text":""},"src":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/116864\/1\/21079\/53025\/61ff9962E196a5844\/c1b0bcc5845ad614.jpg","gid":"03652902","href":"https:\/\/pro.jd.com\/mall\/active\/DMQAamMysqjZ7ZDWHFTBc6ocHAv\/frist.html","srcB":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/116864\/1\/21079\/53025\/61ff9962E196a5844\/c1b0bcc5845ad614.jpg","type":"material"},{"ext_columns":{"focustype":"g"},"type":"ad","href":"https:\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9scHMuamQuY29tL3BjL3BzcC81MDE3MDExP2ltdXA9Q2g0S0dPVzV2LVczbnVTN2dlUzRtdVNfb2VhQnItZW5rZWFLZ0JJQUdBQVNHZ2l6bTdJQ0VQT2E2OXdER2dodWEzbDRlWEY0Y3lEQUJpZ0JHTm9oSUFBcUlHbGlMSFZoTEhoblpTeG5hV0VzWTJsbUxHWmZZbUZmWm14ZmJERTJNek00TWdKcFlrcW5BVWw4VTBoVlRsUmZTVUlzU1Y5QlgwWk1YMElzU1Y5QlgxSkZYMElzU1Y5QlgxQk1YMElzU1Y5QlgxTk1YMElzU1Y5QlgwTlRYMElzU1Y5QlgxSlRYMElzU1Y5VlgwWk1YMElzU1Y5VFgwWk1YMElzU1Y5U1gwWk1YMElzU1Y5UVgwWk1YMElzU1Y5SFgxSk1YMElzU1Y5SFgxaEhYMUlzU1Y5Q1gwWk1YMUlzUjBsQkxGaEhSU3hWUVh3N1JueE5TVmhVUVVkZlJsSXNSbDlDUVY5R1RGOU1NVFl6TXpoOA&log=GAzYUXYleBiYx0yi3tCBS_1z9BscamtkMEa4naoSoI8F4fSENdrxcaC38YMbZREFpsXjXNB4_Ypm53RtKSHBrazQvD1ci4f4r3NxR-yU37iCyPP0Nx3Ksdo9hVXBwTt3HNCuZKimPzdqV8DuXlDgrFWcxkJOjuSYNOSTOKruMd5nib6Ke85jPV59_TNBOxLuz40xpc0K52c5pb2BW-CidRAwuvEJ2UV2pu2ACc5TnQYOoIFfvqnq_pjIGT5OzW1vmGodybyGxpjZPg5LOzlzGCmErNpxLG8KmmtZuAHBwJv5a6hRyJMefh3cM2PX42YYmRUhyd1ZWU3KNsK4cmpbU1tiwiDP09sYWdIH1PwB6Xc4YYmcK-kfjde6dbUWd03FaALzdP9hAl1Mlx8Kpt3WxbXQSV6bYzerVLLN7Yxsp7V--fI1C5uABMVtDvu0dVwlkn514XsVQ-PoyMoyTYItSW4k_7U7MrhCBHtupFLJo6EDu1ZZ0r5CUAQ4jUaeQKpwflnnm2IvkrMdtXbxQEmcro5wxUC1XBhINeohtirkRbGkoyIsQ_2tx-EcXDmU7VWrN76AjLom69JO5Dg6bn1Nln7UWlXCXVjkUPnw6VasWvMVFLomIju6G2gv9pJ-6LbxbmwZQQqzSOHa2LENDMNoiw3UcfWYInAXwkzkyyjMV6AOgeUhU_tvmcjpEwiY9a_0KqHNs5Iq2wzhfbwezNb7mEjMJj3tSASBdppSEShPAn2-t9aBir0DnNhKXZNc2Q3-36CF8Lm0n7w34cs61JbOZTY5NkTeTgJ7YHVUMyH_6Srjt7Yu45-S8_bZrM8Bvu59zI8SfGdwY9lOqh6xtVov3aNHrKsb_1t8E0B1qQcJqU7uxoLs8xe8rQbso2IZ_zoomIHHLUBw_jh09gmx_QfALz0KFHgMWW2Y7PUhz-zc9BDl79oyrvk9UWrxdFX9M5hN-QLGcnpTw9U8LpxLP8zWO1NwaoJBvVx1DT4oKx65OQznXSWxxrAyK3lhHjbpUKByLwsS-x94Pj4G6Vh-_D_x-sH_wRLNOgrz11q2hygreZYQaAFP-EdREzDYm5impKFX1zbwTQ1jMLYvsx5a96hOHCRh-pnpPDuJ4H3bFLyPJLnW-B-hsPwNC7zOd4SWlw90&v=404","src":"https:\/\/img1.360buyimg.com\/da\/jfs\/t1\/104009\/20\/18514\/63913\/5e94f1a7Ef66e61f6\/5c41baf664c71c25.png","clog":"https:\/\/im-x.jd.com\/dsp\/np?log=GAzYUXYleBiYx0yi3tCBS_1z9BscamtkMEa4naoSoI8F4fSENdrxcaC38YMbZREFpsXjXNB4_Ypm53RtKSHBrazQvD1ci4f4r3NxR-yU37iCyPP0Nx3Ksdo9hVXBwTt3HNCuZKimPzdqV8DuXlDgrFWcxkJOjuSYNOSTOKruMd5nib6Ke85jPV59_TNBOxLuz40xpc0K52c5pb2BW-CidRAwuvEJ2UV2pu2ACc5TnQYOoIFfvqnq_pjIGT5OzW1vm9wMFMUIdcSqGleQ7DBERpB23DfOdDkfBgrEcyPckgwSOGz6_ea1d3RhiQ0RfaT8i9FfpupZbQSJUJ9Ka-ZQ2JXZbXkKX5LpsFFDBo1MkUcGWMD5MmFmX4YNfWTVijMbXuF6rsUKQept-5qNj1h0EXrt_nLI9-8-yGsh0kOlHbtDPhBImL0D2ATTMocFmNNClp8Ku3y9wAn9b4KEzzGYXr4YxPjmkCP4B4XxXXmxAOba0eudmGHtheAO6ZaHNj9IB9zzoSvFYPCMdVnRI5MiH9PIFalXjQpicQAkHCWzlfutKJYMTUf0EFYwrYr-WKcIWI8fCQ-d7ypUPe-zrC5iTXcF-1uFtusPEFkmLHMQ6YO5XXy6NSO465S11eVyVDf3nsRYE60H9kgrysqWPSW6g50BMlDBQFD2QyDsyXVw-OTWNd6p5QpdLa6nut_x-MaQwmHbMmwajW3cBTIBFRSCZg3i88J0ECjnmNcf-B30FGEGvPGIfyIDzaenYvdaA1DpHsOobR1faNHgJURHZP0Y52sqa0OfdnDpD5D4B0s96YbRfOCCh_UIsEGLtgcT2ohcmLjhJRGhTIDN-GjgFZfURlusSJ-aCA6e_POrD80CCOAkiXeBxZpZV_dgu3P5uEC9JdenLqNEbXcrZnmQCacb9iCg7cCdjDNzN0m57lah9sffuP9uRdA5YOjvQ7e3F-tiihHvIxWVJV5f4LYXHcSq0A8newQoDu59EgWnjC218SmjhtnqPQNMk_Z6vxh3ZuDIM_UhVVwY_YyfNlTCuxQgf4ACHT4j37Frwt8-tLHkwYS0gj6ixux5dEg_0DCIttDOtzrEIAJZgLluCwBxfmc-64AHTHO7IIxC-ic3cG8LiTqVpx239kby0Q6-B-ZLl_kY&v=404&seq=1"},{"ext_columns":{"focustype":"g"},"type":"ad","href":"https:\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9scHMuamQuY29tL3BjL3BzcC85ODQyMjI_aW11cD1DaDRLR09XNXYtVzNudVM3Z2VTNG11U19vZWFCci1lbmtlYUtnQklBR0FBU0ZRaWVpVHdRcE1EcjNBTWFCSGhuWkhvZ3N3VW9BUmphSVNBQUtpQnBZaXgxWVN4NFoyVXNaMmxoTEdOcFppeG1YMkpoWDJac1gyd3hOak16T0RJQ2FXSktwd0ZKZkZOSVZVNVVYMGxDTEVsZlFWOUdURjlDTEVsZlFWOVNSVjlDTEVsZlFWOVFURjlDTEVsZlFWOVRURjlDTEVsZlFWOURVMTlDTEVsZlFWOVNVMTlDTEVsZlZWOUdURjlDTEVsZlUxOUdURjlDTEVsZlVsOUdURjlDTEVsZlVGOUdURjlDTEVsZlIxOVNURjlDTEVsZlIxOVlSMTlTTEVsZlFsOUdURjlTTEVkSlFTeFlSMFVzVlVGOE8wWjhUVWxZVkVGSFgwWlNMRVpmUWtGZlJreGZUREUyTXpNNGZB&log=GAzYUXYleBiYx0yi3tCBS_1z9BscamtkMEa4naoSoI-CJarMJhq6_agQ762Wvx24jWEpt2TB8lW0fsIYlP4Fe-seuZoGZlp6l8wgBEGBCrnpg3X_k-a_n-DwR0gszKeuhP2dFWx5X1KFBBnt2O_11cwDJ8_olKV3TM1s9e43ULmOHGBMHBCwE141418YwuCuujf2Be2NohSbNu1LI8p2y_tLKno3b2dW2MjLtvcLN7vItTry-ohHHcwC7H32MnTQ0WSiuw91rbCrNqpzSl8XWQEqTyusHQDJvQpxzel7FBUwg1nvs5o4wdkl_zLEfRGXmuAv9fXxmsBHvq8SMDZ-XhllnkemJnRwLf0GFTHuQz13m-YRl_Q7Z4TSNxX80LBbr79MC7fbkpFrOWqV3imz0bNkmyZXRvyNUxzK1ZEczJqOH4Y-DZDOsDH8HC_xaYD9zBYZqyMb0HkTLz2E2zMVUECw0sQam5QJ7Fl1Sk3W_G2ZtA3-3D2_HUQm2MBO6pTNknOgp38W3Pk3qzM3Ilvc2sOBaPAcUlCg_12fCdUIs6YTKSMvsKbmQOQUvGMDNX1acDc1m-RYyed9Ws1A_4UljrZCWXXR3awKfg7_1A5RA5OxKusLaF8uAzGBW4GLVyVPp6bzOcGX38F7-pebU6syqF9XTkoTd8S4-oTepaNYwLo89BY1S5y3TwYkDpZPImNJa-XJEEkDI9Ok3iPG0OysFE8rcCoGxGdVQRXIroxef0FbrbbekRb8CfGJUqt8c_4zFIsiESHn5PAqhCpzWsbtCTn-2mCiXskQ9FW_N4T41wR8QU8nqRWbUFlErK5TCjEf_0qZvxrl9BAr_Yc8cLM6Mt--rPpdB9zJ7NprZHwFebNDBGP6dmDpLvSelXhNnUS69xIsA7mJlE_8UcRSLsQlcAoaT9yOmrzoeHwbGwcu7vqTzPq_gaTyzOlXxpiefflWsF5dcxUguhmP9ZmLnwks9jTJVYikn8LTrM-lSAWNb3YuvwyKPI8T1ZJCQWtt0Bg-o4IDoNXiBknLwOhuamnmcfUtt0wpsBSZYyqGv-Nct-Kd2lCuo5IiFh0XXHJV9PVb59EkFL_tcuLaJOIHbuDYBIHpgem8qWqJii2Dl8GoAeg&v=404","src":"https:\/\/img1.360buyimg.com\/da\/jfs\/t1\/65519\/18\/5109\/86986\/5d349331E52fea75f\/5671237d9584131b.png","clog":"https:\/\/im-x.jd.com\/dsp\/np?log=GAzYUXYleBiYx0yi3tCBS_1z9BscamtkMEa4naoSoI-CJarMJhq6_agQ762Wvx24jWEpt2TB8lW0fsIYlP4Fe-seuZoGZlp6l8wgBEGBCrnpg3X_k-a_n-DwR0gszKeuhP2dFWx5X1KFBBnt2O_11cwDJ8_olKV3TM1s9e43ULmOHGBMHBCwE141418YwuCuujf2Be2NohSbNu1LI8p2y_tLKno3b2dW2MjLtvcLN7vItTry-ohHHcwC7H32MnTQbuspoohbCGR5W77K4uX6JU3jKd0rINTxk70lAYmurUFNjb-BvvKvwQjsqHj2iXRVq6LJheU-nCPwUNkRSz7dGGxuyZoTfik4p_r2otcpi-JHG9MhAzFFjThvONi28IfKBCYqM__5Y8KM9FizlxdZrIN7JW_DhewNPz_41pameKPfrFd0FnfsZcy-vvyZCrTvb-4P_TkUt-mnjMVDNx5OJ8DUlUtPv2oA3YNgvzeuo95j8Ql12y7mFXxsg-SilVJMo_s67ZXnW9J9vL88hoSmnPp7Gq1oIVEDzhYY_2SfSEIVp-mE44HPidftXOjI9_KNQc0rTtuOny0-EvG_w4uR45t18GlSvvMDsemVK1_DtnLJ4mh0X7-MCQCGsOUWxMxGLl_-k1lf2K7DMTL6w3RpMf3rSAXRXFXUPPt6D4-Q1pXL4iJ1vU8BYkCOrrnrG5lgy9tA1Ev60tS-1l9M0UI6AEHN415TUVu-V0ZHwSoYbKdYPEoQm6vCNePdJXquM5QHgd_ohcIF97vuTdBX1OZKG1hRhv5Euysm_iK4y9c8AdecjndizrcyS1ix6Qs3lfIEL2uZiy6f9Pye8lwXnnAKy_5Ngc-p8XysQGG6ZzcBftY-E5sw6al9c_5JxJsIgrSza8qVlawtwzjg1Yk4ezNX73xnR7Btd6KpOlIQ8eSTgiPjRelco3rGJlXgU18JAYQPT6Hbhpzp6SWDvyBCjOflyBOgVU2uCRTclhBX2G6TOxPwIHBRarL6JQ-StOPQB6hH3lSlfgEXRFogBwaP9UsRLsovureecA-yWvsP6N5EzA7jhoWO-Rh5NcHJeTpLCDo8SeHboTS23XulEcaNOETdK90EA1X77cbkUpwRHHXrUwY&v=404&seq=2"},{"alt":"","ext_columns":{"biclk":"1#a889a3b4cf7bd9198608242923b049cfdec968df-103-619066#43494363","focustype":"s","ap":"j0Spnb54kus=","mcinfo":"03652902-17044221-8101611202-M#0-2-1--59--#1-tb-#102-43494363#pc-home","url":"https:\/\/prodev.jd.com\/mall\/active\/gi4Pq4ek5494Wu2stU11VwjK9iS\/frist.html","desc":"","text":""},"src":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/94432\/11\/20795\/78385\/62012655Ed228f0b7\/367cca04c2aa3077.jpg","gid":"03652902","href":"https:\/\/prodev.jd.com\/mall\/active\/gi4Pq4ek5494Wu2stU11VwjK9iS\/frist.html","srcB":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/94432\/11\/20795\/78385\/62012655Ed228f0b7\/367cca04c2aa3077.jpg","type":"material"},{"alt":"","ext_columns":{"biclk":"1#a889a3b4cf7bd9198608242923b049cfdec968df-103-619066#43494363","focustype":"s","ap":"z\/ep\/M8C9uoBBlITEyBAiQ==","mcinfo":"03652902-17044221-8101611231-M#0-2-1--59--#1-tb-#102-43494363#pc-home","url":"https:\/\/pro.jd.com\/mall\/active\/kdLV9FcYcKP6s7KdLRVcEPqrUrg\/frist.html?babelChannel=ttt2","desc":"","text":""},"src":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/87414\/17\/21797\/50526\/62010949E99c1a828\/71dc7e61d06f9a36.jpg","gid":"03652902","href":"https:\/\/pro.jd.com\/mall\/active\/kdLV9FcYcKP6s7KdLRVcEPqrUrg\/frist.html?babelChannel=ttt2","srcB":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/87414\/17\/21797\/50526\/62010949E99c1a828\/71dc7e61d06f9a36.jpg","type":"material"},{"ext_columns":{"focustype":"g"},"type":"ad","href":"https:\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9scHMuamQuY29tL3BjL3BzcC83MzAyNDM5P2ltdXA9Q2g0S0dPVzV2LVczbnVTN2dlUzRtdVNfb2VhQnItZW5rZWFLZ0JJQUdBQVNGZ2luMnIwREVPeWM2OXdER2dSa2JHUnpJS3NVS0FFWTJpRWdBQ29nYVdJc2RXRXNlR2RsTEdkcFlTeGphV1lzWmw5aVlWOW1iRjlzTVRZek16Z3lBbWxpU3FjQlNYeFRTRlZPVkY5SlFpeEpYMEZmUmt4ZlFpeEpYMEZmVWtWZlFpeEpYMEZmVUV4ZlFpeEpYMEZmVTB4ZlFpeEpYMEZmUTFOZlFpeEpYMEZmVWxOZlFpeEpYMVZmUmt4ZlFpeEpYMU5mUmt4ZlFpeEpYMUpmUmt4ZlFpeEpYMUJmUmt4ZlFpeEpYMGRmVWt4ZlFpeEpYMGRmV0VkZlVpeEpYMEpmUmt4ZlVpeEhTVUVzV0VkRkxGVkJmRHRHZkUxSldGUkJSMTlHVWl4R1gwSkJYMFpNWDB3eE5qTXpPSHc&log=GAzYUXYleBiYx0yi3tCBS_1z9BscamtkMEa4naoSoI_wQyoHBV5oLDP5wj4Lm6249pyEIshvL3a0kk99Gx7WEB0khRkNhmOPvlXQY7qpYl9u5K23WRZOEmU30WDXW_dlJFxaeh19H7rea1Gf6-JaTYjEhRWP8sjPpHXNVbzhYvVyMAhxWyCgQ5H6opF9C4aW5L0kllYbyAAfSMOgqLqcTDlZilc98ZpZINH6twfJb-haFi9wWch4y3iXjQ8_nEjnZeDvS2v77CDX_IyF-u_td7YRyLbHZadEeSWXKVJQ8CMBDkUvpnPSerEcD2HSdPuiGuqt4b7yTL5jJy_2GrQCxLfjJri6vssxeYnLfm0798OSvj-PA6YhqOPiaSBk3v58eqX1Ofaj9rCjKa5m45DaLQF0e6RggqoMtzrV8-YOCicxVbvrpDfHUmLwC9lKu2oO01ye_aDhMGiEgux6wdiCzjeBz0Q5iJsSVOYzMVFtkKOCfEuptI-azusJcusoGxfmT0L0hnR-XyB0xxnDhQ-XZhKYC-sVqbgmta5UhmKZGtpuPUyXhtvbtvFr2VWW30AHYd-bqB7IhwabIgcCrHzQSQ-8da_KsjpAJIHbQgXdaIRhhDqOxLQHdbuBpQFTcLTs-bRc0cLLfgEG7TlnHCSbPAgonxcZP3HtbtnYJgiVsncfq9YmspTpPR8rqivNflJqERGU5C_f8g07qepu2_xwFB6AS3SCD2MzHxErXDgDthZ-MzZQXLyv9rkIED2_1R_mtCmEHOmL234ie85-ceuPe4ba6gxjNnFJbUDc9lBy98uxle5zBHEGmLMrOgc18wisaNPjEoti3GmPGxTl6CkY-P9RvXUQ75sRU2hJcFmw9ye1Qeo-3ulNHV7Tvmek76J7Tqv-T-QP9a1ALGsMHG0UNxULUtvb0ajs7klneRy0jA_R3W1VZ2mRN9ythOCe_-b-QI_O9TPWHB25DgErWomr6C1JU1NKT69VYHzuEOhz70lOgEXe_-T8AgeLeKpMpaMdiFlkVdZ_3APferq4pwENbUY10anJWgwlpehckGwcsJkzOwa-Rj8eOufOY_u9TPJEHdzmQJ-BKEwGkr9MfqoBDHfl0wly1NRZ_uYRdmyfkqcFCmzbfKqtRhw0j2E9kEBq&v=404","src":"https:\/\/img1.360buyimg.com\/da\/jfs\/t1\/39535\/22\/12149\/77249\/5d337987Ea4fc5f10\/29ba50d1c1eca3bf.png","clog":"https:\/\/im-x.jd.com\/dsp\/np?log=GAzYUXYleBiYx0yi3tCBS_1z9BscamtkMEa4naoSoI_wQyoHBV5oLDP5wj4Lm6249pyEIshvL3a0kk99Gx7WEB0khRkNhmOPvlXQY7qpYl9u5K23WRZOEmU30WDXW_dlJFxaeh19H7rea1Gf6-JaTYjEhRWP8sjPpHXNVbzhYvVyMAhxWyCgQ5H6opF9C4aW5L0kllYbyAAfSMOgqLqcTDlZilc98ZpZINH6twfJb-haFi9wWch4y3iXjQ8_nEjnZANYZSU-C5r6PfQFDsmwPn-SdG2TPy5DFbOQxQios5sxrx9SY1NhtyC0VSEA1ArTsEkHVjPINaIBVv2FJV4pwrkG0XLKK6nqTZdLU_ZaqnkHgfamAniGNJU_bYp7VxS8DH8wLDDVLLexChHhtwkC8fuyx2oH8K_uKH66nE1xfW3yY-S-BFQ7Ol3QRskJ2rRsqVeLIaVEVuaB0Ru-G-guctz5I6zGAGvqsYa8A6iIepr-zm4DXRwmakAh4J_L-BxxZtCi6cGlN99Q7I77LIUrhdyFRPvwfILR0ZY7nAbv6e4zxLlC4LBWVRgfD2A4NWZWs1ailY3EdxKXZV0AF1xuZrTGrkrKuEsJMIEtqYuE1Qgv7Z92cjiGTzBTN58Q-oczXGqHf-aCLlj88lKvAI_-YeHKoAZcJz424cn3LxvFrlQbckkXYWeOQ2fe-xu9qIPuqhmhgg7AQScd1-eyZu8e3_7hvrcRrOM7o9DwxnbDESVLaJPCgElKBCcp8Qzs0Xp4nHNXJKbbU-XI4qwn98nOWfvej2jRfnXGx95Yy8WHzjZH2mcRg4ms-l1EtXhxI7jO1Y6K5sTiLsIyFfNyDD-JE00RPxAEPeXbNJt_-y2nXOid76NI_0XGHC4ReSk6w12_23ltmagvmUKPVmHZzn5omAAWx5CVmCKeEyUHf5XTyxikzJb-V6zkHnnynFw4Niw6Ui9kb6DELV8vh-26qmMefxOmxG59YRvHKa6I0LZRJqSM8prQUT5NhuAfYmwb2gZj3dRpMtA3-LYmVDmkEpWPKQtb17XPcWWSybfXsOxBfdkLnHolwJ0a8QH-EiE7OvrJ9Ay2-wlDlrt8TWV0JJLNXbsh4ZoWggqkBURybN2ZCpb1VgEkIwLvjVDinu2r_iJ_&v=404&seq=3"},{"alt":"\u5546\u7528\u5f00\u5de5\u5b63","ext_columns":{"biclk":"1#a889a3b4cf7bd9198608242923b049cfdec968df-103-619066#43494363","focustype":"s","ap":"9gLGFXP7q4f4h0Arqq\/GuA==","mcinfo":"03652902-17044221-8101610921-M#0-2-1--59--#1-tb-#102-43494363#pc-home","url":"https:\/\/shang.jd.com\/","desc":"\u5546\u7528\u5f00\u5de5\u5b63","text":"\u5546\u7528\u5f00\u5de5\u5b63"},"src":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/120972\/34\/22737\/59798\/61f5468aEcfcd30bd\/3e4c9f12dac8e80b.jpg","gid":"03652902","href":"https:\/\/shang.jd.com\/","srcB":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/120972\/34\/22737\/59798\/61f5468aEcfcd30bd\/3e4c9f12dac8e80b.jpg","type":"material"},{"alt":"","ext_columns":{"biclk":"1#a889a3b4cf7bd9198608242923b049cfdec968df-103-619066#43494363","focustype":"s","ap":"yxgo8R761YABBlITEyBAiQ==","mcinfo":"03652902-17044221-8101611201-M#0-2-1--59--#1-tb-#102-43494363#pc-home","url":"https:\/\/prodev.jd.com\/mall\/active\/34qAaUk6AW39g9BX6me3z2F6pYUG\/frist.html","desc":"","text":""},"src":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/116391\/11\/27363\/76966\/6200d724E4fde75ac\/861537c907516dbf.jpg","gid":"03652902","href":"https:\/\/prodev.jd.com\/mall\/active\/34qAaUk6AW39g9BX6me3z2F6pYUG\/frist.html","srcB":"https:\/\/m.360buyimg.com\/babel\/jfs\/t1\/116391\/11\/27363\/76966\/6200d724E4fde75ac\/861537c907516dbf.jpg","type":"material"}];

        //首焦兜底(新)
        window.backup.focusbak=[[{"sourceTag":"1","id":"4272","extension_id":"{\"ad\":\"\",\"ch\":\"\",\"shop\":\"\",\"sku\":\"\",\"ts\":\"\",\"uniqid\":\"{\\\"material_id\\\":\\\"7524724277\\\",\\\"pos_id\\\":\\\"4272\\\",\\\"sid\\\":\\\"c51c7210-55fe-490d-bd6e-77934590978d\\\",\\\"type\\\":\\\"1\\\"}\"}","ad_billing_type":2,"src":"https:\/\/img1.360buyimg.com\/pop\/jfs\/t1\/40588\/8\/17960\/59407\/62e34ddcE9dbbf4f6\/553bb2b4bf1dbc0c.jpg","ext_columns":{"desc":"2:cpd","focustype":"h"},"href":"https:\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9wcm9kZXYuamQuY29tL21hbGwvYWN0aXZlLzI1aUJxVlFBZFFoQkdLWG16TkFzVkFBS3JnWjcvaW5kZXguaHRtbD9iYWJlbENoYW5uZWw9dHR0MzU&log=J7VKdHOblx2yYoCF8mTyorxBoUXCXBt55SgR_Ve50AOK--g21GZQrgWKzpG6oPYwrnEQjBrW64C9-nQrzmwAQD9PRQxf3KicjbFoZU0iLRBj4aayQusQ2khvC4sAaV1Y5F70L1q_1EkWPDplShIXbu2AMS9abS5IwpmuM30WBa6Ax0SMkOMe0CtRvZi8ccpeMWwkHo2CBoM9fjSp49WVgRXowlGMvwEv9GLAFnzkN0vkC23KPC6RXV4WnDl7xvQeuAYjIAju8c9P45Ek7_0VHet7He0DottAh6-6BfMhoW59Zd61tgbRvqs-teY2WtasiJiKx5Vghyw4TSdUOhI9-3jf55TS-pOLoJL04kzvsLjpURkt4M0yzKtyAJpoeclALbsrfEnbe1QsH2sgYWjMFzGOaD8m6a6Necp9bV_FmP7AQgKNyXq3ZIYBQBYLM5YUtZd_Gr4M-vmZE-ya4j5j0dGOEqq7R_D85QHynTc_hZAzfvUZ78RxSxVzRYt4_M7XcK0xpjcrCbIh0lLq-A9yifKpufw2agBd3nTOjnczLwiAMmtZ3JSIbaV6KZV_2UpduD7Cv12ORfSEtx8W37569eU7OEdO4mUpcLtenWDYF_JRcs9AYL8WJtTjwr8kASF_3FbCx6kngKQRu_8kZEoB1KbKb82K65THXs9OYhcBmeUf39L8LlAQ5Zofe0bysy700n5I4VKTl8HYy6VyvbIw45SLVPWHs-3tN-79PDYZjfZ8p-0rg5sZmbwdTCUbQ8PdmUaXFyY4KOf7mZojdmyabmOtFK4GoJPsB9AP3qkVEH1X709b3qbwyIonrCBwepX4v56snZfK0Hzoipf5nXJymplHT6_-sPS_sI6JBf-qMxVrd1tYOYAcMQG70rxBkZRBZ4WR_4hXp4vricVlKiBxuVe-RUk_hhExqVQiQF0pOZ9MD_wAcxCexnu3aJm5jJqLdhqrsyplxr2OyIdxjhRsONe04cMH8Z28e-EPF9aO7ItqNnkuvRiuPyVA69BFbZwYNDLWAt4LZmz7R_R0YUQCnLtOMSZCa1R2YwjZwsF2Tyy7FsIbo7DQMKyT4gcJrreucUqHOL5LZZfSmNxZoPLCnZcslymVzxeHSmrBHCpiqxHaq1VvEa0kBP1vzBvE2UGPPZScPfE7C99UJIeoQnMorA&v=404","clog":"https:\/\/im-x.jd.com\/dsp\/np?log=J7VKdHOblx2yYoCF8mTyorxBoUXCXBt55SgR_Ve50AOK--g21GZQrgWKzpG6oPYwrnEQjBrW64C9-nQrzmwAQD9PRQxf3KicjbFoZU0iLRBj4aayQusQ2khvC4sAaV1Y5F70L1q_1EkWPDplShIXbu2AMS9abS5IwpmuM30WBa6Ax0SMkOMe0CtRvZi8ccpeQxDEoLG8ufyHTGQHzgn5sTEkIbBqYsAF9ps2-KStGDBKkE10jHZoICSsxqmtsAH-jFmohuSDELHXXL0DELmv8Q5zDmhqf5varYpsgoL-X_h2We-HSPMN-BgOiJC8wc9wrPk_lzRpbsr6GflRfpyUDoahXP5OKMtDtC4xkgmO0CQUzY56eATtzjHE9LAuEqdTgKc8Xg1e5M50szA1re_sq7XmVGrhC92Ti3UDqKBVV8FuTwJv__Jcyyc6yK-akKVI2CM6e2kYO3KZoeQBVX5ESqjkLbWByFf8eO5KBTrWpcoWJjHxarNDggN9pkyJSH32CtFqgEd98v8FMiL7QC3oxzfT_tr89yW3Ltk2tYTgSseZo5DHVUKZIi_dZZK3xBzjO_qwQ1ywT0vDj05ZZW_BRpP_CJMA9zeUDBWIuciZ8uHiXOxe-R1rlgy5PjQapfgWTu0f51hjYI8PVx2P-o96IIlqzq3KtcWIs0cG0PFm4B2jcl3eBGHhb5rvKdJHF-40f0dpePyF6yee99cmrjhe12hv9sBfF5CEvd_zLuc29LFVvrp_CMn5LfaUopuNDOGFOs2wuBwylb2swcnsPceouAEvLbSvPSym7bFcBLQLxzZI3hxkfDLOp20Ss2eiA93cd9aIssz__BaKUK51_NqgbCIhRrDHs9E5bWnTTh7ih9Mh_0lj5vIGzKfglem_OqN6fJGv1DOW5dTjbWv49LqIbdkOgDxU5putIv-S82YdlC1WgqzorUqmOx07Qv9myfv4nyUVcszEb9qiV_qAqKsSI9lld1J47ViXRCAEF6PiVVIbEBMcNFse2IDZkoFCP5Nb6iN-UCdyoke0W6E1LNx6wPwqtv8d_68LzxK_SD4bnHHmSmGHN5jtipHQ0XzMdW6p2KYS2Q2W5tY6XRaTmhPArmE5cTdSwsOPQVdaGqHX9384-7ar5Vzy04psuCanHUqIhXF6-Nsf0dO3Z7Tr0FStOEEycSLZdiNW7D6Rm7Nd3E8&v=404&seq=1","type":"ad"}],[{"sourceTag":"0","id":"3503","extension_id":"{\"ad\":\"3503\",\"ch\":\"2\",\"sku\":\"65615087817\",\"ts\":\"1659342394\",\"uniqid\":\"{\\\"material_id\\\":\\\"3414180806\\\",\\\"pos_id\\\":\\\"3503\\\",\\\"sid\\\":\\\"4cd953f1-15dd-4dbd-8e80-808ec26c67ef\\\"}\"}","ad_billing_type":0,"src":"https:\/\/imgcps.jd.com\/img-cubic\/creative_server_cia\/v2\/2000366\/65615087817\/FocusFullshop\/CkNqZnMvdDEvMTkyMjEzLzI0LzI2NjI2LzcyNTgwLzYyYzhhMWRmRTVhN2Y3OThlL2JjYjY0ZjFjYWNjZTkyNjEuanBnEgo5OTktdHlfMF8xMAE47ot6WMmR27f0AQ\/cr\/s\/q.jpg","ext_columns":{"desc":"0:cpc","focustype":"g"},"href":"https:\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS82NTYxNTA4NzgxNy5odG1s&log=GeL0MvrWnYnhLpecixvWpdpkpeCJ6uzY8mDE8DLcpnQeMOWEPXOI-CES7c9_I2aGdrEY4udLmsWD0dDd4aIMvqHc1mTemk_9XJ85iaVMY7vuvDb9FQyzmXfs_oB1703hi_gRq--BLNRhZKePuC8Wuv6doXUTB4LaBeDXNTXSyUVNhcjqG4biWhnWMgO3_tcvlD0sXbMjulLFgCpTE0AS2dH1E16MiLlYmIIDqz6J69GDYxW_WBVcKf7oMQeyGWIN7PRjQ8pYo1pW7ZNYTaiX8UdCNJrh5l5oHLMyxgQKKY2Qb14CuqVILGCeTAaIdWTZpmjxFzyp8B0X10YA_s0affcxJ2UG7w7lwmqBO20hiIXDiIJgODFC3vH87pPCxHwHSZTLDwof3hn88NRB5epd8qwPMQS22T-KafHA5rx3aapEtwvgQUOc3CTNY0a33eI4GhmHaokr3RnIwxFGpCEn98IEkvE22nYAjxypnhXE3l_vt8CEdY5DOqcGYVAIQoSNJpR5A_Gx2GozLabA52tzsK9mIMzgn4VdVTqxZl4o9CghgRAdal-66ZRgO565LL9XdJRiHBqpeaexa9wi3h1Xza7tPe1oPIskADmbZ8zIVX0kne6i5kT9rPJ-xXiblnx1pr6lh87FexM8oFj-M5bHXD3e-phahwApAcmAv77yqRN5j8R7sbviK8__3wIao6unlNC6bTd3Prib5WWPW1O8Lcua9WQR6vISPNxy-CtX3RpSEPPtbhrudljYrJNrvqIOsESIQ5Pjj21weB9LLZPsvFs5DOpm2un0vFH33Kw6XtIWeQbHVTIQQAQQGbny7jxjifKQq6EPbpSTMmRe5Ht6F3HnklgsPrdDS_58fk2SFdESDYBh3CEBXAM83rnG2Ow0XtW3F_kYH-yFnCoCdWsYOJcH7zriMvOJKvtp-XyVsP2-wqYcMHE2Op_rU4TBg3ODEVj37nPajoWtpmsnmuZRo-dSwrrUge8Sxh6nj2qe5Zfyu6zIu3xKgw47kM2d-qRNQllIE6jNcRLwj0yPzKBH4rhSkVeKNmqE7OrftAqGnFzwbtK8F1iA8gTyD8ZSyTID6EEJvs2uuzPVBqoxPqaTHV4IVkW7r_a3qhYdnNLbm1B4-njJyqGP4KSU_tnmvi-92ArbQbGSM7SqzIDRzueYGfsDVq-Fzj2hW11Bfd2RhXJWIw2BmbGz-tJ_PAM9DdQ8WD3n_-HEDh-e6-sIXMgl_yPrDhnLKNBjuEv9T2XY5idn7fMEhl848bAbVq8h1CxcRGSnZSnXyr9qqubCwB2HrGvtwqSieWhXML_TjkB-I_j4miB4tfV0CdpXsXbC_YbI&v=404","clog":"https:\/\/im-x.jd.com\/dsp\/np?log=GeL0MvrWnYnhLpecixvWpdpkpeCJ6uzY8mDE8DLcpnQeMOWEPXOI-CES7c9_I2aGdrEY4udLmsWD0dDd4aIMvqHc1mTemk_9XJ85iaVMY7vuvDb9FQyzmXfs_oB1703hi_gRq--BLNRhZKePuC8Wuv6doXUTB4LaBeDXNTXSyUVNhcjqG4biWhnWMgO3_tcvlD0sXbMjulLFgCpTE0AS2VByK-L5k9-wqkV1iGqiu7pBly2PdMVDjlNM04hbKthNjquRKV_o9XPR1De8GRkYBGTsL5RQu53OfbK7crvrJ5Fei9ZCDLF7M8mTA0yHiKjZm8wGYNORhFsiABQO7z78sSjElTpe8pzV1PSu6mfgUlEiK6JBSJbRtB6KQ864BK23zlSBt4-oO53foLbX7lHUInW79w_ZwikSU1NnTrtJX8VbMyWhv7_r2axlBlIMVfUnubEmEhqUKxBFNWltMSFOE5tz9rTQsqmGZKHXbpYI3qXgJIhzivQzCzu_3z__t4ssJsMIotXI3RxahdGrT0jRdXNxHHOErGB3FwXHdw4yLBcXGmNABNzty_gnSbnwW3v8_GWR394Qen4_S3YyhtyUjRAGWcXSPBruaQox3xS32dPvjP78LAhO42qPNGtX5CoyBp5b50FfO_eRss5M1zMssryky_fhtBkd0dmiyVNog_W1CasMm-eZbnM8C4a8oVuqzHSAV9eMMNDsVzOFh6luDdzaN5icaVZY_w5_PInZ8ampjZTscTVnUiEv09qdmRYFzJRINc3vnAmBtrVyFTwIZOT7dYF9Bvt2A1kk1zSxG35EUTgmLHCZ-z6-9NYreBmdU5VcDJNQ8bK4ySmoEfBxleRxcicw_nAne5ZUGUZ1zGM6JJXdCtF0nBlGeGOXwCjYw2EPNdH9i7YSZC11H1fUukUuYqy4RMKrzYpx7EWprLq1wDRbVWuxTncBdxMZAoTxNlfyVTSVe4NSbIdFECamq-xaRyULwIM_e5LIMyQr1LYpNpRqLTRDEiPtA97NyUB5Gpc1uuzeNEqnFaczuNZeFuCs2MU9KIUsrmP7maYS0bO6Fnmj-3KRNu1C9nzRaqJdTiQjpuUFTs4yKB0jBmfvLOmz3og6Dr8I5o4G46Xk9FgdZH9vx3uyjkIuWrIISmGApMJRd_0qHm6NTyKvxx2rcO0EQclsfeuOaTGIigLm6Srp3m3TbPfePrJVV1tbjIcY4H7xhWYpN7QFiYdFG3-q8VJtGqIirI7vDpd-JIZu1Cp2JtESLklS2dgklgwAhlhwqI8fC6axqz_FovDXFvt2bodbkZupQprfAxvU4zYyVuy2xq-5iMGveP3VSX0B0EeO&v=404&seq=1","type":"ad"}],[{"sourceTag":"0","id":"3504","extension_id":"{\"ad\":\"\",\"ch\":\"\",\"shop\":\"\",\"sku\":\"\",\"ts\":\"\",\"uniqid\":\"{\\\"material_id\\\":\\\"9193291134683590113\\\",\\\"pos_id\\\":\\\"3504\\\",\\\"sid\\\":\\\"6c42d09b-865b-43f1-9b5f-63a74eeb9f58\\\"}\"}","ad_billing_type":0,"src":"https:\/\/imgcps.jd.com\/img-cubic\/creative_server_cia\/v2\/2000367\/100038597306\/FocusFullshop\/CkNqZnMvdDEvMTg3Mjc5LzMyLzI4MjA0LzQyMzk5LzYyZTZkNTY2RTQwNDIwZDhmL2U2YzFmNDE0MmYwYzA2OWQucG5nEgkzLXR5XzBfNTQwAjjvi3pCHAoY6YKm5YWI55Sf5pm66IO95pm-6KGj5py6EAFCFgoS5a6e5oOg5LiN5a656ZSZ6L-HEAJCEAoM56uL5Y2z5oqi6LStEAZCCgoG5Yqb6I2QEAdYurWP1vQC\/cr\/s\/q.jpg","ext_columns":{"desc":"0:cpc","focustype":"g"},"href":"https:\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9scHMuamQuY29tL3BjL3BzcC8xMDAwMzg1OTczMDY_aW11cD1DZzBLQjNaaGMzUjZkMm9TQUJnQUVoNEl1cldQMXZRQ0VLR2w4ZHdER2dsb1lXOTVhV1JwWVc0ZzctNEJLQUVZc0JzZ0FDb21iV2w0ZEdGblgya3NkV0VzZUdkaExHZHBZU3hqYVdVc1psOWlZVjltYkY5c01UWXpNelF5Q0cxcGVIUmhaMTlwT2pBS0NrMVNZbTl1WkRjd01EY1F3TW9vR0FNZzRkdkFfTUt5eU1wX0tLRFMtamN3bjlMNk56Z1RRSUNBSUdBQ2FBRks0UUZKZkUxSldGUkJSMTlKVWl4SlgwRmZSa3hmVWl4SlgwRmZVa1ZmVERFM01URXhMRWxmUVY5UVRGOVNMRWxmUVY5VFRGOVNMRWxmUVY5RFUxOVNMRWxmUVY5U1UxOVNMRWxmVlY5R1RGOU1NakV6T1Rnc1NWOVRYMFpNWDFJc1NWOVNYMFpNWDFJc1NWOVFYMFpNWDB3eU1qQTVNU3hKWDFCZlRsQk1YMUlzU1Y5SFgxaEhYMUlzU1Y5SFgxSk1YMHhETEVsZlFsOUdURjlTTEZOZVNWNWFYa0ZmVGs1ZlJsVmZVaXhIU1VFc1dFZEJMRlZCZkVjcVNWOVZYMFpNWDB3eU1UTXdNanRHZkUxSldGUkJSMTlHVWl4R1gwSkJYMFpNWDB3eE5qTXpOSHc&log=RjGNT7T9liLju7GDZYKB-JVdtpAbaqEd0eGMWHSbfmSoF0jw-rHhJmcXZ3X-UwoZhkQurG6UMvc2wS-dtdS1w22Yr5VbDNDBMIP9Gg_C2P-QJmVgA3XQL9K1-KEwugvCxuFzaIu3el8VPgysq_jaSQOkRASq8M8ssK9Rt11fQLVQ6wM5JnWvZcGOHcLwUrG16rEbAUPCjeC50dH4UFsUFWgJNXEV6a-J7lytOAqCxaY45KgwyD8PeEKTDQatDLQ3fFzkEcVutJioaO5L2KsckxqE5VL7H_x7-euhfjGLVKwEEH7Nz1PFAoJRuzhDIyf9BwF6b5WKPigh71eUsJoXkA-Y-Yz89Z16PjiUJMBWLoBD5_Vxg-J0bf_my60pVLHgCbdXbZycnx9usl1ljbhEpJDRZZo1hQSGfvuhOh6NuyUaqQVhrUApmvtz9kZRbGPaoKC9Fd-EUfUJeC8Lp7huLJ-n6k-vOYl0FA7qGHcFIaIGcoQSF26hsBQSA-Dr1Rk2KTKw9tQxbNjvTNGR5nQkmWPT3iidb986B_BOG9az4um9ZGuTO8QJzazkDnjuYcY3KEN6OKTKie18fp1yIWL8CqO8VQbm8RJYkqQiZeSAvcQ6aMBFi_kBk61gt7FiUJROh7F1h2Hfv1jQc1Hg2xND43e898lseVRQRI3WjpZowGOepBhU8uUutuDPA4PG8Dn5Rq01C_Hn2buTzlGcEkG21T_J2BkyGJzqBo4G28DSgLvTDXl5KIu914J2KdWR2e3ZLRDn-XzVEDY-CF7_g0bYkbXpiRoC1Ekj-4DOgPUGC70YEbh030qyxmcSMLMAtJ6AfcDje3E5UT5MgsAYWf7BlMlIIOhafU98lJ1w7wN-wMvNaCAWSygLSv8xIx8ZHjIvHcsVc-cmgg_0CuJnqypL19PXbIIUovrWLoJsCEKjzNBhuNjOmLNYucWPP9U2epqhi65hg0UVA8QoPxYgSzMCMRt4_WiYIrkn14IHGl-zyLC8URcj0BF2Rym_SfLpMKdMrOnkcgcBpU4TMjsOzRe9FFV1Ovc2GeIKF03p567qGZKSGweN06aq720J-Du6EnlhjDdaRRwtzvHz_eezJOIJfHoAk9jb8Nvq1la8U8ZOIWQ-ShJ6Wh7KHQYKDbth3vVJ_TAhiiY5eD1cG1PzIX_ji2DSadmruwGAJ8oSzo_MRKJgUPqDgvzJoaxGeLXXHPNcwBi_LUT5yYhBgvfsPl4BnGPxagGKJhRtwuH4dZf-iOJfhL_80aqbuEjOkv_0BOADMUlOMhGkttpZPcaSK4ec8idVIW2A9yF_nB-NcN-LOBY&v=404","clog":"https:\/\/im-x.jd.com\/dsp\/np?log=RjGNT7T9liLju7GDZYKB-JVdtpAbaqEd0eGMWHSbfmSoF0jw-rHhJmcXZ3X-UwoZhkQurG6UMvc2wS-dtdS1w22Yr5VbDNDBMIP9Gg_C2P-QJmVgA3XQL9K1-KEwugvCxuFzaIu3el8VPgysq_jaSQOkRASq8M8ssK9Rt11fQLVQ6wM5JnWvZcGOHcLwUrG16rEbAUPCjeC50dH4UFsUFWgJNXEV6a-J7lytOAqCxaZ0eJYuolgDKtnsPVPmtWOpvO_eWVT6wt5sDQM5TxhIQ6C7U0d134OGVjUoU-A4tNR755DiCYnqW4snV3Or7sniC_oHlykHWogni7ibsX4o7QUCecIVMiYV5tjxGrAkvh5-9Pkah-JT6ZAX9AbkgrlLHablPxQTdp-st9tjCSqyWavD9vV_Jx8d72uLCivBdGZnEKcEcAjjeydtUHfAsnaX-bD69sNT4-gLeiFXXjv1uxPJkC2qGEz_tdssTj6pO42Pyg5HyNz2pAeUTXfL6UVOQ6M-nhQOJsK4-YZGf51Rh4DJ_TmfqETNSj0PX0xJ1XEILFfwAwRwvCzFQRmSsLKLnxdFPGNmH5h0VnX0qEvusMjqk1S7P_Yfklq693JWxID1EMxLUJxyU9PQUZOqNxRJVu8xdsEJLvzfI5EHbaLuVKYRWciXsE9JiOcb7oeuMLDaquqSryIXgIQnvxPVJlIuNY2x_0Erkqy1K7kKN6P5tuBaeRrCPHUbFogigTEQXdCYX6ze2UyctkOvDu65BVFoRwyoB2RP6NwLH3bzd1vqIrWMzDtNHmYGp8UO8UwVi56UwpiY8SqKBuVHnuV0rLl0MBT-BfBeFEntzNtaPFZ6Z0Iy0XtXV_10agT90B8YGa6L2Q7A9HwAaj1Ga6gfklSFGzMf-UsFbSc24rFwVdv9wMthgC82QdPA7TfQAfXvUAvjSkBCU_piNshLpi7SgDbA7WOY0qt40k4wyl_lrUxKYnU5UsP7TxtWtXYIpxmRUY3hXI4-8d_sJjskVF5UMRULJn6ODr9bnLuIou6_vsUoDoh--2qsPohk_wTYy6Pb_pp_FbzvftGpdIIN1NkLt79buvJ6YCypTXu1rkTF-TPi9w6UPdU4KCSpGxOLXc1oSxjQWjTgiKdWwc0aFdzImsh1pcS2OU12WrzKGnHc0HDns1CA7mBqyF11ItywCbZxgGxWiYm9-S4PLAsEJrxhYfaDxgp9GCWUgz_8o52LFgUnZgnGb2mN4p6wwDKHDyVOOD-ZRKFP4__yyPA1iP-A2JW5NerWY8sBnam6XRSGzYaLz7Q_r8hAlUDEgjgQ0n9Z3MM&v=404&seq=1","type":"ad"}],[{"sku":"100014546493","did":41,"ext_columns":{"link":"https:\/\/pro.jd.com\/mall\/active\/3ZYfZKGRAhbHzJySpRriJoGWo8v6\/frist.html?innerAnchor=100014546493&focus=3","sku":"100014546493","playImpr":"1#13#100010-e684588d2e124aa3a3b2131c202fcb26___","mcinfo":"null","rt":"0","text":"\u4eac\u9009\u597d\u8d27#100014546493","biclk":"1#13#100010-esm:0-esm:0-e684588d2e124aa3a3b2131c202fcb26#379#100014546493#41#5bd8253082acdd181d02fa2e-random--c1:671","desc":"\u4f60\u503c\u5f97\u62e5\u6709","focustype":"t"},"href":"https:\/\/pro.jd.com\/mall\/active\/3ZYfZKGRAhbHzJySpRriJoGWo8v6\/frist.html?innerAnchor=100014546493&focus=3","type":"delivery","src":"https:\/\/imgcps.jd.com\/ling4\/100014546493\/5Lqs6YCJ5aW96LSn\/5L2g5YC85b6X5oul5pyJ\/p-5bd8253082acdd181d02fa2e\/f068cb7c\/cr\/s\/q.jpg"}],[{"sourceTag":"0","id":"3505","extension_id":"{\"ad\":\"3505\",\"ch\":\"2\",\"sku\":\"1148158683\",\"ts\":\"1659342394\",\"uniqid\":\"{\\\"material_id\\\":\\\"2416232561\\\",\\\"pos_id\\\":\\\"3505\\\",\\\"sid\\\":\\\"9666b05d-7b0f-43c9-b9cb-89d8cf6421c1\\\"}\"}","ad_billing_type":0,"src":"https:\/\/imgcps.jd.com\/img-cubic\/creative_server_cia\/v2\/2000368\/1148158683\/FocusFullshop\/CkJqZnMvdDEvNDYzNjEvNDAvMjA2MzYvNTY3MDMvNjJkNzA2YjhFOTk0Zjk4NDEvNmQ5YWI5N2VlNDhlMDVlYi5wbmcSCTUtdHlfMF81NjACOPCLekIZChXph5Hlj6_lhL_kubPog7bluorlnqsQAUISCg7mu6E4MjAw5YePMjMxMBACQhAKDOeri-WNs-aKoui0rRAGQgoKBueyvumAiRAHWNuFvqME\/cr\/s\/q.jpg","ext_columns":{"desc":"0:cpc","focustype":"g"},"href":"https:\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS8xMTQ4MTU4NjgzLmh0bWw&log=TJlJN8sZQpybajQhsOAe4azn8HjG7U8BBV4uMygsdb40jgqN0oop-Y0b5jz_kXl0uRQhXUZSURFR5G-YxpGUVdMUsguAA9XgafxVuq8ckZs0B1TV2tnNB9zwZ04l-geDz8cB-deGfus5OfZ6jNfnNpGyazAWBqwFNudw5vQVyYHXeU8wk9GaRZn8exhk-3bYYNMJX9TH78t--_qMTrpGGluzKoiH4Y0_2C_TEWHlPexdPRwEc_YxXRXvEr8Hh-R9SA4MpS2OpKwBkSR240ZdKNjVvfiOMbi-ebxx7RyuRI-GqBmuNFAriRBzp9dCIADxr70UR2xMDpxHJlJh0XZzIqEc5zKzknOOKkY_JyRrgRNeHVQrkdtPqd0cLKyG0cHc_7113VDfGMaQQ87YsaGPUHCDSZjyw5hcPGgjLByQ4agVWfWh4GghvGGbVHwWXAiNGBqSwNxBEMR3_dMdt4iwb0R5Pk1HdL7S-2K3ySyjlO61vWhyB7Vg11M7NXM-8ohrKRoZ_6BxmYPfIySiOik2NKMnLMHLIHWnF1WcgsUDx1oZ04E2k3ZrsJyAqG3Tn-wjmAq5iTV5VZgcKNmB0fvIBnDFTkpEOxSL1QMJ1clpkpv5a_PYCdYg8WSNXgf9DakrljVcWbUG49UkOc1H_dEa_lur3C-XnN5taN_44btNiGvgRUS27WrdsbHo5wZwhtWhPzuErgI4rAXaN__1uKPiw0CPPnaD_vi0oHXHDVMidVvcNarQ-CmUafKR11nRxjNEoqMPKH2q0o5smS3fuaIqJDkPwsm596XS1-ixeWawvWBrrynZALe-HjhBJMItIiwBwOKsEK5okJEGLyaAUy3wN6Qri1nAe-2zxpur-qRjutHo7p8SLgTtFYUl-SR8f_RcHQZvPVxCVUzLmYy4UUGGoR3_Nmyr4WdMuKxrhQ_vXld1qP75Uw1w_-gO2xwcUSEhn62b4zXSdvGPy30sLILV3XHl0St6-D0OSpiiPcCxUUqo3-fdc8-UK8kneaY4YVLDsANVqb_dNAbbYFFsgOs81trYe9tAvuyxEqPQjC5J_CbAnclolIN3VIlv1EtkGVeVQ_p9XAAawVab7pxZ2zGPRe6DUVhPetbnRcfI_vuOBaBFjAAoTVHDPzrXkXD-3bhVZj6L6pYwQlxMldvLALgNvAvGQFVImoNVfXoKOAjWu7aUKsSAYgN47OvTJTlFNcmT&v=404","clog":"https:\/\/im-x.jd.com\/dsp\/np?log=TJlJN8sZQpybajQhsOAe4azn8HjG7U8BBV4uMygsdb40jgqN0oop-Y0b5jz_kXl0uRQhXUZSURFR5G-YxpGUVdMUsguAA9XgafxVuq8ckZs0B1TV2tnNB9zwZ04l-geDz8cB-deGfus5OfZ6jNfnNpGyazAWBqwFNudw5vQVyYHXeU8wk9GaRZn8exhk-3bYYNMJX9TH78t--_qMTrpGGlIvXdKUqd8MztSHl_64H4fJMkAlSHd0ZXS683NrvcjWIpxdECZxfkbVV7rzRP6PqdXpjN3MzuPa9apHqtO_JF6wC7JSt07W3PRlFUiPBGF9f_hoi-SD2flhseLsNF8OgIIKqSDAr2kw_emOVtC2B7MOQW2fpaEi8t_Spu2jQt9iZN_VCj6C9B0_VbP8ToLZlwdTGAz6EtpopX-RtHN3RNpTUxrDfAl-2c-TfykFxxju6UEvLarQ9MNBCCCQDLEmbEkwOOpPtLVIdaiy-0HgbVs8qBxtctltK5VhuhROcZRZL8_SGbT624zMe_k7L8jwy-iu93YECcxlUo3SnQ6_t4_FXgHuC3WCWo77Nx3WLdXVPyM-HRiqWZVX0x6PuV5_4xlp8SprpWoRHjvZfdPoA3hcLTBD4AsoV-fHvfgQa5qoPbohNKdU2LoHEX92-9r_LPfJNUKU02Lj0ksuy_NFEr2r2AqWcHNozianC86_PvnXcIOf40tXQZxUpeVQsf-g2d7wcv5msJap4fecdYEq8DVnMlSWzXrdQvIYOtu4Nikh5H7C6TcCsq91p735nPynBL6NO6xpALvEqHDQP7CevQJoAWCv-gaV6KOWc9tBZ757OfCJHfzQF7t-fHCJorAxby666Czw-57p01OdNPbp53omzfpjv0s1Svq1dwuZfrifn20K6KMlJ-yeILzB-x9BbfRTZVAsxTtVbZrac9YiYNMPDFGnCPgWyirk5QLzXi3whnacwzMU5Gb5o5SQQtaCVBjiCvlqtWdv1UK464YLgJAGE1M_dPfLdK8YYIZ8bFRSxh6asMTI1PzCmQaDBeUdpUL98HcpaT6wXSGNIBpms02yi05xSzfBoHGzl7twkTu2tNqmOIcx67FbBwZ1DnZPPZVfRMxDMQtufbrne3gkYLntPoCrdMsBuBRTU3pGnJNcH9WjXPgign05tqiVbV-H_5jgDMvgVcwE5lKzTn1ACK4RyU-BSJA9CTZCacai2Gqw&v=404&seq=1","type":"ad"}],[{"sku":"100026667878","did":41,"ext_columns":{"link":"https:\/\/pro.jd.com\/mall\/active\/3ZYfZKGRAhbHzJySpRriJoGWo8v6\/frist.html?innerAnchor=100026667878&focus=3","sku":"100026667878","playImpr":"1#13#100010-e684588d2e124aa3a3b2131c202fcb26___","mcinfo":"null","rt":"0","text":"\u4eac\u9009\u597d\u8d27#100026667878","biclk":"1#13#100010-esm:4-esm:4-e684588d2e124aa3a3b2131c202fcb26#379#100026667878#41#5bd8253082acdd181d02fa64-random--c1:653","desc":"\u4f60\u503c\u5f97\u62e5\u6709","focustype":"t"},"href":"https:\/\/pro.jd.com\/mall\/active\/3ZYfZKGRAhbHzJySpRriJoGWo8v6\/frist.html?innerAnchor=100026667878&focus=3","type":"delivery","src":"https:\/\/imgcps.jd.com\/ling4\/100026667878\/5Lqs6YCJ5aW96LSn\/5L2g5YC85b6X5oul5pyJ\/p-5bd8253082acdd181d02fa64\/234844e0\/cr\/s\/q.jpg"}],[{"sourceTag":"0","id":"4273","extension_id":"{\"ad\":\"\",\"ch\":\"\",\"shop\":\"\",\"sku\":\"\",\"ts\":\"\",\"uniqid\":\"{\\\"material_id\\\":\\\"7507039422\\\",\\\"pos_id\\\":\\\"4273\\\",\\\"sid\\\":\\\"d8ec23e1-89c4-437a-932d-f2e823c6b9d5\\\",\\\"type\\\":\\\"1\\\"}\"}","ad_billing_type":1,"src":"https:\/\/img1.360buyimg.com\/pop\/jfs\/t1\/67208\/4\/21074\/87040\/62e09ebdE19f9d307\/ce00b54d607416a2.jpg","ext_columns":{"desc":"1:cpm","focustype":"h"},"href":"https:\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9wcm8uamQuY29tL21hbGwvYWN0aXZlLzRKdzVnUnVUS3pOc2RKZlZxTHZyaG1LNWpIQkEvaW5kZXguaHRtbA&log=s2wXmfWbo3hwIqxXNRug4fL0OX3CdEzD6tbPMkqvU1QPoqmt6AB8Ahll5tP69w1GL9jI0eIvHaxYtNOT6BQ79l5cLLeYsUYBkpXQGU16zWf8pA9qGW-5YI3FEbQ5xTbLj4F1YS-7l713QbIZnoJ0e5Q9zlhCIMP77R99gfPeCK1bzM9SYUkeWF6L3rjU2l4G0g2WoQfBp39GBIJcaJyTUuDo9w21svR7_raT-OMC_Alg9edP6LwenrAYcq-Wf_faLW2AstmBlS4BaLFrlkAF9GmVjiTxcbyW1EPu4j07YYHW3__tThsTazL03slWf6qLMMxB6-Ljmt8lGkaTK6MSIFv2nA2rVhcxWCUpX5ElhEECJlprEPTbTSInlxky9_AkmOjQmyHs1VkTDG_HmsOxkpKEBi1it7XMvYRcpnE7GlgjgZsvg8jhRowU4eAFQNZOCvm_0bOoKGgXT6e8KFSVzrR56rOl5ECborrR38occaEBXSbA2wcGw3OakhJwjNriJ_9DlZFEtfu2yBAn-qeHIV_M8MztBrYdKU-DOZnvMveEyvmaKQS6Lbhk6zkxTWaeUfFJPd8W7zdZA8Ckqnz0TH3Ec9qweV4MnjAcD4l3J8R0AbsOFZsqhXfG6qNFVE-4yCqlxi0MCfk4E-9XdjcoPuQwu_MvEzgInWwh54ezNQRYK8fdipSrwNrVC8VfGjNLXavYEX2xGFS2kxt8GbK1CxnZ7t1UIBuCgXJCfWLaX1yZ50WdL1wKjWzoyPHVM36MdT0buwB-v8da7q12e-7Kv2cT6EhwKVM-Y6Daj3BEz4OLyXl2jc9E4l4DCFMC1eAW23HRuS0tX9qNgc2VQpTWrsq84dq76eCyuGIXISbBkUlm2goMbNHVUErJZbdN6POjWinQLbiQOlOxtrgKi4h37Lm1m6tfAfHma0wLbSpqgXRxVibPw7w_g05crhbTpo8K21O6bdumopz_VyGrxdgrU2ugSzFtKSemA2pdlPOVtwGUskLbFjpPBaCCb_abrk9r1HluR1P3WkdO6qELELItWFXJzP2kLWHpPSgEUAP6orNA8j_Sd_eFocKoYF8c4qq9WjsVai4LOjj2lFGXTOoW_ArJB_Nu8Elx6p0yk9S7YxV9C1UkmGPUjEg78RiHom4zC1BQ9qK4eP-MoczbsyVgFg&v=404","clog":"https:\/\/im-x.jd.com\/dsp\/np?log=s2wXmfWbo3hwIqxXNRug4fL0OX3CdEzD6tbPMkqvU1QPoqmt6AB8Ahll5tP69w1GL9jI0eIvHaxYtNOT6BQ79l5cLLeYsUYBkpXQGU16zWf8pA9qGW-5YI3FEbQ5xTbLj4F1YS-7l713QbIZnoJ0e5Q9zlhCIMP77R99gfPeCK1bzM9SYUkeWF6L3rjU2l4G0g2WoQfBp39GBIJcaJyTUuDo9w21svR7_raT-OMC_AldwwUn2RfMAvDPyJcXcG4aPxgSN5loNELLs1WCLGaRecDK-UpWD9rYFxCiZm3nYWOQNQ0mmsOyggGpTcpGXSoTyd1c1Lu-8_gPR3FovkF5G_VO7bcMlQhmb6VWiavc3tYP1dXxmTJAGJN78tDk7znnMPptf_YrWBJv_bLiDUCjsh3Pp682N2rcVkn516fssaIN-D7YGZoSuYbus_8wpbAuH8QhW4dGfTdnRb2mTdwuY-fLru1OhzlEHtEPwa455ADTJ5LDDJKJCgWR0VaFLxLaCSU0K14GywEkNKK1fj5qwLLcfay8DbktprpK59qwW3Qp35MYTrfku3FEsM7BKL2Ok2_lh4_tpILzwCloOnAWOkB5CuH8OhxClGQDZyEDvvk9E924l_s9GvEfvQmy22ZrwiE5LoNT92TVfHHa_qmFbdguR-nsiyQAuxdCK7t1XDs7sXqFmufQEwpypDEjI1lpg6rzQKNq_b2pbarR7xY6NV8c_DZyigieSAZmPTuWDbuvjsllCVtZ3IYw6QTOzWdohOQ44vw1BDKFC-fULR8zHFPDLGyywm2mEdrM5yfvbVIqy31SDls1_UVTZRY2apRiXx42MG8_wYyqiIXMHVPkM4BJC_VEhonB1c1qBy1AUOuNQS21f7K512wQnp2uVvQOgMLJwnzSBQmZHvkt8BV1OkblZIX79h5Yz33RMOM5ZDBAR0LzQ6YY2Z51JlgM-DG4jCl3XnGacG2EbZx9OXC8pkZnG-MfhXFsFZ3HaU5uxokFTfz_5l-YDc80lXqMRxdSJZpZlgi7d5e0DR9bRUW2-jaMP_kdOzwp_mNu2gNq9J2-pGgRTHK9BKmFU1cl13JoJcffbaMUiw9afsWeZJuvcgEDASeAbcQqILElzt7aL6-Kq1916SKvkJ12YKXekqnAyh78amwVPIQS8YkMKdzGMg&v=404&seq=1","type":"ad"}],[{"sku":"100010728845","did":41,"ext_columns":{"link":"https:\/\/pro.jd.com\/mall\/active\/3ZYfZKGRAhbHzJySpRriJoGWo8v6\/frist.html?innerAnchor=100010728845&focus=3","sku":"100010728845","playImpr":"1#13#100010-e684588d2e124aa3a3b2131c202fcb26___","mcinfo":"null","rt":"0","text":"\u4eac\u9009\u597d\u8d27#100010728845","biclk":"1#13#100010-esm:1-esm:1-e684588d2e124aa3a3b2131c202fcb26#379#100010728845#41#5bd8253082acdd181d02f9ff-random--c1:671","desc":"\u4f60\u503c\u5f97\u62e5\u6709","focustype":"t"},"href":"https:\/\/pro.jd.com\/mall\/active\/3ZYfZKGRAhbHzJySpRriJoGWo8v6\/frist.html?innerAnchor=100010728845&focus=3","type":"delivery","src":"https:\/\/imgcps.jd.com\/ling4\/100010728845\/5Lqs6YCJ5aW96LSn\/5L2g5YC85b6X5oul5pyJ\/p-5bd8253082acdd181d02f9ff\/935f8914\/cr\/s\/q.jpg"}]];

        //首焦兜底
        window.backup.focus=[{"recommend":[{"alt":"","position":1,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/151220\/8\/11617\/61079\/5fdff6baE0a6f9504\/2dbfdebc8fd79483.jpg","href":"\/\/pro.jd.com\/mall\/active\/myvknjmTQuCsW7kjrnPRLPufSNu\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"bokuLSNDGKYkus93uySCgA==","mcinfo":"03294000-13573946-8801421457-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/myvknjmTQuCsW7kjrnPRLPufSNu\/frist.html","desc":"","text":""},"type":"ace"},{"alt":"","position":2,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/160427\/8\/216\/44383\/5fea8b3cEa4deb858\/fe57a084e88526f3.jpg","href":"\/\/pro.jd.com\/mall\/active\/26AGXsmM6AChBJXAvFuMKZ8h5T9E\/frist.html?babelChannel=ttt18","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"Zag\/g9b0Dld+fkfVf4Suog==","mcinfo":"03294000-13573946-8801423632-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/26AGXsmM6AChBJXAvFuMKZ8h5T9E\/frist.html?babelChannel=ttt18","desc":"","text":""},"type":"ace"},{"alt":"\u8fd0\u52a8\u6237\u5916","position":3,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/160199\/26\/187\/69636\/5fea04ceE5abe2994\/d12a85889d01cd15.jpg","href":"\/\/prodev.jd.com\/mall\/active\/3X6GiZeEUSw1zfbYxzhVfQpFXbWu\/frist.html?babelChannel=tt9","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"5+Gcq+Ev\/0h5o09w5iB1hQ==","mcinfo":"03294000-13573946-8801423635-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/prodev.jd.com\/mall\/active\/3X6GiZeEUSw1zfbYxzhVfQpFXbWu\/frist.html?babelChannel=tt9","desc":"","text":"\u8fd0\u52a8\u6237\u5916"},"type":"ace"}],"banner":[{"sourceTag":"1","ext_columns":{"desc":"2:cpd","focustype":"h"},"src":"\/\/img1.360buyimg.com\/pop\/jfs\/t1\/40588\/8\/17960\/59407\/62e34ddcE9dbbf4f6\/553bb2b4bf1dbc0c.jpg","href":"\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9wcm9kZXYuamQuY29tL21hbGwvYWN0aXZlLzI1aUJxVlFBZFFoQkdLWG16TkFzVkFBS3JnWjcvaW5kZXguaHRtbD9iYWJlbENoYW5uZWw9dHR0MzU&log=uCSEJhBgrljsjm-WWR7Z6y69L3Qc2D0GTo_IkmzZUJ1AutABQWB5T4YqlukHVwLkU_BKOAls-Q17JRRx-GV-cKH3lA9XViGgKqKgeUtsCsFgmnbpYZrfqEsV9dAW5pJUiQw_l9STV7I7jaBA28aiuvkp-eQa7NFJemM49cHuOtkX7yMr_y-gLFPBkePv7vVC7rLfu9qSX_2NDuypyX3fWmtRHnhz15lvnQLTcb52lmYVbhJXP2RXnimiKHZFHq6AozD05crdWroAwP0rIoe2IV1cDUCHv5d1Lgok8Ma-LurVurxfExbwwvmiAEueQqTsY7A_25FiyjJq0YwGSEkftFg_K5Q-UH50rFhXCCpAZW8_3GAh-zhRPTViMzMnNE-Df1ILL8q6uUoUxUt054MzokX0JMmriDczvumz6TI3cCD-80b6xcg9usJEtTLMNAIpB-PjMWoyPI91x1n8NxiDNyWp88o7xOP4NAEPyB9WLRXxBPszWLVPknZbFLZB0GSz2fBT8O_umfKsOqrP731Pyk9L4tHR6oy_aHI6fXoUMxm_WWhzGup-EmP49k0XTjK838zkgjSpjlXhLVdcduqlCcYo9jGwbzkoLkdZv1IRikHvYKq0osmlZd89irCDeVogrqpRvostUG0vmMHYtLyEu0_PIISQnF50MmRLIc3KlO64rtbIsh6jJT-rfjfqY8EVcoFsf4sxmADcBq0cUSiINmPn6_iAJFNZEjQE2C2H6kAfUS-LnCROQvtBrsmTY0L58BAwkW8kFano5usJy89QB1Ph46gfZYVQoiTNjBEpKpfXK1RE2JowI5E-jzNRb7hl83yIRtJSKqFbgiKxBFaqtZYpbSssFHsu5uQ5qE4ITBal9GLtxC7hTmrfR__TQMCWV30TDC9feQ5P0HLCZ5vubDPmmb4WtGy44mfCLVzJJpUNvDDD3G-MWSqbxeauQxZVAd6Sz5DzFEvxVJCLHyDjaod0KUhFLQq_aJVKHfSZ5NJjXX4rl2nXmLZOV2yibshGb4mXtPon7i-lBi7UqVWqlw&v=404","clog":"\/\/im-x.jd.com\/dsp\/np?log=uCSEJhBgrljsjm-WWR7Z6y69L3Qc2D0GTo_IkmzZUJ1AutABQWB5T4YqlukHVwLkU_BKOAls-Q17JRRx-GV-cKH3lA9XViGgKqKgeUtsCsFgmnbpYZrfqEsV9dAW5pJUiQw_l9STV7I7jaBA28aiuvkp-eQa7NFJemM49cHuOtk_BTMhcJ3gpaZcBy5PcE2qXisXk1UMUsuXxPO5bob8HdFEONteOvjeNpeFpYjmcxRe8ZopE-zPPOdXwjKbAjvyOsLyNI2TVelz1My6MYNg1CbsmK03aae4-ggDbVObQKKrubHHdDuxqU2CHnsALQAdcr3rtntsyIGykEr9EkZhJ2Qb0Q4Yu9QPffBT7g0zAz6xnGVByATwQ3graP1g2iW61JRB6kumJ-T5O8N2HnCuBkvxH7cZhbqp-RDHVe24NvvwIpmyBd9tiIw09AVZ_pTxeChW2-KuOAZvAW-tQFgnR_fzZNpoivqxgcT7Tll3SCPA5OrgblPkO0QnM-mvMgqjYkcjCW7bd-FHTFhYrwpI1CueL9e3ZzYkOhX_X7YKVZ-yLgAxx-VkDrMS2u1uUxYoduxUjzJFBCuf9eR5m4Ua3vmjqW0vh2CF47xUOj-v1qSzEHLX9mshcgTpLyGNN0ZfBmBF8H7g3E825zgq1MdoF1h14GmeXWZE8kPWZkcFai6PIjtJuLSDtidKzckOMQtZO2aimC7eQJBmgtv4kWf-9ko1H_ZvP_M-w1qBqSX25LXXgZ3Zgc9-dAeaJE0MDYyIifkG0LuFr4-Tu_8AkBbDXNL2Fey-KJeJvKrPzswLqhwJx2iEzNOGhfl0mL3G63EKndPnSEHJUIXog1efTW-bNm1R3YqlP4zUfvDMn8yzQ_FFye0JrfdJy9pgMxvZC3vlKe9kIc132_XPBeZYGwG-UqImDuiGlQMuqgfXHIooMOYaMbQ6G_m7uC_tE2jqRxK3eT3oayZxdvWwUzaQ6rvfW2DkVOnDgKS5oNdKuTR-B_HR9eQRPC1-B8NNNHyAR_iB2oV3O_ZN2SvxYwQNzuwkiA&v=404&seq=1","type":"ad"}]},{"recommend":[{"sourceTag":"0","position":4,"ext_columns":{"desc":"0:cpc","focustype":"g"},"src":"\/\/img1.360buyimg.com\/da\/jfs\/t1\/78753\/22\/5901\/65296\/5d42658fE4c601f90\/cd9fc741b452f2e1.png","href":"\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9scHMuamQuY29tL3BjL3BzcC80MTQwMDU5Njc1OD9pbXVwPUNnWUtBQklBR0FBU0VnaVc4cXVkbWdFUW03YzVHZ0FnXzJzb0FSamFJU0FBS2ladGFYaDBZV2RmYVN4MVppeDRaMkVzWjJsaExHTnBZU3htWDJKaFgyWnNYMnd4TmpNek1qSUliV2w0ZEdGblgybEsxUUZKZkUxSldGUkJSMTlKVWl4SlgwRmZSa3hmVWl4SlgwRmZVa1ZmVEVNc1NWOUJYMUJNWDFJc1NWOUJYMU5NWDFJc1NWOUJYME5UWDB4RExFbGZRVjlTVTE5U0xFbGZWVjlHVEY5TVF5eEpYMU5mUmt4ZlVpeEpYMUpmUmt4ZlVpeEpYMUJmUmt4ZlVpeEpYMUJmVGxCTVgxSXNTVjlIWDFoSFgweERMRWxmUjE5U1RGOVNMRWxmUWw5R1RGOVNMRk5lU1Y1YVhrRmZUazVmUmxWZlVpeEhTVUVzV0VkRkxGVkVmRWNxU1Y5VlgwWk1YMHd5TVRNd01qdEdmRTFKV0ZSQlIxOUdVaXhHWDBKQlgwWk1YMHd4TmpNek1Idw&log=oFz7Em0p840gY1Wp2pfVRnqMDa2GbtcvCeyzlSA2PRcLj2NnS8clCaN1qGUXpFPk4b2FSUsDgFlH0vAkKgejMTfONLDLUFtaIE6CSVmSanTrLqdnncolKj-Ocht-8uFla54f7Whvn9LvqMvxvdD_N0Jqm7m6jdszdIp2PwR3LBSutNKQpweAe1uewHO0DygCghqJ4rqODnlzNomwOE3368TWYCTlTQ2k9ti9aipEnI7ffhCOHIlDYgRvva5uY0RXy-uV1z-XIodCY2aCLeWtEtmD7rJRYgVpKZjZxGC3ddMeqVjxa2m4TYpp_BX60ai-rpm1Ryp6Y_woNu2le17sBaU3wclnzbA-qWcDJWwKPArcWtbZhuP6WOSNnhYfWP-GFm-gjAujeLnEKwDW-zt6CwNU5FQQOW2GvTduecsDyuZVBimdbtdFr6ZJcfHPbA-nHNAqXjf7DADu0CdQEdgxBy1h5QobtgxYKOQugr8vg_90nL6Iq06rZ4qL8Wy4a2OK_v-Keqbahz1upl0gRO0kfgSQvmibhdi9R_l2y5UA9OxgZff96sJL0otNXhAVmRr4An9QGIQOrsw9p0UPK0AK4rmHiJMK5xG_0buN6iDXRF9y5nQG2idM1BoIdQQsecni1Dihdfj00_xKBk46bVK4LJGf7tOHYogN80e4akooeclrps0hheD8yfZ58C-7UHOfM0gyg1skDFV5dd-gawIG0pEyLRZNq1LG1S7pDIuI0LXqIsTwtdCAysgRIYVDbruqZnbU9ujsltvbczU0IIajWZ_q41_MSKJf0ix1GDUQjGylKsp7bRkshNzYT-tO9_Lopa5XodY-nSHKsVz6n1A0cnI11UzjOYIx9WBCJhogUvPcshqRel1dTFUozzGv44KrtKek0zdAoDcwXk_fBQnKaNnfxR_RPnHluuwFTwLPqWjkTm_G6nrwsLFOvE2t27IXPllAAwJhnTCIEhG0RneMtiW2MuYOqhmp7dhcDGSP1mBdwN4j-s8SoeouaU6gJs_zr0s4lEfP9GYKDjr1h4aRT6vMxlNfZj_wJC0ggmC_nktm1VYmnqT5dqJovkAiJ1in8xAabLwmeHF6-L5tf-WEh-Sdxx-m9f9kKUIq-mtOrhNDGWnSnzWhtXH99WSLPntn&v=404","clog":"\/\/im-x.jd.com\/dsp\/np?log=oFz7Em0p840gY1Wp2pfVRnqMDa2GbtcvCeyzlSA2PRcLj2NnS8clCaN1qGUXpFPk4b2FSUsDgFlH0vAkKgejMTfONLDLUFtaIE6CSVmSanTrLqdnncolKj-Ocht-8uFla54f7Whvn9LvqMvxvdD_N0Jqm7m6jdszdIp2PwR3LBSutNKQpweAe1uewHO0DygC-uRDAtZ3nFDBruSCZnPiqiqju-8HNCd8Sq2FloKKYXccqHQkjOjtOkl6HIAvvNtPt69j9tN4Qv2sLbmlwQnWgSpvYruKba9y8po5A_V4ff_V8wN2KMg5snPhYrkFqu2mHLW7U0Bd86AtiyrUylOtX4WuxP5eO5nKvfLoFADRAT9F1Qyno4Tp38dkLiMP8I97QM9dk98GIPsUuvlvYBJ_wlhurgpcT4mFSqmSCX3dAuy0phDLxvaFEcATjoLRJeIPUDXYMJAbhPBYhskzbjkiHPHS8m88Wet1-ZVlR8Z6TY8uECiz5e2TUW26xsks4tl1hLyUtNZe-oeMla5ncq-2Pe9HS87B6nTjgS4BhRYEjitLC16veeQYkYaCCCax2lugYHDqnx6LULNkLivcVhXKpDUfbqyQlrGNVdD3stkSxRgLlxWh2DKc21KvNR0vgbu7_sfIcASmrrj7UtSnApspgC1TCKKZCX-wuWohiHrNqkfDFhlcueaWL0rCzvevAdECpg--rQUcmKdZuGgnPiOxMfOOEIYXasOYUtM1Wd8Qnucb9WfmD4xLJiPbtwzXt2WS9b8FsobdMJ50O18FduSfErV3H-q-N9e9gnIyr3OX9hu3d68VXT1IsSyGs7m2QRZ8Xtqf7p_er8-PQr7rCLIcWG1grx9cJYS_yUeer7qw87_v6Si7HD1wygtlW0bNHUSpHCytlOByJkSjys85j8AX3WbK-dFPF_PkdMz94Qva1oV8m9SeaE2ynUnvoYmF-s_KctkPzXJl_CnbcBNN_xxM9x2O6ubdm7X6mA7SxkEtPe4nb2NsF9z7IdaQS81aaFswMtVZZx_YGfNgv-WyW8s_iXitxeG2HKXjYBmasaARqzJ05yPm4pARt4WV4VlxwEKSYfxSN10rnXGS7cT5tMPuTW6oH1TcS1FnGPVD-MF0Mgk&v=404&seq=1","type":"ad"},{"alt":"","position":5,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/151106\/13\/12106\/70958\/5fe5669fEeb4a53c5\/ff4c2841360b1db2.jpg","href":"\/\/prodev.jd.com\/mall\/active\/2KS7qX4VEn8pt5atxK5W1jGAvrc5\/frist.html?babelChannel=ttt32","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"IRwFC2C28awBBlITEyBAiQ==","mcinfo":"03294000-13573946-8801422732-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/prodev.jd.com\/mall\/active\/2KS7qX4VEn8pt5atxK5W1jGAvrc5\/frist.html?babelChannel=ttt32","desc":"","text":""},"type":"ace"},{"alt":"","position":6,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/144093\/37\/19883\/83175\/5fe407c2E1b76b792\/68ed75dabb686375.jpg","href":"\/\/prodev.jd.com\/mall\/active\/37ThKCmK6tFnWd3V8PqwMJ1SE3TK\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"qGh6sTt79QoBBlITEyBAiQ==","mcinfo":"03294000-13573946-8801422298-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/prodev.jd.com\/mall\/active\/37ThKCmK6tFnWd3V8PqwMJ1SE3TK\/frist.html","desc":"","text":""},"type":"ace"}],"banner":[{"sourceTag":"0","ext_columns":{"desc":"0:cpc","focustype":"g"},"src":"\/\/imgcps.jd.com\/img-cubic\/creative_server_cia\/v2\/2000366\/10048963769427\/FocusFullshop\/CkNqZnMvdDEvMjE5NTc0LzE1LzIwMzUwLzkzNTE5LzYyYTRlNmNhRTAyNjEyMWE4L2I0NDI3ZWQ4MWFlYmZlMjkuanBnEgo5OTktdHlfMF8xMAE47ot6WNPoqae7pAI\/cr\/s\/q.jpg","href":"\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9scHMuamQuY29tL3BjL3BzcC8xMDA0ODk2Mzc2OTQyNz9pbXVwPUNnWUtBQklBR0FBU0ZBalQ2S21udTZRQ0VLdUZ4Z1VhQUNEa1hTZ0JHSzhiSUFBcUptMXBlSFJoWjE5cExIVmtMSGhuWlN4bmFXRXNZMmxoTEdaZlltRmZabXhmYkRFMk16TXdNZ2h0YVhoMFlXZGZhVXJWQVVsOFRVbFlWRUZIWDBsU0xFbGZRVjlHVEY5U0xFbGZRVjlTUlY5TVF5eEpYMEZmVUV4ZlVpeEpYMEZmVTB4ZlVpeEpYMEZmUTFOZlRFTXNTVjlCWDFKVFgxSXNTVjlWWDBaTVgweERMRWxmVTE5R1RGOVNMRWxmVWw5R1RGOVNMRWxmVUY5R1RGOVNMRWxmVUY5T1VFeGZVaXhKWDBkZldFZGZURU1zU1Y5SFgxSk1YMUlzU1Y5Q1gwWk1YMUlzVTE1SlhscGVRVjlPVGw5R1ZWOVNMRWRKUVN4WVIwVXNWVVI4UnlwSlgxVmZSa3hmVERJeE16QXlPMFo4VFVsWVZFRkhYMFpTTEVaZlFrRmZSa3hmVERFMk16TXdmQQ&log=mNGaluQCKHKcgN_Lq7DxGahEhcZQkJ1E5XvQNhCSUhlCc6VNbWnnr5RIDRZITVdafaCz9Ri0dm_cjQ0iuqrMhZ403C942THLgf1B5fA_bIapx2qsAVRqh1he7xbFzLwhyqBINXN_oMkXEeDSkeRWVoFSjwuTjQEgOVYTJSLcqUYYcAat3dQ0IstUSsrvctKUSsNo4YhZ6BriWKFWjc3M0Ib3xdwS9xfdWsgc2izgJDDbE1DUj0F7L1AwPSvHuQwBCOnCpYLcufbEM9Z86Tm3K2CVoUqCaksBwLBC3H7MD3lzOUgBeOlUDcvsANd8Qmcrd4EkuYdoPJbdspPOI9RJR2vr0nI1IWkDnl6lcSvYSNdZmIEdgY4VUUSqHUKW-b3DnMTeBLNAuU8UU-rWhJk7zvEL-hlKOsambabWHTQePs_dF7WpQf-aiSdEzZIWQk6klGQkJkdW4zTy6Wj5y57sZBsdz8qx8enUllDdgJAAF-KZa6PqcqdU3i5dpShdYsH7hyAS4JHlkVTZ37bZho_drYE5-HclzTmaVV7aQm-T9XF2yi2OXP4mOBU5HXEDU58nJwm-qf1cBHxSI85Wn3VURdgAimzW5Hk2sy1jI2tjDBYMg5cn_WlUTtjR5AfjeGMycAghY7UeTonz4IStQpQCIF96BA99GhPhPRm5wJjV9UaXFPURGwHOux5J_GQQTvwtz4ethmhRXtDpnQJgYfDCBAWyEWACNsIphX38NqBkLbcTUHxfuMRYPsHIX6ZiaxtB6vsTVo0DQhj8jEQcp6WCJJoKU9HU9jqrn5OIEm3SJ3ZVqgbIxPR-iOjIPs1DDFkb9ZyiNLHn6uLpgcXf_xgaStnUDL4iJ4TKMu_DVBxLaqjCJZ-eiyQo8qTDXBxEnL8-1swzQYSPXmp7eM3iDqERsrddsObFkUftYBLCaUQI9eJKyKY0yVUL7-KFkEynFIR7Jp_1PChHdrxlUwTwPCYsSQcRp0pfp_K5bXvwlPKdpAd8gmDKN6Uzm0_d0Nstx-QZUGlR2eLd21JdTrsZxcdEjDPWktMA1WXduqDHfhloryWJ7RrSBMt1pum45mfwgrQM42Mnp42OTOZI380zCwpaT_KZRCY1t3bEr1PtS7AYXyLTBOuZ_Bki8M8wo0uzbUIdNCx9-Wd5bzVyIwQ8oVPAaJp0yWeVrmwexdQu_wlzfmQUGC0qpH_Jrlu5AS0ISM-gP4Ww5A_f0J61_UH-gbhyvtvHRDhub9AcuMexBD-NyEr-skbvacYTVUfa9kCGUjyK&v=404","clog":"\/\/im-x.jd.com\/dsp\/np?log=mNGaluQCKHKcgN_Lq7DxGahEhcZQkJ1E5XvQNhCSUhlCc6VNbWnnr5RIDRZITVdafaCz9Ri0dm_cjQ0iuqrMhZ403C942THLgf1B5fA_bIapx2qsAVRqh1he7xbFzLwhyqBINXN_oMkXEeDSkeRWVoFSjwuTjQEgOVYTJSLcqUYYcAat3dQ0IstUSsrvctKUqSRHGlSPJW-A7qxUlzNYLU-nMHwV743BrRju60BNUxYYrxUv7ILvsOqY7hz3cEHvceUnPb59TxVDTWJsupf01tYJ8ZxGEFUzhUE1jornWIxEelct5X9KdBE2LVIaGSFxswBnSdQ9157ViuOjlLYydVUyH2AUy__NrMqr3LqqITHXf9hPxjNN3Yl7T-T6ak_QIlPDSa3bhpS1ptiijjEoqodkXQi_LXs151jit9OXP0gT9qxq6-ZNmp1ZgrAS5wzHDffyZTbm_QBV-_i5BbZ49ZVCvFkiFkJGwICBtQmbhj7aFgfmRFHt7elWfAq9q0J92N4N1kyrV-RtxjBhIGB6rJC_scgF3crAwCxKMfXjUKKSd2eSBpgHLZsZ6aUKlBhloZkx9zaePZI4nZrRT-a3_sbB044dkjzL0qfm4UGaRW-UKYeicjQK9wX3JEP-wjOLXtXHG71sYQmlD4HMv5IPk26hCUl39G75U1wO9i6zbRoSt7Ly8cyUoL5GouPqD-U8vtL2El_N12flLccw4XWJWgda6eOQAuU0kOKyuqJiN4GsazohlSredmn9GIQHwfDRtnw4JnPYGjbAXXRJompv1FS6ZDFTJEarZJ_ztKRzsinsxWRZ57tkti-Nev5tTqkSMYZbnVfiHU4PbgjwK9I95FcTTFcaJeWMFDuK9D8nACOs8iB-kDrHJufElR2sHo8rHY7wyb3QzPe333ZI4YjiYxJVeVUKTs_Uw6uRVfLuFrD_odwxRd-RpTqupexk4FogWWFVHzxS2B_VOqOLW0ZqbKYjZOUA07rKBFuQdIndYKJmX0K390KgtW36dVrP593TU8oL6QIEi7RjwjE_4RarI9TsN42vTOZXK2tEZVjDe6T4bgxzpZt6gnhbZy8PScKNgEd3ugaTn3iwCirGFHmWyvL_nTzaxnVAXiUSxTQ7O2wEDCEHNRjylxWMs1hP2MqzVXz8NmXzlUspzviG4eB9P7QF-5uMC7-zh2NWE_Ua6_D7Q7gJ_LDJjWdtHL1SlAzctrlep45tr0aqxVVQXP7rxjqRLg8YXzOzZMeJPn8uiEkGl6L83ldoocF1ot4GGwl_&v=404&seq=1","type":"ad"}]},{"recommend":[{"alt":"","position":7,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/138772\/31\/20178\/39292\/5fe5cd5fEfce38cdd\/375bf42ad6dedfad.jpg","href":"\/\/pro.jd.com\/mall\/active\/46Vsus7SpKRgDbyAUitFHeBJnthu\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"PMS5koVkFfmNOxwMgDd+Yw==","mcinfo":"03294000-13573946-8801422822-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/46Vsus7SpKRgDbyAUitFHeBJnthu\/frist.html","desc":"","text":""},"type":"ace"},{"alt":"","position":8,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/129709\/30\/17733\/53433\/5fc20ebaE16d5e08d\/bba7d0a8e8e7fb10.jpg","href":"\/\/prodev.jd.com\/mall\/active\/zGwAUzL3pVGjptBBGeYfpKjYdtX\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"+BuvoFpWY12V+3PXLySUMQ==","mcinfo":"03294000-13573946-8801420745-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/prodev.jd.com\/mall\/active\/zGwAUzL3pVGjptBBGeYfpKjYdtX\/frist.html","desc":"","text":""},"type":"ace"},{"alt":"","position":9,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/153447\/39\/11074\/46465\/5fe2e757E465bdd19\/a3db919bd4cd1490.jpg","href":"\/\/pro.jd.com\/mall\/active\/G6dB2UyBBfwfTVCBp3iMQQQ6GHi\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"rGjgT8k0RWIilVEYymoeQg==","mcinfo":"03294000-13573946-8801422515-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/G6dB2UyBBfwfTVCBp3iMQQQ6GHi\/frist.html","desc":"","text":""},"type":"ace"}],"banner":[{"sourceTag":"0","ext_columns":{"desc":"0:cpc","focustype":"g"},"src":"\/\/imgcps.jd.com\/img-cubic\/creative_server_cia\/v2\/2000367\/100004707458\/FocusFullshop\/CkJqZnMvdDEvMjE0MzEvMTIvMTgxMTIvNzU2NDIvNjJkNzA0NDVFNDM4MzQxMGUvZjk5ODk3YmFmMzYzMDExYy5wbmcSCTMtdHlfMF81NDACOO-LekIZChXljY7luJ3nh4PmsJTng63msLTlmagQAUIQCgzlpb3otKfmsYfogZoQAkIQCgznq4vljbPmiqLotK0QBkIKCgbotoXlgLwQB1iC-frF9AI\/cr\/s\/q.jpg","href":"\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9scHMuamQuY29tL3BjL3BzcC8xMDAwMDQ3MDc0NTg_aW11cD1DZ1lLQUJJQUdBQVNHUWlDLWZyRjlBSVFvcHZyM0FNYUJYcHpaSEpxSVB0cUtBRVlzQnNnQUNvbWJXbDRkR0ZuWDJrc2RXRXNlR2RpTEdkcFlTeGphV0VzWmw5aVlWOW1iRjlzTVRZek16SXlDRzFwZUhSaFoxOXBTdFVCU1h4TlNWaFVRVWRmU1ZJc1NWOUJYMFpNWDFJc1NWOUJYMUpGWDB4RExFbGZRVjlRVEY5U0xFbGZRVjlUVEY5U0xFbGZRVjlEVTE5TVF5eEpYMEZmVWxOZlVpeEpYMVZmUmt4ZlRFTXNTVjlUWDBaTVgxSXNTVjlTWDBaTVgxSXNTVjlRWDBaTVgxSXNTVjlRWDA1UVRGOVNMRWxmUjE5WVIxOU1ReXhKWDBkZlVreGZVaXhKWDBKZlJreGZVaXhUWGtsZVdsNUJYMDVPWDBaVlgxSXNSMGxCTEZoSFJTeFZSSHhIS2tsZlZWOUdURjlNTWpFek1ESTdSbnhOU1ZoVVFVZGZSbElzUmw5Q1FWOUdURjlNTVRZek16Qjg&log=FRihD9CmuNFug8IvmAzyjJCU4iy0lj3kCD0DhWOGHBcIf19u33tTHbsURMJ8ruPjzz8KSsawql8SlN8nT6V18evQNs69NIYY_pd8T6yWEaS2Y_yEVJonx4i5yVKTWTYqdqzkuHo3s34I1zmaQpeEKkcrrRJhfmYE1Bpg4ApaMReyJlivI0omdy27ho-LPbn-dfERIypDVarMGy4_-Ag41jLiHXwySg-I1Wkfk2jKS6LFF_h1J7d1petjd9BPfgSaqXSv9e_rR_SgLDy1R1RZ8UKxffaWx43CCJ4Sjz_fKDiEtWapmZ6qVqVaVkAl588FPMNkaMtCzWXe7BWCQp9So7hvCN7PLMqxsGTPE9RB9UKi-I-WD7s_Ha_nyWxCRKIv88pRyNBL6UzFGAnA84biVx5UlGRUu-X9BsSyQqKUKYUwtZHhFuoZOJP4OYlz6HzVoOCJaFPnog6bOL1NMp2Vpp_zbaIYmAX0-YeBlJb7GDu0GYswzsnwc6Gg-zKNNC7VQPn3jJXwfbDwbeDKTG46EW3c_xV7DUqZ1yansOO0bEvBm_uxOj28afFaZg9ulna3aWdWrOXGdvp4-TjLzruxyU4laUM6N3UAUXHvIgO4FGiMCmxToowu51FnlPQb9te6C6YA22BtPRIUJZqiw_T3vTmMIyU_UQmRVAiM5_zXvVQfbd7EbhKdsAufyNuw86bMf8MsogG697GcVaE-JdFMDAKZfZHZTnkMpOYmb1UYkJi3UXcu-31i0wQ-p8wKSWTtJHLlt3-jB-P36BAicq8t1D4Dbsr-GdZAK6b0PcxSElMc5fgDTdQm6rt_U10xSWuLLU8wM6icsGG6gRyCT9Wz_-UIe06KevhwSBZvtxjbAGaj4ehwdMqfJ8InyFgM6qUV5CkI1FmVrdOtiompX4Oo5MJ9hSqQfD8amVpP8D1C8zjXTUo-1inVY3LsHUOUf2nQ6RFBg2lTnHuAkdcTH7HziTytm8FLG-nKzZ5AjZTYNTxHfBIXpOMi2IlpQp62sftP1bADmQoRLnjfr3hUBjCj8EdDlyNXkhrqouexpcmPftutMSXL2KH9kjx1cf-ih8hYvNuW3FYczkPR3yEVprtACcNhnGh66idhhgjJwCXZJzI_qVkvbNGccNhPmC30R8AeOKa-8oIUdUIIMubKoEdVMxDtqykJBYTAIR6spSM--7M&v=404","clog":"\/\/im-x.jd.com\/dsp\/np?log=FRihD9CmuNFug8IvmAzyjJCU4iy0lj3kCD0DhWOGHBcIf19u33tTHbsURMJ8ruPjzz8KSsawql8SlN8nT6V18evQNs69NIYY_pd8T6yWEaS2Y_yEVJonx4i5yVKTWTYqdqzkuHo3s34I1zmaQpeEKkcrrRJhfmYE1Bpg4ApaMReyJlivI0omdy27ho-LPbn-geyz-a0gmkR9m7AA1MLx1hhE8053Rykyj8Q5goF8Zl5MV0BQUbfNHy4NTdA14t0sHcB_2ziIMg7rXte2l-da9USYA1zow7uPxAVUY8wGvjhdZrJtNeH5PQ-FYpqqMeGWZ5fiyHA_GDtRE_396eZYwwSWNadQFAgvRdACj9Mja253LWA_3MOq4fAWbTgY1DZReDTtnt-ynJuz5JfDeuZDpVOb0lHfNtbi5DmNkxZJfThmsauorMnG-C7HgyxSc64SzZ63ipsNQDw72OSG4tIu2yhI0LFh6xLyqniw44axsN_nZT72uEQY3PzkIso4JorTepWd5vU8JJSUvrWjPi8fTbhb0PaoR0wj3YdwVybQLuQkDwHfuaa0wC53-n_s-5P3HMY9znnSA1WFiYxxpg4isIUuVraJhQVJz1aa1WZeM5W0VDhyxiXM55RjvmurlOLtJznYGAIfT_MXk1PRgtbuCwVeKLPrqNaMbVFS40IHl9JYbCRxC9l9xx898IlS69GQnhxRVI1n1UZyjxu9bp9ddyvaJsX1dFpf2iDiAMfz7GOyvQumYrz0CV8NEj6JGWLumN4thrgH3fk4flzgPPjBw9yYqk3pvyVjzU--QiQH0j0QkWlNfEVAOoJNs-XqnPEV08aWMo-Ky2wtHLfwwzXYKloPX1LMYrgZSSiSvIZYwgY_Y3U4ZvuSgGItZGGmAuFMMiY73xy1ePQIJXtPhei59MXjklA6nRPicJyu__7DAKLHL-pqjkQZWlOLKN9vJTdcRtiAYnlyPyOJdWzzBmF-TDZ97saV_CdEtEP6KcJpfw99it1ABT6uhFC7BMoFrmhO-7Q9x6--MITqP9XFsTEo6NkltqMf48WZnrOgdyAe4xUiNyAFMibaD0t4v2N_UaY0sA-BqgA_Qiihk0c8mOe-NghojVn5yLHUrWocLJ52IjPrQIRhFDrhxSMynTTdUbOS0mj9JJpbG6zvAIHw3aatedpgmBx8vYlfZbRweIbstrQ&v=404&seq=1","type":"ad"}]},{"recommend":[{"alt":"","position":10,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/151690\/5\/12181\/71606\/5fe9bf3bE80b775d9\/d67be1ff0b8fa2a6.jpg!q90","href":"\/\/pro.jd.com\/mall\/active\/2tRyWk6vGETjF5aPtAZoXxdnddYA\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"gIoMIiWo0D\/LhPR2RJZQ2g==","mcinfo":"03294000-13573946-8801423636-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/2tRyWk6vGETjF5aPtAZoXxdnddYA\/frist.html","desc":"","text":""},"type":"ace"},{"alt":"","position":11,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/145833\/33\/17892\/73340\/5fd1f9d8E7ec88331\/4caf9bb9de747f80.jpg","href":"\/\/pro.jd.com\/mall\/active\/37p81TGQS7wcEaHNjA1C1WokKPeT\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"U6gP9cS8gV5xMdJYrWgQ\/Q==","mcinfo":"03294000-13573946-8801420756-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/37p81TGQS7wcEaHNjA1C1WokKPeT\/frist.html","desc":"","text":""},"type":"ace"},{"alt":"","position":12,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/152823\/26\/12012\/68654\/5fe97bc9E430fb6b1\/3f7f6bcef1350531.jpg","href":"\/\/pro.jd.com\/mall\/active\/2i8TdgieNtGwuDqV2yHPSFqRr29t\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"bkSlXW4t4\/oh7WXA5Q6F0w==","mcinfo":"03294000-13573946-8801423369-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/2i8TdgieNtGwuDqV2yHPSFqRr29t\/frist.html","desc":"","text":""},"type":"ace"}],"banner":[{"src":"\/\/imgcps.jd.com\/ling\/100003909373\/5a6P56KB5pqX5b2x6aqR5aOr5aiB\/Nuacn-WFjeaBryDmmZLljZXmnInnpLw\/p-5bd8253082acdd181d02fa22\/d4150b6d.jpg","href":"\/\/pro.jd.com\/mall\/active\/qvR5WfiLRi2e9eUKdHCv9eP7Pht\/frist.html?innerAnchor=100003909373","type":"delivery","ext_columns":{"link":"\/\/pro.jd.com\/mall\/active\/qvR5WfiLRi2e9eUKdHCv9eP7Pht\/frist.html?innerAnchor=100003909373","sku":"100003909373","playImpr":"1#13#300002-4___","mcinfo":"null","focustype":"t","biclk":"1#13#acthot-B0036314-0-100003909373-acthot-0#88","desc":"6\u671f\u514d\u606f \u6652\u5355\u6709\u793c","text":"\u5b8f\u7881\u6697\u5f71\u9a91\u58eb\u5a01#100003909373"}}]},{"recommend":[{"alt":"","position":13,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/147490\/11\/20231\/58763\/5fe554d2Ed968d82d\/0e749fd6e3e38af1.jpg","href":"\/\/pro.jd.com\/mall\/active\/3XjkyqALMxPUtxHp3VPvPzR2USqK\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"gGIXsI7ZKj4cCPOFSR5xbw==","mcinfo":"03294000-13573946-8801422820-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/3XjkyqALMxPUtxHp3VPvPzR2USqK\/frist.html","desc":"","text":""},"type":"ace"},{"alt":"OPPO\u5dc5\u5cf024\u5c0f\u65f6","position":14,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/155218\/21\/11512\/71383\/5fe5532cE2e68cd5a\/d6a736a88863c103.jpg","href":"\/\/pro.jd.com\/mall\/active\/2kr2j6fCYET7LtjRww5vB9DJNfwV\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"w\/Oz53F4tqc=","mcinfo":"03294000-13573946-8801422620-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/2kr2j6fCYET7LtjRww5vB9DJNfwV\/frist.html","desc":"12\u671f\u767d\u6761\u514d\u606f","text":"OPPO\u5dc5\u5cf024\u5c0f\u65f6"},"type":"ace"},{"alt":"\u7f8e\u5986\u7cbe\u9009\u8bd5\u7528","position":15,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/144331\/15\/16230\/75371\/5fc4e20cEce63f6cb\/0148abea8250fc3b.jpg","href":"\/\/pro.jd.com\/mall\/active\/4W2AmqrXWJDtT4t5v5P6Wxe1WTec\/frist.html?babelChannel=pcjinrituijian","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"2CeAlBiVB6aN5qElSwcuOg==","mcinfo":"03294000-13573946-8801420753-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/4W2AmqrXWJDtT4t5v5P6Wxe1WTec\/frist.html?babelChannel=pcjinrituijian","desc":"","text":"\u7f8e\u5986\u7cbe\u9009\u8bd5\u7528"},"type":"ace"}],"banner":[{"sourceTag":"0","ext_columns":{"desc":"0:cpc","focustype":"g"},"src":"\/\/imgcps.jd.com\/img-cubic\/creative_server_cia\/v2\/2000368\/100023357050\/FocusFullshop\/CkNqZnMvdDEvMTc1NzkyLzM3LzIwMTcxLzY4MjQ1LzYwZjNmM2IwRTc5ZWIxN2U5LzIzNDJmMzMyYWFkZDYzMDkuanBnEgo5OTktdHlfMF8xMAE48It6WPqc7c70Ag\/cr\/s\/q.jpg","href":"\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9scHMuamQuY29tL3BjL3BzcC8xMDAwMjMzNTcwNTA_aW11cD1DZ1lLQUJJQUdBQVNHUWo2bk8zTzlBSVFtLTJBM1FNYUJYTnFjM053SU1FTUtBRVlzUnNnQUNvbWJXbDRkR0ZuWDJrc2RXSXNlR2RsTEdkcFlTeGphV0VzWmw5aVlWOW1iRjlzTVRZek16WXlDRzFwZUhSaFoxOXBTdFVCU1h4TlNWaFVRVWRmU1ZJc1NWOUJYMFpNWDFJc1NWOUJYMUpGWDB4RExFbGZRVjlRVEY5U0xFbGZRVjlUVEY5U0xFbGZRVjlEVTE5TVF5eEpYMEZmVWxOZlVpeEpYMVZmUmt4ZlRFTXNTVjlUWDBaTVgxSXNTVjlTWDBaTVgxSXNTVjlRWDBaTVgxSXNTVjlRWDA1UVRGOVNMRWxmUjE5WVIxOU1ReXhKWDBkZlVreGZVaXhKWDBKZlJreGZVaXhUWGtsZVdsNUJYMDVPWDBaVlgxSXNSMGxCTEZoSFJTeFZSSHhIS2tsZlZWOUdURjlNTWpFek1ESTdSbnhOU1ZoVVFVZGZSbElzUmw5Q1FWOUdURjlNTVRZek16Qjg&log=SqJpcMQe6tMCV9up_ezOCuA9_3fQhG9LjxTf5WMTEYpfwGIr8lCWDLsfAZQRtHe06ISAE5UFcDE9eQhxZhEuc3O3JTigA_HEBCuKGILlp8guYE64jCRjMyPnAy_b4sSvsIvFdFvCd1N2_dYBT6p_m9lGacYHiQ9SvW_XMelINyFsHJ9bQITOgC4R2Lq7sz68vT1Xp-ofG3tkowDw9I-XQv0lmw7dUKbZcOmcjUXjPHplwCX3HWBikLQlCxeegqupbSaNKhr0trEj36LuIFk_UF-Dx2spiyMVb51EJxr9ZAKVsXpzzvJ_NRplzHZkRv-dlfDQeewDiU6ecY-8-cx-A2VZ9H_V5CnNzDisBZZp0aagEcBNjJhK-Ngk1SFwkhXG9ViYESSQKRH0ux_KXJbZH2V2CXAxsGKmWmKLF30mQmzWePdXm486JrBwsrbubRVS_9UfjRqi7vU3KStEgll8ZczF1tbT_b2GzHZm9siboLgkbrDVnJKh5IFus2CpLDkKzFi2OzYdZu92c6syn0YxuO9y6EL2oN2EY3KpcugYz0iVI-nqVRiaZmTNpkM1E49l4USjqbLadmhUpjsmF8aEa7t9a4LmtTY2d1BAvMFtYM4dKEaaXIYyUYmxkyqlYTOW7TXYcwPyq9cEJEbdjlnppMvx9sZwycq-tsWZfT_KcHZlOZxcdhU6KHMasq7ckwyebJFqKzSKAMuX4Xuvd7rfbX3BPDmosUP7FTSm8TcUM9GpURRVUmDh6_KohtggWfD5S_-ykqfHpYoWCM0VZhLrIxJK4D4e7ClG7upH-UbcHGJMzdmFPQu2W35JDS5bPx_zdJp_uGr9LTT3yXbayeKpzu4bASZmKos7ZkIzIFWL24pLKEqTtzsxAUXy9Tr0iwipqtBtwDzsbw4bNShdSonYnV8HhLh_7FXZN5ezN3kMqVfbRn10xzKYKh_axmFBJA2CY8Dczlq5tLYBVJgCdQcHlKvZVeFh7LdSlOINqY-AeLpwSn-jlhxpoDwg6XEWELSUftBW5Z2v_WsCAiupRXB-Qb3y7Nnyq8jp6USS095I8MS4PtGAWzpITakb-5SVzbivNlCVVI1VKLj51c4nN-i339QfPc7jCJ3SBPV_NOPqEMbyxDNWwrS6TR39mn9Ac8_nyp8LZM58-hOCFiEr9SbGuBKA4tJxSku_zMUoCm-dBLA&v=404","clog":"\/\/im-x.jd.com\/dsp\/np?log=SqJpcMQe6tMCV9up_ezOCuA9_3fQhG9LjxTf5WMTEYpfwGIr8lCWDLsfAZQRtHe06ISAE5UFcDE9eQhxZhEuc3O3JTigA_HEBCuKGILlp8guYE64jCRjMyPnAy_b4sSvsIvFdFvCd1N2_dYBT6p_m9lGacYHiQ9SvW_XMelINyFsHJ9bQITOgC4R2Lq7sz68Bq1rLuCTHtLNWV9xjbsRQtj3zGN62BW1Z6AfHJkvCnx1BQaS7IDsSmTUBl8UFI55Kd0yac2RQ_JOWo9x1hiCaeup-DDBE-E9shFHDgnAfG4rkoU9yoyRRBqjxG62BzuFL_rDqhcYAXs3ykNHAZRd89Kk3xWNaIT8WKE1p0rV3EH4bSzoT_8wRez0D-YjPZmrIcBtYZ9XX5BZYMvQAsk_pc9EXRgGfy3O2zYfJ-trIC0Q7fnbCEtvMarOIRTcX_nzHEsVd1mEgRFR1n4o-Ei598wjUfnW2moPxmcwgXPTzH2ib_YWqbbLr-ldvu3BeMajOMFfFY3TXXVYQSusJyJHc8jUHVTwz8tJqbtNlFx0mD0SqF-PjftpeZfA8CG84Tk0JelqpPeV24bb3oIcsBQyRkp76P_hmDIWRHuZnhjxlzAb_jMPEmOmRyQOXjUfUxNZ7Q0BTfZs-Je6xGslPJOJQCmL58IYw5AAf-cKpiS6R68Qk3rcu6h2bdYVXo1ZVMSPE94QXYV3uDLSwtjzkEA3PcRsgnTROKOuHpVXIPAgrxzSkiAWeMAuCAlPwShNK7hu_tMHlLpbPnD82AZELRB-6LNHeVZ7FGaO8OWlPG5MiGvjkCyppwUaO8kVIBNY5F4KtDPqOgrAa6QMNcIyaNykBHHG2dvgQr8YjNAPHVcMYlc8UmBV3oNbX_cp0yfy1lm4oFMvXZVzQx_ei9aBBR5BIXWEQrOngFd5TQb0l4Rsj6uyvfIS-mzePWsxvcSEQP0MMCzrql4BSEF7HkfuPOl3GgWLUGQ4ESLH-HeBkAit4V54nN7A1wJH3wR7oEQZpylgp8jpvimgNutQKXrRtNf5_Zk-w4AG2wyHWi3g5Xeexl88KI7ymBVfVhSHdcnmLrgy6l73zLXiRJW3n0ERk7qtCFzPfbkZFCVuY39WgnKS8ZsJs0DLy-sN3xVf4iY8UEA5x4y0LyYX1nxwbWTHlMSYD2uQNBfVOyPrlwKbcQhS0nw&v=404&seq=1","type":"ad"}]},{"recommend":[{"alt":"","position":16,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/152492\/21\/12040\/52119\/5fe93622E8bc3302f\/67857d409c58d0f9.jpg","href":"\/\/pro.jd.com\/mall\/active\/4AfQf3FkPRGHhtqqKh9tsWyV97sy\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"TteIvHssJv+j1USc28Th3w==","mcinfo":"03294000-13573946-8801423368-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/4AfQf3FkPRGHhtqqKh9tsWyV97sy\/frist.html","desc":"","text":""},"type":"ace"},{"alt":"\u8fbe\u80fd\u8de8\u5883\u5976\u7c89","position":17,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/142076\/21\/16719\/81798\/5fc755a4E765768a0\/3e35cebd45e72fcf.jpg","href":"\/\/pro.jd.com\/mall\/active\/34G4aLZqete3T2VDrQfwa4z5hdAm\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"QGSzAaCfP34=","mcinfo":"03294000-13573946-8801423371-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/34G4aLZqete3T2VDrQfwa4z5hdAm\/frist.html","desc":"\u65b0\u5ba2\u5165\u4f1a\u7acb\u51cf40","text":"\u8fbe\u80fd\u8de8\u5883\u5976\u7c89"},"type":"ace"},{"alt":"","position":18,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/159465\/15\/15\/54794\/5fe97b93Edc6d2106\/705acb97ee03fa41.jpg","href":"\/\/pro.jd.com\/mall\/active\/SyNEMyANkXQuUmzn5dUef8CQGPA\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"bkSlXW4t4\/oh7WXA5Q6F0w==","mcinfo":"03294000-13573946-8801423370-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/SyNEMyANkXQuUmzn5dUef8CQGPA\/frist.html","desc":"","text":""},"type":"ace"}],"banner":[{"sourceTag":"0","ext_columns":{"desc":"1:cpm","focustype":"h"},"src":"\/\/img1.360buyimg.com\/pop\/jfs\/t1\/67208\/4\/21074\/87040\/62e09ebdE19f9d307\/ce00b54d607416a2.jpg","href":"\/\/ccc-x.jd.com\/dsp\/nc?ext=aHR0cHM6Ly9wcm8uamQuY29tL21hbGwvYWN0aXZlLzRKdzVnUnVUS3pOc2RKZlZxTHZyaG1LNWpIQkEvaW5kZXguaHRtbA&log=qAasVHIbtBdZHr63ACHYYxEFxI_HG_0AtgeQI-4ZtsJP4CX1Ahap2HXRbBmQowV-C3ynQH-um7FpVYJvdQacX69wLEorc8TTJY_E1o1eZYldpsnGqt7QyBnNs2bestPqbYhg8laFQvH7BiRPxg7WzLA0nego8RCXBxKOHrpNf9H4hfEUfP4E9Gi5i9kEahfqtrdcERw1kOs9-vW0AkDnTaqFgSdOU_gNEvZ8nNqOBXCbLemFL0ZRqBHyfTyUdY3vfjbG1bF-aPfHWjr2bqOXNcUNGqBI9sZaCCDU0XoKtlbihWPs-Mt46CWikNdAs2P7s53jr7zQBLbhKsxxRRJf97oXs-CGIztzEOY2qN6ruRvD6HOtRES_M8Vcd0Ap4MdSeHdxmyMMM1blpXnUMc-Tp4s3sMkoXDMthTKQFsCc_pPFBTjOvSMHnn2-90XUIf_MuTU_HdesF3XO9JYfy52FsMJbHTNaixSPKQw-h0LPSK8ztpkp8LthDSFXRntb4cZZHSkASze-sdsJ9aP-612hYOGTXsEYCZSTNr-NXKOoI4rhQALo4CHAXahQYGhFJazNIIRnqCWaIymMgQ89dOva8AQJXhhoVssnas4wBvjslot3QZFXZ3o9fQv2DnkNw9tDKI5f5PlGR4dkUr7pNoBtAkKZvwfqe71524Z-NDszlgfEz1zFslLc76P_We4PGqOQdFPmYutnnmcKSXF0xLawjfyMcwBxbAzgcxpeJqJYzY1kq-iSdCauccSgxb28THga2topmagEgMcy-TmCsJI_33WPikE8wpNIgY72KdBoBirz6bpUWxq0brSlHXMJ_jxFR9Hx1yXd71hnJFs0KFgqycPfTCAh3_dE13johzBB14i4edGwRgQat7EIILlJJcCkOv1cqLRrH0UT1tE7NOwdP0KESUMH_kziAwD2cAaIsp9bdGNjATuELVRoUyza0fS-So79B6BAkbFnaahR8T5j77sVtAepYBJB2R7nFBpANbTYzP0YeET5xuXf9rYSHy88KGkfO7CMFeyADWwe50IZNCXYqmubXVuZyKvJnlV4uJY&v=404","clog":"\/\/im-x.jd.com\/dsp\/np?log=qAasVHIbtBdZHr63ACHYYxEFxI_HG_0AtgeQI-4ZtsJP4CX1Ahap2HXRbBmQowV-C3ynQH-um7FpVYJvdQacX69wLEorc8TTJY_E1o1eZYldpsnGqt7QyBnNs2bestPqbYhg8laFQvH7BiRPxg7WzLA0nego8RCXBxKOHrpNf9H4hfEUfP4E9Gi5i9kEahfqOVzCEzxNlxPQg9a7ejRbmGagyCC3lR-BC8cg0P7MXARNYFliWbkHxQi8gRCuFj13rFYqHFub9-tNq3JtssRjgUTu3C2PdpmGinM8unOEbjSYZVa_INJiH833cj1GfW6UEOpJHbGTg2kbg25TBbsRoOcaAFj53XP6np-QMbcdPCennJkSYLE6pHADx1tvMCxuPgX9r_Cu8AeqhfsIrCVTaKRL1Whad4H33wlqblM0Cmy7_rZvpRwFnRg-ouM4vJBLOPQtpamuhS_39o-4sPALuVIiFAbTtXGsTuFYg5gd8uSQWPucmKSiuSCfvB8Rt1h2ESvjw81QuUlsvOuUSO_-0ZaT9vZAcTHt9NgJnXLVHY11ozWP7kldzE4fpfrpTI1ai7txr2glP6R3lIDlnwgnq79iF0dRAF6Fy1ZVJo_EDzU9AONBys5T8Xil8CjhLfohDlE7AxlsmbQozSv53tJkIQZdZAJIBycv773H_EqRlo5eE2zia6X7H_o7BfPh9YeKvWcDFkdSasjPvUGbqX2aJk0N_z8UiC3Xmg1V7RiZxvPQCzAUd7OUW4hGgR4ylzmPzu30DmkaYos83Q0sK9nIZuAP77m0CLtdFeLRRmjR0PGw3X1Rwvs42rLuGYvDI5Wai5uAenl94J5lu0Wx-lHVSCkOHY0SPDbEoI3kHAZVPQ7TPLov0_tIhQB43tNRi5Qi5BNCHnJam1zv7RAjj6zA_QIqjG9kmv8NudF3IStulV0WfpQu7gZ9ANdK5lHDWpHPP-PZr7Q9Fy-oH8J_IYBIbBN58YRbzepifqUm8-UPpFpQrMB0CNQjm-UU8yPz_IbL7OnMH10Xu3hUws6jm6wxZoChWjHWPz6d9Bd0uZ-G7pw&v=404&seq=1","type":"ad"}]},{"recommend":[{"alt":"","position":19,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/143220\/17\/17461\/57750\/5fcd86f8Ef9a8199c\/0f3a18493a9f64ed.jpg","href":"\/\/pro.jd.com\/mall\/active\/3fNa4gg4udob1juiWbWWBp9z9PBs\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"8E9EFljRna9sk5iyH5TJyQ==","mcinfo":"03294000-13573946-8801422413-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/3fNa4gg4udob1juiWbWWBp9z9PBs\/frist.html","desc":"","text":""},"type":"ace"},{"alt":"","position":20,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/154590\/23\/10967\/74195\/5fe2df62E45a142d9\/883e4bda6f5cd278.jpg","href":"\/\/pro.jd.com\/mall\/active\/29aweHKvVWPaPXgJMbtiLsHk9pFR\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"RAv3J0fJGDZCyu6kQERnLQ==","mcinfo":"03294000-13573946-8801422593-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/29aweHKvVWPaPXgJMbtiLsHk9pFR\/frist.html","desc":"","text":""},"type":"ace"},{"alt":"","position":21,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/158239\/17\/80\/59624\/5fe980daEc6af0098\/0b6bcc0f5587720c.jpg","href":"\/\/pro.jd.com\/mall\/active\/31e4RpwAWH66gXmn7UdN9dMGVY7F\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"oWH9E4RbFQwBBlITEyBAiQ==","mcinfo":"03294000-13573946-8801423361-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/31e4RpwAWH66gXmn7UdN9dMGVY7F\/frist.html","desc":"","text":""},"type":"ace"}],"banner":[{"src":"\/\/imgcps.jd.com\/ling\/7776792\/5Lyg57uf5bCP6aOf\/6Zu26aOf57OV54K5\/p-5bd8253082acdd181d02fa02\/71ccf55f.jpg","href":"\/\/pro.jd.com\/mall\/active\/2zMKHHhui8H95uEg63v5aSVFLsZ1\/frist.html?innerAnchor=7776792","type":"delivery","ext_columns":{"link":"\/\/pro.jd.com\/mall\/active\/2zMKHHhui8H95uEg63v5aSVFLsZ1\/frist.html?innerAnchor=7776792","sku":"7776792","playImpr":"1#13#300002-4___","mcinfo":"null","focustype":"t","biclk":"1#13#acthot-B0036759-0-7776792-acthot-1#88","desc":"\u96f6\u98df\u7cd5\u70b9","text":"\u4f20\u7edf\u5c0f\u98df#7776792"}}]},{"recommend":[{"alt":"","position":22,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/139567\/10\/19800\/44582\/5fe46a35E7004831c\/9721fda27a9495ca.jpg","href":"\/\/pro.jd.com\/mall\/active\/2g9n7V52rEtSdKDkPHKMCURGR9aD\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"vTzmnuWTYC1fchOIQe8O+w==","mcinfo":"03294000-13573946-8801422592-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/2g9n7V52rEtSdKDkPHKMCURGR9aD\/frist.html","desc":"","text":""},"type":"ace"},{"alt":"","position":23,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/146800\/33\/20186\/78685\/5fe5c755Ec3a48986\/df7e8df0dd87913d.jpg","href":"\/\/pro.jd.com\/mall\/active\/HkuJmKguhv6jGeEXdrKPR4ygyje\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"0B9WUXoekna8pOynkQjB1g==","mcinfo":"03294000-13573946-8801423360-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/HkuJmKguhv6jGeEXdrKPR4ygyje\/frist.html","desc":"","text":""},"type":"ace"},{"alt":"","position":24,"src":"\/\/m.360buyimg.com\/babel\/jfs\/t1\/140042\/21\/20481\/60091\/5fe7f503Eea69fdd7\/b4b2147f196a9001.jpg!q95","href":"\/\/pro.jd.com\/mall\/active\/3s4A3dfrTy9K6FTXZWd1U67xJ9VR\/frist.html","ext_columns":{"biclk":"1#665d5684d2c8f77eb50e572ca2319914a7ad5e98-0-619066#27274062","focustype":"s","ap":"Wbj96fOBwO5Cyu6kQERnLQ==","mcinfo":"03294000-13573946-8801423363-M#0-2-1--59--#1-tb-#102-27274062#pc-home","url":"\/\/pro.jd.com\/mall\/active\/3s4A3dfrTy9K6FTXZWd1U67xJ9VR\/frist.html","desc":"","text":""},"type":"ace"}],"banner":[{"src":"\/\/imgcps.jd.com\/ling\/3486678\/6L-Q5Yqo5YGl6Lqr5oyH5Y2X\/6JCl5YW76L-b6Zi256-H\/p-5bd8253082acdd181d02fa5f\/f2af4529.jpg","href":"\/\/pro.jd.com\/mall\/active\/2DPCwovvaBUa7HciiQ2PHCvyECac\/frist.html?innerAnchor=3486678","type":"delivery","ext_columns":{"link":"\/\/pro.jd.com\/mall\/active\/2DPCwovvaBUa7HciiQ2PHCvyECac\/frist.html?innerAnchor=3486678","sku":"3486678","playImpr":"1#13#300002-4___","mcinfo":"null","focustype":"t","biclk":"1#13#acthot-B0007061-0-3486678-acthot-2#88","desc":"\u8425\u517b\u8fdb\u9636\u7bc7","text":"\u8fd0\u52a8\u5065\u8eab\u6307\u5357#3486678"}}]}];        //618大促上报降级配置
        window.pageConfig.handleReportStart=new Date('2020/11/10 22:00:00').getTime();

		window.pageConfig.handleReportEnd=new Date('2020/11/12 10:00:00').getTime();

		    </script>

    <script type="text/javascript">
        !function(e){pageConfig.isWide=function(){var n=e,i=document,o=i.documentElement,t=i.getElementsByTagName("body")[0],a=n.innerWidth||o.clientWidth||t.clientWidth;return a>=1370}();var n=[];pageConfig.isWide?(n.push("root61"),n.push("o2_wide")):n.push("o2_mini");var i=document.getElementsByTagName("html")[0];i.className=n.join(" ")}(window,void 0);
    </script>

    <script type="text/javascript">
        !function (n) {
            function o(n) {
                for (var o = n + "=", t = document.cookie.split(";"), e = 0; e < t.length; e++) {
                    for (var i = t[e]; " " == i.charAt(0);) i = i.substring(1, i.length);
                    if (0 == i.indexOf(o)) return i.substring(o.length, i.length)
                }
                return null
            }

            var t = o("pcm"), e = n.navigator.userAgent.toLocaleLowerCase(), i = "//m.jd.com",
                r = /iphone|android|symbianos|windows\sphone/g, c = /micromessenger|qq\/[\d.]+/i;
            return c.test(e) ? (n.location.href = "//wqs.jd.com/?from=jdindex", !1) : r.test(e) && "1" != t ? (n.location.href = i, !1) : void 0
        }(window);
    </script>

    <script type="text/javascript">
        window.search = function (a) {
            var b, c = "//search.jd.com/Search?keyword={keyword}&enc={enc}{additional}";
            var d = search.additinal || "";
            var e = document.getElementById(a);
            var f = e.value;
            if (f = f.replace(/^\s*(.*?)\s*$/, "$1"), f.length > 100 && (f = f.substring(0, 100)), "" == f) return void (window.location.href = window.location.href);
            var g = 0;
            "undefined" != typeof window.pageConfig && "undefined" != typeof window.pageConfig.searchType && (g = window.pageConfig.searchType);
            var h = "&cid{level}={cid}";
            var i = "string" == typeof search.cid ? search.cid : "";
            var j = "string" == typeof search.cLevel ? search.cLevel : "";
            var k = "string" == typeof search.ev_val ? search.ev_val : "";
            switch (g) {
                case 0:
                    break;
                case 1:
                    j = "-1", d += "&book=y";
                    break;
                case 2:
                    j = "-1", d += "&mvd=music";
                    break;
                case 3:
                    j = "-1", d += "&mvd=movie";
                    break;
                case 4:
                    j = "-1", d += "&mvd=education";
                    break;
                case 5:
                    var l = "&other_filters=%3Bcid1%2CL{cid1}M{cid1}[cid2]";
                    switch (j) {
                        case "51":
                            h = l.replace(/\[cid2]/, ""), h = h.replace(/\{cid1}/g, "5272");
                            break;
                        case "52":
                            h = l.replace(/\{cid1}/g, "5272"), h = h.replace(/\[cid2]/, "%3Bcid2%2CL{cid}M{cid}");
                            break;
                        case "61":
                            h = l.replace(/\[cid2]/, ""), h = h.replace(/\{cid1}/g, "5273");
                            break;
                        case "62":
                            h = l.replace(/\{cid1}/g, "5273"), h = h.replace(/\[cid2]/, "%3Bcid2%2CL{cid}M{cid}");
                            break;
                        case "71":
                            h = l.replace(/\[cid2]/, ""), h = h.replace(/\{cid1}/g, "5274");
                            break;
                        case "72":
                            h = l.replace(/\{cid1}/g, "5274"), h = h.replace(/\[cid2]/, "%3Bcid2%2CL{cid}M{cid}");
                            break;
                        case "81":
                            h = l.replace(/\[cid2]/, ""), h = h.replace(/\{cid1}/g, "5275");
                            break;
                        case "82":
                            h = l.replace(/\{cid1}/g, "5275"), h = h.replace(/\[cid2]/, "%3Bcid2%2CL{cid}M{cid}")
                    }
                    c = "//search-e.jd.com/searchDigitalBook?ajaxSearch=0&enc=utf-8&key={keyword}&page=1{additional}";
                    break;
                case 6:
                    j = "-1", c = "//music.jd.com/8_0_desc_0_0_1_15.html?key={keyword}";
                    break;
                case 7:
                    c = "//s-e.jd.com/Search?key={keyword}&enc=utf-8";
                    break;
                case 8:
                    c = "//search.jd.hk/Search?keyword={keyword}&enc=utf-8";
                    break;
                case 9:
                    d += "&market=1"
            }
            if ("string" == typeof i && "" != i && "string" == typeof j) {
                var m = /^(?:[1-8])?([1-3])$/;
                j = "-1" == j ? "" : m.test(j) ? RegExp.$1 : "";
                var n = h.replace(/\{level}/, j);
                n = n.replace(/\{cid}/g, i), d += n
            }
            if ("string" == typeof k && "" != k && (d += "&ev=" + k), f = encodeURIComponent(f), b = c.replace(/\{keyword}/, f), b = b.replace(/\{enc}/, "utf-8"), b = b.replace(/\{additional}/, d), "object" == typeof $o && ("string" == typeof $o.lastKeyword && (b += "&wq=" + encodeURIComponent($o.lastKeyword)), "string" == typeof $o.pvid && (b += "&pvid=" + $o.pvid)), b.indexOf("/search.jd.com/") > 0) try {
                JA.tracker.ngloader("search.000009", {key: f, posid: a, target: b})
            } catch (o) {
            }
            ("undefined" == typeof search.isSubmitted || 0 == search.isSubmitted) && (setTimeout(function () {
                window.location.href = b
            }, 50), search.isSubmitted = !0)
        };
    </script>


</head>

<body class="index">
<div class="mod_container">
    <!--无障碍占位-->
    <div id="J_accessibility"></div>
    <!--顶通占位 -->
    <div id="J_promotional-top">
    </div>
    <div id="shortcut">
        <div class="w">
            <ul class="fl" clstag="h|keycount|head|topbar_01">
                <li class="dropdown" id="ttbar-mycity"></li>
            </ul>

            <ul class="fr">
                <li class="fore1 dropdown" id="ttbar-login" clstag="h|keycount|head|topbar_02">
					<a href="//passport.jd.com/uc/login?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F" class="link-login">你好，请登录</a>&nbsp;&nbsp;<a
					href="//reg.jd.com/reg/person?ReturnUrl=https%3A//www.jd.com/" class="link-regist style-red">免费注册</a>
                </li>
                <li class="spacer"></li>
                <li class="fore2" clstag="h|keycount|head|topbar_03">
                    <div class="dt"><a target="_blank" href="//order.jd.com/center/list.action">我的订单</a></div>
                </li>
                <li class="spacer"></li>
                <li class="fore3 dropdown" id="ttbar-myjd" clstag="h|keycount|head|topbar_04">
                    <div class="dt cw-icon"><a target="_blank" href="//home.jd.com/">我的京东</a><i class="iconfont">&#xe610;</i><i
                            class="ci-right"><s>◇</s></i></div>
                    <div class="dd dropdown-layer"></div>
                </li>
                <li class="spacer"></li>
                <li class="fore4" clstag="h|keycount|head|topbar_05">
                    <div class="dt"><a target="_blank" href="//vip.jd.com/">京东会员</a></div>
                </li>
                <li class="spacer"></li>
                <li class="fore5" clstag="h|keycount|head|topbar_06">
                    <div class="dt"><a target="_blank" href="//b.jd.com/">企业采购</a></div>
                </li>
                <li class="spacer"></li>
                <li class="fore8 dropdown" id="ttbar-serv" clstag="h|keycount|head|topbar_07">
                    <div class="dt cw-icon">客户服务<i class="iconfont">&#xe610;</i><i class="ci-right"><s>◇</s></i></div>
                    <div class="dd dropdown-layer"></div>
                </li>
                <li class="spacer"></li>
                <li class="fore9 dropdown" id="ttbar-navs" clstag="h|keycount|head|topbar_08">
                    <div class="dt cw-icon">网站导航<i class="iconfont">&#xe610;</i><i class="ci-right"><s>◇</s></i></div>
                    <div class="dd dropdown-layer"></div>
                </li>
                <li class="spacer"></li>
                <li class="fore10 mobile" id="J_mobile" clstag="h|keycount|head|topbar_09">
                    <div class="dt mobile_txt">手机京东</div>
                    <div class="mobile_static">
                        <div class="mobile_static_qrcode"></div>
                    </div>
                    <div id='J_mobile_pop' class='mod_loading mobile_pop'>
                    </div>
                </li>
            </ul>
        </div>
    </div>


    <div id="header">
        <div class="w">
            <div id="logo" class="logo">
                <h1 class="logo_tit">
                    <a href="//www.jd.com" class="logo_tit_lk" clstag="h|keycount|head|logo_01">京东</a>
                </h1>
                <h2 class="logo_subtit">京东,多快好省</h2>
                <div class="logo_extend" clstag="h|keycount|head|logo_02"></div>
            </div>

            <div id="search">
                <div class="search-m">
                    <div class="search_logo">
                        <a href="//www.jd.com" class="search_logo_lk" clstag="h|keycount|head|logo_01" tabindex="-1">京东，多快好省</a>
                    </div>

                    <div class="form" role="serachbox">
                        <ul id="shelper" class="search-helper" style="display: none"></ul>
                        <input clstag="h|keycount|head|search_c" type="text"
                               onkeydown="javascript:if(event.keyCode==13) search('key');" autocomplete="off" id="key"
                               accesskey="s"
                               class="text"
                               aria-label="搜索"/>
                        <button clstag="h|keycount|head|search_a" onclick="search('key');return false;" class="button" aria-label="搜索">
                            <i
                                    class="iconfont">&#xe60b;</i></button>
                    </div>

                    <div id="settleup" class="dropdown" clstag="h|keycount|head|cart_null">
                        <div class="cw-icon">
                            <i class="iconfont">&#xe60c;</i>
                            <a target="_blank" href="//cart.jd.com/cart.action">我的购物车</a>
                            <i class="ci-count" id="shopping-amount"></i>
                        </div>
                        <div class="dropdown-layer">
                            <div id="J_cart_pop">
                                <span class="loading"></span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div id="hotwords" clstag="h|keycount|head|search_d" role=""></div>

            <div id="navitems" role="navigation">
                <div class="spacer"></div>
                                                            <ul id="navitems-group1">
                                        <li clstag="h|keycount|head|navi_01" class="fore1">
                                                    <a class="navitems-lk"
                               target="_blank"
                               href="https://miaosha.jd.com/"
                               aria-lable="秒杀">秒杀                                                            </a>
                                            </li>
                                                                            <li clstag="h|keycount|head|navi_02" class="fore2">
                                                    <a class="navitems-lk"
                               target="_blank"
                               href="https://a.jd.com/"
                               aria-lable="优惠券">优惠券                                                            </a>
                                            </li>
                                                                            <li clstag="h|keycount|head|navi_03" class="fore3">
                                                    <a class="navitems-lk"
                               target="_blank"
                               href="https://plus.jd.com/index?flow_system=appicon&flow_entrance=appicon11&flow_channel=pc"
                               aria-lable="PLUS会员">PLUS会员                                                            </a>
                                            </li>
                                                                            <li clstag="h|keycount|head|navi_04" class="fore4">
                                                    <a class="navitems-lk"
                               target="_blank"
                               href="https://red.jd.com/"
                               aria-lable="品牌闪购">品牌闪购                                                            </a>
                                            </li>
                                            </ul>
                        <div class="spacer"></div>
                                                                                <ul id="navitems-group2">
                                        <li clstag="h|keycount|head|navi_05" class="fore5">
                                                    <a class="navitems-lk"
                               target="_blank"
                               href="https://paimai.jd.com/"
                               aria-lable="拍卖">拍卖                                                            </a>
                                            </li>
                                                                            <li clstag="h|keycount|head|navi_06" class="fore6">
                                                    <a class="navitems-lk"
                               target="_blank"
                               href="https://jiadian.jd.com/"
                               aria-lable="京东家电">京东家电                                                            </a>
                                            </li>
                                                                            <li clstag="h|keycount|head|navi_07" class="fore7">
                                                    <a class="navitems-lk"
                               target="_blank"
                               href="https://chaoshi.jd.com/"
                               aria-lable="京东超市">京东超市                                                            </a>
                                            </li>
                                                                            <li clstag="h|keycount|head|navi_08" class="fore8">
                                                    <a class="navitems-lk"
                               target="_blank"
                               href="https://fresh.jd.com/"
                               aria-lable="京东生鲜">京东生鲜                                                            </a>
                                            </li>
                                            </ul>
                        <div class="spacer"></div>
                                                                                <ul id="navitems-group3">
                                        <li clstag="h|keycount|head|navi_09" class="fore9">
                                                    <a class="navitems-lk"
                               target="_blank"
                               href="https://www.jd.hk/"
                               aria-lable="京东国际">京东国际                                                            </a>
                                            </li>
                                                                            <li clstag="h|keycount|head|navi_10" class="fore10">
                                                    <a class="navitems-lk"
                               target="_blank"
                               href="https://www.jdcloud.com/cn/?utm_source=DMT_jdcom&utm_medium=title&utm_campaign=regular&utm_term=NA"
                               aria-lable="京东云">京东云                                                            </a>
                                            </li>
                                            </ul>
                        <div class="spacer"></div>
                                    
            </div>

            <div id="treasure"></div>
        </div>
    </div>
    <div class="fs">
        <div class="grid_c1 fs_inner">
            <div class="fs_col1">
                <div id='J_cate' class="cate J_cate" role="navigation" aria-label="左侧导航">
                    <ul class="JS_navCtn cate_menu">
                                                    <li class="cate_menu_item" data-index="1" clstag="h|keycount|head|category_01a">
                                                                <a target="_blank" class="cate_menu_lk" href="//jiadian.jd.com">家用电器</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="2" clstag="h|keycount|head|category_02a">
                                                                <a target="_blank" class="cate_menu_lk" href="//search.jd.com&#47;Search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;wq=%E6%89%8B%E6%9C%BA&amp;pvid=8858151673f941e9b1a4d2c7214b2b52">手机</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//wt.jd.com">运营商</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//shuma.jd.com&#47;">数码</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="3" clstag="h|keycount|head|category_03a">
                                                                <a target="_blank" class="cate_menu_lk" href="//diannao.jd.com&#47;">电脑</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//bg.jd.com">办公</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="4" clstag="h|keycount|head|category_04a">
                                                                <a target="_blank" class="cate_menu_lk" href="//channel.jd.com&#47;home.html">家居</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//channel.jd.com&#47;furniture.html">家具</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//jzjc.jd.com&#47;">家装</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//channel.jd.com&#47;kitchenware.html">厨具</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="5" clstag="h|keycount|head|category_05a">
                                                                <a target="_blank" class="cate_menu_lk" href="//phat.jd.com&#47;10-603.html">男装</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//phat.jd.com&#47;10-507.html">女装</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//phat.jd.com&#47;10-156.html">童装</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//channel.jd.com&#47;1315-1345.html">内衣</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="6" clstag="h|keycount|head|category_06a">
                                                                <a target="_blank" class="cate_menu_lk" href="//beauty.jd.com&#47;">美妆</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//phat.jd.com&#47;10-816.html">个护清洁</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//channel.jd.com&#47;pet.html">宠物</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="7" clstag="h|keycount|head|category_07a">
                                                                <a target="_blank" class="cate_menu_lk" href="//phat.jd.com&#47;10-184.html">女鞋</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//phat.jd.com&#47;10-183.html">箱包</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//pro.jd.com&#47;mall&#47;active&#47;2BcJPCVVzMEtMUynXkPscCSsx68W&#47;frist.html">钟表</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//channel.jd.com&#47;jewellery.html">珠宝</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="8" clstag="h|keycount|head|category_08a">
                                                                <a target="_blank" class="cate_menu_lk" href="//phat.jd.com&#47;10-185.html">男鞋</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//phat.jd.com&#47;10-109.html">运动</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//phat.jd.com&#47;10-272.html">户外</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="9" clstag="h|keycount|head|category_09a">
                                                                <a target="_blank" class="cate_menu_lk" href="//xinfang.jd.com&#47;">房产</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//car.jd.com&#47;">汽车</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//che.jd.com&#47;">汽车用品</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="10" clstag="h|keycount|head|category_10a">
                                                                <a target="_blank" class="cate_menu_lk" href="//search.jd.com&#47;Search?keyword=%E6%AF%8D%E5%A9%B4&amp;enc=utf-8&amp;wq=%E6%AF%8D%E5%A9%B4&amp;pvid=3e86f063795740d594b1bb1187e02063">母婴</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//toy.jd.com&#47;">玩具乐器</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="11" clstag="h|keycount|head|category_11a">
                                                                <a target="_blank" class="cate_menu_lk" href="//food.jd.com&#47;">食品</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//jiu.jd.com">酒类</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//fresh.jd.com">生鲜</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//prodev.jd.com&#47;mall&#47;active&#47;41YdRWconKueXwVVnLLM6YY4x4wU&#47;frist.html">特产</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="12" clstag="h|keycount|head|category_12a">
                                                                <a target="_blank" class="cate_menu_lk" href="//art.jd.com">艺术</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//channel.jd.com&#47;1672-2599.html">礼品鲜花</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//nong.jd.com">农资绿植</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="13" clstag="h|keycount|head|category_13a">
                                                                <a target="_blank" class="cate_menu_lk" href="//phat.jd.com&#47;10-925.html">医药保健</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//channel.jd.com&#47;9192-9196.html">计生情趣</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="14" clstag="h|keycount|head|category_14a">
                                                                <a target="_blank" class="cate_menu_lk" href="//pro.jd.com&#47;mall&#47;active&#47;3sAaxodHF7kfo3s95cjxo2UZUxu2&#47;frist.html">图书</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//pro.jd.com&#47;mall&#47;active&#47;2TxxbZnqAm7M8tkDpTN3VJNtoSKo&#47;frist.html">文娱</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//education.jd.com">教育</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//e.jd.com&#47;ebook.html">电子书</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="15" clstag="h|keycount|head|category_15a">
                                                                <a target="_blank" class="cate_menu_lk" href="//jipiao.jd.com&#47;">机票</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//hotel.jd.com&#47;">酒店</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//trip.jd.com&#47;">旅游</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//ish.jd.com&#47;">生活</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="16" clstag="h|keycount|head|category_16a">
                                                                <a target="_blank" class="cate_menu_lk" href="//licai.jd.com&#47;">理财</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//pro.jd.com&#47;mall&#47;active&#47;4EYjXQ6xjnM9TgeSjuMRE8ACEk6q&#47;frist.html">众筹</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//baitiao.jd.com">白条</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//pro.jd.com&#47;mall&#47;active&#47;4NuyHPocGdSDUzmSVosXjVwvEGdG&#47;frist.html">保险</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="17" clstag="h|keycount|head|category_17a">
                                                                <a target="_blank" class="cate_menu_lk" href="//anzhuang.jd.com">安装</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//search.jd.com&#47;Search?keyword=维修&amp;enc=utf-8&amp;wq=维修&amp;pvid=eba9b7454da0494c960f074db37be847">维修</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//cleanclean.jd.com">清洗</a>
                                                                            <span class="cate_menu_line">/</span>
                                                                                                    <a target="_blank" class="cate_menu_lk" href="//2.jd.com&#47;">二手</a>
                                                                                                </li>
                                                    <li class="cate_menu_item" data-index="18" clstag="h|keycount|head|category_18a">
                                                                <a target="_blank" class="cate_menu_lk" href="//mro.jd.com&#47;">工业品</a>
                                                                                                </li>
                                            </ul>
                    <div id="J_popCtn" class="JS_popCtn cate_pop mod_loading" style="display: none;"></div>
                </div>
            </div>

            <div class="fs_col2">
                <div id='J_focus' class="focus">
                    <div class="focus__loading focus__main skeleton-wrapper">
                        <div class="focus-slider">
                        <div class="focus-item__core skeleton-elementDark mod_lazyload"></div>
                        <div class="focus-item__recommend">
                            <div class="recommend-item skeleton-elementDark"></div>
                            <div class="recommend-item skeleton-elementDark"></div>
                            <div class="recommend-item skeleton-elementDark"></div>
                        </div>
                        </div>
                    </div>
                </div>
            </div>

            <div id="J_fs_col3" class="fs_col3">
                <div id='J_user' class="J_user user mod_loading">
                    <div class="user__loading user_inner">
                    <div class="user_avatar">
                        <div class="user_avatar_lk skeleton-element"></div>
                    </div>
                    <div class="user_show skeleton-element">
                        <p></p><p></p>
                    </div>
                    <div class="user_profit_placeholder skeleton-element"></div>
                </div>
                </div>
                <div id='J_news' class="news J_news">
                    <div class="news__loading news2">
                        <div class="news_hd">
                        <div class="news_hd_placeholder skeleton-element"></div>
                        </div>
                        <div class="news_list"><div class="news_item skeleton-element"></div><div class="news_item skeleton-element"></div><div class="news_item skeleton-element"></div><div class="news_item skeleton-element"></div></div>
                    </div>
                </div>
                <div id="J_service" class="service">
                    <div class="service_entry">
                        <ul class="J_tab_head service_list">
                            <li class="service_item service_frame mod_tab_head_item">
                                <a href="//chongzhi.jd.com/" class="service_lk"
                                   target="_blank" clstag="h|keycount|head|shortcut_01" aria-label="话费">
                                                                                                                                                    <i class="service_ico service_ico_huafei">
                                        <img class="service_ico_img"
                                             src="//m.360buyimg.com/babel/jfs/t1/30057/19/14881/720/5cbf064aE187b8361/eed6f6cbf1de3aaa.png"/>
                                        <img class="service_ico_img_hover"
                                             src="//m.360buyimg.com/babel/jfs/t1/45423/33/385/778/5cd4f265E442a9342/0aff0a42cece09ee.png"/>
                                    </i>
                                    <span class="service_txt">话费</span>
                                </a>
                            </li>
                            <li class="service_item service_frame mod_tab_head_item">
                                <a href="//jipiao.jd.com/" class="service_lk" target="_blank"
                                   clstag="h|keycount|head|shortcut_02" aria-label="机票">
                                                                                                                                                    <i class="service_ico service_ico_jipiao">
                                        <img class="service_ico_img"
                                             src="//m.360buyimg.com/babel/jfs/t1/36478/38/5384/2901/5cbf065aEb0c60a12/afb4399323fe3b76.png"/>
                                        <img class="service_ico_img_hover"
                                             src="//m.360buyimg.com/babel/jfs/t1/34261/15/10242/3120/5cd4f256E10257aba/8f3f63ae04ff19af.png"/>
                                    </i>
                                    <span class="service_txt">机票</span>
                                </a>
                            </li>
                            <li class="service_item service_frame mod_tab_head_item">
                                <a href="//hotel.jd.com/" class="service_lk" target="_blank"
                                   clstag="h|keycount|head|shortcut_03" aria-label="酒店">
                                                                                                                                                    <i class="service_ico service_ico_jiudian">
                                        <img class="service_ico_img"
                                             src="//m.360buyimg.com/babel/jfs/t1/31069/34/14642/979/5cbf0665Ec7dc8223/5fee386254dd2ebc.png"/>
                                        <img class="service_ico_img_hover"
                                             src="//m.360buyimg.com/babel/jfs/t1/44601/19/915/1039/5cd4f1cfE2e46473c/b61f083872a7a1de.png"/>
                                    </i>
                                    <span class="service_txt">酒店</span>
                                </a>
                            </li>
                            <li class="service_item service_frame service_frame2 mod_tab_head_item" data-row="2">
                                <a href="//game.jd.com/" class="service_lk" target="_blank"
                                   clstag="h|keycount|head|shortcut_04" aria-label="游戏">
                                                                                                                                                    <i class="service_ico service_ico_youxi">
                                        <img class="service_ico_img"
                                             src="//m.360buyimg.com/babel/jfs/t1/32403/22/14829/3699/5cbf0674E04723693/caa83ce9b881cd24.png"/>
                                        <img class="service_ico_img_hover"
                                             src="//m.360buyimg.com/babel/jfs/t1/57520/8/375/4092/5cd4f1d8Ea1266047/1c590322ece537ba.png"/>
                                    </i>
                                    <span class="service_txt">游戏</span>
                                </a>
                            </li>
                                                                                                                                                                                                                                                                                                                                                <li class="service_item service_noframe">
                                        <a href="https:&#47;&#47;jiayouka.jd.com&#47;" class="service_lk" target="_blank"
                                           clstag="h|keycount|head|shortcut_05" aria-label="加油卡">
                                                                                        <i class="service_ico">
                                                <!-- 常态 icon -->
                                                <img class="service_ico_img"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;71890&#47;14&#47;9897&#47;3048&#47;5d7739ddE93eb94f8&#47;f1f6dc5c207329f9.png"/>
                                                <!-- hover 态 icon -->
                                                <img class="service_ico_img_hover"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;36002&#47;35&#47;9106&#47;3311&#47;5cd4f1bdE06ff07ed&#47;9570fdd46ecd3a76.png"/>
                                            </i>
                                            <span class="service_txt">加油卡</span>
                                        </a>
                                    </li>
                                                                                                                                <li class="service_item service_noframe">
                                        <a href="https:&#47;&#47;train.jd.com&#47;" class="service_lk" target="_blank"
                                           clstag="h|keycount|head|shortcut_06" aria-label="火车票">
                                                                                        <i class="service_ico">
                                                <!-- 常态 icon -->
                                                <img class="service_ico_img"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;45761&#47;32&#47;10307&#47;1581&#47;5d7739e2Ece4b6671&#47;0004c1b85fbf7bde.png"/>
                                                <!-- hover 态 icon -->
                                                <img class="service_ico_img_hover"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;58891&#47;36&#47;278&#47;1745&#47;5cd4f1e0Ef4cc50a7&#47;f12276b17e5dcf3b.png"/>
                                            </i>
                                            <span class="service_txt">火车票</span>
                                        </a>
                                    </li>
                                                                                                                                <li class="service_item service_noframe">
                                        <a href="https:&#47;&#47;pro.jd.com&#47;mall&#47;active&#47;4EYjXQ6xjnM9TgeSjuMRE8ACEk6q&#47;frist.html" class="service_lk" target="_blank"
                                           clstag="h|keycount|head|shortcut_07" aria-label="众筹">
                                                                                        <i class="service_ico">
                                                <!-- 常态 icon -->
                                                <img class="service_ico_img"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;51584&#47;31&#47;10221&#47;1685&#47;5d7739e7E1adb25cd&#47;1d0957d7f2ae01a2.png"/>
                                                <!-- hover 态 icon -->
                                                <img class="service_ico_img_hover"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;50929&#47;1&#47;374&#47;1847&#47;5cd4f1eaE5daf90db&#47;cebbff76b25dc22e.png"/>
                                            </i>
                                            <span class="service_txt">众筹</span>
                                        </a>
                                    </li>
                                                                                                                                <li class="service_item service_noframe">
                                        <a href="https:&#47;&#47;jr.jd.com&#47;" class="service_lk" target="_blank"
                                           clstag="h|keycount|head|shortcut_08" aria-label="理财">
                                                                                        <i class="service_ico">
                                                <!-- 常态 icon -->
                                                <img class="service_ico_img"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;52683&#47;35&#47;10394&#47;3447&#47;5d7739edE270aa7b3&#47;d4d1151b09b5553b.png"/>
                                                <!-- hover 态 icon -->
                                                <img class="service_ico_img_hover"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;47544&#47;23&#47;372&#47;3943&#47;5cd4f24eE92fbcf79&#47;4b49b55af25a7bdf.png"/>
                                            </i>
                                            <span class="service_txt">理财</span>
                                        </a>
                                    </li>
                                                                                                                                <li class="service_item service_noframe">
                                        <a href="https:&#47;&#47;baitiao.jd.com&#47;?from=jrscyn_20160" class="service_lk" target="_blank"
                                           clstag="h|keycount|head|shortcut_09" aria-label="白条">
                                                                                        <i class="service_ico">
                                                <!-- 常态 icon -->
                                                <img class="service_ico_img"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;56296&#47;3&#47;10260&#47;1443&#47;5d7739f3E233abc53&#47;e6976f3cb30c9a8a.png"/>
                                                <!-- hover 态 icon -->
                                                <img class="service_ico_img_hover"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;39983&#47;24&#47;6834&#47;1596&#47;5cd4f247E8cf89f1e&#47;b8a8418d5418f471.png"/>
                                            </i>
                                            <span class="service_txt">白条</span>
                                        </a>
                                    </li>
                                                                                                                                <li class="service_item service_noframe">
                                        <a href="https:&#47;&#47;movie.jd.com&#47;frist.html" class="service_lk" target="_blank"
                                           clstag="h|keycount|head|shortcut_10" aria-label="电影票">
                                                                                        <i class="service_ico">
                                                <!-- 常态 icon -->
                                                <img class="service_ico_img"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;60778&#47;37&#47;9838&#47;3066&#47;5d7739faEd3b7dbb9&#47;dd4d9ef7ce8fc169.png"/>
                                                <!-- hover 态 icon -->
                                                <img class="service_ico_img_hover"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;41106&#47;15&#47;4551&#47;3300&#47;5cd4f1c7E507148c7&#47;90a218f053e903d2.png"/>
                                            </i>
                                            <span class="service_txt">电影票</span>
                                        </a>
                                    </li>
                                                                                                                                <li class="service_item service_noframe">
                                        <a href="https:&#47;&#47;b.jd.com&#47;" class="service_lk" target="_blank"
                                           clstag="h|keycount|head|shortcut_11" aria-label="企业购">
                                                                                        <i class="service_ico">
                                                <!-- 常态 icon -->
                                                <img class="service_ico_img"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;40738&#47;20&#47;14562&#47;826&#47;5d773a01E09eb8121&#47;d6f3909618c6307a.png"/>
                                                <!-- hover 态 icon -->
                                                <img class="service_ico_img_hover"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;45316&#47;3&#47;388&#47;884&#47;5cd4f25eEea4c67ed&#47;671f7c186c5e9b01.png"/>
                                            </i>
                                            <span class="service_txt">企业购</span>
                                        </a>
                                    </li>
                                                                                                                                <li class="service_item service_noframe">
                                        <a href="https:&#47;&#47;o.jd.com" class="service_lk" target="_blank"
                                           clstag="h|keycount|head|shortcut_12" aria-label="礼品卡">
                                                                                        <i class="service_ico">
                                                <!-- 常态 icon -->
                                                <img class="service_ico_img"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;57014&#47;6&#47;10297&#47;815&#47;5d773a07Ec7a61fc9&#47;97917a2daa34be0f.png"/>
                                                <!-- hover 态 icon -->
                                                <img class="service_ico_img_hover"
                                                        src="https:&#47;&#47;m.360buyimg.com&#47;babel&#47;jfs&#47;t1&#47;55911&#47;31&#47;402&#47;858&#47;5cd4f23eE6f536460&#47;5da079255c6dfabe.png"/>
                                            </i>
                                            <span class="service_txt">礼品卡</span>
                                        </a>
                                    </li>
                                                                                    </ul>
                    </div>
                    <div class="J_tab_content service_pop" tabindex="-1" aria-hidden="true">
                        <div class="mod_tab_content_item service_pop_item mod_loading"></div>
                        <div class="mod_tab_content_item service_pop_item mod_loading"></div>
                        <div class="mod_tab_content_item service_pop_item mod_loading"></div>
                        <div class="mod_tab_content_item service_pop_item mod_loading"></div>
                        <a class="J_service_pop_close service_pop_close iconfont" href="javascript:;" tabindex="-1"></a>
                    </div>
                </div>
            </div>
        </div>
        <div id="J_fs_act" class="fs_act"></div>
    </div>
    <!-- CLUB_LINK start seo  -->
    <div style="display:none">
                <a href="//itb2b.jd.com/">京采汇</a>
                <a href="//pro.m.jd.com/mall/active/2ukQm4T7b9utHWDn2cXGH2KEnUYV/frist.html">电动车十大排行榜</a>
                <a href="//pro.m.jd.com/mall/active/pVc2ZtPRvzzCuAE8eRSfXFvan1d/frist.html">电动车价钱</a>
                <a href="//jzt.m.jd.com/school/market/2021/11/11">京准通11.11</a>
                <a href="//pro.m.jd.com/mall/active/wcvrZNcfWbUV6spvqoY17CXwny1/frist.html">电动车十大名牌排名</a>
                <a href="//pro.m.jd.com/mall/active/2GYft5Ph4ZAAAQKWxJyHtsFun1ef/frist.html">十大名牌电动车</a>
                <a href="//pro.m.jd.com/mall/active/2GL7sRxRYrRSE6Zk7DesxmQ5JDvc/frist.html">电动车三轮车</a>
                <a href="//pro.m.jd.com/mall/active/22ADrLDeC31kzfT171t8UYDcRf23/frist.html">电动车排行</a>
                <a href="//union.jd.com">网络赚钱</a>
                <a href="//pro.m.jd.com/mall/active/1X36PoLQQ6JYgrLusHZpfowpxpc/frist.html">电动车十大品牌排行榜</a>
                <a href="//pro.m.jd.com/mall/active/3VLqBaQBjR3XxwDBNdDYMMAAX1wc/frist.html">电动车十大排行</a>
                <a href="//pro.m.jd.com/mall/active/3ERkqhxNQozbNJ3BQCxUX3p1sFEC/frist.html">电动车十佳品牌排行榜</a>
                <a href="//pro.m.jd.com/mall/active/TU6auzpj8HDPAqumWMZ35uML4HB/frist.html">电动车电池十大排名</a>
                <a href="//pro.m.jd.com/mall/active/3uxWVvqh2dmwN2eLbqDfGj6BBoAk/frist.html">台铃电动车</a>
                <a href="//www.jd.com/sptopic/117296ca19d46b24dfeb3.html">女士鞋</a>
                <a href="//www.jd.com/cppf/9847333cd3d99d6886d9.html">实木沙发</a>
                <a href="//www.jd.com/book/737280eea8ac7dfea03.html">索尼电视</a>
                <a href="//www.jd.com/hotitem/9855fbd5a67b591890f1.html">卫浴品牌</a>
                <a href="//www.jd.com/zuozhe/7378d855fa5f85d59a5.html">奥克斯空调</a>
                <a href="//fresh.jd.com/shengxian/12218e48f879c700b44c1.html">百香果</a>
                <a href="https://yp.jd.com/7377d3c8a4968258130.html">GRUNDIG单门冰箱</a>
                <a href="https://www.jd.com/phb/737f64b59e992c66a6f.html">冷藏电冰箱</a>
                <a href="https://www.jd.com/phb/key_73725f14e47c03c15c5.html">容声冰箱298</a>
                <a href="https://www.jd.com/jiage/7376fe7f55502d0a7ec.html">透明门冰箱</a>
                <a href="https://www.jd.com/tupian/73792191caea54bc808.html">tcl冰箱bcd</a>
                <a href="https://www.jd.com/xinkuan/7371d3a90210ed3fcaf.html">志高冰箱150升</a>
                <a href="https://www.jd.com/book/737443fc26555bfdac0.html">海尔331wdgq</a>
                <a href="https://www.jd.com/zuozhe/7377972dc445b62f582.html">松下C33PX3</a>
                <a href="https://www.jd.com/brand/737365576432376ed6c.html">哪个牌子小型冰箱好</a>
                <a href="https://www.jd.com/xinghao/737b70ebe94be829e97.html">京东自营商品三门冰箱</a>
                <a href="https://www.jd.com/cppf/737453941288c954b5f.html">冰箱全球排名</a>
                <a href="https://www.jd.com/hprm/737cd4a708adc7ba68e.html">SMEG十字对开门变频冰箱</a>
                <a href="https://www.jd.com/sptopic/7378f81be6e97539ff7.html">樱花两门冰箱</a>
                <a href="https://www.jd.com/hotitem/737224025527511c7b3.html">格力晶弘冰箱302</a>
                <a href="https://www.jd.com/nrjs/12cd9dbc6ebf9a4e.html">双门JINSONG冰箱排行榜，双门JINSONG冰箱十大排名推荐</a>
                <a href="https://www.jd.com/zxnews/4909539db88bec6c.html">三门定频冰箱排行榜，三门定频冰箱十大排名推荐</a>
                <a href="https://www.jd.com/phb/zhishi/caab8e540c2a400e.html">容声对开门排行榜，容声对开门十大排名推荐</a>
                <a href="https://www.jd.com/phb/zhishi/f149f48ad864e784.html">【冰箱推荐】食材保鲜不等待，变频冰箱来助力</a>
                <a href="https://www.jd.com/jxinfo/79dbe5f667bf14bc.html">Casarte多门排行榜，Casarte多门十大排名推荐</a>
                <a href="https://www.jd.com/jxinfo/5f453727e1a3640b.html">婴儿小冰箱排行榜，婴儿小冰箱十大排名推荐</a>
            </div>
    <!-- CLUB_LINK end -->
    <script type="text/javascript">
        window.point.fs = new Date().getTime();
    </script>
    <!-- E ad2 -->

</div>

<script src="//storage.360buyimg.com/pc-pre-tmp/jquery.js"></script>
<script src="//misc.360buyimg.com/??mtd/pc/common/js/o2_ua.js,mtd/pc/base/1.0.0/event.js"></script>
<script src="//wl.jd.com/wl.js"></script>

<script>

</script>

<style>

.o2_ie8 .more2_international {

    filter: progid:dximagetransform.microsoft.alphaimageloader(src='//storage.360buyimg.com/mtd/home/more_international1575014601797.png',sizingMethod='scale');

    background: none;

}

.mod_help_cover {

    background-image: none;

}

#settleup:hover .cw-icon {

    border-bottom: 1px solid #c81623;

}

.o2_mini .company .feed-tab {

    margin: 0 auto;

}

.company .feed-tab {

    margin: 0 auto;

}

.channelsB .channels_block_1 .channels_item_1 .channels_item_link {

    height: 370px;

    width: 290px;

}

.channelsB .channels_block_1 .channels_item_2 .channels_item_link {

    height: 370px;

    width: 290px;

}

.JD_close-button--square {

  z-index: 1;

}

</style>
<div id="app"></div>
<script type="text/javascript">
    window.point.dom = new Date().getTime();
</script>

<style type="text/css">
.mod_footer {
  height: 500px;
  background-color: #eaeaea;
}

/* 服务承诺 */
.mod_service {
  padding: 30px 0;
  border-bottom: 1px solid #dedede;
}

.mod_service_list {
  overflow: hidden;
  height: 42px;
}

.mod_service_item {
  float: left;
  width: 297px;
}

.mod_service_unit {
  position: relative;
  margin: 0 auto;
  padding-left: 45px;
  width: 180px;
}

.mod_service_tit {
  overflow: hidden;
  position: absolute;
  left: 0;
  top: 0;
  width: 36px;
  height: 42px;
  text-indent: -999px;
}

.mod_service_txt {
  overflow: hidden;
  width: 100%;
  height: 42px;
  line-height: 42px;
  font-size: 18px;
  font-weight: 700;
  text-overflow: ellipsis;
  white-space: nowrap;
  color: #444;
}

/* 多快好省的图标 */
.mod_service_duo {
  background-repeat: no-repeat;
  background-position: 0 -192px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_service_kuai {
  background-repeat: no-repeat;
  background-position: -41px -192px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_service_hao {
  background-repeat: no-repeat;
  background-position: -82px -192px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_service_sheng {
  background-repeat: no-repeat;
  background-position: -123px -192px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

/* 帮助清单 */
.mod_help {
  padding: 20px 0;
}

.mod_help_list {
  overflow: hidden;
  height: 160px;
}

.mod_help_nav {
  float: left;
  width: 198px;
  line-height: 22px;
}

.mod_help_nav_tit {
  margin-bottom: 5px;
  font-size: 14px;
}

.mod_help_cover {
  background-repeat: no-repeat;
  background-position: 0 0;
  float: right;
  width: 200px;
  height: 150px;
}

.mod_help_cover_tit {
  margin-bottom: 15px;
  font-size: 14px;
  text-align: center;
}

.mod_help_cover_con {
  padding: 0 10px;
}

.mod_help_cover_more {
  text-align: right;
}

/* 版权信息 */
.mod_copyright_inner {
  padding: 15px 0;
  border-top: 1px solid #e1e1e1;
  text-align: center;
}

.mod_copyright_split {
  margin: 0 7px;
  color: #ccc;
}

.mod_copyright_info {
  padding: 10px 0;
  line-height: 22px;
  color: #999;
}

.mod_copyright_info a {
  color: #999;
}

.mod_copyright_info a:hover {
  color: #c81623;
}

.mod_copyright_inter_ico {
  display: inline-block;
  width: 15px;
  height: 10px;
  vertical-align: -1px;
  margin-right: 10px;
  background-repeat: no-repeat;
}

.mod_copyright_inter_ico_global {
  background-repeat: no-repeat;
  background-position: -108px -155px;
  width: 15px;
  height: 12px;
  margin-top: -1px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_copyright_inter_ico_rissia {
  background-repeat: no-repeat;
  background-position: -168px -155px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_copyright_inter_ico_indonesia {
  background-repeat: no-repeat;
  background-position: -148px -155px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_copyright_inter_ico_thailand {
  background-repeat: no-repeat;
  background-position: -108px -172px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_copyright_inter_ico_spain {
  background-repeat: no-repeat;
  background-position: -128px -155px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_copyright_auth {
  margin: 25px 0;
}

.mod_copyright_auth_ico {
  overflow: hidden;
  display: inline-block;
  margin: 0 3px;
  width: 103px;
  height: 32px;
  line-height: 1000px;
}

.mod_copyright_auth_ico_1 {
  background-repeat: no-repeat;
  background-position: -205px -148px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_copyright_auth_ico_2 {
  background-repeat: no-repeat;
  background-position: -205px -111px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_copyright_auth_ico_3 {
  background-repeat: no-repeat;
  background-position: -205px -74px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_copyright_auth_ico_4 {
  background-repeat: no-repeat;
  background-position: -205px -37px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_copyright_auth_ico_5 {
  background-repeat: no-repeat;
  background-position: 0 -66px;
  background-image: url(//img13.360buyimg.com/imagetools/jfs/t1/108497/17/22418/15570/6215e0d0E01387603/81e883d9e15cebb7.png);
}

.mod_copyright_auth_ico_6 {
  background-repeat: no-repeat;
  background-position: 0 -155px;
  background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211298/12/18097/67160/6215e091E7fb1c693/cc1d8d291ea917c0.png);
}

.mod_copyright_auth_ico_7 {
  background-repeat: no-repeat;
  background-position: 0 -99px;
  background-image: url(//img13.360buyimg.com/imagetools/jfs/t1/108497/17/22418/15570/6215e0d0E01387603/81e883d9e15cebb7.png);
}

.mod_copyright_auth_ico_8 {
  width: 70px;
  background-repeat: no-repeat;
  background-position: -104px -99px;
  background-image: url(//img13.360buyimg.com/imagetools/jfs/t1/108497/17/22418/15570/6215e0d0E01387603/81e883d9e15cebb7.png);
}

.mod_copyright_auth_ico_9 {
  width: 88px;
  background-repeat: no-repeat;
  background-position: -104px -131px;
  background-image: url(//img13.360buyimg.com/imagetools/jfs/t1/108497/17/22418/15570/6215e0d0E01387603/81e883d9e15cebb7.png);
}

// .mod_copyright_license {
//   margin-left: 16px;
// }

/* 适配高清屏 */

@media only screen and (-webkit-min-device-pixel-ratio: 1.5),
  only screen and (min--moz-device-pixel-ratio: 1.5),
  only screen and (-o-min-device-pixel-ratio: 3/2),
  only screen and (min-device-pixel-ratio: 1.5) {

  .mod_service_duo {
    background-repeat: no-repeat;
    background-size: 113px 86.5px;
    background-position: 0 0;
    background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211722/38/13035/9322/6215e10cEa9918ac1/7f8686ee76e42123.png);
  }

  .mod_service_kuai {
    background-repeat: no-repeat;
    background-size: 113px 86.5px;
    background-position: -38.5px 0;
    background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211722/38/13035/9322/6215e10cEa9918ac1/7f8686ee76e42123.png);
  }

  .mod_service_hao {
    background-repeat: no-repeat;
    background-size: 113px 86.5px;
    background-position: -77px 0;
    background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211722/38/13035/9322/6215e10cEa9918ac1/7f8686ee76e42123.png);
  }

  .mod_service_sheng {
    background-repeat: no-repeat;
    background-size: 113px 86.5px;
    background-position: 0 -44.5px;
    background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211722/38/13035/9322/6215e10cEa9918ac1/7f8686ee76e42123.png);
  }

  .mod_copyright_inter_ico_global {
    background-repeat: no-repeat;
    background-size: 113px 86.5px;
    background-position: -38.5px -44.5px;
    background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211722/38/13035/9322/6215e10cEa9918ac1/7f8686ee76e42123.png);
  }

  .mod_copyright_inter_ico_rissia {
    background-repeat: no-repeat;
    background-size: 113px 86.5px;
    background-position: -56px -44.5px;
    background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211722/38/13035/9322/6215e10cEa9918ac1/7f8686ee76e42123.png);
  }

  .mod_copyright_inter_ico_indonesia {
    background-repeat: no-repeat;
    background-size: 113px 86.5px;
    background-position: -73.5px -44.5px;
    background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211722/38/13035/9322/6215e10cEa9918ac1/7f8686ee76e42123.png);
  }

  .mod_copyright_inter_ico_thailand {
    background-repeat: no-repeat;
    background-size: 113px 86.5px;
    background-position: -91px -44.5px;
    background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211722/38/13035/9322/6215e10cEa9918ac1/7f8686ee76e42123.png);
  }

  .mod_copyright_inter_ico_spain {
    background-repeat: no-repeat;
    background-size: 113px 86.5px;
    background-position: -38.5px -59px;
    background-image: url(//img10.360buyimg.com/imagetools/jfs/t1/211722/38/13035/9322/6215e10cEa9918ac1/7f8686ee76e42123.png);
  }

  .mod_copyright_inter_lk {
    font-family: initial;
  }
}

/* 窄版 */
.o2_mini .mod_service_item {
  width: 247px;
}

.o2_mini .mod_help_nav {
  width: 158px;
}

.o2_mini .mod_copyright_links .mod_copyright_split {
  margin: 0 6px;
}
</style>
<script type="text/javascript">
  function clickReport(){
    $("body").delegate("[poi]", "click", function(e){
        let $current = $(e.target)
        let tagName = $current.prop("tagName")

        if(tagName === 'A' || tagName === 'a'){
          let fullpoi = $current.attr('poi') ? $current.attr('poi') : $current.parents('[poi]').attr('poi')
          let url = $current.attr('href')
          let text = $.trim($current.text())

          window.footerGetOnClick && window.footerGetOnClick(fullpoi, url, text)
        }
    })
  }
  clickReport()
</script>
<div id="J_footer" class="footer">
  <div class="mod_service" clstag="btm|btmnavi_null01" poi="btm|btmnavi|null01">
    <div class="grid_c1 mod_service_inner">
      <ul class="mod_service_list">
        <li class="mod_service_item">
          <div class="mod_service_unit">
            <h5 class="mod_service_tit mod_service_duo">多</h5>
            <p class="mod_service_txt">品类齐全，轻松购物</p>
          </div>
        </li>
        <li class="mod_service_item">
          <div class="mod_service_unit">
            <h5 class="mod_service_tit mod_service_kuai">快</h5>
            <p class="mod_service_txt">多仓直发，极速配送</p>
          </div>
        </li>
        <li class="mod_service_item">
          <div class="mod_service_unit">
            <h5 class="mod_service_tit mod_service_hao">好</h5>
            <p class="mod_service_txt">正品行货，精致服务</p>
          </div>
        </li>
        <li class="mod_service_item">
          <div class="mod_service_unit">
            <h5 class="mod_service_tit mod_service_sheng">省</h5>
            <p class="mod_service_txt">天天低价，畅选无忧</p>
          </div>
        </li>
      </ul>
    </div>
  </div>

  <div class="mod_help" clstag="btm|btmnavi_null02" poi="btm|btmnavi|null02">
    <div class="grid_c1 mod_help_inner">
      <div class="mod_help_list">
        <div class="mod_help_nav">
          <h5 class="mod_help_nav_tit">购物指南</h5>
          <ul class="mod_help_nav_con">
            <li>
              <a href="//help.jd.com/user/issue/list-29.html" target="_blank" rel="noopener noreferrer">
                购物流程
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/list-151.html" target="_blank" rel="noopener noreferrer">
                会员介绍
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/list-297.html" target="_blank" rel="noopener noreferrer">
                生活旅行
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue.html" target="_blank" rel="noopener noreferrer">
                常见问题
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/list-136.html" target="_blank" rel="noopener noreferrer">
                大家电
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/custom.html" target="_blank" rel="noopener noreferrer">
                联系客服
              </a>
            </li>
          </ul>
        </div>
        <div class="mod_help_nav">
          <h5 class="mod_help_nav_tit">配送方式</h5>
          <ul class="mod_help_nav_con">
            <li>
              <a href="//help.jd.com/user/issue/list-81-100.html" target="_blank" rel="noopener noreferrer">
                上门自提
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/list-81.html" target="_blank" rel="noopener noreferrer">
                211限时达
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/103-983.html" target="_blank" rel="noopener noreferrer">
                配送服务查询
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/109-188.html" target="_blank" rel="noopener noreferrer">
                配送费收取标准
              </a>
            </li>
            <li>
              <a href="//help.joybuy.com/help/question-list-201.html" target="_blank" rel="noopener noreferrer">
                海外配送
              </a>
            </li>
          </ul>
        </div>
        <div class="mod_help_nav">
          <h5 class="mod_help_nav_tit">支付方式</h5>
          <ul class="mod_help_nav_con">
            <li>
              <a href="//help.jd.com/user/issue/list-172.html" target="_blank" rel="noopener noreferrer">
                货到付款
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/list-173.html" target="_blank" rel="noopener noreferrer">
                在线支付
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/list-176.html" target="_blank" rel="noopener noreferrer">
                分期付款
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/list-175.html" target="_blank" rel="noopener noreferrer">
                公司转账
              </a>
            </li>
          </ul>
        </div>
        <div class="mod_help_nav">
          <h5 class="mod_help_nav_tit">售后服务</h5>
          <ul class="mod_help_nav_con">
            <li>
              <a href="//help.jd.com/user/issue/list-112.html" target="_blank" rel="noopener noreferrer">
                售后政策
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/list-132.html" target="_blank" rel="noopener noreferrer">
                价格保护
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/130-978.html" target="_blank" rel="noopener noreferrer">
                退款说明
              </a>
            </li>
            <li>
              <a href="//myjd.jd.com/repair/repairs.action" target="_blank" rel="noopener noreferrer">
                返修/退换货
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/list-50.html" target="_blank" rel="noopener noreferrer">
                取消订单
              </a>
            </li>
          </ul>
        </div>
        <div class="mod_help_nav">
          <h5 class="mod_help_nav_tit">特色服务</h5>
          <ul class="mod_help_nav_con">
            <li>
              <a href="//1paipai.jd.com/" target="_blank" rel="noopener noreferrer">
                夺宝岛
              </a>
            </li>
            <li>
              <a href="//help.jd.com/user/issue/list-134.html" target="_blank" rel="noopener noreferrer">
                DIY装机
              </a>
            </li>
            <li>
              <a href="//fuwu.jd.com/" target="_blank" rel="noopener noreferrer">
                延保服务
              </a>
            </li>
            <li>
              <a href="//o.jd.com/market/index.action" target="_blank" rel="noopener noreferrer">
                京东E卡
              </a>
            </li>
            <li>
              <a href="//mobile.jd.com/" target="_blank" rel="noopener noreferrer">
                京东通信
              </a>
            </li>
            <li>
              <a href="//smart.jd.com/" target="_blank" rel="noopener noreferrer">
                京鱼座智能
              </a>
            </li>
          </ul>
        </div>
        <div class="mod_help_cover">
          <h5 class="mod_help_cover_tit">京东自营覆盖区县</h5>
          <div class="mod_help_cover_con">
            <p class="mod_help_cover_info">
              京东已向全国2661个区县提供自营配送服务，支持货到付款、POS机刷卡和售后上门服务。
            </p>
            <p class="mod_help_cover_more">
              <a href="//help.jd.com/user/issue/103-983.html" target="_blank" rel="noopener noreferrer">
                查看详情
                <i class="iconfont">&#xe60d;</i>
              </a>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="mod_copyright">
    <div class="grid_c1 mod_copyright_inner">
      <p
        class="mod_copyright_links"
        clstag="btm|btmnavi_null03"
        poi="btm|btmnavi|null03"
      >
        <a href="//about.jd.com" target="_blank" rel="noopener noreferrer">关于我们</a>
        <span class="mod_copyright_split">|</span>
        <a href="//about.jd.com/contact" target="_blank" rel="noopener noreferrer">联系我们</a>
        <span class="mod_copyright_split">|</span>
        <a href="//help.jd.com/user/custom.html" target="_blank" rel="noopener noreferrer">联系客服</a>
        <span class="mod_copyright_split">|</span>
        <a href="//lai.jd.com" target="_blank" rel="noopener noreferrer">合作招商</a>
        <span class="mod_copyright_split">|</span>
        <a href="//helpcenter.jd.com/venderportal/frist.html" target="_blank" rel="noopener noreferrer">商家帮助</a>
        <span class="mod_copyright_split">|</span>
        <a href="//jzt.jd.com" target="_blank" rel="noopener noreferrer">营销中心</a>
        <span class="mod_copyright_split">|</span>
        <a href="//app.jd.com/" target="_blank" rel="noopener noreferrer">手机京东</a>
        <span class="mod_copyright_split">|</span>
        <a href="//club.jd.com/links.aspx" target="_blank" rel="noopener noreferrer">友情链接</a>
        <span class="mod_copyright_split">|</span>
        <a href="//union.jd.com/index" target="_blank" rel="noopener noreferrer">销售联盟</a>
        <span class="mod_copyright_split">|</span>
        <a href="//pro.jd.com/mall/active/3WA2zN8wkwc9fL9TxAJXHh5Nj79u/frist.html" target="_blank" rel="noopener noreferrer">京东社区</a>
        <span class="mod_copyright_split">|</span>
        <a href="//pro.jd.com/mall/active/3TF25tMdrnURET8Ez1cW9hzfg3Jt/frist.html" target="_blank" rel="noopener noreferrer">风险监测</a>
        <span class="mod_copyright_split">|</span>
        <a href="//about.jd.com/privacy/" target="_blank" rel="noopener noreferrer">隐私政策</a>
        <span class="mod_copyright_split">|</span>
        <a href="//gongyi.jd.com" target="_blank" rel="noopener noreferrer">京东公益</a>
        <span class="mod_copyright_split">|</span>
        <a href="//www.joybuy.com/" target="_blank" rel="noopener noreferrer">English Site</a>
        <span class="mod_copyright_split">|</span>
        <a href="//corporate.jd.com" target="_blank" rel="noopener noreferrer">Media & IR</a>
      </p>


      <div class="mod_copyright_info">
        <div
          class="mod_copyright_cert"
          clstag="btm|btmnavi_null04"
          poi="btm|btmnavi|null04"
        >
          <p>
            <a
              href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11000002000088"
              target="_blank"
              rel="noopener noreferrer"
            >
              京公网安备 11000002000088号
            </a>
            <span class="mod_copyright_split">|</span>
            <a href="http://beian.miit.gov.cn" target="_blank" rel="noopener noreferrer">
              京ICP备11041704号
            </a>
            <span class="mod_copyright_split">|</span>
            <a
              href="//h5.m.jd.com/pc/dev/3T3No18XR8k8rpLGLGhgbJ1StAFq/frist.html"
              target="_blank"
              rel="noopener noreferrer"
            >
              ICP
            </a>
            <span class="mod_copyright_split">|</span>
            <a href="//jdwp.jd.com/544-2927.html" target="_blank" rel="noopener noreferrer">
              互联网药品信息服务资格证编号(京)-经营性-2014-0008
            </a>
            <span class="mod_copyright_split">|</span>
            <span>新出发京零&nbsp;字第大120007号</span>
          </p>
          <p>
            <span>互联网出版许可证编号新出网证(京)字150号</span>
            <span class="mod_copyright_split">|</span>
            <a
              href="//pro.jd.com/mall/active/3bVDLXHdwVmdQksGF8TtS7ocq1NY/frist.html"
              target="_blank"
              rel="noopener noreferrer"
            >
              出版物经营许可证
            </a>
            <span class="mod_copyright_split">|</span>
            <a
              href="//img10.360buyimg.com/ling/jfs/t1/164806/19/5070/567736/6017d6d6Eab06ec9c/d8ca6e029f495447.jpg"
              target="_blank"
              rel="noopener noreferrer"
            >
              网络文化经营许可证京网文[2020]6112-1201号
            </a>
            <span class="mod_copyright_split">|</span>
            <span>违法和不良信息举报电话：4006561155</span>
          </p>
          <p>
            <span class="copyright_txt"></span>
            <span class="mod_copyright_split">|</span>
            <span>消费者维权热线：4006067733</span>
            <span class="mod_copyright_split">|</span>
            <a
              href="//pro.jd.com/mall/active/38PitHBfR7ZopNHRSHnuuWR5AMDL/frist.html"
              target="_blank"
              rel="noopener noreferrer"
              class="mod_copyright_license"
            >
              经营证照
            </a>
            <span class="mod_copyright_split">|</span>
            <span>(京)网械平台备字(2018)第00003号</span>
            <span class="mod_copyright_split">|</span>
            <a
              href="//h5.m.jd.com/babelDiy/Zeus/ARcYnJ8coUdUecn6UQAN6TDaVmH/frist.html"
              target="_blank"
              rel="noopener noreferrer"
              class="mod_business_license"
            >
              营业执照
            </a>
            <span class="mod_copyright_split">|</span>
            <a
              href="//img11.360buyimg.com/imagetools/jfs/t1/148412/19/20641/1513871/6204e24aEd9434d24/b11d1cd7d1d36976.png"
              target="_blank"
              rel="noopener noreferrer"
              class="mod_business_license"
            >
              增值电信业务经营许可证
            </a>
          </p>
        </div>

        <div class="mod_copyright_inter">
          <p>
            <a
              class="mod_copyright_inter_lk"
              href="//www.joybuy.com/?source=1&visitor_from=3"
              target="_blank"
              rel="noopener noreferrer"
              clstag="btm|btmnavi_null0501"
              poi="btm|btmnavi|null0501"
            >
              <i class="mod_copyright_inter_ico mod_copyright_inter_ico_global"></i>
              Global Site
            </a>
            <span class="mod_copyright_split">|</span>
            <a
              class="mod_copyright_inter_lk"
              href="//www.jd.ru/?source=1&visitor_from=3"
              target="_blank"
              rel="noopener noreferrer"
              clstag="btm|btmnavi_null0502"
              poi="btm|btmnavi|null0502"
            >
              <i class="mod_copyright_inter_ico mod_copyright_inter_ico_rissia"></i>
              Сайт России
            </a>
            <span class="mod_copyright_split">|</span>
            <a
              class="mod_copyright_inter_lk"
              href="//www.jd.id/?source=1&visitor_from=3"
              target="_blank"
              rel="noopener noreferrer"
              clstag="btm|btmnavi_null0503"
              poi="btm|btmnavi|null0503"
            >
              <i class="mod_copyright_inter_ico mod_copyright_inter_ico_indonesia"></i>
              Situs Indonesia
            </a>
            <span class="mod_copyright_split">|</span>
            <a
              class="mod_copyright_inter_lk"
              href="//www.joybuy.es/?source=1&visitor_from=3"
              target="_blank"
              rel="noopener noreferrer"
              clstag="btm|btmnavi_null0504"
              poi="btm|btmnavi|null0504"
            >
              <i class="mod_copyright_inter_ico mod_copyright_inter_ico_spain"></i>
              Sitio de España
            </a>
            <span class="mod_copyright_split">|</span>
            <a
              class="mod_copyright_inter_lk"
              href="//www.jd.co.th/?source=1&visitor_from=3"
              target="_blank"
              rel="noopener noreferrer"
              clstag="btm|btmnavi_null0505"
              poi="btm|btmnavi|null0505"
            >
              <i class="mod_copyright_inter_ico mod_copyright_inter_ico_thailand"></i>
              เว็บไซต์ประเทศไทย
            </a>
          </p>
        </div>

        <div
          class="mod_copyright_subsites"
          clstag="btm|btmnavi_null06"
          poi="btm|btmnavi|null06"
        >
          <p>
            <span>京东旗下网站：</span>
            <a href="https://www.jdpay.com/" target="_blank" rel="noopener noreferrer">
              京东钱包
            </a>
            <span class="mod_copyright_split">|</span>
            <a href="http://www.jdcloud.com" target="_blank" rel="noopener noreferrer">
              京东云
            </a>
            <span class="mod_copyright_split">|</span>
            <span>网络内容从业人员违法违规行为举报电话：4006561155-3</span>
          </p>
        </div>
      </div>

      <p
        class="mod_copyright_auth"
        clstag="btm|btmnavi_null07"
        poi="btm|btmnavi|null07"
      >
        <a
          class="mod_copyright_auth_ico mod_copyright_auth_ico_2"
          href="https://ss.knet.cn/verifyseal.dll?sn=2008070300100000031&ampct=df&amppa=294005"
          target="_blank"
          rel="noopener noreferrer"
        >
          可信网站信用评估
        </a>
        <a
          class="mod_copyright_auth_ico mod_copyright_auth_ico_3"
          href="http://www.cyberpolice.cn"
          target="_blank"
          rel="noopener noreferrer"
        >
          网络警察提醒你
        </a>
        <a
          class="mod_copyright_auth_ico mod_copyright_auth_ico_4"
          href="https://search.szfw.org/cert/l/CX20120111001803001836"
          target="_blank"
          rel="noopener noreferrer"
        >
          诚信网站
        </a>
        <a
          class="mod_copyright_auth_ico mod_copyright_auth_ico_5"
          href="http://www.12377.cn/"
          target="_blank"
          rel="noopener noreferrer"
        >
          中国互联网举报中心
        </a>
        <a
          class="mod_copyright_auth_ico mod_copyright_auth_ico_6"
          href="http://www.12377.cn/node_548446.htm"
          target="_blank"
          rel="noopener noreferrer"
        >
          网络举报APP下载
        </a>
        <a
          class="mod_copyright_auth_ico mod_copyright_auth_ico_7"
          href="http://www.shdf.gov.cn/shdf/channels/740.html"
          target="_blank"
          rel="noopener noreferrer"
        >
          扫黄打非网举报专区
        </a>
        <a
          class="mod_copyright_auth_ico mod_copyright_auth_ico_8"
          href="javascript:;"
          target="_self"
          rel="noopener noreferrer"
        >
          适老化无障碍服务
        </a>
        <a
          class="mod_copyright_auth_ico mod_copyright_auth_ico_9"
          href="http://ggfw.cnipa.gov.cn:8010/PatentCMS_Center?fromsite=www.jd.com"
          target="_blank"
          rel="noopener noreferrer"
        >
          国家知识产权公共服务网
        </a>
      </p>
    </div>
  </div>
</div>

<script type="text/javascript">
function footerRender (){
  function getClstagPrefix(){
      var $clstagEles = $('[clstag]');
      $clstagEles.each(function(){
          var fullpoi = $(this).attr('clstag')
          $(this).attr('clstag', pageConfig.clstagPrefix+fullpoi)
      });
  }

  function getCopyrightTxt(){
    var $copyrightEles = $('.copyright_txt');
    $copyrightEles.html("Copyright&nbsp;©&nbsp;2004&nbsp;-&nbsp;"+ new Date().getFullYear() + "&nbsp;&nbsp;京东JD.com&nbsp;版权所有")
  }

  getClstagPrefix()
  getCopyrightTxt()
}

footerRender()
</script>

</body>


<script type="text/javascript" src="//misc.360buyimg.com/mtd/pc/index_2019/1.0.0/static/js/runtime.js"></script>

<script type="text/javascript" src="//misc.360buyimg.com/mtd/pc/index_2019/1.0.0/static/js/index.chunk.js"></script>

<script type="text/javascript">
    window.point.js = new Date().getTime();
</script>
<script defer="defer" async type="text/javascript" src="//static.360buyimg.com/item/assets/oldman/wza1/aria.js?appid=bfeaebea192374ec1f220455f8d5f952"></script>
</html>
': failed to load external entity "<!DOCTYPE html>
<html>

<head>
    <meta charset="utf8" version='1'/>
    <title>京东(JD.COM)-正品低价、品质
>>> 