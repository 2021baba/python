# 导包
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# 创建一个折线图对象
line = Line()

# 给折线图对象添加x轴坐标
line.add_xaxis(["中国","美国","日本"])

# 给折线图对象添加y轴坐标
line.add_yaxis('GDP',[30,20,10])

# set_global_opts方法配置全局配置
line.set_global_opts(
    title_opts=TitleOpts(True,"GDP展示",pos_left="center",pos_bottom="1%"),#标题配置项
    legend_opts=LegendOpts(is_show=True),                                             #图例配置项
    toolbox_opts=ToolboxOpts(is_show=True),                                           #工具箱配置项
    visualmap_opts=VisualMapOpts(is_show=True),                                       #视觉映射配置项
    #全局配置项很多,可以在pyecharts.org官网中查询
)


# 通过render方法,将代码生成为图像
line.render()