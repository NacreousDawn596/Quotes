'''
author: NacreousDawn596
github: https://github.com/NacreousDawn596
instagram: NacreousDawn596
website for buisness: http://TikiZoom.byethost32.com/
'''



# importing kivy
import kivy


# showing the required version
kivy.require('2.0.0')


# importing request to get all what we need from a website
import requests


# importing the rest of kivy'modules
from kivy.app import App
from kivy.uix.label import Label


# request part = importing the website
url = 'https://api.quotable.io/random'
# request part = importing what we need from a website
request = requests.get(url)
# request part = creating a variable that contains what we imported
quotes = request.json()
print(quotes)
# request part = creating a variable that contains what we need from the things imported
n = quotes['content']
#kivy part = customizing the text of the quote
quote = f"{n} \n      -NacreousDawn596"


#kivy part = creating the Application
class MyAppApp(App):
	# request part = importing the website
	url = 'https://api.quotable.io/random'
	# request part = importing what we need from a website
	request = requests.get(url)
	# request part = creating a variable that contains what we imported
	quotes = request.json()
	print(quotes)
	# request part = creating a variable that contains what we need from the things imported
	n = quotes['content']
	#kivy part = customizing the text of the quote
	quote = f"{n} \n      -NacreousDawn596"
	#kivy part = writing what we want to display on the screen
	def build(self):
        	#kivy part = displaying the quote
	        return Label(text=quote)


# executing the code
if __name__ == '__main__':
    MyAppApp().run()
# enjoy!
