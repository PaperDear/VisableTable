import pyecharts.options as opts
from pyecharts.charts import Line
import pandas as pd

df=pd.read_excel("./datas/酸通风柜QDRparticle问题排查.xlsx",sheet_name="空Run一次后颗粒数")

# 取得时间戳数组
y_label = df['日期'].dt.strftime('%m月%d日').tolist()

data_arrays = {}
# 去掉表头后提取第三列开始的所有数据
for i, col in enumerate(df.columns[2:], start=2):
    data_arrays[col] = df.iloc[:, i].values.tolist()

line=Line()

# 添加 X 轴数据
line.add_xaxis(xaxis_data=y_label)

# 循环添加所有 Y 轴数据
for col_name, y_data in data_arrays.items():
    line.add_yaxis(
        series_name=col_name,  # 使用列名作为系列名称
        y_axis=y_data,
        # markpoint_opts=opts.MarkPointOpts(
        #     data=[
        #         opts.MarkPointItem(type_="max", name="最大值"),
        #         opts.MarkPointItem(type_="min", name="最小值"),
        #     ]
        # ),
        # markline_opts=opts.MarkLineOpts(
        #     data=[opts.MarkLineItem(type_="average", name="平均值")]
        # )
    )

# 设置全局选项
line.set_global_opts(
    title_opts=opts.TitleOpts(title="空Run一次后颗粒数图"),
    tooltip_opts=opts.TooltipOpts(trigger="axis"),
    toolbox_opts=opts.ToolboxOpts(is_show=True),
    xaxis_opts=opts.AxisOpts(name="日期"),
    yaxis_opts=opts.AxisOpts(name="颗粒数(ea)")
)

# 渲染图表
line.render("./report/particle_trend.html")