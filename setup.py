# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


def get_files(path):
    import os
    dir_name = os.path.join(os.getcwd(), path)
    dir_list = [x[0] for x in os.walk(dir_name)]

    files = []
    for dir in dir_list:
        if ("__pycache__" not in dir) and sum([True for x in os.listdir(dir) if x.endswith('.py')]) > 0:
            files.append(os.path.join(dir, "*.py"))
    return files


setup(name='chatAgent',
      version='0.1',
      description='',
      package_dir={"": "src"},
      packages=find_packages("src"),
      zip_safe=False,
      include_package_data=True
      )
