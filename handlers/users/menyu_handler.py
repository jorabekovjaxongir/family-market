from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import   Message
from keyboards.default.startKeyboard import phone_keyboard
from keyboards.default.menyu_keyboards import main_menu,location_keyboard
from keyboards.inline.product_keyboard import  Menu,Olma,buyurtmalar,Banan,Ananas,Olcha,Malina,Maymunjon,Apelsin,Xurmo,Qulupnay,Anjir,Anor,Bexi,Gilos,Kivi,Limon,Mandarin,Nok,Mango,Shaftoli,Uzum,Kartoshka,Piyoz,Chesnok,Sabzi,Pomidor,Bodring,Karam,Brokoli,Joxori,Qovoq,Turup,Kok_piyoz,Kashnich,Gulkaram,Qoziqorin,Tarvuz,Qovun,Lovlagi,Baqlajon,Bulgor_qalampir
from states.buyurtma import OrderState

#buyurtma
from loader import dp, bot

user_purchases = {}
m = None

@dp.message_handler(text="Mahsulotlar🛍")
async def shw_menu(message: Message):
    photo = open("photos/community-fridge.png","rb")
    await message.answer("🛍 Mahsulotlarni tanlang:",reply_markup=Menu)
    # await message.answer_photo(photo=photo, reply_markup=Menu)

@dp.callback_query_handler(text="Menuortga")
async def menyu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Menyuga qaytingiz:", reply_markup=main_menu)

@dp.callback_query_handler(text="Mevalar")
async def menyu(call: types.CallbackQuery):
    await call.message.delete()
    
    # Mevalarni ko'rsatish
    fruits = [
        ("photos/olma.jpg", "Olma 🍏  <b>5,000</b> so'm/kg", Olma),
        ("photos/banan.jpg", "Banan 🍌  <b>6,000</b> so'm/kg", Banan),
        ("photos/ananas.jpg", "Ananas 🍍  <b>7,000</b> so'm/kg", Ananas),
        ("photos/olcha.jpg", "Olcha 🍐  <b>8,000</b> so'm/kg", Olcha),
        ("photos/malina.jpg", "Malina 🍇  <b>9,000</b> so'm/kg", Malina),
        ("photos/maymunjon.jpg", "Maymunjon 🍊  <b>10,000</b> so'm/kg", Maymunjon),
        ("photos/apelsin.jpg", "Apelsin 🍊  <b>5,500</b> so'm/kg", Apelsin),
        ("photos/xurmo.jpg", "Xurmo 🌰  <b>6,500</b> so'm/kg", Xurmo),
        ("photos/qulupnay.jpg", "Qulupnay 🍓  <b>8,000</b> so'm/kg", Qulupnay),
        ("photos/anjir.jpg", "Anjir 🍐  <b>9,500</b> so'm/kg", Anjir),
        ("photos/anor.jpg", "Anor 🍏  <b>10,500</b> so'm/kg", Anor),
        ("photos/bexi.jpg", "Bexi 🍈  <b>7,000</b> so'm/kg", Bexi),
        ("photos/gilos.jpg", "Gilos 🍒  <b>11,000</b> so'm/kg", Gilos),
        ("photos/kivi.jpg", "Kivi 🥝  <b>12,000</b> so'm/kg", Kivi),
        ("photos/limon.jpg", "Limon 🍋  <b>6,000</b> so'm/kg", Limon),
        ("photos/mandarin.jpg", "Mandarin 🍊  <b>5,800</b> so'm/kg", Mandarin),
        ("photos/nok.jpg", "Nok 🍐  <b>7,500</b> so'm/kg", Nok),
        ("photos/mango.jpg", "Mango 🥭  <b>14,000</b> so'm/kg", Mango),
        ("photos/shaftoli.jpg", "Shaftoli 🍑  <b>9,000</b> so'm/kg", Shaftoli),
        ("photos/uzum.jpg", "Uzum 🍇  <b>15,000</b> so'm/kg", Uzum),
        ]
    for photo_path, description, button in fruits:
        with open(photo_path, 'rb') as photo:
            await call.message.answer_photo(photo=photo, caption=description, reply_markup=button)

