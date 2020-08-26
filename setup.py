from setuptools import setup, find_packages

setup()
setup(
      name="hm_message",
      version="1.0",
      description="My test module",
      author="杜畅",
      url="http://www.csdn.net",
      py_modules = ["hm_message.send_message",
                    "hm_message.receice_message"]
      )