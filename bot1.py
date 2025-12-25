import logging
from telegram import ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Вставьте сюда ваш токен
TOKEN = "8410059566:AAHzg0sgi9YyVIt37hC1EoamihYwklo21nM"

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Создаем клавиатуру с кнопками
keyboard = [
    ['Тестирование', 'Программирование'],
    ['DevOps', 'Дизайн'],
    ['Помощь']
]
reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# Данные для кнопок (ссылки и описания)
IT_RESOURCES = {
    'Тестирование': [
        {'name': 'Software Testing Help', 'url': 'https://www.softwaretestinghelp.com/',
         'desc': 'Статьи, руководства и форум по тестированию ПО'},
        {'name': 'Ministry of Testing', 'url': 'https://www.ministryoftesting.com/',
         'desc': 'Сообщество тестировщиков с курсами и мероприятиями'},
        {'name': 'Test Automation University', 'url': 'https://testautomationu.applitools.com/',
         'desc': 'Бесплатные курсы по автоматизации тестирования'}
    ],
    'Программирование': [
        {'name': 'Stack Overflow', 'url': 'https://stackoverflow.com/', 'desc': 'Крупнейшее сообщество программистов'},
        {'name': 'GitHub', 'url': 'https://github.com/', 'desc': 'Платформа для хостинга кода и совместной работы'},
        {'name': 'freeCodeCamp', 'url': 'https://www.freecodecamp.org/', 'desc': 'Бесплатные курсы программирования'}
    ],
    'DevOps': [
        {'name': 'DevOps.com', 'url': 'https://devops.com/', 'desc': 'Новости и статьи по DevOps'},
        {'name': 'Kubernetes.io', 'url': 'https://kubernetes.io/', 'desc': 'Официальная документация Kubernetes'},
        {'name': 'Docker Docs', 'url': 'https://docs.docker.com/', 'desc': 'Документация Docker'}
    ],
    'Дизайн': [
        {'name': 'Dribbble', 'url': 'https://dribbble.com/', 'desc': 'Сообщество дизайнеров и портфолио'},
        {'name': 'Figma Community', 'url': 'https://www.figma.com/community',
         'desc': 'Библиотека компонентов и плагинов Figma'},
        {'name': 'Awwwards', 'url': 'https://www.awwwards.com/', 'desc': 'Лучшие примеры веб-дизайна'}
    ]
}


async def start(update, context):
    """Обработчик команды /start"""
    welcome_text = (
        "👋 Привет! Я IT-гид бот.\n\n"
        "Выберите категорию из меню ниже, чтобы получить полезные ссылки:\n\n"
        "• Тестирование - ресурсы по QA и тестированию\n"
        "• Программирование - платформы для разработчиков\n"
        "• DevOps - инструменты и практики\n"
        "• Дизайн - ресурсы для дизайнеров\n\n"
        "Используйте кнопки для навигации!"
    )
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)


async def help_command(update, context):
    """Обработчик команды /help и кнопки Помощь"""
    help_text = (
        "ℹ️ **Помощь**\n\n"
        "Я выдам полезные ссылки в IT-сфере по категориям.\n\n"
        "Доступные категории:\n"
        "• **Тестирование** - ресурсы по QA\n"
        "• **Программирование** - для разработчиков\n"
        "• **DevOps** - инструменты и практики\n"
        "• **Дизайн** - ресурсы для дизайнеров\n\n"
        "Просто нажмите на одну из кнопок в меню!"
    )
    await update.message.reply_text(help_text, reply_markup=reply_markup)


async def handle_message(update, context):
    """Обработчик текстовых сообщений (нажатий на кнопки)"""
    user_message = update.message.text

    if user_message in IT_RESOURCES:
        # Формируем ответ для выбранной категории
        resources = IT_RESOURCES[user_message]
        response = f"🔗 **{user_message}**\n\n"

        for i, resource in enumerate(resources, 1):
            response += f"{i}. **[{resource['name']}]({resource['url']})**\n"
            response += f"   {resource['desc']}\n\n"

        response += f"Всего ресурсов: {len(resources)}"

        # Отправляем сообщение с поддержкой Markdown и отключением предпросмотра ссылок
        await update.message.reply_text(
            response,
            reply_markup=reply_markup,
            parse_mode='Markdown',
            disable_web_page_preview=True
        )
    elif user_message == 'Помощь':
        await help_command(update, context)
    else:
        await update.message.reply_text(
            "Пожалуйста, используйте кнопки меню для навигации.",
            reply_markup=reply_markup
        )


def main():
    """Основная функция запуска бота"""
    # Создаем Application
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запускаем бота
    print("Бот запущен...")
    application.run_polling(allowed_updates=[])


if __name__ == '__main__':
    main()
