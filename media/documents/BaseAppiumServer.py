import os
import platform
import socket
import subprocess
import time
import urllib.request
from multiprocessing import Process
from urllib.error import URLError

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
import threading


class AppiumServer:
    def __init__(self, kwargs=None):
        self.kwargs = kwargs

    def start_server(self):
        """start the appium server
        """

        cmd = "appium"
        print(cmd)
        if platform.system() == "Windows":
            t1 = RunServer(cmd)
            p = Process(target=t1.start())
            p.start()
            while True:
                print("--------start_win_server-------------")
                if self.win_is_runnnig("http://127.0.0.1:4723" + "/wd/hub" + "/status"):
                    print("-------win_server--------------")
                    break
        else:
            appium = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1,
                                      close_fds=True)
            while True:
                appium_line = appium.stdout.readline().strip().decode()
                time.sleep(1)
                print("---------start_server----------")
                if 'listener started' in appium_line or 'Error: listen' in appium_line:
                    print("----server_success---")
                    break

    def win_is_runnnig(self, url):
        """Determine whether server is running
        :return:True or False
        """
        response = None
        time.sleep(1)
        try:
            response = urllib.request.urlopen(url, timeout=5)

            if str(response.getcode()).startswith("2"):
                return True
            else:
                return False
        except URLError:
            return False
        except socket.timeout:
            return False
        finally:
            if response:
                response.close()

    def stop_server(self):
        sysstr = platform.system()

        if sysstr == 'Windows':
            os.popen("taskkill /f /im node.exe")

    def re_start_server(self):
        """reStart the appium server
        """

        pass


class RunServer(threading.Thread):
    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd

    def run(self):
        os.system(self.cmd)


if __name__ == "__main__":
    pass
