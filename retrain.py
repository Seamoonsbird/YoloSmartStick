import os
import glob
import multiprocessing
from ultralytics import YOLO

def find_latest_model(base_dirs=("runs/segment", "runs/detect")):
    candidates = []
    for base in base_dirs:
        base = os.path.normpath(base)
        train_dirs = glob.glob(os.path.join(base, "train*"))
        for d in train_dirs:
            for filename in ["last.pt"]:
                pt_path = os.path.join(d, "weights", filename)
                if os.path.exists(pt_path):
                    candidates.append(pt_path)
    if not candidates:
        for pt in glob.glob("runs/**/last.pt", recursive=True):
            candidates.append(pt)
    if not candidates:
        raise FileNotFoundError("未找到任何训练权重，请确认 'runs/segment/train*' 下存在 last.pt")
    latest = max(candidates, key=os.path.getmtime)
    return latest

if __name__ == '__main__':
    multiprocessing.freeze_support()   # 可选但推荐
    model_path = find_latest_model()
    print(f"✅ 使用模型: {model_path}")
    model = YOLO(model_path)
    results = model.train(resume=True)