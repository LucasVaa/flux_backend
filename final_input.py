import pandas as pd
# df = pd.read_csv('D:/Program Files/RStudio/input_data.csv')


def run_model(P_input=0,
              W_input=0,
              PRO_input=0,
              M_input=0,
              Re_input=0,
              I_input=0):
    df = pd.read_csv('../input_data.csv')

    # P_input = 749325.3

    df['P_new'] = df['P'] * (P_input / df['P'].sum())

    # 输入
    # W_input = 1.69

    PRO_input = PRO_input / 100

    M_input = M_input / 100

    Re_input = Re_input / 100

    I_input = I_input / 100

    # 人均垃圾产量
    urban_df = df[df['W'] == 1.69]
    # print (urban_df)
    # print (urban_df['W'])

    rural_df = df[df['W'] == 0.55]
    # print (rural_df)
    # print (rural_df['W'])

    # print (Z)
    df['W_urban_new'] = (W_input / 1.69) * urban_df['W']
    # print (df['W_urban_new'] )

    # 塑料比例
    # print (Z)
    df['PRO_urban_new'] = (PRO_input / 0.175) * urban_df['PRO']
    # print (df['W_urban_new'] )

    df['M_urban_new'] = (M_input / 0.0039) * urban_df['M']

    # 城镇通量
    df['E_urban'] = df['P_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO'] * 366
    sum_urban = df['E_urban'].sum()
    print(sum_urban)

    # 农村
    # 4为原始数据中城市人均垃圾产量和农村人均垃圾产量的倍数。0.3为农村人均垃圾产量初始值
    df['W_rural_new'] = rural_df['W'] * ((W_input / (1.69 / 0.55)) / 0.55)

    df['PRO_rural_new'] = rural_df['PRO'] * ((PRO_input /
                                              (0.175 / 0.11)) / 0.11)

    df['M_rural_new'] = rural_df['M'] * ((M_input /
                                          (0.0039 / 0.1324)) / 0.1324)

    # 农村通量
    df['E_rural'] = df['P_new'] * df['W_rural_new'] * \
        df['PRO_rural_new'] * df['M_rural_new'] * df['RO'] * 366
    sum_rural = df['E_rural'].sum()
    print(sum_rural)

    # 总通量
    sum = sum_urban + sum_rural

    if (df['E_rural'].max() > df['E_urban'].max()):
        max = df['E_rural'].max()
    else:
        max = df['E_urban'].max()

    # Plastic waste generation总塑料垃圾
    df['PWG_rural'] = df['P_new'] * \
        df['W_rural_new'] * df['PRO_rural_new'] * 366
    sum_PWG_rural = df['PWG_rural'].sum()
    df['PWG_urban'] = df['P_new'] * \
        df['W_urban_new'] * df['PRO_urban_new'] * 366
    sum_PWG_urban = df['PWG_urban'].sum()
    sum_PWG = sum_PWG_urban + sum_PWG_rural

    # Mismanaged plastic waste管理不当
    df['MPW_rural'] = df['P_new'] * df['W_rural_new'] * \
        df['PRO_rural_new'] * df['M_rural_new'] * 366
    sum_MPW_rural = df['MPW_rural'].sum()
    df['MPW_urban'] = df['P_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * 366
    sum_MPW_urban = df['MPW_urban'].sum()
    sum_MPW = sum_MPW_urban + sum_MPW_rural

    # Enter into river入河
    df['ER_urban'] = df['P_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RR'] * 366
    sum_ER_urban = df['ER_urban'].sum()
    df['ER_rural'] = df['P_new'] * df['W_rural_new'] * \
        df['PRO_rural_new'] * df['M_rural_new'] * df['RR'] * 366
    sum_ER_rural = df['ER_rural'].sum()
    sum_ER = sum_ER_urban + sum_ER_rural

    # TOD
    sum_TOD = sum_MPW - sum_ER

    # Enter into sea
    sum_ES = sum

    # Sink
    sum_S = sum_ER - sum_ES

    # Recyclable Waste
    df['RW_urban'] = df['P_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * Re_input * 366
    sum_RW_urban = df['RW_urban'].sum()
    df['RW_rural'] = df['P_new'] * df['W_rural_new'] * \
        df['PRO_rural_new'] * Re_input * 366
    sum_RW_rural = df['RW_rural'].sum()
    sum_RW = sum_RW_urban + sum_RW_rural

    # Garbage collection stations in neighborhood
    sum_GCSIN = sum_PWG - sum_MPW - sum_RW

    # Waste transfer station
    sum_WTS = sum_GCSIN

    # Garbage incineration generation plant
    sum_GIGP = sum_GCSIN * I_input

    # Sanitary landfill site
    sum_SLS = sum_GCSIN - sum_GIGP

    sankey = {
        "PWG": '%.2f' % (sum_PWG / 1000),
        "MPW": '%.2f' % (sum_MPW / 1000),
        "ER": '%.2f' % (sum_ER / 1000),
        "TOD": '%.2f' % (sum_TOD / 1000),
        "ES": '%.2f' % (sum_ES / 1000),
        "S": '%.2f' % (sum_S / 1000),
        "GCSIN": '%.2f' % (sum_GCSIN / 1000),
        "WTS": '%.2f' % (sum_WTS / 1000),
        "GIGP": '%.2f' % (sum_GIGP / 1000),
        "SLS": '%.2f' % (sum_SLS / 1000),
        "RW": '%.2f' % (sum_RW / 1000)
    }

    return {
        "res": '%.2f' % (sum / 1000),
        "max": '%.2f' % (max / 1000),
        "sankey": sankey
    }
