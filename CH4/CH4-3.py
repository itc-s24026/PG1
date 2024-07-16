def show_kwargs(**kwargs):
    '''把给予的多个关键词变量收纳在词典中并表示出来'''
    print('Keyword arguments:', kwargs)
    return kwargs

show_kwargs(pasta='黄油',drink='红酒',main_dish='肉料理',n_customer=3)
