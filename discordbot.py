import discord
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.keys import Keys
import config

driver = uc.Chrome()
driver.get('https://www.cleverbot.com')
driver.find_element_by_id('noteb').click()

def get_response(message):
    driver.find_element_by_xpath('//*[@id="avatarform"]/input[1]').send_keys(message + Keys.RETURN)
    while True:
        try:
            driver.find_element_by_xpath('//*[@id="snipTextIcon"]')
            break
        except:
            continue
    response = driver.find_element_by_xpath('//*[@id="line1"]/span[1]').text
    return response

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author != self.user:
            reponse = get_response(message.content)
            await message.channel.send(f"{message.author.mention} {reponse}")

client = MyClient()
client.run(config.BOTTOKEN)