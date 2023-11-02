# import emoji

from main import Bot
from aiogram import Dispatcher,types
from aiogram.filters.chat_member_updated import \
    ChatMemberUpdatedFilter,  MEMBER, ADMINISTRATOR
from aiogram.types import ChatMemberUpdated

from aiogram import Router, F
from aiogram.types import ChatMemberUpdated,Message,CallbackQuery
from aiogram.filters.command import Command, CommandStart
from aiogram.types import ChatMemberUpdated
from keyboards  import select_work_bot, select_work_bot_on_off, select_action_voicemessage_bot, select_action_video_bot, select_action_file_bot, select_action_gif_bot,format_file_delete
import keyboards




class Settings:
    def __init__(self):
        self.delete_voice_messages = False
        self.delete_video_messages = False
        self.delete_gif_messages = False
        self.delete_filetxt_messages = False
        self.delete_filepdf_messages = False    
        self.delete_filedocx_messages = False
        self.delete_filertf_messages = False
        

    def set_delete_voice_messages(self, value):
        self.delete_voice_messages = value

    def set_delete_video_messages(self, value):
        self.delete_video_messages = value

    def set_delete_gif_messages(self,value):
        self.delete_gif_messages = value
    
    def set_delete_filetxt_messages(self, value):
        self.delete_filetxt_messages = value
        
    def set_delete_filepdf_messages(self, value):
        self.delete_filepdf_messages = value
        
    def set_delete_filedocx_messages(self, value):
        self.delete_filedocx_messages = value
        
    def set_delete_filertf_messages(self, value):
        self.delete_filertf_messages = value

    def get_settings(self):
        return {
            'delete_voice_messages': self.delete_voice_messages,
            'delete_video_messages': self.delete_video_messages,
            'delete_gif_messages': self.delete_gif_messages,
            'delete_filetxt_messages' : self.delete_filetxt_messages,
            'delete_filepdf_messages' : self.delete_filepdf_messages,
            'delete_filedocx_messages' : self.delete_filedocx_messages,
            'delete_filertf_messages' : self.delete_filertf_messages
        }



ID = None

router = Router()

storage = set()

settings = Settings()

@router.message(Command("start"))
async def command_start(message :types.Message):
    await message.answer( text='Вас приветсвует бот по администрированию')
    
        
@router.message(Command('about'))
async def command_about(message :types.Message):
    await message.answer(text='/source - ссылка на исходный код бота\n/settings - текущие настройки бота\n/set_settings - команды для настройки бота\n/save_rules - сохранить или открепить правила чата\n/rules - получить сообщение с правилами чата')
        
@router.message(Command('source'))
async def comand_source(message :types.Message):
    await message.answer(text='ссылка -> https://www.google.de/')
    
@router.message(Command('rules'))
async def comand_rules(message: types.Message):
    welcome_message = (
        f"Уважение 😊: Всегда проявляйте уважение к другим участникам чата. Не используйте оскорбительные слова, уничижительные выражения или агрессивное поведение.\n\n"
        f"Не спамьте 🚫: Не размещайте повторяющиеся сообщения, коммерческую рекламу или ненужные материалы. Помните, что спам может мешать другим пользователям.\n\n"
        f"Безопасность 🔒: Не раскрывайте личную информацию или информацию других людей без их разрешения. Это включает в себя имена, адреса, номера телефонов и другие личные данные.\n\n"
        f"Тематика чата 🗣️: Старайтесь обсуждать темы, соответствующие контексту чата. Избегайте флуда и несвязанных с темой сообщений.\n\n"
        f"Соблюдение законов ⚖️: Соблюдайте действующие законы и правила, включая авторские права и правила интеллектуальной собственности. Не публикуйте незаконный контент."
    )

    await message.answer(welcome_message)
    
    

@router.message(Command('admin'))
async def on_help(message: types.Message, bot: Bot):
    result = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
    if result.status in ['creator', 'admin']:
        await message.reply("Чтобы добавить админ айди, введите /add_admin и укажите айди пользователя. \n"
                                "Чтобы получить админ айди, введите /get_admin. \n"
                                "Чтобы удалить админ айди, введите /delete_admin и укажите айди пользователя.")

@router.message(Command('add_admin'))
async def on_add_admin(message: types.Message, bot: Bot):
    result = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
    if result.status in ['creator', 'admin']:
        ID = message.chat.id
        global storage
        if storage is None:
            storage = set()

        try:
            admin_id = int(message.text.split()[1])
        except IndexError:
            return await message.reply("Не указан айди пользователя.")

        storage.add(admin_id)
        await message.reply(f"Админ айди {admin_id} добавлен.")


