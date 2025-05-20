[EN](../../../../en/general_embedding/visual_embedding/dino_series/README.md) | [ZH](README.md)

# DINO 系列

## dinov2系列

### dinov2-small

模型：facebook/dinov2-small

输出嵌入维度：
- CLS feature: 384
- Patch feature: (256,384)

Hugging Face：[facebook/dinov2-small](https://huggingface.co/facebook/dinov2-small)

GitHub：[facebookresearch/dinov2](https://github.com/facebookresearch/dinov2)

代码：[test_dinov2-small.py](../../../../../code/general_embedding/visual_embedding/dino_series/test_dinov2-small.py)

输出：
```
Feature extraction time: 1.9590 seconds
GPU memory usage: 93.21 MB
CLS features shape: torch.Size([1, 384])
Patch features shape: torch.Size([1, 256, 384])
Features extracted successfully
```

---

### dinov2-base

模型：facebook/dinov2-base

输出嵌入维度：
- CLS feature: 768
- Patch feature: (256,768)

Hugging Face：[facebook/dinov2-base](https://huggingface.co/facebook/dinov2-base)

GitHub：[facebookresearch/dinov2](https://github.com/facebookresearch/dinov2)

代码：[test_dinov2-base.py](../../../../../code/general_embedding/visual_embedding/dino_series/test_dinov2-base.py)

输出：
```
Feature extraction time: 2.0362 seconds
GPU memory usage: 340.49 MB
CLS features shape: torch.Size([1, 768])
Patch features shape: torch.Size([1, 256, 768])
Features extracted successfully
```

---

### dinov2-large

模型：facebook/dinov2-large

输出嵌入维度：
- CLS feature: 1024
- Patch feature: (256,1024)

Hugging Face：[facebook/dinov2-large](https://huggingface.co/facebook/dinov2-large)

GitHub：[facebookresearch/dinov2](https://github.com/facebookresearch/dinov2)

---

### dinov2-giant

模型：facebook/dinov2-giant

输出嵌入维度：
- CLS feature: 1536
- Patch feature: (256,1536)

Hugging Face：[facebook/dinov2-giant](https://huggingface.co/facebook/dinov2-giant)

GitHub：[facebookresearch/dinov2](https://github.com/facebookresearch/dinov2)

---

## webssl-dino 系列

### webssl-dino1b-full2b-224

模型：facebook/webssl-dino1b-full2b-224

输出嵌入维度：
- CLS feature: 1536
- Patch feature: (256,1536)

Hugging Face：[facebook/webssl-dino1b-full2b-224](https://huggingface.co/facebook/webssl-dino1b-full2b-224)

GitHub：[facebookresearch/dinov2](https://github.com/facebookresearch/dinov2)

---

### webssl-dino2b-full2b-224

模型：facebook/webssl-dino2b-full2b-224

输出嵌入维度：
- CLS feature: 2688
- Patch feature: (256,2688)

Hugging Face：[facebook/webssl-dino2b-full2b-224](https://huggingface.co/facebook/webssl-dino2b-full2b-224)

GitHub：[facebookresearch/dinov2](https://github.com/facebookresearch/dinov2)

---

### webssl-dino2b-light2b-224

模型：facebook/webssl-dino2b-light2b-224

输出嵌入维度：
- CLS feature: 2688
- Patch feature: (256,2688)

Hugging Face：[facebook/webssl-dino2b-light2b-224](https://huggingface.co/facebook/webssl-dino2b-light2b-224)

GitHub：[facebookresearch/dinov2](https://github.com/facebookresearch/dinov2)

---

### webssl-dino2b-heavy2b-224

模型：facebook/webssl-dino2b-heavy2b-224

输出嵌入维度：
- CLS feature: 2688
- Patch feature: (256,2688)

Hugging Face：[facebook/webssl-dino2b-heavy2b-224](https://huggingface.co/facebook/webssl-dino2b-heavy2b-224)

GitHub：[facebookresearch/dinov2](https://github.com/facebookresearch/dinov2)

---

### webssl-dino3b-light2b-224

模型：facebook/webssl-dino3b-light2b-224

输出嵌入维度：
- CLS feature: 3072
- Patch feature: (256,3072)

Hugging Face：[facebook/webssl-dino3b-light2b-224](https://huggingface.co/facebook/webssl-dino3b-light2b-224)

GitHub：[facebookresearch/dinov2](https://github.com/facebookresearch/dinov2)

---

### webssl-dino3b-heavy2b-224

模型：facebook/webssl-dino3b-heavy2b-224

输出嵌入维度：
- CLS feature: 3072
- Patch feature: (256,3072)

Hugging Face：[facebook/webssl-dino3b-heavy2b-224](https://huggingface.co/facebook/webssl-dino3b-heavy2b-224)

GitHub：[facebookresearch/dinov2](https://github.com/facebookresearch/dinov2)

---

### webssl-dino7b-full8b-224

模型：facebook/webssl-dino7b-full8b-224

输出嵌入维度：
- CLS feature: 4096
- Patch feature: (256,4096)

Hugging Face：[facebook/webssl-dino7b-full8b-224](https://huggingface.co/facebook/webssl-dino7b-full8b-224)

GitHub：[facebookresearch/dinov2](https://github.com/facebookresearch/dinov2)

---

### webssl-dino7b-full8b-378

模型：facebook/webssl-dino7b-full8b-378

输出嵌入维度：
- CLS feature: 4096
- Patch feature: (729,4096)

Hugging Face：[facebook/webssl-dino7b-full8b-378](https://huggingface.co/facebook/webssl-dino7b-full8b-378)

GitHub：[facebookresearch/dinov2](https://github.com/facebookresearch/dinov2)

---

### webssl-dino7b-full8b-518

模型：facebook/webssl-dino7b-full8b-518

输出嵌入维度：
- CLS feature: 4096
- Patch feature: (1369,4096)

Hugging Face：[facebook/webssl-dino7b-full8b-518](https://huggingface.co/facebook/webssl-dino7b-full8b-518)

GitHub：[facebookresearch/dinov2](https://github.com/facebookresearch/dinov2) 