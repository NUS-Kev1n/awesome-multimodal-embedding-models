import torch
from transformers import AutoImageProcessor, Dinov2Model
from PIL import Image
import sys
import requests
import time
import psutil
import os

def get_gpu_memory_usage():
    """
    获取当前GPU内存使用情况
    
    Returns:
        float: GPU内存使用量（MB），如果GPU不可用则返回0
    """
    if torch.cuda.is_available():
        return torch.cuda.memory_allocated() / 1024**2  # 将字节转换为MB
    return 0

def extract_image_features(image_url):
    """
    从图像URL提取特征向量
    
    Args:
        image_url (str): 图像的URL地址
        
    Returns:
        dict: 包含以下键的字典：
            - cls_features: CLS token的特征向量
            - patch_features: 图像patch的特征向量
            - extraction_time: 特征提取耗时
            - gpu_memory: GPU内存使用量
        如果发生错误则返回None
    """
    try:
        # 设置设备为GPU，如果不可用则使用CPU
        device = torch.device('cuda' if torch.cuda.is_available() else "cpu")
        print(f"Using device: {device}")
        
        # 如果使用GPU，打印CUDA相关信息
        if device == "cuda":
            print(f"CUDA version: {torch.version.cuda}")
            print(f"cuDNN version: {torch.backends.cudnn.version()}")
        
        # 加载预训练的DINOv2模型和图像处理器
        processor = AutoImageProcessor.from_pretrained('facebook/dinov2-base', use_fast=True)
        model = Dinov2Model.from_pretrained('facebook/dinov2-base').to(device)

        # 从URL下载并打开图像
        image = Image.open(requests.get(image_url, stream=True).raw)
        
        # 记录特征提取开始时间
        start_time = time.time()
        
        # 使用torch.no_grad()上下文管理器进行推理，不计算梯度
        with torch.no_grad():
            # 使用处理器处理图像，转换为PyTorch张量，并移至相应设备
            inputs = processor(images=image, return_tensors="pt").to(device)
            # 通过模型获取输出
            outputs = model(**inputs)
            
            # 提取CLS token特征（用于整体图像表示）和patch特征（用于局部区域表示）
            cls_features = outputs.last_hidden_state[:, 0]  # CLS token特征
            patch_features = outputs.last_hidden_state[:, 1:]  # patch级别的token特征
            
            # 记录特征提取结束时间和GPU内存使用情况
            end_time = time.time()
            gpu_memory = get_gpu_memory_usage()
            
            # 打印性能指标
            print(f"Feature extraction time: {end_time - start_time:.4f} seconds")
            print(f"GPU memory usage: {gpu_memory:.2f} MB")
            print(f"CLS features shape: {cls_features.shape}")
            print(f"Patch features shape: {patch_features.shape}")
            
            # 返回提取的特征和性能指标
            return {
                'cls_features': cls_features,
                'patch_features': patch_features,
                'extraction_time': end_time - start_time,
                'gpu_memory': gpu_memory
            }
            
    except Exception as e:
        print(f"Error in feature extraction: {str(e)}")
        return None

if __name__ == "__main__":
    try:
        # 测试图片URL
        image_url = "https://hf-mirror.com/geolocal/StreetCLIP/resolve/main/sanfrancisco.jpeg"
        # 提取图像特征
        features = extract_image_features(image_url)
        if features is not None:
            print("Features extracted successfully")
            # 打印提取的特征信息
            # print("CLS features:", features['cls_features'])
            # print("Patch features mean:", features['patch_features'].mean(dim=1))
    except Exception as e:
        print(f"Error in main execution: {str(e)}")
        sys.exit(1)
