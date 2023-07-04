from selenium import webdriver
browser = webdriver.Edge('C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe')
browser.get('https://www.jd.com')
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
browser.execute_async_script('alert("已经到达页面低端")')