@dp.callback_query_handler(text="Poliz_ekinlari")
async def menyu(call: types.CallbackQuery):
    await call.message.delete()
    poliz_ekinlar = [
        ("photos/kartoshka.jpg", "Kartoshka   <b>8,000</b> so'm/kg", Kartoshka),
        ("photos/piyoz.jpg", "Piyoz   <b>5,000</b> so'm/kg", Piyoz),
        ("photos/chesnok.jpg", "Chesnok   <b>12,000</b> so'm/kg", Chesnok),
        ("photos/sariq_sabzi.jpg", "Sabzi (sariq)   <b>4,000</b> so'm/kg", Sabzi),
        ("photos/pomidor.jpg", "Pomidor   <b>7,000</b> so'm/kg", Pomidor),
        ("photos/bodiring.jpg", "Bodring   <b>6,000</b> so'm/kg", Bodring),
        ("photos/karam1.jpg", "Karam   <b>10,000</b> so'm/kg", Karam),
        ("photos/brokoli.jpg", "Brokoli   <b>15,000</b> so'm/kg", Brokoli),
        ("photos/joxori.jpg", "Jo'xori   <b>2,000</b> so'm/kg", Joxori),
        ("photos/qovoq.jpg", "Qovoq   <b>9,000</b> so'm/kg", Qovoq),
        ("photos/turup.jpg", "Turup   <b>4,000</b> so'm/kg", Turup),
        ("photos/kok_piyoz.jpg", "Ko'k piyoz   <b>3,000</b> so'm/kg", Kok_piyoz),
        ("photos/kashnich.jpg", "Kashnich   <b>2,000</b> so'm/kg", Kashnich),
        ("photos/gulkaram.jpg", "Gulkaram   <b>10,000</b> so'm/kg", Gulkaram),
        ("photos/qoziqorin.jpg", "Qo'ziqorin   <b>12,000</b> so'm/kg", Qoziqorin),
        ("photos/tarvuz.jpg", "Tarvuz   <b>6,000</b> so'm/kg", Tarvuz),
        ("photos/qovun.jpg", "Qovun   <b>8,000</b> so'm/kg", Qovun),
        ("photos/lovlagi.jpg", "Lovlagi   <b>5,000</b> so'm/kg", Lovlagi),
        ("photos/baqlajon.jpg", "Baqlajon   <b>7,000</b> so'm/kg", Baqlajon),
        ("photos/balgari.jpg", "Bulg'or qalampir   <b>10,000</b> so'm/kg", Bulgor_qalampir),
        ]
    for photo_path, description, button in poliz_ekinlar:
        with open(photo_path, 'rb') as photo:
            await call.message.answer_photo(photo=photo, caption=description, reply_markup=button)

basket_total = 0

# Mahsulotlar uchun narxlar dictionary shaklida
product_prices = {
    "olma": 5000,
    "banan": 6000,
    "ananas": 7000,
    "olcha": 8000,
    "malina": 9000,
    "maymunjon": 10000,
    "apelsin": 5500,
    "xurmo": 6500,
    "qulupnay": 8000,
    "anjir": 9500,
    "anor": 10500,
    "bexi": 7000,
    "gilos": 11000,
    "kivi": 12000,
    "limon": 6000,
    "mandarin": 5800,
    "nok": 7500,
    "mango": 14000,
    "shaftoli": 9000,
    "uzum": 15000,
    "kartoshka": 8000,
    "piyoz": 5000,
    "chesnok": 12000,
    "sabzi": 4000,
    "pomidor": 7000,
    "bodiring": 6000,
    "karam": 10000,
    "brokoli": 15000,
    "joxori": 2000,
    "qovoq": 9000,
    "turup": 4000,
    "kokpiyoz": 3000,
    "kashnich": 2000,
    "gulkaram": 10000,
    "qoziqorin": 12000,
    "tarvuz": 6000,
    "qovun": 8000,
    "lovlagi": 5000,
    "baqlajon": 7000,
    "bulgorqalampir": 10000,
}

