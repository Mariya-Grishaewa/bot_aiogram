from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton,ReplyKeyboardMarkup, KeyboardButton

rb1_reply = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='/country')],
    [KeyboardButton(text='/start'),KeyboardButton(text='/help')]
])

ikb1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Россия🇷🇺', callback_data='russia'),
    InlineKeyboardButton(text='Канада🇨🇦', callback_data='kanada'),
    InlineKeyboardButton(text='США🇺🇸', callback_data='USA')],
    [InlineKeyboardButton(text='Китай🇨🇳', callback_data='china'),
    InlineKeyboardButton(text='Бразилия🇧🇷', callback_data='brazil')],
    [InlineKeyboardButton(text='Австралия🇦🇺', callback_data='avstraliya'),
    InlineKeyboardButton(text='Индия🇮🇳', callback_data='indiya'),
    InlineKeyboardButton(text='Аргентина🇦🇷', callback_data='argentina')],
    [InlineKeyboardButton(text='Казахстан🇰🇿', callback_data='kazahstan'),
    InlineKeyboardButton(text='Алжир🇩🇿', callback_data='alshir')]
    
])


ikb1_russia = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Гимн', callback_data='russia_gimn'),
    InlineKeyboardButton(text='столица', callback_data='russia_stol')],
    [InlineKeyboardButton(text='герб', callback_data='russia_gerb')],
    [InlineKeyboardButton(text='Назад⬅', callback_data='left')]
])

ikb1_kanada = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Гимн', callback_data='kanada_gimn'),
    InlineKeyboardButton(text='столица', callback_data='kanada_stol')],
    [InlineKeyboardButton(text='герб', callback_data='kanada_gerb')],
    [InlineKeyboardButton(text='Назад⬅', callback_data='left')]
])

ikb1_USA = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Гимн', callback_data='usa_gimn'),
    InlineKeyboardButton(text='столица', callback_data='usa_stol')],
    [InlineKeyboardButton(text='герб', callback_data='usa_gerb')],
    [InlineKeyboardButton(text='Назад⬅', callback_data='left')]
])

ikb1_China = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Гимн', callback_data='china_gimn'),
    InlineKeyboardButton(text='столица', callback_data='china_stol')],
    [InlineKeyboardButton(text='герб', callback_data='china_gerb')],
    [InlineKeyboardButton(text='Назад⬅', callback_data='left')]
])

ikb1_Brazil = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Гимн', callback_data='braz_gimn'),
    InlineKeyboardButton(text='столица', callback_data='braz_stol')],
    [InlineKeyboardButton(text='герб', callback_data='braz_gerb')],
    [InlineKeyboardButton(text='Назад⬅', callback_data='left')]
])

ikb1_Avstraliya = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Гимн', callback_data='avstr_gimn'),
    InlineKeyboardButton(text='столица', callback_data='avstr_stol')],
    [InlineKeyboardButton(text='герб', callback_data='avstr_gerb')],
    [InlineKeyboardButton(text='Назад⬅', callback_data='left')]
])

ikb1_indiya = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Гимн', callback_data='ind_gimn'),
    InlineKeyboardButton(text='столица', callback_data='ind_stol')],
    [InlineKeyboardButton(text='герб', callback_data='ind_gerb')],
    [InlineKeyboardButton(text='Назад⬅', callback_data='left')]
])

ikb1_argen = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Гимн', callback_data='argen_gimn'),
    InlineKeyboardButton(text='столица', callback_data='argen_stol')],
    [InlineKeyboardButton(text='герб', callback_data='argen_gerb')],
    [InlineKeyboardButton(text='Назад⬅', callback_data='left')]
])

ikb1_kazah = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Гимн', callback_data='kazah_gimn'),
    InlineKeyboardButton(text='столица', callback_data='kazah_stol')],
    [InlineKeyboardButton(text='герб', callback_data='kazah_gerb')],
    [InlineKeyboardButton(text='Назад⬅', callback_data='left')]
])

ikb1_alsh = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Гимн', callback_data='alsh_gimn'),
    InlineKeyboardButton(text='столица', callback_data='alsh_stol')],
    [InlineKeyboardButton(text='герб', callback_data='alsh_gerb')],
    [InlineKeyboardButton(text='Назад⬅', callback_data='left')]
])


ikb1_russia_arr = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад⬅', callback_data='left_rus')]
])

ikb1_kanada_arr = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад⬅', callback_data='left_kan')]
])

ikb1_usa_arr = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад⬅', callback_data='left_us')]
])

ikb1_china_arr = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад⬅', callback_data='left_china')]
])

ikb1_brazil_arr = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад⬅', callback_data='left_braz')]
])

ikb1_avstraliya_arr = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад⬅', callback_data='left_avstr')]
])

ikb1_indiya_arr = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад⬅', callback_data='left_ind')]
])

ikb1_argentina_arr = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад⬅', callback_data='left_arg')]
])

ikb1_kazacstan_arr = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад⬅', callback_data='left_kaz')]
])

ikb1_alshir_arr = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад⬅', callback_data='left_als')]
])