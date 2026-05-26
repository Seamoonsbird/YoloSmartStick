#使用说明：
# 将27行的变量值改成你上次最后一张照片的号码(即已有的照片数，第一次填0)
# 将33行的new_name = f"blind_path[{count}].jpg"中的blind_path改成你的标签
# 将48行的target_folder = r"D:\\programs\\YoloSmartStick_local\\labelme_data"中的文件夹地址改成你的文件夹地址
# 为了防止对原有数据产生影响，建议在新建文件夹重命名后copy到主文件夹

import os

def rename_jpg_files(folder_path):
    """
    批量重命名文件夹中的jpg文件为 blind_path[x].jpg
    :param folder_path: 目标文件夹的路径
    """
    # 检查文件夹是否存在
    if not os.path.isdir(folder_path):
        print(f"错误：文件夹 {folder_path} 不存在！")
        return

    # 筛选出文件夹中所有后缀为 .jpg 的文件（不区分大小写）
    jpg_files = [f for f in os.listdir(folder_path) if f.lower().endswith(".jpg")]
    
    # 如果没有找到jpg文件，直接退出
    if not jpg_files:
        print("未找到任何jpg文件！")
        return

    # 开始重命名，数字从(begin+1)开始
    begin = 61
    count = 1
    for filename in jpg_files:
        # 构建文件的完整路径
        old_path = os.path.join(folder_path, filename)
        # 新文件名
        new_name = f"blind_path[{count+begin}].jpg"
        new_path = os.path.join(folder_path, new_name)

        # 重命名文件
        os.rename(old_path, new_path)
        print(f"已重命名：{filename} -> {new_name}")
        count += 1

    print(f"\n完成！总共重命名了 {count-1} 个文件")

# ====================== 使用方法 ======================
if __name__ == "__main__":
    # 1. 把下面的 文件夹路径 替换成你自己的文件夹地址
    # 示例 Windows："C:\\Users\\Name\\Pictures"
    # 示例 Mac/Linux："/Users/Name/Pictures"
    target_folder = r"D:\\programs\\YoloSmartStick_local\\labelme_data"

    # 执行重命名
    rename_jpg_files(target_folder)