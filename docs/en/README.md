[EN](README.md) | [ZH](../zh/README.md)

# Summary of Multimodal Embedding Models

Please select your preferred language above to view the documentation.

This project collects and organizes detailed information on various multimodal embedding models, including model specifications, output dimensions, and usage instructions.

## Model Series

### General Embedding Models

#### Text Embedding Models
1. [Sentence Transformers Series](general_embedding/text_embedding/sentence_transformers_series/README.md)
   - all-MiniLM-L6-v2

2. [Linq Series](general_embedding/text_embedding/linq_series/README.md)
   - Linq-Embed
   - Linq-Embed-Mistral

3. [BGE Series](general_embedding/text_embedding/bge_series/README.md)
   - BGE

#### Visual Embedding Models
1. [ViT Series](general_embedding/visual_embedding/vit_series/README.md)
   - vit-base-patch16-224-in21k
   - vit-huge-patch14-224-in21k

2. [DINO Series](general_embedding/visual_embedding/dino_series/README.md)
   - DINOv2 Series (small, base, large, giant)
   - WebSSL-DINO Series (various 1b-7b variants)

### Special Embedding Models
1. [Street Scene Model Series](special_embedding/street/README.md)
   - StreetCLIP

#### Cross-modal Embedding Models
1. [SigLiP Series](general_embedding/cross_modal_embedding/siglip_series/README.md)
   - siglip2-giant-opt-patch16-384

2. [InternViT Series](general_embedding/cross_modal_embedding/internvit_series/README.md)
   - InternViT-300M-448px-V2_5

3. [Gme-Qwen Series](general_embedding/cross_modal_embedding/gme_qwen_series/README.md)
   - gme-Qwen2-VL-7B-Instruct

## Usage Instructions

For detailed information on each series, please refer to the README.md file in the corresponding directory.

## Directory Structure

```
.
├── code/                    # Code directory
│   ├── general_embedding/   # General embedding model code
│   │   ├── text_embedding/  # Text embedding model code
│   │   │   ├── sentence_transformers_series/  # Sentence Transformers series code
│   │   │   ├── linq_series/                   # Linq series code
│   │   │   └── bge_series/                    # BGE series code
│   │   │
│   │   ├── visual_embedding/ # Visual embedding model code
│   │   │   ├── vit_series/   # ViT series code
│   │   │   └── dino_series/  # DINO series code
│   │   │
│   │   └── cross_modal_embedding/ # Cross-modal embedding model code
│   │       ├── siglip_series/    # SigLiP series code
│   │       ├── internvit_series/ # InternViT series code
│   │       └── gme_qwen_series/  # Gme-Qwen series code
│   │
│   └── special_embedding/   # Special embedding model code
│       └── street/          # Street scene model code
│
├── docs/                    # Documentation directory
│   ├── en/                  # English documentation
│   │   ├── general_embedding/    # General embedding models
│   │   │   ├── text_embedding/   # Text embedding models
│   │   │   │   ├── sentence_transformers_series/  # Sentence Transformers series
│   │   │   │   ├── linq_series/                   # Linq series
│   │   │   │   └── bge_series/                    # BGE series
│   │   │   │
│   │   │   ├── visual_embedding/ # Visual embedding models
│   │   │   │   ├── vit_series/   # ViT series
│   │   │   │   └── dino_series/  # DINO series
│   │   │   │
│   │   │   └── cross_modal_embedding/ # Cross-modal embedding models
│   │   │       ├── siglip_series/    # SigLiP series
│   │   │       ├── internvit_series/ # InternViT series
│   │   │       └── gme_qwen_series/  # Gme-Qwen series
│   │   │
│   │   └── special_embedding/    # Special embedding models
│   │       └── street/           # Street scene model series
│   │
│   └── zh/                  # Chinese documentation
│       ├── general_embedding/    # General embedding models
│       │   ├── text_embedding/   # Text embedding models
│       │   │   ├── sentence_transformers_series/  # Sentence Transformers series
│       │   │   ├── linq_series/                   # Linq series
│       │   │   └── bge_series/                    # BGE series
│       │   │
│       │   ├── visual_embedding/ # Visual embedding models
│       │   │   ├── vit_series/   # ViT series
│       │   │   └── dino_series/  # DINO series
│       │   │
│       │   └── cross_modal_embedding/ # Cross-modal embedding models
│       │       ├── siglip_series/    # SigLiP series
│       │       ├── internvit_series/ # InternViT series
│       │       └── gme_qwen_series/  # Gme-Qwen series
│       │
│       └── special_embedding/    # Special embedding models
│           └── street/           # Street scene model series
│
└── README.md                # Project main document
```

## Evaluation Metrics

The main metrics for evaluating multimodal embedding models include:

- Cross-modal retrieval accuracy
- Zero-shot classification accuracy
- Semantic similarity correlation
- Computational efficiency
- Model size

## Application Scenarios

Multimodal embedding models play an important role in the following scenarios:

1. LLM RAG (Retrieval-Augmented Generation)
   - Private knowledge base vectorization
   - Multimodal knowledge retrieval enhancement
   - Cross-modal semantic alignment

2. Cross-modal Retrieval and Matching
   - Text-to-image search
   - Image-to-text search
   - Multimodal semantic matching

3. Zero-shot Learning and Classification
   - Image classification and recognition
   - Video scene understanding
   - Cross-modal transfer learning

4. Multimodal Content Understanding
   - Video understanding and analysis
   - Multimodal question answering systems
   - Scene semantic parsing

5. Intelligent Recommendation Systems
   - Cross-modal content recommendation
   - Personalized search ranking
   - User interest modeling

## Contribution Guide

Contributions of new models, evaluation results, or suggestions for improvement are welcome! Please follow these steps:

1. Fork this repository
2. Create a new branch
3. Submit your changes
4. Open a Pull Request

## License

MIT License

## Acknowledgements

Thanks to all researchers and developers in the open-source community whose work has made significant contributions to the field of multimodal AI. 