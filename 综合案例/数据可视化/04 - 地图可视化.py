from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 准备地图对象
map = Map()
# 准备数据
data=[
    ('北京市',19),
    ('上海市',9),
    ('江苏省',29),
    ('湖南省',39),
    ('广东省',199),
]
#添加数据
map.add('测试地图',data,'china')    #(地图名,数据,地图类型)

#全局选项设置
map.set_global_opts(
    visualmap_opts=VisualMapOpts(#显示颜色
        is_show=True,#是否显示
        is_piecewise=True,#是否手动设置颜色范围
        pieces=[#设置颜色范围
            {'min':1,'max':10,'label':'1-10','color':'pink'},
            {'min':11,'max':20,'label':'11-20','color':'blue'},
            {'min':21,'max':30,'label':'21-30','color':'yellow'},
            {'min':31,'max':9999,'label':'31-9999','color':'red'},
        ]
    ),

)
#绘图
map.render('map.html')
