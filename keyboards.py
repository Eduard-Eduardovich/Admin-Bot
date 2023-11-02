from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


select_work_bot = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Включить', callback_data='setting_on'),
            InlineKeyboardButton(text='Отключить', callback_data='setting_off')         
        ]
        
    ]
    
)


select_work_bot_on_off = InlineKeyboardMarkup(
inline_keyboard=[
    [InlineKeyboardButton(text='настройка гс', callback_data='sett_voicemessages')],
    [InlineKeyboardButton(text='настройка видео', callback_data='sett_video')],
    [InlineKeyboardButton(text='настройка гиф', callback_data='sett_gif')],
    [InlineKeyboardButton(text='настройка файл', callback_data='sett_file')],
    [InlineKeyboardButton(text='назад', callback_data='sett_back')]
    
]

    
)


select_action_voicemessage_bot = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Удалять голосовые сообщения', callback_data='voice_on')],
        [InlineKeyboardButton(text='Не удалять голосовые сообщения', callback_data='voice_off')],
        [InlineKeyboardButton(text='назад', callback_data='voice_back')]
    ]
    
)

select_action_video_bot = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Удалять видео', callback_data='videodelete_on'),
        ],
        [
            InlineKeyboardButton(text='Не удалять видео', callback_data='videodelete_off'),
        ],
        [
            InlineKeyboardButton(text='назад', callback_data='videodelete_back')
        ]
        
    ]
    
)

select_action_file_bot = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Удалять файлы', callback_data='filedeletemain_on'),
        ],
        [
            InlineKeyboardButton(text='Не удалять файлы', callback_data='filedeletemain_off')     
        ],
        [
           InlineKeyboardButton(text='назад', callback_data='filedeletemain_back')
        ]
        
    ]
    
)

select_action_gif_bot = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Удалять гиф-сообщения', callback_data='gifdelete_on'),
        ],
        [
            InlineKeyboardButton(text='Не удалять гиф-сообщения', callback_data='gifdelete_off'),
        ],
        [
           InlineKeyboardButton(text='назад', callback_data='gifdelete_back')
        ]
        
    ]
    
)

format_file_delete = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Удалять файлы-.txt ', callback_data='filedelete_txt'),
        ],
        [
            InlineKeyboardButton(text='Удалять файлы-.pdf ', callback_data='filedelete_pdf'),
        ],
        [
            InlineKeyboardButton(text='Удалять файлы-.docx ', callback_data='filedelete_docx'),
        ],
        [
            InlineKeyboardButton(text='Удалять файлы-.rtf ', callback_data='filedelete_rtf')
        ],
        # [
        #    InlineKeyboardButton(text='сброс', callback_data='filedelete_back')
        # ],
        [
           InlineKeyboardButton(text='назад', callback_data='filedelete_back')
        ]
        
        
        
    ]
    
)