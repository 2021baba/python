# 读取数据文件
import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts, TitleOpts

f_map = open('C:\\Users\\29174\\Desktop\\Code\\python\\hello\\资料\\资料\\资料\\可视化案例数据\\地图数据\\疫情.txt','r',encoding='utf8')
data = f_map.read()
# 关闭文件
f_map.close()
# 取各省份数据
# 将JSON转换为python字典
data = json.loads(data)        #基础数据字典
# 从字典中取出各省份的数据
province_data = data['areaTree'][0]['children']
# 组装为元组,并将各省数据封装到列表内
data_list = []
for province in province_data:
    province_name = province['name']
    province_confirm = province['total']['confirm']
    data_list.append((province_name, province_confirm))


# 创建地图
map = Map()
# 添加数据
map.add('各省份确诊人数', data_list,'china')
#设置全局配置,定制分段的视觉映射
map.set_global_opts(
    title_opts=TitleOpts(title='各省份确诊人数'),
    visualmap_opts=VisualMapOpts(           #显示颜色
            is_show=True,                   #是否显示
            is_piecewise=True,              #是否手动设置颜色范围
            pieces=[                        #设置颜色范围
                {'min':1,'max':99,'label':'1-99人','color':'#CCFFFF'},
                {'min':100,'max':999,'label':'100-999人','color':'#FFFF99'},
                {'min':1000,'max':4999,'label':'1000-4999人','color':'#FF9966'},
                {'min':5000,'max':9999,'label':'5000-9999人','color':'#FF6666'},
                {'min':10000,'max':99999,'label':'10000-99999人','color':'#CC3333'},
                {'min':100000,'max':999999,'label':'100000-999999人','color':'#990033'},
            ]
    )
)
# 生成地图
map.render('全国疫情地图.html')
