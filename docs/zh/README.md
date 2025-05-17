[EN](../en/README.md)|[ZH](README.md)
# 多模态嵌入模型总结

本项目收集和整理了各种多模态嵌入模型的详细信息，包括模型型号、输出维度和使用说明等。

## 模型系列

### 通用嵌入模型 (General Embedding Models)

#### 视觉嵌入模型 (Visual Embedding Models)
1. [ViT系列](general_embedding/visual_embedding/vit_series/README.md)
   - vit-base-patch16-224-in21k
   - vit-huge-patch14-224-in21k

2. [DINO系列](general_embedding/visual_embedding/dino_series/README.md)
   - DINOv2系列 (small, base, large, giant)
   - WebSSL-DINO系列 (1b-7b各种变体)

### 专用嵌入模型 (Special Embedding Models)
1. [街景专用模型系列](special_embedding/street/README.md)
   - StreetCLIP

#### 跨模态嵌入模型 (Cross-modal Embedding Models)
1. [SigLiP系列](general_embedding/cross_modal_embedding/siglip_series/README.md)
   - siglip2-giant-opt-patch16-384

2. [InternViT系列](general_embedding/cross_modal_embedding/internvit_series/README.md)
   - InternViT-300M-448px-V2_5

3. [Gme-Qwen系列](general_embedding/cross_modal_embedding/gme_qwen_series/README.md)
   - gme-Qwen2-VL-7B-Instruct

## 使用说明

每个系列的具体信息请查看对应目录下的README.md文件。

## 目录结构

```
.
├── docs/                     # 文档目录
│   ├── general_embedding/    # 通用嵌入模型
│   │   ├── visual_embedding/ # 视觉嵌入模型
│   │   │   ├── vit_series/   # ViT系列
│   │   │   └── dino_series/  # DINO系列
│   │   │
│   │   └── cross_modal_embedding/ # 跨模态嵌入模型
│   │       ├── siglip_series/    # SigLiP系列
│   │       ├── internvit_series/ # InternViT系列
│   │       └── gme_qwen_series/  # Gme-Qwen系列
│   │
│   └── special_embedding/    # 专用嵌入模型
│       └── street_clip_series/   # 街景专用模型系列
│
└── README.md
```

## 评估指标

评估多模态嵌入模型的主要指标包括：

- 跨模态检索准确率（Cross-modal Retrieval Accuracy）
- 零样本分类准确率（Zero-shot Classification Accuracy）
- 语义相似度相关性（Semantic Similarity Correlation）
- 计算效率（Computational Efficiency）
- 模型大小（Model Size）

## 应用场景

多模态嵌入模型在以下场景中发挥着重要作用：

1. 大模型RAG（检索增强生成）
   - 私有化知识库向量化
   - 多模态知识检索增强
   - 跨模态语义对齐

2. 跨模态检索与匹配
   - 文本到图像搜索
   - 图像到文本搜索
   - 多模态语义匹配

3. 零样本学习与分类
   - 图像分类与识别
   - 视频场景理解
   - 跨模态迁移学习

4. 多模态内容理解
   - 视频理解与分析
   - 多模态问答系统
   - 场景语义解析

5. 智能推荐系统
   - 跨模态内容推荐
   - 个性化搜索排序
   - 用户兴趣建模

## 贡献指南

欢迎贡献新的模型、评估结果或改进建议！请遵循以下步骤：

1. Fork 本仓库
2. 创建新的分支
3. 提交你的更改
4. 发起 Pull Request

## 许可证

MIT License

## 致谢

感谢所有开源社区的研究者和开发者，他们的工作为多模态AI领域做出了重要贡献。 