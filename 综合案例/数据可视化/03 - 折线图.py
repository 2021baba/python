# 处理数据
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts,LabelOpts

f_US = open('C:\\Users\\29174\\Desktop\\Code\\python\\hello\\资料\\资料\\资料\\可视化案例数据\\折线图数据\\美国.txt','r',encoding='utf-8')
data_US = f_US.read()
f_ID = open('C:\\Users\\29174\\Desktop\\Code\\python\\hello\\资料\\资料\\资料\\可视化案例数据\\折线图数据\\印度.txt','r',encoding='utf-8')
data_ID = f_ID.read()
f_JP = open('C:\\Users\\29174\\Desktop\\Code\\python\\hello\\资料\\资料\\资料\\可视化案例数据\\折线图数据\\日本.txt','r',encoding='utf-8')
data_JP = f_JP.read()
# 去除不符合JSON规范的开头
data_US = data_US.replace('jsonp_1629344292311_69436(','')
data_ID = data_ID.replace('jsonp_1629350745930_63180(','')
data_JP = data_JP.replace('jsonp_1629350871167_29498(','')
# 去除不符合JSON规范的结尾
data_US = data_US[:-2]
data_ID = data_ID[:-2]
data_JP = data_JP[:-2]

# JSON转Python字典
dict_US = json.loads(data_US)
dict_ID = json.loads(data_ID)
dict_JP = json.loads(data_JP)

# 获取trend key
trend_US = dict_US['data'][0]['trend']
trend_ID = dict_ID['data'][0]['trend']
trend_JP = dict_JP['data'][0]['trend']

# 获取日期数据,用于x轴(取2020年,到314下标结束)
x_data_US = trend_US['updateDate'][:314]
x_data_ID = trend_ID['updateDate'][:314]
x_data_JP = trend_JP['updateDate'][:314]

# 获取确诊数据,用于y轴(取2020年,到314下标结束)
y_data_US = trend_US['list'][0]['data'][:314]
y_data_ID = trend_ID['list'][0]['data'][:314]
y_data_JP = trend_JP['list'][0]['data'][:314]

# 生成图表
line = Line()
line.add_xaxis(x_data_US)  #x轴为公用的,使用一个国家的数据即可
line.add_yaxis('美国确诊人数', y_data_US,label_opts=LabelOpts(is_show=False))  #美国y轴数据
line.add_yaxis('印度确诊人数', y_data_ID,label_opts=LabelOpts(is_show=False))  #印度y轴数据
line.add_yaxis('日本确诊人数', y_data_JP,label_opts=LabelOpts(is_show=False))  #日本y轴数据


# set_global_opts方法配置全局配置
line.set_global_opts(
    title_opts=TitleOpts(True,"2020年疫情确诊统计",pos_left="center",pos_bottom="1%"),#标题配置项
    legend_opts=LegendOpts(is_show=True),                                             #图例配置项
    toolbox_opts=ToolboxOpts(is_show=True),                                           #工具箱配置项
    visualmap_opts=VisualMapOpts(is_show=True),                                       #视觉映射配置项

    #全局配置项很多,可以在pyecharts.org官网中查询
)

#调用render方法,生成图表
line.render()
#关闭文件对象
f_US.close()
f_JP.close()
f_ID.close()


