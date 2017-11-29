# -*- coding:utf-8 -*-
# time:2017/11/22
import re
from html.parser import HTMLParser
a="""<!doctype html>



<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<title>乘小火车在海上穿梭、近距离观察野生大象，这里简直处处是惊喜</title>
<meta name="apple-itunes-app" content="app-id=639087967, app-argument=zhihudaily://story/9657627">
<meta name="viewport" content="user-scalable=no, width=device-width">
<link rel="stylesheet" href="/css/share.css?v=5956a">


<script src="http://static.daily.zhihu.com/js/modernizr-2.6.2.min.js"></script>
<link rel="canonical" href="http://daily.zhihu.com/story/9657627"/>
<base target="_blank">
<script type="text/javascript">
if (localStorage && localStorage.getItem('hideDownloadBanner') !== 'true') {
document.documentElement.className += ' show-download-banner';
}
</script>
<style type="text/css">
[data-za-module="AdItem"] {display:none!important;display:none}</style>
</head>
<body>

<div class="global-header">
<div class="main-wrap">
<div class="download">
<a href="https://itunes.apple.com/cn/app/id639087967?mt=8" class="button" data-device="ios"><i class="sprite-ico-Button_iPhone2x"></i> <span>iPhone</span></a>
<a href="/download/android" class="button" data-device="android-local"><i class="sprite-ico-Button_Android2x"></i> <span>Android</span></a>
</div>
<a href="/" target="_self" title="知乎日报"><i class="web-logo"></i></a>
</div>
</div>
<div class="header-for-mobile">
<a href="/download" class="header-for-mobile-download-link">
<span class="header-for-mobile-btn">立即下载</span>
<img class="header-for-mobile-logo-img" src="http://static.daily.zhihu.com/img/app-logo.png"/>
<span class="header-for-mobile-title">知乎日报</span>
<span class="header-for-mobile-meta">每日提供高质量新闻资讯</span>
</a>
</div>
<div class="main-wrap content-wrap">
<div class="headline">

<div class="img-wrap">
<h1 class="headline-title">乘小火车在海上穿梭、近距离观察野生大象，这里简直处处是惊喜</h1>


<span class="img-source">图片：Cathy Lv / 知乎</span>


<img src="https://pic1.zhimg.com/v2-a5df3583aca661beda6d46411463c94c.jpg" alt="">
<div class="img-mask"></div>
</div>


</div>

<div class="content-inner">



<div class="question">
<h2 class="question-title">坐军车闯进野生大象群不到 3 米的丛林，这里是斯里兰卡</h2>
<div class="answer">

<div class="meta">
<img class="avatar" src="http://pic4.zhimg.com/v2-1e2595cfa141c301dc25833bbdcfbc7b_is.jpg">
<span class="author">Cathy Lv，</span><span class="bio">低调搬砖，高调生活</span>
</div>

<div class="content">
<p>说到斯里兰卡肯定首选要去挂海上小火车，感受现实版的《千与千寻》，我也不例外，不过我绝对想不到不仅挂了小火车，还吃着大螃蟹看了一整晚小火车在海上穿梭；也想不到还有意外机会坐军车，闯进野生大象群不到 3 米的丛林，看到令人心酸的一幕。</p>
<p><strong># 先说说斯里兰卡的人</strong></p>
<p>由于斯里兰卡是个佛教国家，当然北部也有一部分印度教，以及分散的伊斯兰教和基督教，不过总体来说大都非常和善，所以才被称为“微笑的国家”。遇到的小摊贩、司机、商店老板、学生、售票员、酒店员工等总是笑脸相迎，问候 AYUBOWAN（斯里兰卡人见面语，祝您长寿的意思），舒服得像跟自己的老朋友在打招呼，我是很幸运一次也没有碰到所谓的坑蒙拐骗。</p>
<p>比如在加勒古堡灯塔下的海滩上，遇到一家带着爱犬在海中嬉戏的当地家庭，我明目张胆的加入，拍了很多照片，他们一直很开心地逗着爱犬配合我玩了很久，我也并没有被索要任何费用，反正我也没有带一分钱在身上。</p>
<p><img class="content-image" src="http://pic3.zhimg.com/v2-017c78b290912624a5d5d50bc434c2b2_b.jpg" alt=""></p>
<p><img class="content-image" src="http://pic4.zhimg.com/v2-c3a00ce46308059375fcefa36f8b0a97_b.jpg" alt=""></p>
<p>第一次到斯里兰卡的话，大部分人会选择西海岸 - 中部 - 南岸 - 西南岸环岛游，但各个城市间交通没那么方便（如果想感受当地像小火车一样不关门不关窗还一路飙车的超便宜巴士，请忽略这条），加上安全问题，做好攻略、找一个靠谱的向导、包车环岛等等方式都可以帮你规避一些不必要的麻烦。</p>
<p>最幸运的是有一个十分会“宠溺”的网红向导带着玩，会让你颠覆对整个斯里拉卡的印象。我们的向导 Hiran 是位自由的 national guide（斯向导最高级），可以看心情带不带你玩，有资格带游客去斯里兰卡任何一个城市和山沟。他是 Instagram 上的小网红，拍的一手大片和 Video；曾在中国留学，中、英、西、法、德、俄语水平一流，跟僧伽罗语无缝切换，两只大花臂、一手 8 克拉祖传蓝宝石、一秒钟让你笑的幽默能力，让你绝不相信还有这样的向导。</p>
<p><img class="content-image" src="http://pic1.zhimg.com/v2-5fd8658278040675d346885ab0f6e210_b.jpg" alt=""></p>
<p>有了这样的“老朋友”，一路总是突然的惊喜（或惊吓），比如车正行驶在小路上，忽然喊停冲下车，带着跑到火车道上拍大片；看到野生的大蜥蜴或盘踞在树上的蛇就拉我们去看；正坐在红树林的船上，把船夫赶到一旁，让我来开船 ……在东部海岸被我们“承包”的海边酒吧，亲自调一口闷的火焰咖啡酒给我们喝……来感受一张 Hiran 的经典动作，想知道他的 Instagram，请留言，至于他接不接受带你玩，这是要看颜值的╮(￣▽￣)╭。</p>
<p><img class="content-image" src="http://pic1.zhimg.com/v2-aa29a4756305822a31c5fd327dcde8d0_b.jpg" alt=""></p>
<p><strong># 斯里兰卡的动物</strong></p>
<p>除了当地人的笑脸，在斯里兰卡最大的享受就是处处可见的动物，无论是在被热捧的国家公园近距离接触野生动物，还是在景点寺庙、大街上邂逅小动物。这与当地人的信仰有很大关系，据说非常虔诚的佛教信徒从不杀生，连蚊子、老鼠都不会拍死，我也就理解了为什么斯里兰卡的动物如此悠哉横行。</p>
<p>刚落地科伦坡的时候正好赶上日出，最先映入眼帘是遍地或飞或停，在车上、地面上、任何人身边跳来跳去的乌鸦……作为当地代表着吉祥的乌鸦，当地人从来不会有人伸手去驱赶，以至于后来跑遍整个斯里兰卡我已经习以为常他们的四处存在。</p>
<p><img class="content-image" src="http://pic1.zhimg.com/v2-975d08ad922ccbcd4b96903ce9c04668_b.jpg" alt=""></p>
<p>还有无处不在的悠闲晒太阳的土狗，时不时会冲出来过马路的野生大象，国家公园里的拼人品才能见到的豹子，馋嘴爱问你要吃的水鹿，寺庙里比人还多的猴子家族……人与动物的和谐程度，真不是动物园里的表演。</p>
<p><img class="content-image" src="http://pic4.zhimg.com/v2-21dca1efa8ae6def935dfefeca6e9aa7_b.jpg" alt=""></p>
<p>最惊险的的还是刚到斯里兰卡的第二天，车子正驶向东部 passikudah 海滩的路上，刚到 minneriya national park 附近的公路上，我们的车忽然就拐进了左边丛林中！还在迷糊中的我，还没反应过来就被喊下车，说是要看野生大象，不过距离太远了，什么也看不清楚。</p>
<p>这时候从前面开过来一辆军车，只见向导 Hiran 跟他搭讪了几句，副驾上就下来一个人，然后腾出一个位置让我们五个人上去，说带我们去大象身边！（军车的照片是不能放的，大家凭想象吧，1 米八的大长腿一脚踩不上去的那种）</p>
<p><img class="content-image" src="http://pic4.zhimg.com/v2-7104467b3b3985f99acd68e13987a3c7_b.jpg" alt=""></p>
<p>接下来铺开在我们眼前的，除了混在丛林里带着刺激味道的巨大垃圾场，还有 20 多只正在垃圾场里吃着“早餐”的野生大象，我们径直开到了它们身边 3 米远的地方停了下来，他们好像对我们的闯入没有太多感觉，但，我们几个是极其惊恐的盯着眼前的这些庞然大物，紧张到相机都拿不稳，要知道成年野生大象可以轻而易举把我们连人带车掀翻、踩扁。</p>
<p><img class="content-image" src="http://pic1.zhimg.com/v2-aeff0005beb0ef4ac77299ee9bc13f5c_b.jpg" alt=""></p>
<p>不过后来才知道我们坐的这辆军车绝对安全，因为他们经常投食给这些野生象们，它们早已视这辆绿色的车为朋友。野生大象一天要走 20 公里寻觅 30kg 以上的食物，但是在这个隐藏在森林里的巨大垃圾场，他们不用走路就可以轻松吃饱，不知道这对它们来说是喜是悲。</p>
<p><img class="content-image" src="http://pic4.zhimg.com/v2-a3fe20253a62c5465d8a6220f01eadbf_b.jpg" alt=""></p>
<p><strong># 斯里兰卡的信仰和寺庙</strong></p>
<p>佛教对于当地的深远影响不仅体现在人与动物如此和谐的关系上，更体现在他们历代的建筑中以及文化中。作为世界上最古老的佛教文明之一，斯里兰卡拥有 8 处联合国世界文化遗址。</p>
<p>目前尚存的古城建筑和遗址大部分都在中北部文化三角处，最古老的城市阿努拉德普勒（Anuradhapura）、僧伽罗王朝的第二任首都波隆纳鲁沃（Polonnaruwa）、丹布勒（Dambulla）这几个古时王朝所在地。其中名气最大的当属丹布勒东北方向的小村 Sigiriya 的狮子岩（斯里兰卡的地标之一），巨大的红褐色岩石、空中宫殿、仕女图壁画以及当年水自下而上流等建筑奇迹等，被誉为世界第八大奇迹，也是联合国教科文组织保护的世界级珍贵遗产之一。</p>
<p><img class="content-image" src="http://pic1.zhimg.com/v2-71301870dbd0f1bcfb28c2fa108df194_b.jpg" alt=""></p>
<p>建议先看完博物馆了解清楚全盘历史和惊人的建筑结构再去爬山，会更加震撼。我们冒着雨爬到山顶，四周无比开阔的气势随着风和雨瞬间袭来，那一刻就能明白什么是唯我独尊。附一张下雨时的山顶照（天气不好拍的太丑）。</p>
<p><img class="content-image" src="http://pic1.zhimg.com/v2-afceef3f45f7374fc8c25eb061f6c660_b.jpg" alt=""></p>
<p>除了文化三角，中部的康提还有一个著名的全世界佛教信仰者的朝圣地，就是始建于 15 世界的佛牙寺，这里供奉着斯里兰卡的国宝——佛祖释迦牟尼的佛牙舍利。如果恰好在 7、8 月份来斯里兰卡，千万不能错过在康提举行的全球最盛大的佛教节日——佛牙节盛典，届时数十只盛装打扮的大象会背着安放着舍利的巨大华盖游行，游行时间长达 10 天左右，非常隆重和华丽，可惜我这次是完美错过了。</p>
<p><img class="content-image" src="http://pic1.zhimg.com/v2-4d51af66e2ffc904a2ced6aa814f2dbc_b.jpg" alt=""></p>
<p>不过平时来的话，每天早上 6 点、上午 10 点、晚上 6 点也能进入朝拜，而且最好的时间是在下午 6 点，买票进入佛牙寺后，可以在一楼看完表演再携带睡莲或者钱排队到二楼瞻仰舍利子，虽然一般也看不到舍利，但这是离舍利子最近的地方，在这里看到的都是信徒面向舍利子最虔诚的样子。</p>
<p><img class="content-image" src="http://pic2.zhimg.com/v2-d3a1d0e873b7f433d3a281906ba41521_b.jpg" alt=""></p>
<p><strong># 斯里兰卡的风景</strong></p>
<p>斯里兰卡的风景虽然算不上惊艳和独特，却因为变化多端的面孔总让人抱有期待，从满眼绿色的山区、绵延的热带丛林、再到白色的沙滩，从佛教、印度教寺庙到荷兰、葡萄牙和英国殖民时期的文化遗迹……斯里兰卡就像一个调皮的魔术师，下一秒总希望从他的帽子里再变出点什么好玩的出来。</p>
<p><strong>想要海滩：</strong></p>
<p>斯里兰卡的海滩处处给人惊喜，冲浪、潜水、水上游戏、观鲸、度假……一个都不少。成熟的西海岸和南岸，由于有两条中国资助的高速公路大大提高了抵达各个城市的速度，1、2 小时就可以从西南海滩到南部加勒、美瑞莎等地。度假村、玩乐设施齐全，还有著名的海上小火车，最接近大海的一段就在科伦坡——Pinwatta 这一段，可以避开高峰期去体验一下。</p>
<figure><img class="content-image" src="http://pic2.zhimg.com/v2-f6696fa52899c3f72faa31c51e88fb71_b.jpg" alt=""><figcaption>车票请倒过来看= =</figcaption></figure><p>如果想要小众的海滩，那去一定东海岸，比较受追捧的是亭可马里。想要再小众一点，就去最东端的卡尔库达（Kalkudah）的 passikudah 海滩。卡尔库达作为东部第二大城市，优质的海滩资源是新开发出来的“世外桃源”，目前尚未被游客发掘，当地人度假居多。</p>
<figure><img class="content-image" src="http://pic1.zhimg.com/v2-08b1a8a7ce26580191044f67dc090250_b.jpg" alt=""><figcaption>Amaya Beach by 傍晚的无人机</figcaption></figure><p>正值十一之后的淡季，整个酒店性价比极高，而且只有我们几个人，还有一对每天在海边泳池旁静静看书的欧洲小情侣。没有太多人也就没有方便的自助餐，你只能慢慢的享用酒店大厨每隔半个小时送上来的一道餐，一餐吃一整晚，刚好放慢节奏享受美食美酒和无敌海景，还有和身边朋友相处的时间。 推开阳台的门就走到海滩散步，夜晚在沙滩散步，非常之安静。</p>
<p><img class="content-image" src="http://pic2.zhimg.com/v2-4726af88308046f649890e07896bf911_b.jpg" alt=""></p>
<p><strong>想要茶园：</strong></p>
<p>中部高山茶园平均海拔 1000 多米，满眼绿色蜿蜒起伏，很养眼，温度也稍低，在海滩穿的短袖现在要换成外套了，在这里你会看到著名的斯里兰卡红茶茶园，还可以坐茶园小火车，可惜我没去，只有海上小火车对我有吸引力。</p>
<p>如果不是单身狗还可以去逛逛亚洲最大的植物园，曾经康提国王的御花园——皇家植物园（Peradeniya Royal Botanical Garden），周恩来还曾在这里种过 1 棵友谊之树。园内 4000 多种植物其中不乏很多珍稀品种，更是约会、拍婚纱照的好去处，参天古树下经常坐着一对对卿卿我我的年轻人（所以说单身狗请慎行）。</p>
<figure><img class="content-image" src="http://pic2.zhimg.com/v2-41d239d8a44eb9c43369f9f4e423125d_b.jpg" alt=""><figcaption>皇家植物园</figcaption></figure><p><strong>想要自然风景：</strong></p>
<p>斯里兰卡有着丰富的绿色资源，比如倍受追捧的国家公园，到世界自然遗产的霍顿平原（Hortons Plains National Park）徒步看日出，走到“世界尽头”；或者去以金钱豹等众多的珍稀野生动物而闻名雅拉公园（Yala Natnional Park）近距离接触野生动物；再或者专为这个拥有 600+ 只大象的所在地明内里耶国家公园（Minneriya National Park）去看一次野生大象。</p>
<p><img class="content-image" src="http://pic1.zhimg.com/v2-543b84da721add9e5a9fb7c9d2f35c44_b.jpg" alt=""></p>
<p>斯里兰卡各地都处处有惊喜，即使并没有专程计划去一趟国家公园，每每从公路旁路过，也能轻松看到湖边或者参天古树下各种野生动物们的身影，忍不住停车驻足远远观望。</p>
<p><strong>想要古堡：</strong></p>
<p>位于斯里兰卡西南海岸的加勒是大航海时代从欧洲前往远东的重要枢纽之一。由 16 世界葡萄牙人建造的加勒古堡已经成为加勒的标志，在历经几个世纪的风雨以及 2004 年印度洋海啸后，依然牢固完好地保存下来，最南端的灯塔也是在那次海啸中幸存的神奇建筑。</p>
<p><img class="content-image" src="http://pic3.zhimg.com/v2-20f8dca82f265439f43f729396da9f56_b.jpg" alt=""></p>
<p>作为世界遗产的加勒古城，是至今东南亚和南亚地区保存最为完整的古代城堡，它是欧洲人在南亚及东南地区建筑防卫要塞的典型代表，一步一景，甚至一墙一门都能看到欧洲风格。而且这并不是一个“死”的观光地，民房、商铺、学校、教堂、警察局、法院等一系列生活设施应有尽有，最好是在淡季来，不仅会错开人山人海，而且还能更多参与到当地人的生活中。</p>
<p><img class="content-image" src="http://pic2.zhimg.com/v2-26828126405309e9a1032b3b6ba603cd_b.jpg" alt=""></p>
<p><strong>航班 / 酒店以及实用信息</strong></p>
<p><strong>#关于季节：</strong></p>
<blockquote><strong>淡季：</strong>5 - 8 月，雅拉季风来袭，降雨较多，西南海岸和中部山区的淡季；但是却是东海岸和北部的好季节，吃喝玩乐都非常便宜（7、8 月份的佛牙节前后属高峰期除外）。</blockquote>
<p>9 - 11 月，天气较好，雨水不多，物价一般，出行的好季节。</p>
<blockquote><strong>旺季：</strong>12 月 - 次年 4 月，干季，西南海滩的旺季，尤其是圣诞节前后，物价均较高。</blockquote>
<p><strong>#关于签证：</strong></p>
<p>非常简单的电子签，我就不啰嗦了，万能的淘宝帮你搞定一切。</p>
<p><strong>#关于航班：</strong></p>
<p>北上广或者香港出发都有直航（5 - 8 个小时），如果想要舒服一点斯里兰卡航空是首选，以广州和香港为例，5 个半小时左右直达，机票提前购买往返通常不到 3 千就搞定，还包含 30KG 免费行李托运和丰盛餐食。我们这次凌晨 2 点从香港出发的航班，虽然时段不太理想，但是全程餐食丰盛，又舒服睡一觉就到科伦坡了，下飞机在机场买买电话卡、兑换卢比就直接出发去玩了，上班狗的高效完美选择。</p>
<figure><img class="content-image" src="http://pic4.zhimg.com/v2-fcc46ffe4013af61bb3cb418ab2971b3_b.jpg" alt=""><figcaption>斯里兰卡航空</figcaption></figure><p>如果想买廉价机票，多关注各航司活动和促销，亚航提前预订往返 2 千左右，不过缺点也是没有行李托运和餐食，需要中转吉隆坡。至于其他航空，太贵、飞行时间太长已经不在考虑之内了。</p>
<p><strong>#关于酒店：</strong></p>
<blockquote><strong>海滩酒店</strong></blockquote>
<p>斯里兰卡做为一个海岛国家，海滩酒店数不数胜，如果喜欢设施成熟、热闹一点的海滩，可以选择西南或者南部海滩，淡季的时候性价比非常高，不过人多就意味着找个靠谱的酒店极其重要。我们这次在西南海滩特意住了两天斯里兰卡最大的全包度假村 RIU，整个酒店 500 个房间，面朝大海，全世界的美食都搬来给你免费吃，酒吧的酒随便喝，海边无边泳池随你泡，还有免费 massage，每晚还有最地道的表演，跳的还是查尔斯王子最爱的当地传统舞。重点是淡季的价格非常美丽，100 美金起。</p>
<figure><img class="content-image" src="http://pic1.zhimg.com/v2-c51c07b366909dfbbe4db7faf8f64c90_b.jpg" alt=""><figcaption>RIU</figcaption></figure><p>安静一点的海滩，往东部走，虽然景色比南部海滩略为逊色，但以它独有的静美又俘获度假人的心，随便找一家评分高的正规酒店或者度假村都没错。我们找了一家位于 passikudah 海滩的 Amaya Beach 酒店，私人海滩、泳池、酒吧、台球，早上在房间里就能看日出从印度洋升起，黄昏沿着海岸线散步，10 月东海岸的风特别温柔。</p>
<figure><img class="content-image" src="http://pic2.zhimg.com/v2-9e96928eae55a995489cb9a66ea98969_b.jpg" alt=""><figcaption>Amaya Beach</figcaption></figure><blockquote><strong>山景酒店</strong></blockquote>
<p>除了海滩酒店，有机会一定要住一次山里或者茶园附近的酒店，满眼溢出的绿色恨不能把近视都治好了。即使住不起伊丽莎白女王和查尔斯王子曾经住过的 Heritance Tea Factory，倒是可以吃个超便宜的正宗英式下午茶。</p>
<p>我们选了一家山景酒店，是在 Jetwing（个人很喜欢的一家整个斯里兰卡名声非常好的一个旅游集团，集斯里兰卡风情与独特个性于一身，酒店遍布斯里兰卡各地，街上跑满了 Jetwing 旅游大巴）上预订的 Jetwing 位于狮子岩附近的酒店，穿越蜿蜒的森林最终到达一个空气异常清新的森林酒店，所有房间阳台大到可以开趴了，远山、森林和湖泊就铺展在你的眼皮下，目及之处绿色溢出、蔓延、凝结，疲惫一扫而光。</p>
<figure><img class="content-image" src="http://pic1.zhimg.com/v2-e45a7c3647756e0c5ac1637e9485937c_b.jpg" alt=""><figcaption>Jetwing by 无人机</figcaption></figure><figure><img class="content-image" src="http://pic3.zhimg.com/v2-13c6b2b484bcd90a6ea024139c0b8fb2_b.jpg" alt=""><figcaption>Jetwing 酒店阳台远眺</figcaption></figure><blockquote><strong>经济酒店和民宿</strong></blockquote>
<p>虽说斯里兰卡比印度安全了非常多，但毕竟整个国家贫富差距较大，也会出现很多人为了赚钱坑蒙拐骗，为了安全，还是尽量全方面考察酒店的位置、评分、评价。</p>
<p><strong>#关于语言：</strong></p>
<p>非常令人头疼的英语发音和火箭语速的僧伽罗语，不知道你们是怎么交流的，我每天都在怀疑自己的耳朵，只有跟英文发音好的当地人交流才觉得自己不是个白痴。</p>
<p><strong>#关于交通：</strong></p>
<p>看完网上所有交通攻略，只觉得包车最省心，也不见得贵多少，重点是安全。如果想来得更豪华点，到当地声名远扬的 Jetwing 旅游公司包个车，还能顺带看看目的地有没有合心意的酒店一同打包。</p>

<div class="view-more"><a target="_self" href="http://zhuanlan.zhihu.com/p/31073951">查看知乎原文</a></div>

</div>
</div>
</div>



<div class="question">
<div class="answer">
<div class="content">
<p>客官，这篇文章有意思吗？</p>
<p class="p2"><span class="s1"><a href="http://daily.zhihu.com/download?utm_source=article_suffix&amp;utm_campaign=tuijian&amp;utm_medium=daily_share">好玩！下载<span class="s2">&nbsp;App&nbsp;</span>接着看<span class="s2">&nbsp;</span>(<span class="s3">๑</span><span class="s2">&bull;</span><span class="s4">ㅂ</span><span class="s2">&bull;</span>)<span class="s2">&nbsp;</span><span class="s5">✧</span></a></span></p>
<p class="p3"><span class="s6"><a href="http://daily.zhihu.com/story/9116372?utm_source=other_article&amp;utm_campaign=tuijian&amp;utm_medium=daily_share">再逛逛吧<span class="s2">&nbsp;</span><span class="s7">ˊ</span><span class="s2">_&gt;</span><span class="s7">ˋ</span></a></span><span class="s8">&nbsp;&nbsp;</span></p>
</div>
</div>
</div>

</div>
<div class="qr">
<h2 class="heading">扫描二维码下载知乎日报</h2>
<span class="subheading">支持 iOS 和 Android</span>
<div class="qr-wrap">
<img src="http://static.daily.zhihu.com/img/qr1.png" alt="二维码下载知乎日报" width="148" height="148">
</div>
</div>
</div>

<div class="bottom-wrap">
<div class="bottom-recommend">
<span class="bottom-recommend-title">阅读更多</span>
<a class="recommend-link" href="http://daily.zhihu.com/story/9657690" data-story="9657690">

<span style="background-image:url(https://pic3.zhimg.com/v2-a17ccb27f4d43cdd38ac1024f1ebb996.jpg)" class="link-image"></span>

亲爱的，结婚前你能在房产证上加我的名字吗？
</a>
<a class="bottom-recommend-download-link" href="/download">
下载 「知乎日报」 客户端查看更多
</a>
</div>
</div>

<div class="footer">
<a href="http://www.zhihu.com/">知乎网</a> &middot; &copy; 2017 知乎
</div>
<script src="http://static.daily.zhihu.com/js/jquery.1.9.1.js"></script>
<script src="/js/share.js?v=b8b67"></script>

</body>
</html>"""
def prossing(str):
    htmlParser = HTMLParser()
    pa=re.compile(r'<p>(.*?)</p>',re.S)
    items=re.findall(pa,str)
    result = []
    if items !='':
        for content in items:
            tag=re.search(r'<.*?>',content,re.S)            #把含有<>归类处理
            http=re.search(r'.*?html.*?',content,re.S)      #把含有html归类处理
            html_tag=re.search(r'&',content,re.S)           #？？？不知道干啥子的
            #print(content)
            if http:
                continue
            #if html_tag:
            #    content = htmlParser.unescape(content)
            elif tag:
                pa=re.compile(r'(.*?)<.*?>(.*?)<.*?>(.*?)')
                items=re.findall(pa,content)
                #print(items)
                content_tag=''
                if len(items) >0:
                    for item in items:
                        if len(item)>0:
                            for items_s in item:
                                content_tag=content_tag+items_s
                        else:
                            content_tag=content_tag+items_s     #???
                    content_tag=re.sub('<.*?>','',content_tag)
                    result.append(content_tag)
                else:
                    continue
            else:
                result.append(content)
    return result
for i in (prossing(a)):
    print(i)
































