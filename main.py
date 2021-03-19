# import utils

from vkbottle.bot import Bot, Message
from vkbottle.tools import Keyboard
import configparser

# creating funcs

def CONFIGS(config_name, section, key):
    config = configparser.ConfigParser()
    config.read(config_name)
    return config[section][key]

# creating vars

BOT = Bot(CONFIGS('config.ini', 'Cbcon', 'Token'))

# job cycle
@BOT.on.message()
async def HANDLER_MESSAGE(msg: Message):
    await msg.answer(user_id=487334215, message=f'[ВАЖНО]\n[id{msg.from_id}|Пользователь] написал сообщение!')

# start

if __name__ == '__main__':
    BOT.run_forever()