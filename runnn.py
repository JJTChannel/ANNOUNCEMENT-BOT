import nextcord
from nextcord.ext import commands
from os import system 
from colorama import Fore
from time import sleep
	


guild_id = 1066668605476962354
owner = 750677078986195003
prefixs = "/"
  
          
class Announce(nextcord.ui.Modal):

    def __init__(self):
        super().__init__(
            title="ประกาศ",
            custom_id="persistent_modal:feedback",
            timeout=None,
        )

        self.b = nextcord.ui.TextInput(
            label="หัวข้อ",
            custom_id="persistent_modal:b",
        )
        self.add_item(self.b)

        self.d = nextcord.ui.TextInput(
              label="ข้อความ",
              max_length=100,
              custom_id="persistent_modal:d",
           )
        self.add_item(self.d)
      
        self.a = nextcord.ui.TextInput(
              label="ข้อความด้านล่าง",
              custom_id="persistent_modal:a",
            )
        self.add_item(self.a)

        self.s = nextcord.ui.TextInput(
              label="ลิ้งรูป",
              custom_id="persistent_modal:s",
            )
        self.add_item(self.s)

    async def callback(self, interaction: nextcord.Interaction):
      embedsucceed = nextcord.Embed(title=self.b.value, description=self.d.value,color=0xfffff)
      embedsucceed.set_image(url=self.s.value)
      embedsucceed.set_footer(text=self.a.value)
      await interaction.send(embed=embedsucceed)
      
      
        


      



class Bot(commands.Bot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.persistent_modals_added = False

    async def on_ready(self):
        if not self.persistent_modals_added:
            self.add_modal(Announce())
            self.persistent_modals_added = True
            system('cls')
            print(F"""{Fore.LIGHTRED_EX}
░░░░░██╗░░░░░██╗████████╗██╗░░██╗░██████╗████████╗░█████╗░██████╗░███████╗
{Fore.RED}░░░░░██║░░░░░██║╚══██╔══╝╚██╗██╔╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝
{Fore.YELLOW}░░░░░██║░░░░░██║░░░██║░░░░╚███╔╝░╚█████╗░░░░██║░░░██║░░██║██████╔╝█████╗░░
{Fore.GREEN}██╗░░██║██╗░░██║░░░██║░░░░██╔██╗░░╚═══██╗░░░██║░░░██║░░██║██╔══██╗██╔══╝░░
{Fore.CYAN}╚█████╔╝╚█████╔╝░░░██║░░░██╔╝╚██╗██████╔╝░░░██║░░░╚█████╔╝██║░░██║███████╗
{Fore.BLUE}░╚════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝""")
            sleep(0.5)
            system('cls')
            print(' -----')
            print(f'\n > {bot.user}')
            print('\n -----')
    
bot = Bot(command_prefix=prefixs)








@bot.slash_command(
    name="announce",
    description="ประกาศ",
    guild_ids=[guild_id],
)
async def announce (interaction: nextcord.Interaction):
    if (interaction.user.id == owner):
      await interaction.response.send_modal(Announce())



bot.run("TOKEN")


