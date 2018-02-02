#斗鱼数据按日合并
import pandas as pd
data = pd.DataFrame()
cate = pd.DataFrame()
zhubo = pd.DataFrame()
data1 = pd.DataFrame()
for d in range(3,16):
    print('开始'+str(d)+'日数据整合')
    df = pd.DataFrame()
    filename = ''
    if d<10:
        filename = '/home/miracle/文档/douyu/100'+str(d)
    elif d>=10:
        filename = '/home/miracle/文档/douyu/10'+str(d)
    print('开始'+str(d)+'日数据合并')
    for h in range(24):
        filename1 = filename
        if h<10:
            filename1 = filename1+'0'+str(h)
        elif h>=10:
            filename1 = filename1+str(h)
        try:
            tmpA = pd.read_json(filename1+'Adouyudata.json')
            tmpA['selecttime'] = filename1[-6:]+' 00'
            tmpB = pd.read_json(filename1+'Bdouyudata.json')
            tmpB['selecttime'] = filename1[-6:]+' 30'
        except ValueError:
            print(filename1+'停电数据缺失')
            pass
        df = pd.concat([df,tmpA,tmpB])
    df['hour'] = df['selecttime'].str[4:6]
    df['hour'] = df['hour'].astype('int')
    df['时段'] = None
    df['时段'][(df['hour'] < 8) & (df['hour'] >= 0)] = 0
    df['时段'][(df['hour'] < 16) & (df['hour'] >= 8)] = 1
    df['时段'][(df['hour'] < 24) & (df['hour'] >= 16)] = 2
    cate_tmp = df[['cate_id','cate_name']].drop_duplicates()
    zhubo_tmp = df[['roomid','zhubo']].drop_duplicates()
    g = df.groupby([df['roomid'],df['cate_id'],df['时段']])
    df_tmp = pd.DataFrame()
    df_tmp['online'] = g['online'].mean()
    df_tmp.reset_index(inplace=True)
    data = pd.concat([data,df_tmp])
    cate = pd.concat([cate,cate_tmp]).drop_duplicates()
    zhubo = pd.concat([zhubo,zhubo_tmp]).drop_duplicates()
    print(str(d)+'日数据合并完成')
data.index = range(len(data))
data_g = data.groupby([data['roomid'],data['cate_id'],data['时段']])
data1['平均在线人数'] = data_g['online'].mean()
data1.reset_index(inplace=True)
data1 = pd.merge(data1, cate, how='left', on='cate_id')
data1 = pd.merge(data1, zhubo, how='left', on='roomid')
data1.to_csv('/home/miracle/文档/斗鱼分时段在线人数汇总2.0.csv')