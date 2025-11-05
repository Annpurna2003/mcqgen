from setuptools import setup, find_packages
setup(
    name="mcqgen",
    version="0.0.1",
    author="Annpurna Srivastava",
    author_email="anusri22112003@gmail.com",
    install_requires=[
        "openai","langchain","streamlit","python-dotenv","pypdf2"   ],
    packages=find_packages()
)