from pyecharts.charts import Bar,Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType


bar1 = Bar()
# 添加x轴数据
bar1.add_xaxis(['中国','美国','日本'])
# 添加y轴数据
bar1.add_yaxis('GDP',[30,20,10],label_opts=LabelOpts(position='right'))
# x,y轴反转
bar1.reversal_axis()

bar2 = Bar()
# 添加x轴数据
bar2.add_xaxis(['中国','美国','日本'])
# 添加y轴数据
bar2.add_yaxis('GDP',[50,40,20],label_opts=LabelOpts(position='right'))
# x,y轴反转
bar2.reversal_axis()

bar3 = Bar()
# 添加x轴数据
bar3.add_xaxis(['中国','美国','日本'])
# 添加y轴数据
bar3.add_yaxis('GDP',[90,60,40],label_opts=LabelOpts(position='right'))
# x,y轴反转
bar3.reversal_axis()

# 创建时间线对象
timeline = Timeline({
    'theme': ThemeType.LIGHT}# 主题设置
 )
# 在时间线内添加柱状图对象
timeline.add(bar1,'点1')
timeline.add(bar2,'点2')
timeline.add(bar3,'点3')
# 自动播放设置
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True

)


#
timeline.render('基础时间线柱状图.html')