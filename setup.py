# Dummy setup.py to install cpplint properly.
try:
    from setuptools import setup
except ImportError:
    raise ImportError(
        "'setuptools' is required but not installed. To install it, "
        "follow the instructions at "
        "https://pip.pypa.io/en/stable/installing/#installing-with-get-pip-py"
    )

install_req = ["cpplint"]

setup(
    name="dummy-cpplint-setup",
    version="0",
    author="Ben Morcos",
    license="MIT",
    description="Dummy setup for cpp pre-commit hooks",
    install_requires=install_req,
)
