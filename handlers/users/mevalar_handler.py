# from aiogram import types
# from keyboards.inline.product_keyboard import Menu,sotish, mevalar 
# from loader import dp


# @dp.callback_query_handler(text="Mevalar")
# async def menyu(call: types.CallbackQuery):
#     await call.message.delete()
#     photo = open("photos/mevalar.jpg", "rb")
#     await call.message.answer_photo(photo=photo, reply_markup=mevalar)

# @dp.callback_query_handler(text="Olma")
# async def olma_handler(call: types.CallbackQuery):
#     await call.message.delete()
#     photo = open("photos/olma.jpg","rb")
#     msg = """
#     <b>Olma</b> (lotincha: Malus) — raʼnodoshlar oilasiga mansub, barg toʻkuvchi daraxtlar yoki butalar turkumi; urugʻli meva daraxti. Shimoliy va janubiy yarim sharning moʻtadil mintaqalarida olmaning 25— 30 turi, jumladan, Sharqiy Osiyo, Oʻrta Osiyo va Kavkazda 10 xil turi tarqalgan. Ekiladigan mevali daraxtlar orasida maydoni jihatidan birinchi oʻrinda turadi.
#     """
#     # await call.message.answer("<b>Olma:</b>",reply_markup=ReplyKeyboardRemove())
#     await call.message.answer_photo(photo=photo, caption=msg, reply_markup=sotish)

# # @dp.callback_query_handler(text="sotishortga")
# # async def sotish_handler(call: types.CallbackQuery):
# #     await call.message.delete()
# #     photo = open("photos/mevalar.jpg", "rb")
# #     await call.message.answer_photo(photo=photo, reply_markup=mevalar)

# @dp.callback_query_handler(text="Banan")
# async def banan_handler(call: types.CallbackQuery):
#     await call.message.delete()
#     photo = open("photos/banan.jpg", "rb")
#     msg = """
#     <b>Banan</b> (Musa) – banansimonlar oilasiga mansub koʻp yillik tropik oʻsimlik. Vatani Afrika va Osiyoning tropik va subtropik zonalari hamda Malayya arxipelagi. Asosan, Lotin Amerikasi mamlakatlarida oʻstiriladi. Bananning boʻyi 15 m gacha boradi, bargi yirik (uzunligi 4 m gacha, eni 90 sm gacha). Bananning 40 ga yaqin turi bor. Guli qoʻsh jinsli. 
#     """
#     # await call.message.answer("<b>Banan:</b>",reply_markup=ReplyKeyboardRemove())
#     await call.message.answer_photo(photo=photo, caption=msg, reply_markup=sotish)

# @dp.callback_query_handler(text="Anans")
# async def ananas_handeler(call: types.CallbackQuery):
#     await call.message.delete()
#     photo = open("photos/ananas.jpg", "rb")
#     msg = """
#     <b>Ananas</b> (Ananas) – ananasdoshlar (Bromeliaceae) oilasiga mansub oʻtlar turkumi (urugʻi). 5 – 6 turi maʼlum. Asosan, Amerika qitʼasining tropik hududlarida va Osiyoning Filippin, Tayvan orollarida oʻsadi. Barglari qalin, uzun, xanjarsimon. Ekiladigan ananas (Sativus) Amerika va Tayvandan boshqa joylarda ham oʻsadi. Bu toʻrning mevasi qubba shaklidagi toʻp mevadan iborat, ogʻirligi 2 – 5 kg, tusi sargʻish, xushxoʻr. Hoʻl meva yoki konserva holida isteʼmol qilinadi. Baʼzi turlarining barglaridan ipaksimon nozik tolalar ham olinadi.
#     """
#     # await call.message.answer("<b>Ananas:</b>",reply_markup=ReplyKeyboardRemove())
#     await call.message.answer_photo(photo=photo, caption=msg, reply_markup=sotish)

