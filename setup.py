from setuptools import setup, find_packages
from typing import List


PROJECT_NAME = "ML Project"
VERSION = "0.0.1"
DESCRIPTION = "First Machine Learning Project"
AUTHOR = "Pallavi Jagre"
AUTHOR_EMAIL = "pallavijagre123@gmail.com"

REQUIREMENTS_FILE_NAME = "requirements.txt"

HYPHEN_E_DOT = "-e ."


# open requirements.txt
# read reauirements.txt line by line
# replace \n with ""

def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
    
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    
    return requirement_list



from distutils.core import setup

setup(name= PROJECT_NAME,
      version= VERSION,
      description= DESCRIPTION,
      author= AUTHOR,
      author_email= AUTHOR_EMAIL,
      packages= find_packages(),
      install_requires = get_requirements_list()
     )