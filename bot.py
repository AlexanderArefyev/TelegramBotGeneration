import configBot
import btnConfig
import asyncio
import algoForBot
import search_img
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.middlewares.logging import LoggingMiddleware

bot = Bot(token=configBot.API_TOKEN) # Токен бота
dp = Dispatcher(bot, storage=MemoryStorage()) # События и обновление в боте 
dp.middleware.setup(LoggingMiddleware())

class Wait(StatesGroup):
    
    name_img = State()

@dp.message_handler(state=Wait.name_img)
async def img(message: types.Message):  
          
    await message.answer(search_img.search_img(name_req=message.text))

# Запуск бота
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(text = f'Привет, {message.from_user.first_name}!',
                         reply_markup=btnConfig.markup)
    await bot.send_sticker(message.from_user.id, 
                           sticker='CAACAgIAAxkBAAEGeCBjeP_Hy8bGy7u5XnwxJ6zbvRL33wACPAADwDZPE9eVZhJ0WTE5KwQ') # Стикер ID

# Генерация никнейма, пароля и поиск аватарки
@dp.message_handler()
async def gen(message: types.Message):
    
    if message.text == 'Сгенерировать никнейм':
        
        nickname = await message.answer(algoForBot.gen_nickname())
        txt_nick = await message.answer(text = 'Через 2 минуты я удалю это, чтобы не мусорить в нашем чате.')
        await asyncio.sleep(10) # Время для удаления записей 
                                
        # Проверка на удаление
        try:
            await txt_nick.delete()
            await nickname.delete()
            await message.delete()
        except:
            pass
    
    elif message.text == 'Сгенерировать пароль':
            
        txt_pass = await message.answer(text = 'Ваш пароль:')
        cur_pass = await message.answer(algoForBot.gen_password())
        cur_text = await message.answer(text = f'{message.from_user.first_name}, для безопасности через 2 минуты пароль будет удален.')            
        await asyncio.sleep(10) # Время для удаления записей                    
        
        # Проверка на удаление
        try:
            await txt_pass.delete()
            await cur_pass.delete()
            await cur_text.delete()
            await message.delete()
        except:
            pass
        
    elif message.text == 'Найти аватарку':
        
        txt_img = await message.answer(text='Что Вам найти?')
        await Wait.name_img.set()
        # await asyncio.sleep(10)
        
        # Проверка на удаление                
        # try:
        #     await txt_img.delete()
        #     await message.delete()
        # except:
        #     pass 
        
    else: # Если задан неизвестный текст
        if message.text:
            error_msg = await message.answer(text = f'{message.from_user.first_name}, Я не понимаю Вас. \nИспользуйте кнопки управления.')
            await asyncio.sleep(5)
            
            # Проверка на удаление                
            try:
                await error_msg.delete()
                await message.delete()
            except:
                pass 
                
  
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)