# @dp.callback_query_handler(text="Olcha")
# async def olcha_handeler(call: types.CallbackQuery):
#     await call.message.delete()
#     photo = open("photos/olcha.jpg", "rb")
#     msg = """
#     <b>Olcha</b> (Cerasus) — raʼnodoshlar oilasiga mansub barg toʻkuvchi daraxtlar turkumi; mevali daraxt, 150 ga yaqin turi bor. Asosan, Osiyoda, shu jumladan, Oʻrta Osiyo va Kavkazda 25 ga yaqin turi usadi. Madaniy turlaridan oddiy O. (C.vulgaris) koʻp tarqalgan. Juda qadimdan Markaziy va Jan. Yevropada, Shim. Afrika, Sharq-iy Osiyo, Shim. Amerikada ekiladi.
#     """
#     # await call.message.answer("<b>Olcha:</b>",reply_markup=ReplyKeyboardRemove())
#     await call.message.answer_photo(photo=photo, caption=msg, reply_markup=sotish)

# @dp.callback_query_handler(text="Malina")
# async def malina_handeler(call: types.CallbackQuery):
#     await call.message.delete()
#     photo = open("photos/malina.jpg", "rb")
#     msg = """
#     <b>Malina</b>, xo'jag'at, buldurgʻun (Rubus) — raʼnoguldoshlar oilasi rubus turkumiga mansub koʻp yillik chala butalar; rezavor meva. Malinaning 120 yovvoyi turi boʻlib, Yevrosiyoning moʻʼtadil va subtropik mintaqalarida keng tarqalgan. Malinaning madaniy navlari oddiy yoki qizil (Rubus idaeus), dagʻal tukli yoki amerika Malinasi (Rubus strigosus), gʻarbiy yoki maymunjonsimon Malina (Rubus occidentalis) va boshqa turlari uchraydi
#     """
#     # await call.message.answer("<b>Malina:</b>",reply_markup=ReplyKeyboardRemove())
#     await call.message.answer_photo(photo=photo, caption=msg, reply_markup=sotish)

# @dp.callback_query_handler(text="Maymunjon")
# async def maymunjon_handeler(call: types.CallbackQuery):
#     await call.message.delete()
#     photo = open("photos/maymunjon.jpg", "rb")
#     msg = """
#     <b>Maymunjon</b> — raʼnoguldoshlar oilasiga mansub koʻp yillik buta; rezavor meva. Shim. Amerika, Yevrosiyoda 400 dan ortiq turi uchraydi. Shulardan 90 turi, asosan, koʻk M. (Rubus caesius) va mayda mevali M. (R. nensensis) turlari Kavkaz, Ukrainaning janubi va Oʻrta Osiyoda uchraydi. Amerika, Markaziy va Gʻarbiy Yevropada koʻp ekiladi. Oʻzbekistonning togʻ oldi mintaqalarida oʻsadi va dala, tomorqa-bogʻlarda oʻstiriladi. Yer ustki qismi ikki yillik novdalardan iborat. Barglari patsimon. Bir yillik novdasi hosil tugadi. Gullari ikki jinsli, oq, baʼzan pushti boʻlib, shingilsimon toʻpgulda joylashgan.
#     """
#     # await call.message.answer("<b>Maymunjon:</b>",reply_markup=ReplyKeyboardRemove())
#     await call.message.answer_photo(photo=photo, caption=msg, reply_markup=sotish)

# @dp.callback_query_handler(text="Apelsin")
# async def apelsin_handeler(call: types.CallbackQuery):
#     await call.message.delete()
#     photo = open("photos/apelsin.jpg", "rb")
#     msg = """
#     <b>Apelsin</b>, poʻrtaxol (Citrus sinensis — gollandcha appelsien — aynan xitoy olmasi) — rutadoshlar (apel-singullilar oilasi)ning sitruslar turkumiga mansub doim yashil daraxt va buta. Vatani — Birma va Janubi-Gʻarbiy Xitoy. Yovvoyi holda uchramaydi. Tropik va subtropik mamlakatlarda qadimdan madaniylashtirilgan (Xitoyda 2 ming yildan beri, Janubiy Yevropada 15-asrdan, Kavkazning Qora dengiz buylarida 11-asrdan). Boʻyi 6 — 12 m. Shox va novdalarida ingichka tikanlari bor.
#     """
#     # await call.message.answer("<b>Apelsin:</b>",reply_markup=ReplyKeyboardRemove())
#     await call.message.answer_photo(photo=photo, caption=msg, reply_markup=sotish)

