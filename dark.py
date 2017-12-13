from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
import time
import execjs

dcap = dict(DesiredCapabilities.PHANTOMJS)  # 设置userAgent
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36 ")
# driver=webdriver.Safari();
# driver = webdriver.Chrome();
driver = webdriver.PhantomJS(desired_capabilities=dcap)  # 加载网址
driver.get("http://wsjs.saic.gov.cn");
time.sleep(0.1)
print(driver.page_source)
js = "goUrl('/txnS02.do')";
# 调用给搜索输入框标红js脚本
driver.execute_script(js)
time.sleep(1)
driver.find_element_by_name("request:hnc").send_keys("无讼")
submit = "$('#submitForm').submit();";
driver.execute_script(submit);
# driver.find_element_by_xpath("//*[@id='_searchButton']").click();
time.sleep(10)
driver.refresh();
handles = driver.window_handles  # 获取当前全部窗口句柄集合
print(handles)  # 输出句柄集合
soup = BeautifulSoup(driver.page_source, 'xml');
print(driver.current_url)
time.sleep(10);
driver.quit();