@dp.callback_query_handler(lambda call: call.data.split("_")[0] in product_prices)
async def add_to_basket(call: types.CallbackQuery):
    user_id = call.from_user.id
    data = call.data.split("_")
    product, quantity = data[0], int(data[1])
    total_price = product_prices[product] * quantity

    user_purchases[user_id] = user_purchases.get(user_id, 0) + total_price

    msg = f"Umumiy narx: <b>{user_purchases[user_id]:,}</b> so'm"
    await call.message.answer(text=msg, reply_markup=buyurtmalar)

@dp.callback_query_handler(text="Bekor_qilish")
async def cancel_order(call: types.CallbackQuery):
    user_id = call.from_user.id
    user_purchases[user_id] = 0  # Savatni tozalash
    await call.message.answer("Buyurtmangiz bekor qilindi. Savatcha tozalandi.", reply_markup=buyurtmalar)

@dp.callback_query_handler(text="Tasdiqlash")
async def confirm_order(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    total_price = user_purchases.get(user_id, 0)

    if total_price > 0:
        await call.message.answer("Buyurtmangiz qabul qilindi. Familiya va ismni kiriting:")
        await OrderState.name.set()  # Familiya va ismni kiritish holatiga o'tadi
    else:
        await call.message.answer("Savatda buyurtma mavjud emas.")

@dp.message_handler(state=OrderState.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Telefon raqamingizni kiriting:", reply_markup=phone_keyboard)
    await OrderState.phone.set()  # Telefon raqamni kiritish holatiga o'tadi

@dp.message_handler(state=OrderState.phone, content_types=[types.ContentType.TEXT, types.ContentType.CONTACT])
async def process_phone(message: types.Message, state: FSMContext):
    # Agar foydalanuvchi kontaktni yuborgan bo'lsa
    if message.contact is not None:
        phone_number = message.contact.phone_number
        user_id = message.from_user.id

        # Foydalanuvchi ma'lumotlarini konsolda ko'rsatish
        print(f"\x1b[32m[👤USER]:\x1b[0m {message.from_user.full_name}, \x1b[32m[🆔]:\x1b[0m {user_id}", end=", ")
        print(f"\x1b[32m[📱]:\x1b[31m\x1b[42m{phone_number}\x1b[0m")

        # Holat ma'lumotlarini yangilash
        await state.update_data(phone=phone_number)
        
        # Lokatsiyani so'rash
        await message.answer(f"Yetkazib berish uchun lokatsiyani yuboring", reply_markup=location_keyboard)#Yetkazib berish uchun lokatsiyani yuboring:
        # await OrderState.waiting_for_card.set()
        await OrderState.location.set()  # Lokatsiya holatiga o'tadi
    else:
        await message.answer("Iltimos, telefon raqamingizni yuboring.")
    


@dp.message_handler(state=OrderState.location, content_types=[types.ContentType.LOCATION])
async def process_location(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    
    if message.location is not None:
        user_location = message.location
        user_id = message.from_user.id

        print(f"\x1b[32m[👤USER]:\x1b[0m {message.from_user.full_name}, \x1b[32m[🆔]:\x1b[0m {user_id}", end=", ")
        print(f"\x1b[32m[📱]:\x1b[31m\x1b[42m{message.location}\x1b[0m")

        await state.update_data(location=(user_location.latitude, user_location.longitude))

        # Buyurtma qabul qilinganini tasdiqlovchi xabar
        await message.answer("Buyurtmangiz qabul qilindi va yetkazib berish manzili saqlandi. Rahmat!",reply_markup=Menu)
        

        # Holat mavjud bo'lsa uni tozalash
        if await state.get_state() is not None:
            await state.finish()
    else:
        await message.answer("Iltimos, yetkazib berish uchun lokatsiyani yuboring.")