@router.message(Command('get_admin'))
async def on_get_admin(message: types.Message):
   global storage
   if storage is None:
       await message.reply("Админ айди еще не добавлены.")
   else:
       admin_list = "\n".join(map(str, storage))
       await message.reply(f"Список админ айди:\n\n{admin_list}")


@router.message(Command('settings'))
async def command_settings(message: Message):
    state_voice = settings.get_settings()["delete_voice_messages"]
    state_video = settings.get_settings()["delete_video_messages"]
    state_gif = settings.get_settings()["delete_gif_messages"]
    state_file_txt = settings.get_settings()["delete_filetxt_messages"]
    state_file_pdf = settings.get_settings()["delete_filepdf_messages"]
    state_file_docx = settings.get_settings()["delete_filedocx_messages"]
    state_file_rtf = settings.get_settings()['delete_filertf_messages']
    
    settings_message = f"""
*Текущие настройки:*
_Настройка гс:_ {state_voice}
_Настройка видео:_ {state_video}
_Настройка гиф:_ {state_gif}
_Настройка файл:_
 *txt* - {state_file_txt}
 *pdf* - {state_file_pdf}
 *docx* - {state_file_docx}
 *rtf* - {state_file_rtf}
"""
    
    await message.answer(settings_message, parse_mode='Markdown')
    
@router.message(Command('delete_admin'))
async def on_delete_admin(message: types.Message):
   global storage
   if storage is None:
       storage = set()

   try:
       admin_id = int(message.text.split()[1])
   except IndexError:
       return await message.reply("Не указан айди пользователя.")

   if admin_id in storage:
       storage.remove(admin_id)
       await message.reply(f"Админ айди {admin_id} удален.")
   else:
       await message.reply(f"Админ айди {admin_id} не найден.")

    
@router.message(Command('set_settings'))
async def comad_set_settings(message: types.Message,bot: Bot):
    result = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
    if message.from_user.id  in storage:
        await message.answer('Включить/отключить настройку:', reply_markup=keyboards.select_work_bot)
        
    else:
        await message.reply('Вы не являетесь администратором или создателем чата')
    
    
        
@router.callback_query(F.data.startswith('setting_'))     
async def bot_setting_on(callback: types.CallbackQuery):
    result = callback.data.split('_')[1]
    if result == 'on':
        await callback.message.answer('Настройка бота его возможностей',reply_markup=keyboards.select_work_bot_on_off)
        await callback.message.delete()
    else:
        await callback.message.delete()
    
    
@router.callback_query(F.data.startswith('sett_'))     
async def bot_sett_on(callback: types.CallbackQuery):
    global settings
    
    state_voice = settings.get_settings()["delete_voice_messages"]
    state_video = settings.get_settings()["delete_video_messages"]
    state_gif = settings.get_settings()["delete_gif_messages"]
    state_file_txt = settings.get_settings()["delete_filetxt_messages"]
    state_file_pdf = settings.get_settings()["delete_filepdf_messages"]
    state_file_docx = settings.get_settings()["delete_filedocx_messages"]
    state_file_rtf = settings.get_settings()['delete_filertf_messages']
     
    
    result = callback.data.split('_')[1]
    if result == 'voicemessages':
        await callback.message.answer(f'Настройка гс\nСейчас состояние {state_voice}',reply_markup=keyboards.select_action_voicemessage_bot)
        await callback.message.delete()
    elif result == 'video':
        await callback.message.answer(f'Настройка видео\nСейчас состояние {state_video}',reply_markup=keyboards.select_action_video_bot)
        await callback.message.delete()    
    elif result == 'gif':
        await callback.message.answer(f'Настройка гиф\nСейчас состояние {state_gif}',reply_markup=keyboards.select_action_gif_bot)
        await callback.message.delete()
    elif result == 'file':
        await callback.message.answer(f'Настройка файл\nСейчас состояние\ntxt - {state_file_txt}\npdf - {state_file_pdf}\ndocx - {state_file_docx}\nrtf - {state_file_rtf}',reply_markup=keyboards.select_action_file_bot)
        await callback.message.delete()
    elif result == 'back':
        await callback.message.delete()
        await callback.message.answer('Включить/отключить настройку:',reply_markup=keyboards.select_work_bot)




