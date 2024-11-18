import plotly.graph_objects as go

import pandas as pd

# 读取在线的csv文件

z_data = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv",
    index_col=0,
)  # index_col参数表示将第一列的数据当做索引
z_data.head()


fig = go.Figure(data=[go.Surface(z=z_data.values)])

fig.update_layout(
    title="3D Surface图形绘制",  # 标题
    autosize=False,  # 尺度自动缩放
    width=700,  # 长宽
    height=600,
    margin=dict(l=65, r=50, b=65, t=90),  # 4个位置的距离
)

fig.show()
