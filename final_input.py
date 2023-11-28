import pandas as pd
#df = pd.read_csv('D:/Program Files/RStudio/data.csv')

def run_model(P_input = 0, W_input = 0, PRO_input = 0, M_input = 0):
    df = pd.read_csv('../input_data.csv')

    # P_input = 749325.3

    df['P_new'] = df['P']*(P_input/df['P'].sum())

    # 输入
    # W_input = 1.69

    # PRO_input = 0.175

    # M_input = 0.0039


    # 人均垃圾产量
    urban_df = df[df['W']== 1.69]
    #print (urban_df)
    #print (urban_df['W'])

    rural_df = df[df['W']== 0.55]
    #print (rural_df)
    #print (rural_df['W'])

    #print (Z)
    df['W_urban_new'] = (W_input/1.69)  * urban_df['W']
    #print (df['W_urban_new'] )

    # 塑料比例
    #print (Z)
    df['PRO_urban_new'] = (PRO_input/0.175)  * urban_df['PRO']
    #print (df['W_urban_new'] )


    df['M_urban_new'] = (M_input/0.0039) * urban_df['M']



    #城镇通量
    df['E_urban']=df['P_new'] * df['W_urban_new'] * df['PRO_urban_new'] * df['M_urban_new'] * df['R'] * 366
    sum_urban = df['E_urban'].sum()
    print (sum_urban)




    #农村
    df['W_rural_new'] = rural_df['W']*((W_input/(1.69/0.55))/0.55)         #4为原始数据中城市人均垃圾产量和农村人均垃圾产量的倍数。0.3为农村人均垃圾产量初始值

    df['PRO_rural_new'] = rural_df['PRO']*((PRO_input/(0.175/0.11))/0.11)

    df['M_rural_new'] = rural_df['M']*((M_input/(0.0039/0.1324))/0.1324)

    #农村通量
    df['E_rural']=df['P_new'] * df['W_rural_new'] * df['PRO_rural_new'] * df['M_rural_new'] * df['R'] * 366
    sum_rural = df['E_rural'].sum()
    print (sum_rural)

    #总通量

    sum = sum_urban + sum_rural
    return sum


