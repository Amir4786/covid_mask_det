import setuptools
with open("README.md", "r", encoding="utf-8") as f:
    long_description= f.read()
__version__="0.0.0"
REPO_NAME="COVID_MASK_DET"
AUTHOR_USER_NAME="Amir4786"
SRC_REPO="Covid_Detection"
AUTHOR_EMAIL="er.a.khan47@gmail.com"
setuptools.setup(
    name= SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="This project is created on Covid safety guidlines",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={"Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"},
    package_dir={"":"src"},
    packages= setuptools.find_packages(where="src")
)