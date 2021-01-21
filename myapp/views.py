import os
import unittest

from django.shortcuts import redirect, render

from media.base.BaseAdb import AndroidDebugBridge
from media.base.BaseAppiumServer import AppiumServer
from media.base.BaseRunner import ParametrizedTestCase
from media.tests.test_appium import EribankTest
from .forms import DocumentForm
from .models import Document

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def my_view(request):
    print(f"Great! You're using Python 3.6+. If you fail here, use the right version.")
    message = 'Upload as many files as you want!'
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'], name=request.POST['name'],
                              class_name=request.POST['class_name'])
            newdoc.save()

            # Redirect to the document list after POST
            return redirect('my-view')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm()  # An empty, unbound form

    # Load base for the list page
    documents = Document.objects.all()

    # Render list page with the base and the form
    context = {'base': documents, 'form': form, 'message': message}
    return render(request, 'list.html', context)


def kill_adb():
    os.system(PATH("../media/base/kill5037.bat"))
    os.system("adb start-server")


def runnerPool(device):
    _initApp = {}
    _initApp['deviceName'] = device[0]
    _initApp['platformVersion'] = '10'
    _initApp["platformName"] = "android"
    _initApp["automationName"] = "uiautomator2"
    _initApp["appPackage"] = 'com.experitest.ExperiBank'
    _initApp["appActivity"] = 'com.experitest.ExperiBank.LoginActivity'
    _initApp['unicodeKeyboard'] = True
    _initApp['resetKeyboard'] = True
    _initApp['androidScreenshotPath'] = '/storage/emulated/0/Pictures/Screenshots/'

    runnerCaseApp(_initApp)


def runnerCaseApp(device):
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(EribankTest, param=device))
    unittest.TextTestRunner(verbosity=2).run(suite)


def run_view(request):
    kill_adb()
    device = AndroidDebugBridge().attached_devices()
    appium_server = AppiumServer()
    appium_server.start_server()
    runnerPool(device)
    appium_server.stop_server()
    return render(request, 'list.html')
