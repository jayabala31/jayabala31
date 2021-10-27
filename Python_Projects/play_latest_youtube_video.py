from selenium import webdriver

class Music():
	def __init__(self):
        self.driver =  webdriver.Chrome()
        
    def play(self):
        name = input("Enter a youtube channel name: ")
        self.driver.get("https://www.youtube.com/user/"+name+"/videos")
        
        new = self.driver.find_element_by_xpath('//*[@id="primary"]/ytd-section-list-renderer')
        new.click()
    
bot = Music()
bot.play()
