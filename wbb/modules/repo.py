from pyrogram.types import Message
from wbb import app
from wbb.utils import cust_filter


__MODULE__ = "Repo"
__HELP__ = "/repo - To Get My Github Repository Link " + \
           "And Support Group Link"


@app.on_message(cust_filter.command(commands=("repo")))
async def repo(client, message: Message):  # pylint: disable=W0613
    app.set_parse_mode("markdown")
    await message.reply_text(
        "[Github](https://github.com/thehamkercat/WilliamButcherBot)"
        + " | [Group](t.me/WBBSupport)", disable_web_page_preview=True)