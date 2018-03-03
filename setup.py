from cx_Freeze import setup, Executable

setup(
    name = "PF_Stream",
    version = "0.1",
    description = "PonyFiction_Stream",
    executables = [Executable("main.py")]
)