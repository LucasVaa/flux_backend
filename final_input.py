import pandas as pd
# df = pd.read_csv('D:/Program Files/RStudio/input_1226data.csv')


def run_model(P1_1_input=0,
              P1_2_input=0,
              P1_3_input=0,
              W_input=0,
              PRO_input=0,
              M_input=0,
              Re_input=0,
              I_input=0):
    df = pd.read_csv('../input_0214.csv')
     # 输入
    # W_input = 1.69

    PRO_input = PRO_input / 100

    M_input = M_input / 100

    Re_input = Re_input / 100

    I_input = I_input / 100

    # 原常住人口792757.8
    

    df['P1_1_new'] = df['P1_1'] * (P1_1_input / 792757.8)
    #城镇候鸟游客
    df['P1_2_new'] = df['P1_2'] * (P1_2_input / 958145.8)
    #城镇过夜游客
    df['P1_3_new'] = df['P1_3'] * (P1_3_input / 6002341)
    #耕地人口数量P2
    df['P2_new'] = df['P2'] * (P1_1_input/ 792757.8)
    #林地人口数量P3
    df['P3_new'] = df['P3'] * (P1_1_input / 792757.8)
    #草地人口数量P4
    df['P4_new'] = df['P4'] * (P1_1_input / 792757.8)
    #裸地人口数量P5
    df['P5_new'] = df['P5'] * (P1_1_input / 792757.8)
    #人均垃圾产生量W
    #城市垃圾产生量
    df['W_urban_new'] = W_input 
    #其他地域类型垃圾产生量
    df['W_else_new'] = 0.55 * W_input / 1.69 

    #塑料垃圾占比PRO
    #城市塑料垃圾占比
    df['PRO_urban_new'] = PRO_input 
    #其他地域类型塑料垃圾占比
    df['PRO_else_new'] = 0.11 * PRO_input / 0.175

    #管理不当垃圾比例M
    #城市垃圾管理不当比例
    df['M_urban_new'] = M_input 
    #其他地域类型垃圾管理不当比例
    df['M_else_new'] = 0.1324 * M_input / 0.0039 

    #塑料入海通量
    #城市常驻
    df['E_P1_1'] = df['P1_1_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 366
    sum_E_P1_1 = df['E_P1_1'].sum()

    #城市候鸟
    df['E_P1_2_JAN'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 31
    df['E_P1_2_FEB'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 29 * 0.28813549 / 0.255543474
    df['E_P1_2_MAR'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 31 * 0.146319146 / 0.255543474
    df['E_P1_2_APR'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 30 * 0.049097196 / 0.255543474
    df['E_P1_2_MAY'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 31 * 0.029609108 / 0.255543474
    df['E_P1_2_JUN'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 30 * 0.023980634 / 0.255543474 
    df['E_P1_2_JUL'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 31 * 0.020251616 / 0.255543474
    df['E_P1_2_AUG'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 31 * 0.020372161 / 0.255543474
    df['E_P1_2_SEPT'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 30 * 0.006317024 / 0.255543474
    df['E_P1_2_OCT'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 31 * 0.020060334 / 0.255543474
    df['E_P1_2_NOV'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 30 * 0.045519787 / 0.255543474
    df['E_P1_2_DEC'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 31 *0.09479403 / 0.255543474
    df['E_P1_2'] = df['E_P1_2_JAN'] + df['E_P1_2_FEB'] + df['E_P1_2_MAR'] + df['E_P1_2_APR']+ df['E_P1_2_MAY'] \
          + df['E_P1_2_JUN'] + df['E_P1_2_JUL'] + df['E_P1_2_AUG'] + df['E_P1_2_SEPT'] + df['E_P1_2_OCT'] + df['E_P1_2_NOV'] \
              + df['E_P1_2_DEC']
    sum_E_P1_2 = df['E_P1_2_JAN'].sum() + df['E_P1_2_FEB'].sum() + df['E_P1_2_MAR'].sum() + df['E_P1_2_APR'].sum() + df['E_P1_2_MAY'].sum() \
          + df['E_P1_2_JUN'].sum() + df['E_P1_2_JUL'].sum() + df['E_P1_2_AUG'].sum() + df['E_P1_2_SEPT'].sum() + df['E_P1_2_OCT'].sum() + df['E_P1_2_NOV'].sum() \
              + df['E_P1_2_DEC'].sum()

    
    #城市过夜 (过夜游客每月平均停留时长为4.74天)
    df['E_P1_3_JAN'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 4.74
    df['E_P1_3_FEB'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 4.74 * 0.178006256 / 0.166165525
    df['E_P1_3_MAR'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 4.74 * 0.06280382 / 0.166165525
    df['E_P1_3_APR'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 4.74 * 0.033534039 / 0.166165525
    df['E_P1_3_MAY'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 4.74 * 0.052368763 / 0.166165525
    df['E_P1_3_JUN'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 4.74 * 0.106990437 / 0.166165525
    df['E_P1_3_JUL'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 4.74 *0.128388663 / 0.166165525
    df['E_P1_3_AUG'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 4.74 * 0.030614807 / 0.166165525
    df['E_P1_3_SEPT'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 4.74 * 0.011645852 / 0.166165525
    df['E_P1_3_OCT'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 4.74 * 0.045719543 / 0.166165525
    df['E_P1_3_NOV'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 4.74 * 0.067962721 / 0.166165525
    df['E_P1_3_DEC'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 4.74 * 0.115799574 / 0.166165525
    df['E_P1_3'] = df['E_P1_3_JAN'] + df['E_P1_3_FEB'] + df['E_P1_3_MAR'] + df['E_P1_3_APR']+ df['E_P1_3_MAY'] \
          + df['E_P1_3_JUN'] + df['E_P1_3_JUL'] + df['E_P1_3_AUG'] + df['E_P1_3_SEPT'] + df['E_P1_3_OCT'] + df['E_P1_3_NOV'] \
              + df['E_P1_3_DEC']
    sum_E_P1_3 = df['E_P1_3_JAN'].sum() + df['E_P1_3_FEB'].sum() + df['E_P1_3_MAR'].sum() + df['E_P1_3_APR'].sum() + df['E_P1_3_MAY'].sum() \
          + df['E_P1_3_JUN'].sum() + df['E_P1_3_JUL'].sum() + df['E_P1_3_AUG'].sum() + df['E_P1_3_SEPT'].sum() + df['E_P1_3_OCT'].sum() + df['E_P1_3_NOV'].sum() \
              + df['E_P1_3_DEC'].sum()

    #城市总
    df['E_P1'] = df['E_P1_1'] + df['E_P1_2'] + df['E_P1_3']

    #耕地
    df['E_P2'] = df['P2_new'] * df['W_else_new'] * \
        df['PRO_else_new'] * df['M_else_new'] * df['RO2'] * 366
    sum_E_P2 = df['E_P2'].sum()  
    
    #林地
    df['E_P3'] = df['P3_new'] * df['W_else_new'] * \
        df['PRO_else_new'] * df['M_else_new'] * df['RO3'] * 366
    sum_E_P3 = df['E_P3'].sum()

    #草地
    df['E_P4'] = df['P4_new'] * df['W_else_new'] * \
        df['PRO_else_new'] * df['M_else_new'] * df['RO4'] * 366
    sum_E_P4 = df['E_P4'].sum()

    #裸地
    df['E_P5'] = df['P5_new'] * df['W_else_new'] * \
        df['PRO_else_new'] * df['M_else_new'] * df['RO5'] * 366
    sum_E_P5 = df['E_P5'].sum()

    # 总通量
    sum = sum_E_P1_1 + sum_E_P1_2 + sum_E_P1_3 + sum_E_P2 + sum_E_P3 + sum_E_P4 + sum_E_P5

    #图例用
    max_grid = max( df['E_P1'].max(), df['E_P2'].max(), df['E_P3'].max(),df['E_P4'].max(),df['E_P5'].max() )

    





    # Plastic waste generation总塑料垃圾
    #城市常驻
    df['PWG_P1_1'] = df['P1_1_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * 366
    sum_PWG_P1_1 = df['PWG_P1_1'].sum()
    #城市候鸟
    df['PWG_P1_2_JAN'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new']* 31
    df['PWG_P1_2_FEB'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * 29 * 0.28813549 / 0.255543474
    df['PWG_P1_2_MAR'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * 31 * 0.146319146 / 0.255543474
    df['PWG_P1_2_APR'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * 30 * 0.049097196 / 0.255543474
    df['PWG_P1_2_MAY'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * 31 * 0.029609108 / 0.255543474
    df['PWG_P1_2_JUN'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new']* 30 * 0.023980634 / 0.255543474 
    df['PWG_P1_2_JUL'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new']* 31 * 0.020251616 / 0.255543474
    df['PWG_P1_2_AUG'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new']* 31 * 0.020372161 / 0.255543474
    df['PWG_P1_2_SEPT'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new']* 30 * 0.006317024 / 0.255543474
    df['PWG_P1_2_OCT'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new']* 31 * 0.020060334 / 0.255543474
    df['PWG_P1_2_NOV'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * 30 * 0.045519787 / 0.255543474
    df['PWG_P1_2_DEC'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * 31 *0.09479403 / 0.255543474
    sum_PWG_P1_2 = df['PWG_P1_2_JAN'].sum() + df['PWG_P1_2_FEB'].sum() + df['PWG_P1_2_MAR'].sum() + df['PWG_P1_2_APR'].sum() + df['PWG_P1_2_MAY'].sum() \
          + df['PWG_P1_2_JUN'].sum() + df['PWG_P1_2_JUL'].sum() + df['PWG_P1_2_AUG'].sum() + df['PWG_P1_2_SEPT'].sum() + df['PWG_P1_2_OCT'].sum() + df['PWG_P1_2_NOV'].sum() \
              + df['PWG_P1_2_DEC'].sum()
    #城市过夜 (过夜游客每月平均停留时长为4.74天)
    df['PWG_P1_3_JAN'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * 4.74
    df['PWG_P1_3_FEB'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new']* 4.74 * 0.178006256 / 0.166165525
    df['PWG_P1_3_MAR'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new']* 4.74 * 0.06280382 / 0.166165525
    df['PWG_P1_3_APR'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new']* 4.74 * 0.033534039 / 0.166165525
    df['PWG_P1_3_MAY'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new']* 4.74 * 0.052368763 / 0.166165525
    df['PWG_P1_3_JUN'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new']* 4.74 * 0.106990437 / 0.166165525
    df['PWG_P1_3_JUL'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new']* 4.74 * 0.128388663 / 0.166165525
    df['PWG_P1_3_AUG'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new']* 4.74 * 0.030614807 / 0.166165525
    df['PWG_P1_3_SEPT'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new']* 4.74 * 0.011645852 / 0.166165525
    df['PWG_P1_3_OCT'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new']* 4.74 * 0.045719543 / 0.166165525
    df['PWG_P1_3_NOV'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new']* 4.74 * 0.067962721 / 0.166165525
    df['PWG_P1_3_DEC'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new']* 4.74 * 0.115799574 / 0.166165525
    sum_PWG_P1_3 = df['PWG_P1_3_JAN'].sum() + df['PWG_P1_3_FEB'].sum() + df['PWG_P1_3_MAR'].sum() + df['PWG_P1_3_APR'].sum() + df['PWG_P1_3_MAY'].sum() \
          + df['PWG_P1_3_JUN'].sum() + df['PWG_P1_3_JUL'].sum() + df['PWG_P1_3_AUG'].sum() + df['PWG_P1_3_SEPT'].sum() + df['PWG_P1_3_OCT'].sum() + df['PWG_P1_3_NOV'].sum() \
              + df['PWG_P1_3_DEC'].sum()
    #耕地
    df['PWG_P2'] = df['P2_new'] * df['W_else_new'] * \
        df['PRO_else_new'] * 366
    sum_PWG_P2 = df['PWG_P2'].sum()   
    #林地
    df['PWG_P3'] = df['P3_new'] * df['W_else_new'] * \
        df['PRO_else_new']  * 366
    sum_PWG_P3 = df['PWG_P3'].sum()
    #草地
    df['PWG_P4'] = df['P4_new'] * df['W_else_new'] * \
        df['PRO_else_new']  * 366
    sum_PWG_P4 = df['PWG_P4'].sum()
    #裸地
    df['PWG_P5'] = df['P5_new'] * df['W_else_new'] * \
        df['PRO_else_new']  * 366
    sum_PWG_P5 = df['PWG_P5'].sum()

    sum_PWG = sum_PWG_P1_1 + sum_PWG_P1_2 + sum_PWG_P1_3 + sum_PWG_P2 + sum_PWG_P3 + sum_PWG_P4 + sum_PWG_P5

    # Mismanaged plastic waste管理不当
    sum_MPW_P1_1 = sum_PWG_P1_1 * M_input
    sum_MPW_P1_2 = sum_PWG_P1_2 * M_input
    sum_MPW_P1_3 = sum_PWG_P1_3 * M_input
    sum_MPW_P2 = sum_PWG_P2 * 0.1324 * M_input / 0.0039 
    sum_MPW_P3 = sum_PWG_P3 * 0.1324 * M_input / 0.0039 
    sum_MPW_P4 = sum_PWG_P4 * 0.1324 * M_input / 0.0039 
    sum_MPW_P5 = sum_PWG_P5 * 0.1324 * M_input / 0.0039 

    sum_MPW = sum_MPW_P1_1 + sum_MPW_P1_2 + sum_MPW_P1_3 + sum_MPW_P2 + sum_MPW_P3 + sum_MPW_P4 + sum_MPW_P5

    # Enter into river入河
    #城市常驻
    df['ER_P1_1'] = df['P1_1_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RR1'] * 366
    sum_ER_P1_1 = df['ER_P1_1'].sum()

    #城市候鸟
    df['ER_P1_2_JAN'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RR1'] * 31
    df['ER_P1_2_FEB'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RR1'] * 29 * 0.28813549 / 0.255543474
    df['ER_P1_2_MAR'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RR1'] * 31 * 0.146319146 / 0.255543474
    df['ER_P1_2_APR'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RR1'] * 30 * 0.049097196 / 0.255543474
    df['ER_P1_2_MAY'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RR1'] * 31 * 0.029609108 / 0.255543474
    df['ER_P1_2_JUN'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RR1'] * 30 * 0.023980634 / 0.255543474 
    df['ER_P1_2_JUL'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RR1'] * 31 * 0.020251616 / 0.255543474
    df['ER_P1_2_AUG'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RR1'] * 31 * 0.020372161 / 0.255543474
    df['ER_P1_2_SEPT'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RR1'] * 30 * 0.006317024 / 0.255543474
    df['ER_P1_2_OCT'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RR1'] * 31 * 0.020060334 / 0.255543474
    df['ER_P1_2_NOV'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RR1'] * 30 * 0.045519787 / 0.255543474
    df['ER_P1_2_DEC'] = df['P1_2_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RR1'] * 31 *0.09479403 / 0.255543474
    df['ER_P1_2'] = df['ER_P1_2_JAN'] + df['ER_P1_2_FEB'] + df['ER_P1_2_MAR'] + df['ER_P1_2_APR']+ df['ER_P1_2_MAY'] \
          + df['ER_P1_2_JUN'] + df['ER_P1_2_JUL'] + df['ER_P1_2_AUG'] + df['ER_P1_2_SEPT'] + df['ER_P1_2_OCT'] + df['ER_P1_2_NOV'] \
              + df['ER_P1_2_DEC']
    sum_ER_P1_2 = df['ER_P1_2_JAN'].sum() + df['ER_P1_2_FEB'].sum() + df['ER_P1_2_MAR'].sum() + df['ER_P1_2_APR'].sum() + df['ER_P1_2_MAY'].sum() \
          + df['ER_P1_2_JUN'].sum() + df['ER_P1_2_JUL'].sum() + df['ER_P1_2_AUG'].sum() + df['ER_P1_2_SEPT'].sum() + df['ER_P1_2_OCT'].sum() + df['ER_P1_2_NOV'].sum() \
              + df['ER_P1_2_DEC'].sum()

    
    #城市过夜 (过夜游客每月平均停留时长为4.74天)
    df['ER_P1_3_JAN'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RR1'] * 4.74
    df['ER_P1_3_FEB'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RR1'] * 4.74 * 0.178006256 / 0.166165525
    df['ER_P1_3_MAR'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RR1'] * 4.74 * 0.06280382 / 0.166165525
    df['ER_P1_3_APR'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RR1'] * 4.74 * 0.033534039 / 0.166165525
    df['ER_P1_3_MAY'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RR1'] * 4.74 * 0.052368763 / 0.166165525
    df['ER_P1_3_JUN'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RR1'] * 4.74 * 0.106990437 / 0.166165525
    df['ER_P1_3_JUL'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RR1'] * 4.74 *0.128388663 / 0.166165525
    df['ER_P1_3_AUG'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RR1'] * 4.74 * 0.030614807 / 0.166165525
    df['ER_P1_3_SEPT'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RR1'] * 4.74 * 0.011645852 / 0.166165525
    df['ER_P1_3_OCT'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RR1'] * 4.74 * 0.045719543 / 0.166165525
    df['ER_P1_3_NOV'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RR1'] * 4.74 * 0.067962721 / 0.166165525
    df['ER_P1_3_DEC'] = df['P1_3_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RR1'] * 4.74 * 0.115799574 / 0.166165525
    df['ER_P1_3'] = df['ER_P1_3_JAN'] + df['ER_P1_3_FEB'] + df['ER_P1_3_MAR'] + df['ER_P1_3_APR']+ df['ER_P1_3_MAY'] \
          + df['ER_P1_3_JUN'] + df['ER_P1_3_JUL'] + df['ER_P1_3_AUG'] + df['ER_P1_3_SEPT'] + df['ER_P1_3_OCT'] + df['ER_P1_3_NOV'] \
              + df['ER_P1_3_DEC']
    sum_ER_P1_3 = df['ER_P1_3_JAN'].sum() + df['ER_P1_3_FEB'].sum() + df['ER_P1_3_MAR'].sum() + df['ER_P1_3_APR'].sum() + df['ER_P1_3_MAY'].sum() \
          + df['ER_P1_3_JUN'].sum() + df['ER_P1_3_JUL'].sum() + df['ER_P1_3_AUG'].sum() + df['ER_P1_3_SEPT'].sum() + df['ER_P1_3_OCT'].sum() + df['ER_P1_3_NOV'].sum() \
              + df['ER_P1_3_DEC'].sum()

    #耕地
    df['ER_P2'] = df['P2_new'] * df['W_else_new'] * \
        df['PRO_else_new'] * df['M_else_new'] * df['RR2'] * 366
    sum_ER_P2 = df['ER_P2'].sum()  
    
    #林地
    df['ER_P3'] = df['P3_new'] * df['W_else_new'] * \
        df['PRO_else_new'] * df['M_else_new'] * df['RR3'] * 366
    sum_ER_P3 = df['ER_P3'].sum()

    #草地
    df['ER_P4'] = df['P4_new'] * df['W_else_new'] * \
        df['PRO_else_new'] * df['M_else_new'] * df['RR4'] * 366
    sum_ER_P4 = df['ER_P4'].sum()

    #裸地
    df['ER_P5'] = df['P5_new'] * df['W_else_new'] * \
        df['PRO_else_new'] * df['M_else_new'] * df['RR5'] * 366
    sum_ER_P5 = df['ER_P5'].sum()

    # 总Enter River
    sum_ER = sum_ER_P1_1 + sum_ER_P1_2 + sum_ER_P1_3 + sum_ER_P2 + sum_ER_P3 + sum_ER_P4 + sum_ER_P5


    # Terrestrial leakage& Open-pit burning& Dumpsites
    sum_TOD = sum_MPW - sum_ER

    # Enter into sea
    sum_ES = sum

    # Sink
    sum_S = sum_ER - sum_ES

    # Recyclable Waste
    sum_RW = sum_PWG * Re_input

    # Garbage collection stations in neighborhood
    sum_GCSIN = sum_PWG - sum_MPW - sum_RW

    # Waste transfer station
    sum_WTS = sum_GCSIN

    # Garbage incineration generation plant
    sum_GIGP = sum_GCSIN * I_input

    # Sanitary landfill site
    sum_SLS = sum_GCSIN - sum_GIGP

        #JAN
    df['E_P1_1_JAN'] =  df['E_P1_1'] = df['P1_1_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 31
    JAN_P1_1 = df['E_P1_1_JAN'].sum() 
    JAN_P1_2 = df['E_P1_2_JAN'].sum()
    JAN_P1_3 = df['E_P1_3_JAN'].sum()
    JAN_P2 = sum_E_P2 * 31 / 366
    JAN_P3 = sum_E_P3 * 31 / 366  
    JAN_P4 = sum_E_P4 * 31 / 366  
    JAN_P5 = sum_E_P5 * 31 / 366  
    sum_JAN = JAN_P1_1 + JAN_P1_2 + JAN_P1_3 + JAN_P2 + JAN_P3 + JAN_P4 + JAN_P5
    JAN_YR = JAN_P1_1 / sum_JAN
    JAN_SR = JAN_P1_2 / sum_JAN 
    JAN_OT = JAN_P1_3 / sum_JAN
    JAN_CL = JAN_P2 / sum_JAN
    JAN_F = JAN_P3 / sum_JAN
    JAN_GL =  JAN_P4 / sum_JAN
    JAN_BL = JAN_P5 / sum_JAN
    
        #FEB
    df['E_P1_1_FEB'] =  df['E_P1_1'] = df['P1_1_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 29
    FEB_P1_1 = df['E_P1_1_FEB'].sum() 
    FEB_P1_2 = df['E_P1_2_FEB'].sum()
    FEB_P1_3 = df['E_P1_3_FEB'].sum()
    FEB_P2 = sum_E_P2 * 29 / 366
    FEB_P3 = sum_E_P3 * 29 / 366  
    FEB_P4 = sum_E_P4 * 29 / 366  
    FEB_P5 = sum_E_P5 * 29 / 366 
    sum_FEB = FEB_P1_1 + FEB_P1_2 + FEB_P1_3 + FEB_P2 + FEB_P3 + FEB_P4 + FEB_P5 
    FEB_YR = FEB_P1_1 / sum_FEB
    FEB_SR = FEB_P1_2 / sum_FEB 
    FEB_OT = FEB_P1_3 / sum_FEB
    FEB_CL = FEB_P2 / sum_FEB
    FEB_F = FEB_P3 / sum_FEB
    FEB_GL =  FEB_P4 / sum_FEB
    FEB_BL = FEB_P5 / sum_FEB

        #MAR
    df['E_P1_1_MAR'] =  df['E_P1_1'] = df['P1_1_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 31
    MAR_P1_1 = df['E_P1_1_MAR'].sum() 
    MAR_P1_2 = df['E_P1_2_MAR'].sum()
    MAR_P1_3 = df['E_P1_3_MAR'].sum()
    MAR_P2 = sum_E_P2 * 31 / 366
    MAR_P3 = sum_E_P3 * 31 / 366  
    MAR_P4 = sum_E_P4 * 31 / 366  
    MAR_P5 = sum_E_P5 * 31 / 366  
    sum_MAR = MAR_P1_1 + MAR_P1_2 + MAR_P1_3 + MAR_P2 + MAR_P3 + MAR_P4 + MAR_P5 
    MAR_YR = MAR_P1_1 / sum_MAR
    MAR_SR = MAR_P1_2 / sum_MAR 
    MAR_OT = MAR_P1_3 / sum_MAR
    MAR_CL = MAR_P2 / sum_MAR
    MAR_F = MAR_P3 / sum_MAR
    MAR_GL =  MAR_P4 / sum_MAR
    MAR_BL = MAR_P5 / sum_MAR    
        #APR
    df['E_P1_1_APR'] =  df['E_P1_1'] = df['P1_1_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 30
    APR_P1_1 = df['E_P1_1_APR'].sum() 
    APR_P1_2 = df['E_P1_2_APR'].sum()
    APR_P1_3 = df['E_P1_3_APR'].sum()
    APR_P2 = sum_E_P2 * 30 / 366
    APR_P3 = sum_E_P3 * 30 / 366  
    APR_P4 = sum_E_P4 * 30 / 366  
    APR_P5 = sum_E_P5 * 30 / 366  
    sum_APR = APR_P1_1 + APR_P1_2 + APR_P1_3 + APR_P2 + APR_P3 + APR_P4 + APR_P5 
    APR_YR = APR_P1_1 / sum_APR
    APR_SR = APR_P1_2 / sum_APR 
    APR_OT = APR_P1_3 / sum_APR
    APR_CL = APR_P2 / sum_APR
    APR_F = APR_P3 / sum_APR
    APR_GL =  APR_P4 / sum_APR
    APR_BL = APR_P5 / sum_APR    
        #MAY
    df['E_P1_1_MAY'] =  df['E_P1_1'] = df['P1_1_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 31
    MAY_P1_1 = df['E_P1_1_MAY'].sum() 
    MAY_P1_2 = df['E_P1_2_MAY'].sum()
    MAY_P1_3 = df['E_P1_3_MAY'].sum()
    MAY_P2 = sum_E_P2 * 31 / 366
    MAY_P3 = sum_E_P3 * 31 / 366  
    MAY_P4 = sum_E_P4 * 31 / 366  
    MAY_P5 = sum_E_P5 * 31 / 366  
    sum_MAY = MAY_P1_1 + MAY_P1_2 + MAY_P1_3 + MAY_P2 + MAY_P3 + MAY_P4 + MAY_P5 
    MAY_YR = MAY_P1_1 / sum_MAY
    MAY_SR = MAY_P1_2 / sum_MAY 
    MAY_OT = MAY_P1_3 / sum_MAY
    MAY_CL = MAY_P2 / sum_MAY
    MAY_F = MAY_P3 / sum_MAY
    MAY_GL =  MAY_P4 / sum_MAY
    MAY_BL = MAY_P5 / sum_MAY    
        #JUN
    df['E_P1_1_JUN'] =  df['E_P1_1'] = df['P1_1_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 30
    JUN_P1_1 = df['E_P1_1_JUN'].sum() 
    JUN_P1_2 = df['E_P1_2_JUN'].sum()
    JUN_P1_3 = df['E_P1_3_JUN'].sum()
    JUN_P2 = sum_E_P2 * 30 / 366
    JUN_P3 = sum_E_P3 * 30 / 366  
    JUN_P4 = sum_E_P4 * 30 / 366  
    JUN_P5 = sum_E_P5 * 30 / 366  
    sum_JUN = JUN_P1_1 + JUN_P1_2 + JUN_P1_3 + JUN_P2 + JUN_P3 + JUN_P4 + JUN_P5 
    JUN_YR = JUN_P1_1 / sum_JUN
    JUN_SR = JUN_P1_2 / sum_JUN 
    JUN_OT = JUN_P1_3 / sum_JUN
    JUN_CL = JUN_P2 / sum_JUN
    JUN_F = JUN_P3 / sum_JUN
    JUN_GL =  JUN_P4 / sum_JUN
    JUN_BL = JUN_P5 / sum_JUN    
        #JUL
    df['E_P1_1_JUL'] =  df['E_P1_1'] = df['P1_1_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 31
    JUL_P1_1 = df['E_P1_1_JUL'].sum() 
    JUL_P1_2 = df['E_P1_2_JUL'].sum()
    JUL_P1_3 = df['E_P1_3_JUL'].sum()
    JUL_P2 = sum_E_P2 * 31 / 366
    JUL_P3 = sum_E_P3 * 31 / 366  
    JUL_P4 = sum_E_P4 * 31 / 366  
    JUL_P5 = sum_E_P5 * 31 / 366  
    sum_JUL = JUL_P1_1 + JUL_P1_2 + JUL_P1_3 + JUL_P2 + JUL_P3 + JUL_P4 + JUL_P5 
    JUL_YR = JUL_P1_1 / sum_JUL
    JUL_SR = JUL_P1_2 / sum_JUL 
    JUL_OT = JUL_P1_3 / sum_JUL
    JUL_CL = JUL_P2 / sum_JUL
    JUL_F = JUL_P3 / sum_JUL
    JUL_GL =  JUL_P4 / sum_JUL
    JUL_BL = JUL_P5 / sum_JUL    
        #AUG
    df['E_P1_1_AUG'] =  df['E_P1_1'] = df['P1_1_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 31
    AUG_P1_1 = df['E_P1_1_AUG'].sum() 
    AUG_P1_2 = df['E_P1_2_AUG'].sum()
    AUG_P1_3 = df['E_P1_3_AUG'].sum()
    AUG_P2 = sum_E_P2 * 31 / 366
    AUG_P3 = sum_E_P3 * 31 / 366  
    AUG_P4 = sum_E_P4 * 31 / 366  
    AUG_P5 = sum_E_P5 * 31 / 366  
    sum_AUG = AUG_P1_1 + AUG_P1_2 + AUG_P1_3 + AUG_P2 + AUG_P3 + AUG_P4 + AUG_P5 
    AUG_YR = AUG_P1_1 / sum_AUG
    AUG_SR = AUG_P1_2 / sum_AUG 
    AUG_OT = AUG_P1_3 / sum_AUG
    AUG_CL = AUG_P2 / sum_AUG
    AUG_F = AUG_P3 / sum_AUG
    AUG_GL =  AUG_P4 / sum_AUG
    AUG_BL = AUG_P5 / sum_AUG    
        #SEPT
    df['E_P1_1_SEPT'] =  df['E_P1_1'] = df['P1_1_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 30
    SEPT_P1_1 = df['E_P1_1_SEPT'].sum() 
    SEPT_P1_2 = df['E_P1_2_SEPT'].sum()
    SEPT_P1_3 = df['E_P1_3_SEPT'].sum()
    SEPT_P2 = sum_E_P2 * 30 / 366
    SEPT_P3 = sum_E_P3 * 30 / 366  
    SEPT_P4 = sum_E_P4 * 30 / 366  
    SEPT_P5 = sum_E_P5 * 30 / 366  
    sum_SEPT = SEPT_P1_1 + SEPT_P1_2 + SEPT_P1_3 + SEPT_P2 + SEPT_P3 + SEPT_P4 + SEPT_P5 
    SEPT_YR = SEPT_P1_1 / sum_SEPT
    SEPT_SR = SEPT_P1_2 / sum_SEPT 
    SEPT_OT = SEPT_P1_3 / sum_SEPT
    SEPT_CL = SEPT_P2 / sum_SEPT
    SEPT_F = SEPT_P3 / sum_SEPT
    SEPT_GL =  SEPT_P4 / sum_SEPT
    SEPT_BL = SEPT_P5 / sum_SEPT    
        #OCT
    df['E_P1_1_OCT'] =  df['E_P1_1'] = df['P1_1_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 31
    OCT_P1_1 = df['E_P1_1_OCT'].sum() 
    OCT_P1_2 = df['E_P1_2_OCT'].sum()
    OCT_P1_3 = df['E_P1_3_OCT'].sum()
    OCT_P2 = sum_E_P2 * 31 / 366
    OCT_P3 = sum_E_P3 * 31 / 366  
    OCT_P4 = sum_E_P4 * 31 / 366  
    OCT_P5 = sum_E_P5 * 31 / 366  
    sum_OCT = OCT_P1_1 + OCT_P1_2 + OCT_P1_3 + OCT_P2 + OCT_P3 + OCT_P4 + OCT_P5 
    OCT_YR = OCT_P1_1 / sum_OCT
    OCT_SR = OCT_P1_2 / sum_OCT 
    OCT_OT = OCT_P1_3 / sum_OCT
    OCT_CL = OCT_P2 / sum_OCT
    OCT_F = OCT_P3 / sum_OCT
    OCT_GL =  OCT_P4 / sum_OCT
    OCT_BL = OCT_P5 / sum_OCT   
        #NOV
    df['E_P1_1_NOV'] =  df['E_P1_1'] = df['P1_1_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 30
    NOV_P1_1 = df['E_P1_1_NOV'].sum() 
    NOV_P1_2 = df['E_P1_2_NOV'].sum()
    NOV_P1_3 = df['E_P1_3_NOV'].sum()
    NOV_P2 = sum_E_P2 * 30 / 366
    NOV_P3 = sum_E_P3 * 30 / 366  
    NOV_P4 = sum_E_P4 * 30 / 366  
    NOV_P5 = sum_E_P5 * 30 / 366  
    sum_NOV = NOV_P1_1 + NOV_P1_2 + NOV_P1_3 + NOV_P2 + NOV_P3 + NOV_P4 + NOV_P5 
    NOV_YR = NOV_P1_1 / sum_NOV
    NOV_SR = NOV_P1_2 / sum_NOV 
    NOV_OT = NOV_P1_3 / sum_NOV
    NOV_CL = NOV_P2 / sum_NOV
    NOV_F = NOV_P3 / sum_NOV
    NOV_GL =  NOV_P4 / sum_NOV
    NOV_BL = NOV_P5 / sum_NOV
       #DEC
    df['E_P1_1_DEC'] =  df['E_P1_1'] = df['P1_1_new'] * df['W_urban_new'] * \
        df['PRO_urban_new'] * df['M_urban_new'] * df['RO1'] * 31
    DEC_P1_1 = df['E_P1_1_DEC'].sum() 
    DEC_P1_2 = df['E_P1_2_DEC'].sum()
    DEC_P1_3 = df['E_P1_3_DEC'].sum()
    DEC_P2 = sum_E_P2 * 31 / 366
    DEC_P3 = sum_E_P3 * 31 / 366  
    DEC_P4 = sum_E_P4 * 31 / 366  
    DEC_P5 = sum_E_P5 * 31 / 366  
    sum_DEC = DEC_P1_1 + DEC_P1_2 + DEC_P1_3 + DEC_P2 + DEC_P3 + DEC_P4 + DEC_P5 
    DEC_YR = DEC_P1_1 / sum_DEC
    DEC_SR = DEC_P1_2 / sum_DEC 
    DEC_OT = DEC_P1_3 / sum_DEC
    DEC_CL = DEC_P2 / sum_DEC
    DEC_F = DEC_P3 / sum_DEC
    DEC_GL =  DEC_P4 / sum_DEC
    DEC_BL = DEC_P5 / sum_DEC   
    
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

    bar = {
        "JAN": {
            "JAN_SUM": '%.2f' % (sum_JAN / 1000),
            "JAN_YR": '%.2f' % (JAN_YR * 100),
            "JAN_SR": '%.2f' % (JAN_SR * 100),
            "JAN_OT": '%.2f' % (JAN_OT * 100),
            "JAN_CL": '%.2f' % (JAN_CL * 100),
            "JAN_F": '%.2f' % (JAN_F * 100),
            "JAN_GL": '%.2f' % (JAN_GL * 100),
            "JAN_BL": '%.2f' % (JAN_BL * 100),
        },
        "FEB": {
            "FEB_SUM": '%.2f' % (sum_FEB / 1000),
            "FEB_YR": '%.2f' % (FEB_YR * 100),
            "FEB_SR": '%.2f' % (FEB_SR * 100),
            "FEB_OT": '%.2f' % (FEB_OT * 100),
            "FEB_CL": '%.2f' % (FEB_CL * 100),
            "FEB_F": '%.2f' % (FEB_F * 100),
            "FEB_GL": '%.2f' % (FEB_GL * 100),
            "FEB_BL": '%.2f' % (FEB_BL * 100),
        },
        "MAR": {
            "MAR_SUM": '%.2f' % (sum_MAR / 1000),
            "MAR_YR": '%.2f' % (MAR_YR * 100),
            "MAR_SR": '%.2f' % (MAR_SR * 100),
            "MAR_OT": '%.2f' % (MAR_OT * 100),
            "MAR_CL": '%.2f' % (MAR_CL * 100),
            "MAR_F": '%.2f' % (MAR_F * 100),
            "MAR_GL": '%.2f' % (MAR_GL * 100),
            "MAR_BL": '%.2f' % (MAR_BL * 100),
        },
        "APR": {
            "APR_SUM": '%.2f' % (sum_APR / 1000),
            "APR_YR": '%.2f' % (APR_YR * 100),
            "APR_SR": '%.2f' % (APR_SR * 100),
            "APR_OT": '%.2f' % (APR_OT * 100),
            "APR_CL": '%.2f' % (APR_CL * 100),
            "APR_F": '%.2f' % (APR_F * 100),
            "APR_GL": '%.2f' % (APR_GL * 100),
            "APR_BL": '%.2f' % (APR_BL * 100),
        },
        "MAY": {
            "MAY_SUM": '%.2f' % (sum_MAY / 1000),
            "MAY_YR": '%.2f' % (MAY_YR * 100),
            "MAY_SR": '%.2f' % (MAY_SR * 100),
            "MAY_OT": '%.2f' % (MAY_OT * 100),
            "MAY_CL": '%.2f' % (MAY_CL * 100),
            "MAY_F": '%.2f' % (MAY_F * 100),
            "MAY_GL": '%.2f' % (MAY_GL * 100),
            "MAY_BL": '%.2f' % (MAY_BL * 100),
        },
        "JUN": {
            "JUN_SUM": '%.2f' % (sum_JUN / 1000),
            "JUN_YR": '%.2f' % (JUN_YR * 100),
            "JUN_SR": '%.2f' % (JUN_SR * 100),
            "JUN_OT": '%.2f' % (JUN_OT * 100),
            "JUN_CL": '%.2f' % (JUN_CL * 100),
            "JUN_F": '%.2f' % (JUN_F * 100),
            "JUN_GL": '%.2f' % (JUN_GL * 100),
            "JUN_BL": '%.2f' % (JUN_BL * 100),
        },
        "JUL": {
            "JUL_SUM": '%.2f' % (sum_JUL / 1000),
            "JUL_YR": '%.2f' % (JUL_YR * 100),
            "JUL_SR": '%.2f' % (JUL_SR * 100),
            "JUL_OT": '%.2f' % (JUL_OT * 100),
            "JUL_CL": '%.2f' % (JUL_CL * 100),
            "JUL_F": '%.2f' % (JUL_F * 100),
            "JUL_GL": '%.2f' % (JUL_GL * 100),
            "JUL_BL": '%.2f' % (JUL_BL * 100),
        },
        "AUG": {
            "AUG_SUM": '%.2f' % (sum_AUG / 1000),
            "AUG_YR": '%.2f' % (AUG_YR * 100),
            "AUG_SR": '%.2f' % (AUG_SR * 100),
            "AUG_OT": '%.2f' % (AUG_OT * 100),
            "AUG_CL": '%.2f' % (AUG_CL * 100),
            "AUG_F": '%.2f' % (AUG_F * 100),
            "AUG_GL": '%.2f' % (AUG_GL * 100),
            "AUG_BL": '%.2f' % (AUG_BL * 100),
        },
        "SEPT": {
            "SEPT_SUM": '%.2f' % (sum_SEPT / 1000),
            "SEPT_YR": '%.2f' % (SEPT_YR * 100),
            "SEPT_SR": '%.2f' % (SEPT_SR * 100),
            "SEPT_OT": '%.2f' % (SEPT_OT * 100),
            "SEPT_CL": '%.2f' % (SEPT_CL * 100),
            "SEPT_F": '%.2f' % (SEPT_F * 100),
            "SEPT_GL": '%.2f' % (SEPT_GL * 100),
            "SEPT_BL": '%.2f' % (SEPT_BL * 100),
        },
        "OCT": {
            "OCT_SUM": '%.2f' % (sum_OCT / 1000),
            "OCT_YR": '%.2f' % (OCT_YR * 100),
            "OCT_SR": '%.2f' % (OCT_SR * 100),
            "OCT_OT": '%.2f' % (OCT_OT * 100),
            "OCT_CL": '%.2f' % (OCT_CL * 100),
            "OCT_F": '%.2f' % (OCT_F * 100),
            "OCT_GL": '%.2f' % (OCT_GL * 100),
            "OCT_BL": '%.2f' % (OCT_BL * 100),
        },
        "NOV": {
            "NOV_SUM": '%.2f' % (sum_NOV / 1000),
            "NOV_YR": '%.2f' % (NOV_YR * 100),
            "NOV_SR": '%.2f' % (NOV_SR * 100),
            "NOV_OT": '%.2f' % (NOV_OT * 100),
            "NOV_CL": '%.2f' % (NOV_CL * 100),
            "NOV_F": '%.2f' % (NOV_F * 100),
            "NOV_GL": '%.2f' % (NOV_GL * 100),
            "NOV_BL": '%.2f' % (NOV_BL * 100),
        },
        "DEC": {
            "DEC_SUM": '%.2f' % (sum_DEC / 1000),
            "DEC_YR": '%.2f' % (DEC_YR * 100),
            "DEC_SR": '%.2f' % (DEC_SR * 100),
            "DEC_OT": '%.2f' % (DEC_OT * 100),
            "DEC_CL": '%.2f' % (DEC_CL * 100),
            "DEC_F": '%.2f' % (DEC_F * 100),
            "DEC_GL": '%.2f' % (DEC_GL * 100),
            "DEC_BL": '%.2f' % (DEC_BL * 100),
        },

    }

    return {
        "res": '%.2f' % (sum / 1000),
        "max": '%.2f' % (max_grid / 1000),
        "sankey": sankey,
        "bar": bar
    }
