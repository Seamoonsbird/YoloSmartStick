import os
import glob
from ultralytics import YOLO

def find_latest_model(base_dirs=("runs/segment", "runs/detect")):
    candidates = []
    for base in base_dirs:
        # 处理不同操作系统下的路径分隔符
        base = os.path.normpath(base)
        # 匹配 train, train2, train3... 等目录
        train_dirs = glob.glob(os.path.join(base, "train*"))
        for d in train_dirs:
            for filename in ["last.pt"]:
                pt_path = os.path.join(d, "weights", filename)
                if os.path.exists(pt_path):
                    candidates.append(pt_path)
    if not candidates:
    # 兜底只搜索名为 last.pt 的文件
        for pt in glob.glob("runs/**/last.pt", recursive=True):
            candidates.append(pt)
    if not candidates:
        raise FileNotFoundError("未找到任何训练权重，请确认 'runs/segment/train*' 下存在 best.pt 或 last.pt")
    latest = max(candidates, key=os.path.getmtime)
    return latest

# 加载模型并恢复训练
model_path = find_latest_model()
print(f"✅ 使用模型: {model_path}")
model = YOLO(model_path)
results = model.train(resume=True)
