from aiogram import F,Router
from aiogram.filters import CommandStart,Command
from aiogram.types import Message, CallbackQuery


from app.keyboards import ikb1

import app.keyboards as kb

router = Router()



@router.message(Command('help'))
async def cmd_start(message:Message):
    await message.reply('Привет, это бот-справочник, в котором будет информация о некоторых странах, просто введи команду /country и нажми на страну, о которой хочешь узнать!')

@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.reply(f'Привет! Я помогу тебе узнать что-то новое о странах',reply_markup=kb.rb1_reply)

#InLine
@router.message(Command('country'))
async def countrys(message: Message):
    await message.reply('Страны:',
                        reply_markup=kb.ikb1)

#Россия
@router.callback_query(F.data == 'russia')
async def Russia(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Россия - многонациональное государство с широким этнокультурным многообразием[24]. Согласно результатам переписей населения России 2010 года, а также аннексированных Россией украинских Крыма и Севастополя 2014 года, в стране живут представители свыше 190 национальностей, среди которых русские составляют свыше 80 %, а русским языком владеют свыше 99,4 % россиян. Бо́льшая часть населения (около 75 %) в религиозном отношении относит себя к православию, что делает Россию страной с самым многочисленным православным населением в мире', reply_markup=kb.ikb1_russia)

@router.callback_query(F.data == 'russia_gimn')
async def rus_gimn(callback: CallbackQuery):
    await callback.message.edit_text('Россия — священная наша держава,\nРоссия — любимая наша страна.\nМогучая воля, великая слава —\nТвое достояние на все времена!Ссылка на гимн https://www.chitalnya.ru/work/3070043/', reply_markup=kb.ikb1_russia_arr)

@router.callback_query(F.data == 'russia_stol')
async def rus_stol(callback: CallbackQuery):
    await callback.message.edit_text('Москва', reply_markup=kb.ikb1_russia_arr)

@router.callback_query(F.data == 'russia_gerb')
async def rus_gerb(callback: CallbackQuery):
    await callback.message.edit_text('https://pic.rutubelist.ru/video/7f/f2/7ff2fc80672d420e6e4ce2172296c5f1.jpg', reply_markup=kb.ikb1_russia_arr)

@router.callback_query(F.data == 'left')
async def lef_arrow(callback: CallbackQuery):
    await callback.message.edit_text('Страны:', reply_markup=kb.ikb1)

@router.callback_query(F.data == 'left_rus')
async def Russia(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Россия', reply_markup=kb.ikb1_russia)

#Канада

@router.callback_query(F.data == 'kanada')
async def Kanada(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Канада - государство в Северной Америке, крупнейшее по площади на этом континенте и второе в мире. По численности населения 37-е государство в мире (более 41 млн жителей в марте 2024 года). Плотность населения (4,2 чел. на 1 км²) является одной из самых низких в мире. Омывается Атлантическим, Тихим и Северным Ледовитым океанами, имея самую длинную береговую линию в мире (более 202 тыс. км). Граничит с Соединёнными Штатами Америки на юге и на северо-западе (Аляска) и с Данией (остров Ханс) на северо-востоке, имеет морскую границу с Францией (Сен-Пьер и Микелон) на востоке. Граница Канады и США является самой протяжённой общей границей в мире', reply_markup=kb.ikb1_kanada)

@router.callback_query(F.data == 'kanada_stol')
async def rus_stol(callback: CallbackQuery):
    await callback.message.edit_text('Оттава', reply_markup=kb.ikb1_kanada_arr)

@router.callback_query(F.data == 'kanada_gimn')
async def rus_stol(callback: CallbackQuery):
    await callback.message.edit_text('O, Канада! Наш Дом в Родной земле!\nЧистая любовь в сердцах твоих детей.\nhttps://wikiway.com/canada/gimn/',reply_markup=kb.ikb1_kanada_arr)

@router.callback_query(F.data == 'kanada_gerb')
async def rus_stol(callback: CallbackQuery):
    await callback.message.edit_text('https://w7.pngwing.com/pngs/809/405/png-transparent-arms-of-canada-royal-coat-of-arms-of-the-united-kingdom-history-of-canada-canada-canada-maple-leaf-world.png',reply_markup=kb.ikb1_kanada_arr)

@router.callback_query(F.data == 'left_kan')
async def Kanada(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Канада', reply_markup=kb.ikb1_kanada)

#США

@router.callback_query(F.data == 'USA')
async def USA(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('США - государство в Северной Америке. Площадь — 9,8 млн км² (3-е место в мире). Население — чуть более 336 млн человек (2023, оценка, 3-е место в мире). США — федеративная президентская республика, которая административно состоит из 50 штатов и федерального округа Колумбия, а также административно контролирует ряд островных территорий (Пуэрто-Рико, Виргинские Острова, Гуам и другие).', reply_markup=kb.ikb1_USA)

@router.callback_query(F.data == 'usa_gimn')
async def us_gimn(callback: CallbackQuery):
    await callback.message.edit_text('О, скажи, видишь ты в первых солнца лучах,\nЧто средь битвы мы шли на вечерней зарнице?\nhttps://ru.wikipedia.org/wiki/%D0%93%D0%B8%D0%BC%D0%BD_%D0%A1%D0%A8%D0%90',reply_markup=kb.ikb1_usa_arr)

@router.callback_query(F.data == 'usa_stol')
async def us_stol(callback: CallbackQuery):
    await callback.message.edit_text('Вашингтон',reply_markup=kb.ikb1_usa_arr)

@router.callback_query(F.data == 'usa_gerb')
async def us_gerb(callback: CallbackQuery):
    await callback.message.edit_text('https://e7.pngegg.com/pngimages/567/289/png-clipart-usa-gerb-usa-gerb.png',reply_markup=kb.ikb1_usa_arr)

@router.callback_query(F.data == 'left_us')
async def USA(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('США', reply_markup=kb.ikb1_USA)

#Китай

@router.callback_query(F.data == 'china')
async def USA(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Китай — государство в Восточной Азии. Занимает 4-е место в мире по территории среди государств (9 598 962 км2), уступая России, Канаде и США, а по численности населения — 1 411 750 000 жителей (без Тайваня, Гонконга и Макао) — второе после Индии. Уровень урбанизации равен 65 %. Большинство населения — этнические китайцы, самоназвание — хань.', reply_markup=kb.ikb1_China)

@router.callback_query(F.data == 'china_gimn')
async def us_gimn(callback: CallbackQuery):
    await callback.message.edit_text('Вставай, кто рабом стать не желает!\nИз своей плоти Великую стену поставим!\nhttps://discoveric.ru/anthem/kitay',reply_markup=kb.ikb1_china_arr)

@router.callback_query(F.data == 'china_stol')
async def us_stol(callback: CallbackQuery):
    await callback.message.edit_text('Пекин',reply_markup=kb.ikb1_china_arr)

@router.callback_query(F.data == 'china_gerb')
async def us_gerb(callback: CallbackQuery):
    await callback.message.edit_text('https://www.okaytravel.ru/wp-content/uploads/2023/07/gerb-kitaja.jpg',reply_markup=kb.ikb1_china_arr)

@router.callback_query(F.data == 'left_china')
async def USA(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Китай', reply_markup=kb.ikb1_China)


#Бразилия

@router.callback_query(F.data == 'brazil')
async def USA(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Бразилия — суверенное государство в Южной Америке. Площадь — 8 515 767 км² (эквивалентна 47,3 % южноамериканской территории). Будучи пятой среди стран мира по площади и седьмой по численности населения (с более чем 218 млн жителей), Бразилия является крупнейшей страной Южной Америки и Латинской Америки как по территории, так и по численности населения. Единственная португалоязычная страна во всей Америке, а также крупнейшая лузофонная страна в мире.', reply_markup=kb.ikb1_Brazil)

@router.callback_query(F.data == 'braz_gimn')
async def us_gimn(callback: CallbackQuery):
    await callback.message.edit_text('Услышали Ипиранги-реки тихие берега\nГромоподобный клич героического народа\nhttps://ru.wikipedia.org/wiki/%D0%93%D0%B8%D0%BC%D0%BD_%D0%91%D1%80%D0%B0%D0%B7%D0%B8%D0%BB%D0%B8%D0%B8',reply_markup=kb.ikb1_brazil_arr)

@router.callback_query(F.data == 'braz_stol')
async def us_stol(callback: CallbackQuery):
    await callback.message.edit_text('Бразилиа',reply_markup=kb.ikb1_brazil_arr)

@router.callback_query(F.data == 'braz_gerb')
async def us_gerb(callback: CallbackQuery):
    await callback.message.edit_text('https://w7.pngwing.com/pngs/27/485/png-transparent-empire-of-brazil-coat-of-arms-of-brazil-coat-of-arms-of-australia-brazil-rio-decorative-elements-flag-leaf-decorative.png',reply_markup=kb.ikb1_brazil_arr)

@router.callback_query(F.data == 'left_braz')
async def USA(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Бразилия', reply_markup=kb.ikb1_Brazil)


#Австралия

@router.callback_query(F.data == 'avstraliya')
async def USA(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Австралия - одна из самых развитых стран мира, будучи четырнадцатой по размеру экономикой в мире, и имеет девятое место в мире по ВВП в расчёте на душу населения. Военные расходы Австралии являются двенадцатыми по размеру в мире. С пятым по величине индексом человеческого развития Австралия занимает высокое место во многих сферах, таких как качество жизни, здоровье, образование, экономическая свобода, защита гражданских свобод и политических прав. Австралия является членом G20, ОЭСР, ВТО, АТЭС, ООН, Содружества наций, АНЗЮСа, АУКУСа и Форума тихоокеанских островов.', reply_markup=kb.ikb1_Avstraliya)

@router.callback_query(F.data == 'avstr_gimn')
async def us_gimn(callback: CallbackQuery):
    await callback.message.edit_text('Австралийцы, всё к счастью для нас\nЗдесь, где юность с свободой цветут.\nhttps://discoveric.ru/anthem/avstraliya',reply_markup=kb.ikb1_avstraliya_arr)

@router.callback_query(F.data == 'avstr_stol')
async def us_stol(callback: CallbackQuery):
    await callback.message.edit_text('Канберра',reply_markup=kb.ikb1_avstraliya_arr)

@router.callback_query(F.data == 'avstr_gerb')
async def us_gerb(callback: CallbackQuery):
    await callback.message.edit_text('https://abali.ru/wp-content/uploads/2010/12/gerb_australia.png',reply_markup=kb.ikb1_avstraliya_arr)

@router.callback_query(F.data == 'left_avstr')
async def USA(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Австралия', reply_markup=kb.ikb1_Avstraliya)


#Индия

@router.callback_query(F.data == 'indiya')
async def USA(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Индия — независимое государство в Южной Азии. Население на начало 2023 года составило 1,41 миллиарда человек, территория — 3 287 263 км², по обоим этим показателям является крупнейшей страной Южной Азии. Занимает первое место в мире по численности населения и седьмое по территории. Наравне с Египтом и Китаем является родиной одной из древнейших цивилизаций в истории человечества. В прошлом — одна из важнейших колониальных провинций Британской империи.', reply_markup=kb.ikb1_indiya)

@router.callback_query(F.data == 'ind_gimn')
async def us_gimn(callback: CallbackQuery):
    await callback.message.edit_text('Слава тебе — властителю дум всех народов,\nВершителю судьбы Индии\nhttps://discoveric.ru/anthem/indiya',reply_markup=kb.ikb1_indiya_arr)

@router.callback_query(F.data == 'ind_stol')
async def us_stol(callback: CallbackQuery):
    await callback.message.edit_text('Нью-Дели',reply_markup=kb.ikb1_indiya_arr)

@router.callback_query(F.data == 'ind_gerb')
async def us_gerb(callback: CallbackQuery):
    await callback.message.edit_text('https://bumper-stickers.ru/54997-thickbox_default/gerb-emblema-indii.jpg',reply_markup=kb.ikb1_indiya_arr)

@router.callback_query(F.data == 'left_ind')
async def USA(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Индия', reply_markup=kb.ikb1_indiya)


#Аргентина

@router.callback_query(F.data == 'argentina')
async def USA(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Аргентина — второе после Бразилии по территории и третье после Бразилии и Колумбии по населению государство Южной Америки, состоящее из 24 административных единиц: 23 провинций и федерального столичного округа Буэнос-Айрес. Крупнейшая по площади в мире из испаноязычных стран. По состоянию на 2023 год, по оценкам всемирной книги фактов ЦРУ, по численности населения Аргентина 33-е государство в мире (46 621 847 человек). Состав населения Аргентины по вероисповеданию по состоянию на 2022 год: католики — 48,9 %, другие христиане — 10 %, нерелигиозны — 39,8 %, верующие в другую религию или конфессию — 1,3 %.', reply_markup=kb.ikb1_argen)

@router.callback_query(F.data == 'argen_gimn')
async def us_gimn(callback: CallbackQuery):
    await callback.message.edit_text('Слушайте смертные! Крики священные:\nСвобода, Свобода, Свобода!\nhttps://discoveric.ru/anthem/argentina',reply_markup=kb.ikb1_argentina_arr)

@router.callback_query(F.data == 'argen_stol')
async def us_stol(callback: CallbackQuery):
    await callback.message.edit_text('Буэнос-Айрес',reply_markup=kb.ikb1_argentina_arr)

@router.callback_query(F.data == 'argen_gerb')
async def us_gerb(callback: CallbackQuery):
    await callback.message.edit_text('https://bellville.gob.ar/wp-content/uploads/2019/03/Escudo-Nacional.jpg',reply_markup=kb.ikb1_argentina_arr)

@router.callback_query(F.data == 'left_arg')
async def USA(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Аргентина', reply_markup=kb.ikb1_argen)


#Казахстан

@router.callback_query(F.data == 'kazahstan')
async def USA(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Казахстан — государство в Центральной Азии и в Восточной Европе. Население — 20 млн чел. (2023), площадь территории — 2 724 902 км² (занимает 9-е место в мире по территории и 62-е по численности населения). Казахстан — многонациональное государство с широким этнокультурным, языковым, религиозным, расовым и национальным многообразием. Конституция Республики Казахстан провозглашает страну демократическим, светским, унитарным государством с президентской формой правления', reply_markup=kb.ikb1_kazah)

@router.callback_query(F.data == 'kazah_gimn')
async def us_gimn(callback: CallbackQuery):
    await callback.message.edit_text(' В её небе золотое солнце,\nВ её степях золотое зерно.\nhttps://discoveric.ru/anthem/kazahstan',reply_markup=kb.ikb1_kazacstan_arr)

@router.callback_query(F.data == 'kazah_stol')
async def us_stol(callback: CallbackQuery):
    await callback.message.edit_text('Нур-Султан',reply_markup=kb.ikb1_kazacstan_arr)

@router.callback_query(F.data == 'kazah_gerb')
async def us_gerb(callback: CallbackQuery):
    await callback.message.edit_text('https://img.razrisyika.ru/kart/63/1200/248388-gerb-kazahstana-33.jpg',reply_markup=kb.ikb1_kazacstan_arr)

@router.callback_query(F.data == 'left_kaz')
async def USA(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Казахстан', reply_markup=kb.ikb1_kazah)


#Алжир


@router.callback_query(F.data == 'alshir')
async def USA(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Алжир — государство в Северной Африке в западной части Средиземноморского бассейна, крупнейшее по территории африканское государство. Площадь составляет 2 381 741 км², что чуть больше, чем у Демократической Республики Конго (2-е место по площади на континенте). Алжир граничит с Марокко на западе, Мавританией и Мали — на юго-западе, Нигером — на юго-востоке и Ливией и Тунисом — на востоке. Бо́льшая часть территории страны лежит в пустыне Сахара.', reply_markup=kb.ikb1_alsh)

@router.callback_query(F.data == 'alsh_gimn')
async def us_gimn(callback: CallbackQuery):
    await callback.message.edit_text('Мы клянемся! Опустошительными бурями, охватившими нас\nЩедро пролитой благородной, чистой кровью\nhttps://discoveric.ru/anthem/alzhir',reply_markup=kb.ikb1_alshir_arr)

@router.callback_query(F.data == 'alsh_stol')
async def us_stol(callback: CallbackQuery):
    await callback.message.edit_text('Алжир',reply_markup=kb.ikb1_alshir_arr)

@router.callback_query(F.data == 'alsh_gerb')
async def us_gerb(callback: CallbackQuery):
    await callback.message.edit_text('https://w7.pngwing.com/pngs/451/446/png-transparent-algeria-coat-of-arms-heraldry.png',reply_markup=kb.ikb1_alshir_arr)

@router.callback_query(F.data == 'left_als')
async def USA(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Алжир', reply_markup=kb.ikb1_alsh)





















