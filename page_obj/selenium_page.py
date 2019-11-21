import time
import traceback
from logging import exception

from pip._vendor.retrying import retry
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC



class SeleniumPage(object):
    '''
    基础类，用于页面对象类的继承
    '''

    def __init__(self, driver):
        self.driver = driver

    def open(self,url):
        '''打开登录页面'''
        self.driver.get(url)

    # 基础方法开始
    def window_scroll_to(self, yy):
        script = 'window.scrollTo(0,' + yy + ')'  # 滚动到控件可以看到后面的代码执行才不会报错
        self.driver.execute_script(script)

    #         #time.sleep(0.3)

    def click_elem_by_js(self, locator):
        '''通过js点击元素'''
        elem = self.find_elemByCSS(locator)
        self.driver.execute_script("arguments[0].click();", elem)


    def remove_locator_Attr(self, locator,attr):
        '''js设置元素属性'''
        elem = self.find_elemByXPATH (locator)
        self.driver.execute_script ("arguments[0].removeAttribute('"+attr+"');", elem)

    def hide_elem_by_jq(self, locator):
        '''通过jq将元素隐藏'''
        script = '$("' + locator + '").hide()'
        self.driver.execute_script(script)


    def show_elem_by_jq(self, locator):
        '''通过jq将元素显示'''
        script = '$("' + locator + '").show()'
        self.driver.execute_script(script)
        self.wait_elem_visible(locator)

    def remove_locator(self, locator):
        '''js移除元素'''
        script = '$("' + locator + '").remove()'  # 从dom移除元素
        self.driver.execute_script(script)





    def find_elem_visibleByCSS(self, locator, timeout=2):
        '''判断5s内，定位的元素是否存在dom结构里并且可见。存在则返回元素，不存在则返回None'''
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        except:
            return None

    def find_elem_visibleByXPATH(self, locator, timeout=2):
        '''判断5s内，定位的元素是否存在dom结构里并且可见。存在则返回元素，不存在则返回None'''
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, locator)))
        except:
            return None

    def find_elems_visible(self, locator, timeout=5):
        '''判断5s内，定位的元素是否存在dom结构里并且可见。存在则返回元素，不存在则返回None'''
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, locator)))
        except:
            return None

    def find_elem_is_clickableByCSS(self, locator, timeout=5):
        '''判断5s内，定位的元素是否可见并且可以点击。存在则返回元素，不存在则返回None'''
        try:
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
        except:
            return None

    def find_elem_is_clickableByXPATH(self, locator, timeout=5):
        '''判断5s内，定位的元素是否可见并且可以点击。存在则返回元素，不存在则返回None'''
        try:
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, locator)))
        except:
            return None

    def is_element_visible(self, locator, timeout=3, ):
        '''判断元素是否可见，可见Ture or 不可见False'''
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            return True
        except:
            return False

    def is_element_in_dom(self, locator, timeout=5):
        '''判断5s内，定位的元素是否存在dom结构里。存在则返回Ture，不存在则返回False'''
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
            return True
        except:
            return False

    def wait_element_presence_(self, locator, timeout=5):
        '''等待元素出现'''
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        except TimeoutException as ex:
            print('wait_element_presence_ 异常：%s 获取 %s 超时' % (ex, locator))

    def wait_elem_visible(self, locator, timeout=5):
        # 一直等待某元素可见，默认超时3秒只做等待动作不返回值
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        except TimeoutException as ex:
            print('wait_elem_visible 异常：%s 获取 %s 超时' % (ex, locator))

    def wait_elem_disappearByCSS(self, locator, timeout=3):
        # 一直等待某个元素消失，默认超时3秒只做等待动作不返回值
        try:
            WebDriverWait(self.driver, timeout).until_not(
                EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        except TimeoutException as ex:
            print('wait_elem_visible 异常：%s 获取 %s 超时' % (ex, locator))

    def wait_elem_disappearByXPATH(self, locator, timeout=3):
        # 一直等待某个元素消失，默认超时3秒只做等待动作不返回值
        try:
            WebDriverWait(self.driver, timeout).until_not(
                EC.visibility_of_element_located((By.XPATH, locator)))
        except TimeoutException as ex:
            print('wait_elem_visible 异常：%s 获取 %s 超时' % (ex, locator))

    def is_alert_exist(self):
        '''判断页面上是否存在alert,如果有就切换到alert并返回alert的内容'''
        try:
            instance = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            print('存在警告框')
            return instance.text
        except:
            return False

    def is_alert_present(self):
        '''判断页面上是否存在alert,如果有就返回Ture,否则返回False'''
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            return True
        except:
            return False

    def scroll_to_target_element(self, element):
        '''传入元素，滚动到目标元素的位置'''
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
        except:
            time.sleep(0.5)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def is_and_switch_to_iframe(self, locator, timeout=3):
        '''判断是否存在iframe,存在则切进去，不返回值'''
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, locator)))
        except TimeoutException:
            print('无法切到 %s ifarme' % locator)

    def is_text_in_element(self, locator, text):
        '''判断某个元素中的text是否 包含 了预期的字符串'''
        return EC.text_to_be_present_in_element((By.CSS_SELECTOR, locator), text)

    def wait_elem_remove_dom(self, locator, timeout=3):
        '''等待元素从dom中移除，常用于判页面是否已刷新'''
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.staleness_of((By.CSS_SELECTOR, locator)))
        except TimeoutException:
            print('无法切到 %s ifarme' % locator)

    def is_elem_invisibility(self, locator, timeout=3):
        '''判断元素是否不可见，不可见返回Ture, 可见返回False------常用于判断元素是否隐藏'''
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, locator)))
            return True
        except TimeoutException:
            return False

    def wait_elem_invisibility(self, locator, timeout=3):
        '''等待元素不可见，但仍存在于dom'''
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located((By.XPATH, locator)))
        except TimeoutException:
            print('元素一直可见')