@router.callback_query(F.data.startswith('voice_'))
async def bot_setting_voice(callback: CallbackQuery):
    
    global settings
    result = callback.data.split('_')[1]
    
    if result == 'on':
        settings.set_delete_voice_messages(True)
        state_voice = settings.get_settings()["delete_voice_messages"]
        await callback.message.answer(f'Настройка гс\nСейчас состояние {state_voice}',reply_markup=keyboards.select_action_voicemessage_bot)
        await callback.message.delete() 
    elif result == 'back':
        await callback.message.delete()
        await callback.message.answer('Настройка бота его возможностей',reply_markup=keyboards.select_work_bot_on_off)
    else:
        settings.set_delete_voice_messages(False)
        state_voice = settings.get_settings()["delete_voice_messages"]
        await callback.message.answer(f'Настройка гс\nСейчас состояние {state_voice}',reply_markup=keyboards.select_action_voicemessage_bot)
        await callback.message.delete() 
    

@router.message(F.voice)
async def on_voice_message(message: types.Message, bot: Bot):
   if settings.delete_voice_messages:
       await bot.delete_message(message.chat.id, message.message_id)


@router.callback_query(F.data.startswith('videodelete_'))
async def bot_setting_video(callback: CallbackQuery):
    global settings
    result = callback.data.split('_')[1]
    

    if result == 'on':
        settings.set_delete_video_messages(True)
        state_video = settings.get_settings()["delete_video_messages"]
        await callback.message.answer(f'Настройка видео\nСейчас состояние {state_video}',reply_markup=keyboards.select_action_video_bot)
        await callback.message.delete() 
    elif result == 'back':
        await callback.message.delete()
        await callback.message.answer('Настройка бота его возможностей',reply_markup=keyboards.select_work_bot_on_off)
    else:
        settings.set_delete_video_messages(False)
        state_video = settings.get_settings()["delete_video_messages"]
        await callback.message.answer(f'Настройка видео\nСейчас состояние {state_video}',reply_markup=keyboards.select_action_video_bot)
        await callback.message.delete() 

@router.message(F.video)
async def on_video_message(message: types.Message, bot: Bot):
    if settings.delete_video_messages:
        await bot.delete_message(message.chat.id, message.message_id)

@router.callback_query(F.data.startswith('gifdelete_'))
async def bot_setting_gif(callback: CallbackQuery):
    result = callback.data.split('_')[1]
    global settings

    if result == 'on':
        settings.set_delete_gif_messages(True)
        state_gif = settings.get_settings()["delete_gif_messages"]
        await callback.message.answer(f'Настройка гиф\nСейчас состояние {state_gif}',reply_markup=keyboards.select_action_gif_bot)
        await callback.message.delete() 
    elif result == 'back':
        await callback.message.delete()
        await callback.message.answer('Настройка бота его возможностей',reply_markup=keyboards.select_work_bot_on_off)
    else:
        settings.set_delete_gif_messages(False)
        state_gif = settings.get_settings()["delete_gif_messages"]
        await callback.message.answer(f'Настройка гиф\nСейчас состояние {state_gif}',reply_markup=keyboards.select_action_gif_bot)
        await callback.message.delete() 

@router.message(F.animation)
async def on_gif_message(message: types.Message, bot: Bot):
   if settings.delete_gif_messages:
       await bot.delete_message(message.chat.id, message.message_id)


@router.callback_query(F.data.startswith('filedeletemain_'))
async def bot_setting_gif(callback: CallbackQuery):
    result = callback.data.split('_')[1]
    global settings
    state_file_txt = settings.get_settings()["delete_filetxt_messages"]
    state_file_pdf = settings.get_settings()["delete_filepdf_messages"]
    state_file_docx = settings.get_settings()["delete_filedocx_messages"]
    state_file_rtf = settings.get_settings()['delete_filertf_messages']
    
    if result == 'on':
            await callback.message.delete()
            await callback.message.answer(f'Выбирете какой тип файла будет удалять\nСейчас состояние\ntxt - {state_file_txt}\npdf - {state_file_pdf}\ndocx - {state_file_docx}\nrtf - {state_file_rtf}',reply_markup=keyboards.format_file_delete)
    elif result == 'back':
        await callback.message.delete()
        await callback.message.answer('Настройка бота его возможностей',reply_markup=keyboards.select_work_bot_on_off)
    elif result == 'off':
            settings.set_delete_filetxt_messages(False)
            settings.set_delete_filepdf_messages(False)
            settings.set_delete_filedocx_messages(False)
            settings.set_delete_filertf_messages(False)
            state_file_txt = settings.get_settings()["delete_filetxt_messages"]
            state_file_pdf = settings.get_settings()["delete_filepdf_messages"]
            state_file_docx = settings.get_settings()["delete_filedocx_messages"]
            state_file_rtf = settings.get_settings()['delete_filertf_messages']
            await callback.message.delete()
            await callback.message.answer(f'Выбирете какой тип файла будет удалять\nСейчас состояние\ntxt - {state_file_txt}\npdf - {state_file_pdf}\ndocx - {state_file_docx}\nrtf - {state_file_rtf}',reply_markup=keyboards.format_file_delete)
            

