#!/usr/bin/python
"""
Purpose: working with calculator application
"""

from subprocess import Popen

from pywinauto import Desktop

Popen("calc.exe", shell=True)

dlg = Desktop(backend="uia").Calculator

dlg.wait("visible")
