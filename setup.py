from setuptools import setup, find_packages

setup(
    name="singtown_ai_mock_server",
    version="0.4.2",
    packages=find_packages(),
    install_requires=["Flask", "singtown_ai"],
    package_data={
        "singtown_ai_mock_server": ["media/**/*", "projects/*.json"],
    },
)