@router.callback_query(F.data.startswith('filedelete_'))
async def bot_setting_video(callback: CallbackQuery):
    result = callback.data.split('_')[1]
    global settings
    state_file_txt = settings.get_settings()["delete_filetxt_messages"]
    state_file_pdf = settings.get_settings()["delete_filepdf_messages"]
    state_file_docx = settings.get_settings()["delete_filedocx_messages"]
    state_file_rtf = settings.get_settings()['delete_filertf_messages']

    if result == 'txt':
        settings.set_delete_filetxt_messages(True)
        state_file_txt = settings.get_settings()["delete_filetxt_messages"]
        await callback.message.answer(f'Сейчас состояние\ntxt - {state_file_txt}\npdf - {state_file_pdf}\ndocx - {state_file_docx}\nrtf - {state_file_rtf}',reply_markup=keyboards.format_file_delete)
        await callback.message.delete()
    elif result == 'pdf':
        settings.set_delete_filepdf_messages(True)
        state_file_pdf = settings.get_settings()["delete_filepdf_messages"]
        await callback.message.answer(f'Сейчас состояние\ntxt - {state_file_txt}\npdf - {state_file_pdf}\ndocx - {state_file_docx}\nrtf - {state_file_rtf}',reply_markup=keyboards.format_file_delete)
        await callback.message.delete()
    elif result == 'docx':
        settings.set_delete_filedocx_messages(True)
        state_file_docx = settings.get_settings()["delete_filedocx_messages"]
        await callback.message.answer(f'Сейчас состояние\ntxt - {state_file_txt}\npdf - {state_file_pdf}\ndocx - {state_file_docx}\nrtf - {state_file_rtf}',reply_markup=keyboards.format_file_delete)
        await callback.message.delete()
    elif result == 'rtf':
        settings.set_delete_filertf_messages(True)
        state_file_rtf= settings.get_settings()["delete_filertf_messages"]
        await callback.message.answer(f'Сейчас состояние\ntxt - {state_file_txt}\npdf - {state_file_pdf}\ndocx - {state_file_docx}\nrtf - {state_file_rtf}',reply_markup=keyboards.format_file_delete)
        await callback.message.delete()
    elif result == 'back':
        await callback.message.answer('Настройка бота его возможностей',reply_markup=keyboards.select_work_bot_on_off)
        await callback.message.delete()


async def get_file_extension(message: Message):
    format_file = message.document.file_name.split('.')[-1]
    return format_file

@router.message(F.content_type == types.ContentType.DOCUMENT)
async def on_message(message: types.Message, bot: Bot): 
    
    file_extension = await get_file_extension(message)
    if file_extension == "txt":
        if settings.set_delete_filetxt_messages:
           await bot.delete_message(message.chat.id, message.message_id)
    elif file_extension == "pdf":
        if settings.set_delete_filepdf_messages:
            await bot.delete_message(message.chat.id, message.message_id)
    elif file_extension == "docx":
        print('wdqwdqw')
        if settings.set_delete_filedocx_messages:
            await bot.delete_message(message.chat.id, message.message_id)
    elif file_extension == "rtf":
        if settings.set_delete_filertf_messages:
            await bot.delete_message(message.chat.id, message.message_id)



@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=ADMINISTRATOR >>  MEMBER))
async def check_bot_admin_status(message: types.Message,bot: Bot):
    new_chat_member = message.new_chat_member
    user = await bot.get_chat_member(chat_id=message.chat.id, user_id=new_chat_member.user.id)
    if user.status != "administrator":
        # bot.dispatcher.disable_for_chat(message.chat.id)
        await message.answer('я не админ') 
    # elif user.status == 'administrator':
    #      bot.dispatcher.enable_for_chat(message.chat.id)
    #      await message.answer('я  админ') 
        

        

forbidden_commands = ["/set_settings", "/source", "/about"]

@router.message()
async def handle_forbidden_commands(message: types.Message):
    if message.text in forbidden_commands:
        await message.delete()
        await message.reply("Ты не имеешь доступа к этой команде")
    elif message.chat.type == 'supergroup':
        if message.chat.is_channel:
            await message.reply('Группа преобразована в супергруппу.')