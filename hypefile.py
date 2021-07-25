# This Python file uses the following encoding: utf-8
""" 
⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝
|----------------------------------------------------------------------------------------|
                          GNU GENERAL PUBLIC LICENSE
                            Version 3, 29 June 2007
                            
        Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.

                        ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝,
                        Telegram Music player userbot 
                has been licensed under GNU General Public License
            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
|----------------------------------------------------------------------------------------|       
⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝
"""




"""⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝   𝗧𝗘𝗦𝗧𝗜𝗡𝗚 𝗖𝗢𝗟𝗢𝗥𝗦   ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝"""
import os
import sys
import subprocess
from termcolor import *
from sys import platform
"""⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝   𝗧𝗘𝗦𝗧𝗜𝗡𝗚 𝗖𝗢𝗟𝗢𝗥𝗦   ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝"""



"""⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝   𝗧𝗘𝗦𝗧𝗜𝗡𝗚 𝗖𝗢𝗟𝗢𝗥𝗦   ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝"""
print('Test basic colors:')

cprint('Grey color', 'grey')
cprint('Red color', 'red')
cprint('Green color', 'green')
cprint('Yellow color', 'yellow')
cprint('Blue color', 'blue')
cprint('Magenta color', 'magenta')
cprint('Cyan color', 'cyan')
cprint('White color', 'white')

print('Test highlights:')

cprint('On grey color', on_color='on_grey')
cprint('On red color', on_color='on_red')
cprint('On green color', on_color='on_green')
cprint('On yellow color', on_color='on_yellow')
cprint('On blue color', on_color='on_blue')
cprint('On magenta color', on_color='on_magenta')
cprint('On cyan color', on_color='on_cyan')
cprint('On white color', color='grey', on_color='on_white')

print('Test attributes:')

cprint('Bold grey color', 'grey', attrs=['bold'])
cprint('Dark red color', 'red', attrs=['dark'])
cprint('Underline green color', 'green', attrs=['underline'])
cprint('Blink yellow color', 'yellow', attrs=['blink'])
cprint('Reversed blue color', 'blue', attrs=['reverse'])
cprint('Concealed Magenta color', 'magenta', attrs=['concealed'])
cprint('Bold underline reverse cyan color', 'cyan',attrs=['bold', 'underline', 'reverse'])
cprint('Dark blink concealed white color', 'white',attrs=['dark', 'blink', 'concealed'])
cprint('Underline red on grey color', 'red', 'on_grey',['underline'])
cprint('Reversed green on red color', 'green', 'on_red', ['reverse'])
"""⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝   𝗧𝗘𝗦𝗧𝗜𝗡𝗚 𝗖𝗢𝗟𝗢𝗥𝗦   ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝"""




"""⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝   𝗧𝗘𝗦𝗧𝗜𝗡𝗚 𝗖𝗢𝗟𝗢𝗥𝗦   ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝"""
cprint('♣       ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝', on_color='on_blue')
cprint(f'{platform.upper()}','green')
os.system("pip install -U pip;pip install -r Ӽɛʀօռօɨɖ.txt")
os.system("clear")
cprint('⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝', on_color='on_cyan')


subprocess.run("python3 -m Ӽɛʀօռօɨɖ & python3 -m Ӽɛʀօռօɨɖɮօȶ",
shell=True,
check=True)



cprint('⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝', on_color='on_yellow')
print(platform.upper())
"""⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝   𝗧𝗘𝗦𝗧𝗜𝗡𝗚 𝗖𝗢𝗟𝗢𝗥𝗦   ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝"""