# @dp.callback_query_handler(text="Xurmo")
# async def xurmo_handeler(call: types.CallbackQuery):
#     await call.message.delete()
#     photo = open("photos/xurmo.jpg", "rb")
#     msg = """
#     <b>Xurmo</b> (Diospyros) — xurmodoshlar oilasiga mansub subtropik daraxt yoki butalar turkumi, ekiladigan meva daraxti. Tropik va subtropik mintaqalarda 500 ga yaqin turi uchraydi. Xitoy, Yaponiya, Oʻrta dengiz boʻyi mamlakatlari, Avstraliya, AQSH, Kavkaz, Oʻrta Osiyoda ekiladi. Mevasi uchun, asosan, sharq X., sovuqqa chidamli virginiya X.si (D. virginiana), shuningdek, Kavkaz X.si (D. lotus) oʻstiriladi. Oʻzbekistonda ekiladigan sharq X.si (D. kaki Tpip.)ning vatani — Xitoy.
#     """
#     # await call.message.answer("<b>Xurmo:</b>",reply_markup=ReplyKeyboardRemove())
#     await call.message.answer_photo(photo=photo, caption=msg, reply_markup=sotish)

# @dp.callback_query_handler(text="Qulupnay")
# async def qulupnay_handeler(call: types.CallbackQuery):
#     await call.message.delete()
#     photo = open("photos/qulupnay.jpg", "rb")
#     msg = """
#     <b>Qulupnay</b>, yertut – raʼnoguldoshlar oilasiga mansub koʻp yillik oʻtsimon oʻsimliklar turkumi; rezavor ekin.Yevrosiyo va Amerikada 50 turi maʼlum. Asosan „bogʻ qulupnayi“ turi, shuningdek, „oʻrmon qulupnayi“, „muskat taʼmli qulupnay“, „virginiya qulupnayi“ va „chili qulupnay“ kabi qulupnayning birinchi navlari 18-asr da Niderlandiyada paydo boʻlgan. Amerika turi – virginiya va chili qulupnayi Yevropaga olib kelingan. Qulupnay Yer sharining turli iqlimli mintaqalarida – Qutb doirasidan to subtropiklargacha oʻstiriladi.
#     """
#     # await call.message.answer("<b>Qulupnay:</b>",reply_markup=ReplyKeyboardRemove())
#     await call.message.answer_photo(photo=photo, caption=msg, reply_markup=sotish)

# @dp.callback_query_handler(text="Anjir")
# async def anjir_handeler(call: types.CallbackQuery):
#     await call.message.delete()
#     photo = open("photos/anjir.jpg", "rb")
#     msg = """
#     <b>Anjir</b> (Ficus carica L.) — tutdoshlar (anjirgullilar) oilasiga mansub subtropik meva turi. Turkiya, Jazoir, Yevropaning janubida, AQShda katta may-donlarni egallaydi, Kavkaz, Oʻrta Osiyo, Qrimda ham yetishtiriladi. Yovvoyi holda Oʻrta dengiz boʻyi, Kichik Osiyo, Eron, Shimoli-gʻarbiy Hindistonda oʻsadi. A. juda qadimdan madaniylashtirilgan oʻsimlik hisoblanadi (Osiyoda 5 ming yildan, Yevropada kamida 2 ming yildan beri).
#     """
#     # await call.message.answer("<b>Anjir:</b>",reply_markup=ReplyKeyboardRemove())
#     await call.message.answer_photo(photo=photo, caption=msg, reply_markup=sotish)

