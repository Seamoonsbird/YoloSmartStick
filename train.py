# from ultralytics import YOLO

# # Load a model
# model = YOLO("yolo11n-seg.pt")  # load a pretrained model (recommended for training)

# # Train the model
# results = model.train(data="data\dataset.yaml", epochs=100, imgsz=640, device=0)
from ultralytics import YOLO

# 导入语句和函数定义可以放在外面
# ...

# 关键：将训练逻辑放入这个判断语句中
if __name__ == '__main__':
    # 加载模型
    model = YOLO('yolo26n-seg.pt')
    # 开始训练
    results = model.train(data='data\dataset.yaml', epochs=100, batch=8)