####点击元素方法
    @retry(stop_max_attempt_number=5,wait_fixed = 2000)
    def clickElemByXpath_Visibility(self, locator, timeout=2):
        '''点击单个可见元素Xpath'''
        elem = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        self.driver.execute_script ("arguments[0].scrollIntoView();", elem)
        elem.click()

    @retry(stop_max_attempt_number=5,wait_fixed = 2000)
    def clickElemByXpath_Presence(self, locator, timeout=2):
        '''点击单个存在dom的元素Xpath'''
        elem = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, locator)))
        self.driver.execute_script ("arguments[0].scrollIntoView();", elem)
        elem.click()


    @retry(stop_max_attempt_number=5,wait_fixed = 2000)
    def clickElemByCSS_Visibility(self, locator, timeout=2):
        '''点击单个可见元素CSS'''
        elem = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        self.driver.execute_script ("arguments[0].scrollIntoView();", elem)
        elem.click()

    @retry(stop_max_attempt_number=5,wait_fixed = 2000)
    def clickElemByCSS_Presence(self, locator, timeout=2):
        '''点击单个存在dom的元素CSS'''
        elem = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        self.driver.execute_script ("arguments[0].scrollIntoView();", elem)
        elem.click()


    @retry(stop_max_attempt_number=5,wait_fixed = 2000)
    def clickElemsByCSS_Visibility(self, locator, num=0,timeout=2):
        '''点击可见元素组里的某个元素CSS'''
        elems = WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, locator)))
        self.driver.execute_script ("arguments[0].scrollIntoView();", elems[num])
        elems[num].click()


    @retry(stop_max_attempt_number=5,wait_fixed = 2000)
    def clickElemsByCSS_Presence(self, locator,num=0,timeout=2):
        '''点击存在dom里的元素组里的某个元素CSS'''
        elems = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, locator)))
        self.driver.execute_script ("arguments[0].scrollIntoView();", elems[num])
        elems[num].click()

####元素写值方法

    @retry(stop_max_attempt_number=5,wait_fixed = 2000)
    def sendkeysElemByXpath_Visibility(self, locator,key, timeout=2):
        '''给一个可见元素写入值Xpath'''
        elem = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        self.driver.execute_script ("arguments[0].scrollIntoView();", elem)
        elem.send_keys(key)



    @retry(stop_max_attempt_number=5,wait_fixed = 2000)
    def sendkeysElemByXpath_Presence(self, locator,key, timeout=2):
        '''给一个存在dom的元素写入值Xpath'''
        elem = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, locator)))
        self.driver.execute_script ("arguments[0].scrollIntoView();", elem)
        elem.send_keys(key)


    @retry(stop_max_attempt_number=5,wait_fixed = 2000)
    def sendkeysElemByCSS_Visibility(self, locator,key, timeout=2):
        '''给一个可见元素写入值CSS'''
        elem = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        self.driver.execute_script ("arguments[0].scrollIntoView();", elem)
        elem.send_keys(key)

    @retry(stop_max_attempt_number=5,wait_fixed = 2000)
    def sendkeysElemsByCSS_Visibility(self, locator,key,num=0, timeout=2):
        '''给可见的元素组里的某个元素写入值CSS'''
        elems = WebDriverWait(self.driver, timeout).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, locator)))
        self.driver.execute_script ("arguments[0].scrollIntoView();", elems[num])
        elems[num].send_keys(key)

    @retry(stop_max_attempt_number=5,wait_fixed = 2000)
    def sendkeysElemByCSS_Presence(self, locator,key, timeout=2):
        '''给存在dom里的元素组里的某个元素写入值CSS'''
        elem = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        self.driver.execute_script ("arguments[0].scrollIntoView();", elem)
        elem.send_keys(key)

    @retry(stop_max_attempt_number=5,wait_fixed = 2000)
    def sendkeysElemsByCSS_Presence(self, locator,key,num=0,timeout=2):
        '''给存在dom里的元素组里的某个元素写入值CSS'''
        elems = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, locator)))
        self.driver.execute_script ("arguments[0].scrollIntoView();", elems[num])
        elems[num].send_keys(key)

##################
    # 查找元素方法
    def find_elemByCSS(self, locator, timeout=5):
        '''判断5s内，定位的元素是否存在dom结构里。存在则返回元素，不存在则返回None'''
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        except:
            return None


    def find_elemByXPATH(self, locator, timeout=5):
        '''判断5s内，定位的元素是否存在dom结构里。存在则返回元素，不存在则返回None'''
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, locator)))
        except:
            return None


    def find_elemsByCSS(self, locator, timeout=5):
        '''判断5s内，定位的一组元素是否存在dom结构里。存在则返回元素列表，不存在则返回None'''
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, locator)))
        except:
            return None

    def find_elemsByXPATH(self, locator, timeout=5):
        '''判断5s内，定位的一组元素是否存在dom结构里。存在则返回元素列表，不存在则返回None'''
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.XPATH, locator)))
        except:
            return None