# @dp.callback_query_handler(text="Anor")
# async def anor_handeler(call: types.CallbackQuery):
#     await call.message.delete()
#     photo = open("photos/anor.jpg", "rb")
#     msg = """
#     <b>Oddiy anor</b> ( lotincha: Púnica granátum) — derbenlar oilasiga  (Lythraceae) turkumiga mansub o‘simlik turi, mevasi iste’molga yaroqli. Anor mevalarini ozuqa mevasi sifatida xom holda, tayyor ovqatga solishda, shuningdek, sharbatini olib, ichimlik sifatida foydalanish mumkin. Shimoliy yarimsharda anor mavsumi odatda sentabrdan fevralgacha, janubiy yarimsharda — martdan maygacha davom etadi.
#     """
#     # await call.message.answer("<b>Anor:</b>",reply_markup=ReplyKeyboardRemove())
#     await call.message.answer_photo(photo=photo, caption=msg, reply_markup=sotish)

# @dp.callback_query_handler(text="Bexi")
# async def bexi_handeler(call: types.CallbackQuery):
#     await call.message.delete()
#     photo = open("photos/bexi.jpg", "rb")
#     msg = """
#     <b>Behi</b> (Cydonia oblonga Mill.) — raʼnodoshlar oilasiga mansub mevali daraxt yoki buta. Behining Ozarbayjon, Dogʻiston, Turkmaniston, Eronda yovvoyi turlari uchraydi, turk tilida ayva nomi bilan yuritilgan. Mahmud Koshgʻariyning "Devonu lugʻotit turk" asarida "avya" shaklida tilga olingan. Behi Kavkaz, Oʻrta Osiyo, Qrim, Ukrainaning jan. hamda Astraxon viloyatida keng tarqalgan. Oʻzbekistondagi Behizorlarning 80%/ Fargʻona vodiysida.
#     """
#     # await message.answer("<b>Bexi:</b>",reply_markup=ReplyKeyboardRemove())
#     await call.message.answer_photo(photo=photo, caption=msg, reply_markup=sotish)

# @dp.callback_query_handler(text="Gilos")
# async def gilos_handeler(call: types.CallbackQuery):
#     await call.message.delete()
#     photo = open("photos/gilos.jpg", "rb")
#     msg = """
#     <b>Gilos</b> (lotincha: Prúnus ávium)(forscha: گیلاس — gilos) —  atirgullilar oilasiga mansub koʻpyillik mevali daraxt va uning mevasi. Sariq gilos. Qizil Yovvoyi holda Oʻrta va Janubiy Yevropa, Eron, Kavkaz, Ukraina, Moldovada uchraydi. Yevropa mamlakatlari, Turkiya, Eron, Afgʻoniston, Xitoy, Yaponiya, Ukrainaning janubi, Kavkaz, Boltiqboʻyi va Oʻrta Osiyoda ekiladi.
#     """
#     # await message.answer("<b>Gilos:</b>",reply_markup=ReplyKeyboardRemove())
#     await call.message.answer_photo(photo=photo, caption=msg, reply_markup=sotish)

# @dp.callback_query_handler(text="Kivi")
# async def kivi_handeler(call: types.CallbackQuery):
#     await call.message.delete()
#     photo = open("photos/kivi.jpg", "rb")
#     msg = """
#     Kivi- (Maymun shaftoli) o'simligining vatani Xitoy hisoblanadi. Kivi mevasi katta uzumga o'xshash mevadir, shuning uchun kivi baʼzan „Xitoy krijovnigi“ deb ataladi. 2017-yilda Xitoy dunyodagi kivi mevasining 50%\ini ishlab chiqargan.
#     """
#     # await message.answer("<b>Kivi:</b>",reply_markup=ReplyKeyboardRemove())
#     await call.message.answer_photo(photo=photo, caption=msg, reply_markup=sotish)

