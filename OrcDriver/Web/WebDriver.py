# coding=utf-8
import json
import socket
import time

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException

from OrcDriver.Web.Widget.OrcWidget import OrcWidget
from OrcDriver.Web.Widget.WidgetButton import WidgetButton
from OrcDriver.Web.Widget.WidgetInput import WidgetInput
from OrcDriver.Web.Widget.WidgetA import WidgetA
from OrcLib.LibLog import OrcLog
from WebDriverService import WebDriverService


class DriverSelenium:

    def __init__(self, p_ip, p_port):

        self.__logger = OrcLog("driver")
        self.__service = WebDriverService()

        self.__browser = "FIREFOX"  # 浏览器
        self.__env = "TEST"  # 环境

        self.__window = None  # 当前窗口
        self.__root = None  # 根节点

        self.__objects = {}  # 存储出现过的对象

        self.__ip = p_ip
        self.__port = int(p_port)

    def start(self):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.__ip, self.__port))
        sock.listen(1)

        while True:

            connection, address = sock.accept()

            try:
                connection.settimeout(5)

                _cmd = connection.recv(1024)
                _result = self.__execute(json.loads(_cmd))

                connection.send(str(_result))

            except socket.timeout:
                self.__logger.error("time out")
            except Exception, err:
                self.__logger.error(err)

            connection.close()

    def __execute(self, p_cmd):
        """
        执行调用
        :param p_cmd: {TYPE, PARA, OPERATE}
        :return:
        """
        self.__logger.debug(p_cmd)

        _type = p_cmd["TYPE"]

        if "PAGE" == _type:
            _status = self.__get_page(p_cmd)
        elif "WIDGET" == _type:
            _status = self.__action(p_cmd)
        else:
            _status = False
            self.__logger.error("Wrong type %s." % _type)

        return _status

    def __action(self, p_para):

        _id = p_para["OBJECT"]
        _definition = self.__service.widget_get_definition(_id)

        # 输入框
        if "INP" == _definition.widget_type:
            _node = WidgetInput(self.__root, _id)
            _node.execute(p_para)

        # Button
        elif "BTN" == _definition.widget_type:
            _node = WidgetButton(self.__root, _id)
            _node.execute(p_para)

        # <a href>
        elif "A" == _definition.widget_type:
            _node = WidgetA(self.__root, _id)
            _node.execute(p_para)

        # 自定义控件
        else:
            _node = OrcWidget(self.__root, _id)
            _node.basic_execute(p_para)

        return True

    def __get_page(self, p_para):
        """
        打开浏览器
        :param p_para: {BROWSER, ID, ENV, OPERATION}
        :return:
        """
        self.__logger.debug(p_para)

        self.__browser = "FIREFOX" if "BROWSER" not in p_para else p_para["BROWSER"]
        self.__env = "TEST" if "ENV" not in p_para else p_para["ENV"]
        _page_det_id = p_para["OBJECT"]
        _page_operation = p_para["OPERATION"]

        if self.__root is None:

            try:

                if "IE" == self.__browser:
                    self.__root = webdriver.Ie()
                elif "FIREFOX" == self.__browser:
                    self.__root = webdriver.Firefox()
                elif "CHROME" == self.__browser:
                    self.__root = webdriver.Chrome()
                else:
                    pass

            except WebDriverException:
                self.__logger.error("Open browser failed.")

        if "GET" == _page_operation:
            # 设置加载时间
            self.__root.set_page_load_timeout(10)

            # 获取 URL
            _url = self.__service.page_get_url(self.__env, _page_det_id)

            # 打开界面
            try:
                self.__root.get(_url)
            except TimeoutException:
                pass

        elif "MAX" == _page_operation:
            self.__root.maximize_window()

        return self.__root is not None

    def save_screen(self, p_file):

        time.sleep(0.5)
        self.__root.save_screenshot(p_file)




