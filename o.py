import json
import os
import requests
import shutil

# 删除已存在的 versionlist 文件夹
if os.path.exists("versionlist"):
    shutil.rmtree("versionlist")

# 下载 versionList.json 文件
url = "https://bmclapi2.bangbang93.com/optifine/versionList"
response = requests.get(url)
version_list = response.json()

# 保存 versionList.json 文件
with open("versionlist.json", "w") as file:
    json.dump(version_list, file)

# 创建文件夹 versionlist
os.mkdir("versionlist")

# 遍历 versionList.json 中的每个元素
for version_entry in version_list:
    # 读取 versionList.json 的 forge 值
    forge_value = version_entry.get("forge")
    helpforge = ""
    if forge_value is None or forge_value == "Forge N/A":
        helpforge = "nohelp"
    elif "#" in forge_value:
        mcversion_value = version_entry.get("mcversion")
        forge_url = f"https://bmclapi2.bangbang93.com/forge/minecraft/{mcversion_value}"
        forge_response = requests.get(forge_url)
        forge_list = forge_response.json()
        for forge_entry in forge_list:
            forge_build = str(forge_entry.get("build"))
            if forge_build and forge_build.split(".")[-1] == forge_value.split("#")[-1]:
                helpforge = f"Forge {forge_entry.get('version')}"
                break
    else:
        helpforge = forge_value

    # 读取 versionList.json 的 mcversion、type、patch 值
    mcversion_value = version_entry.get("mcversion")
    type_value = version_entry.get("type")
    patch_value = version_entry.get("patch")

    # 创建并写入文本文件
    file_name = f"{mcversion_value}-{type_value}_{patch_value}.md"
    file_path = os.path.join("versionlist", file_name)
    with open(file_path, "w") as file:
        if helpforge == "nohelp":
            file.write(f"# {mcversion_value} {type_value}_{patch_value} 不支持**任何** Forge 版本\n\n")
            file.write("### 你需要在 HMCL 的 `版本设置` -> `自动安装` 中卸载 Optifine 或 Forge。\n")
        else:
            file.write(f"# {mcversion_value} {type_value}_{patch_value} 支持 {helpforge} 版本\n\n")
            file.write("### 你需要在 HMCL 的 `版本设置` -> `自动安装` 中调整 Optifine 版本（和）或 Forge 版本。\n")