# @dp.callback_query_handler(text="Limon")
# async def limon_handeler(call: types.CallbackQuery):
#     await call.message.delete()
#     photo = open("photos/limon.jpg", "rb")
#     msg = """
#     <b>Limon</b> - Daraxtning sariq mevasi butun dunyoda, birinchi navbatda uning sharbati uchun ishlatiladi. Pulpa va qobiq pishirish va pishirishda ishlatiladi. Limon sharbati taxminan 5-6%/ limon kislotasidan iborat bo'lib, unga nordon ta'm beradi. Bu uni ichimliklar va limonad va limonli beze pirogi kabi oziq-ovqat mahsulotlarining asosiy tarkibiy qismiga aylantiradi. Mevalar san'atda qadimgi Misr davridan beri paydo bo'lgan.
#     """
#     # await message.answer("<b>Limon:</b>",reply_markup=ReplyKeyboardRemove())
#     await call.message.answer_photo(photo=photo, caption=msg, reply_markup=sotish)

# @dp.callback_query_handler(text="Mandarin")
# async def mandarin_handeler(call: types.CallbackQuery):
#     await call.message.delete()
#     photo = open("photos/mandarin.jpg", "rb")
#     msg = """
#     <b>Mandarin</b> so'zi rus tiliga ispan tilidan (ehtimol frantsuz tili orqali) olingan. Ispancha mandarin portugal tiliga qaytadi mandarim (ma'nosida gu guānlì "amaldorlar"), bu o'z navbatida qadimgi hind tiliga qaytadi mantrī (mantrín-) — "maslahatchi, vazir".
#     Rus tiliga "mandarin" so'zi "meva" ma'nosida frantsuz tilidan (mandarinier), "mansabdor shaxs" ma'nosida esa portugal tilidan nemis (Mandarin) orqali kelgan.
#     """
#     # await message.answer("<b>Mandarin:</b>",reply_markup=ReplyKeyboardRemove())
#     await call.message.answer_photo(photo=photo, caption=msg, reply_markup=sotish)

# @dp.callback_query_handler(text="Nok")
# async def nok_handeler(call: types.CallbackQuery):
#     await call.message.delete()
#     photo = open("photos/nok.jpg", "rb")
#     msg = """
#     <b>Nok, nashvati, olmurut</b> (lotincha: Pýrus) — Atirguldoshlar (Rosaceae) oilasiga mansub mevali va manzarali daraxt va butalar turi.Yevropada nok yovvoyi koʻrinishda taxminan 60° shahri k.da tarqalgan. Arealning shimoliy chegarasida - siyrak.
#     2006-yilda sovuqqa chidamli navlarini muvaffaqiyatli seleksiya qilish natijasida nok Ural va Gʻarbiy Sibirda 55° shahri k.gacha joylashgan bogʻ maydonlarida samarali oʻstirilmoqda.
#     """
#     # await message.answer("<b>Nok:</b>",reply_markup=ReplyKeyboardRemove())
#     await call.message.answer_photo(photo=photo, caption=msg, reply_markup=sotish)

# @dp.callback_query_handler(text="Mango")
# async def mango_handeler(call: types.CallbackQuery):
#     await call.message.delete()
#     photo = open("photos/mango.jpg", "rb")
#     msg = """
#     <b>Mango</b>-Anakardiya (sumak) oilasining Mango (Mangifera) jinsidagi o'simliklarning mevalari.
#     Hind mangosining mevalari
#     Mango-xushbo'y Mango (chapda) va xushbo'y Mango (o'ngda)ning qutulish mumkin bo'lgan mevalari
#     Hind mangosining turi (Mangifera indica) katta qishloq xo'jaligi ahamiyatiga ega. 2009 yilda butun dunyo bo'ylab qishloq xo'jaligida ushbu turning 300 dan ortiq navlari etishtirildi. (1969 yilga kelib 200 ga yaqin navlari ma'lum edi.) Ushbu turdagi Mangoning eng yirik eksportchilaridan biri bu Hindiston. Hind mangosining mevalari tolali tuzilishga va shirin ta'mga ega, qobig'i qizil, yashil yoki sariq ranglarda bo'yalgan, go'shti sariq yoki to'q sariq rangga ega
#     """
#     # await message.answer("<b>Mango:</b>",reply_markup=ReplyKeyboardRemove())
#     await call.message.answer_photo(photo=photo, caption=msg, reply_markup=sotish)

