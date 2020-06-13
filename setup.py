from setuptools import setup, find_packages

setup(
    name="UITestsOpencart",
    version="1.4",
    packages=find_packages(),
    package_data={
        "": ["*.json", "*.jpg", "*.txt", "README.md", "docker-compose.yml", "Dockerfile", "Jenkinsfile"]
    },
    author="agrigoreva",
    description="UI Tests for Opencart",
    url="https://github.com/lousdanl/otus_ui_tests_opencart"
)
