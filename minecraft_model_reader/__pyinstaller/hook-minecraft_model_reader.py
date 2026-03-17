from PyInstaller.utils.hooks import collect_data_files, collect_submodules

hiddenimports = collect_submodules("minecraft_model_reader")

datas = collect_data_files(
    "minecraft_model_reader",
    includes=[
        "**/*.png",
        "**/*.json",
        "**/*.mcmeta",
    ],
)