# @dp.callback_query_handler(text="Shaftoli")
# async def shaftoli_handeler(call: types.CallbackQuery):
#     await call.message.delete()
#     photo = open("photos/shaftoli.jpg", "rb")
#     msg = """
#     <b>Shaftoli</b> (Persica) — raʼnodoshlar oilasiga mansub bo‘lgan mevali daraxt; Vatani — Oʻrta Osiyo.
#     AQSH, Yevropaning janubi, Yaponiya, Xitoy, Turkiya, Oʻrta Osiyo, Kavkazortida keng tarqalgan. Bundan 2 ming yil oldin madaniylashtirilgan. 5000 ga yaqin navi bor. Hozirgi davrda Shimoliy va Janubiy yarim sharning barcha subtropik va tropik mamlakatlarida oʻstiriladi. Jahon boʻyicha yalpi hosili 12,0 mln. tonna (1999-yil). Oʻzbekistonda ekin maydoni jihatidan mevali daraxtlar orasida 3-oʻrinni egallaydi.
#     """
#     # await message.answer("<b>Shaftoli:</b>",reply_markup=ReplyKeyboardRemove())
#     await call.message.answer_photo(photo=photo, caption=msg, reply_markup=sotish)

# @dp.callback_query_handler(text="Uzum")
# async def uzum_handeler(call: types.CallbackQuery):
#     await call.message.delete()
#     photo = open("photos/uzum.jpg", "rb")
#     msg = """
#     Uzum tokning gʻujumlardan iborat mevasidir. Botanik jihatdan rezavor meva hisoblanadi.
#     Uzumni vino, murabbo, uzum sharbati, jele, uzum urugʻi ekstrakti, sirka va uzum urugʻi yogʻi kabilarni tayyorlashda ishlatish yoki quritib, mayiz hosil qilish mumkin. Uzum noklimakterik turdagi meva hisoblanadi.
#     Xom uzum tarkibida 81%/ suv, 18%/ uglevodlar, 1% protein va oz miqdorda yogʻ boʻladi.
#     """
#     # await message.answer("<b>Uzum:</b>",reply_markup=ReplyKeyboardRemove())
#     await call.message.answer_photo(photo=photo, caption=msg, reply_markup=sotish)

# @dp.callback_query_handler(text="mevalar_ortga")
# async def mevalar_ortga(call: types.CallbackQuery):
#     await call.message.delete()
#     photo = open("photos/mevalar.jpg", "rb")
#     # await message.answer("<b>Siz ortga qaydingiz!</b>",reply_markup=ReplyKeyboardRemove())
#     await call.message.answer_photo(photo=photo,reply_markup=Menu)



# @dp.callback_query_handler(lambda call: call.data == "sotishortga")
# async def buy_product(call: types.CallbackQuery):
#     await call.message.delete()
#     photo = open("photos/mevalar.jpg", "rb")
#     await call.message.answer_photo(photo=photo, reply_markup=mevalar)
#     # await call.message.answer("Mahsulot sotib olish jarayoni boshlandi.", reply_markup=quantity_selection)

# @dp.callback_query_handler(lambda call: call.data == "-")
# async def decrease_quantity(call: types.CallbackQuery):
#     await call.message.answer("Mahsulot miqdori kamaytirildi.")

# # @dp.callback_query_handler(lambda call: call.data == "+")
# # async def increase_quantity(call: types.CallbackQuery):
# #     await call.message.answer("Mahsulot miqdori oshirildi.")

# @dp.callback_query_handler(lambda call: call.data == "add_to_cart")
# async def add_to_cart(call: types.CallbackQuery):
#     await call.message.answer("Mahsulot savatga qo'shildi.")
