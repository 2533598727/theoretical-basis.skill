# Theoretical Basis Skill / 理论依据 Skill

[中文](#中文) · [English](#english)

## 中文

### 作用

`theoretical-basis` 是一个面向科研探索与算法开发的 Codex Skill。它要求 AI 在修改会影响科研结论或算法行为的模块之前，先找到可追溯且适用的理论依据。

适用范围包括：

- 算法、模型组件和损失函数的设计或替换；
- 优化方法、数据处理步骤和评估方法的调整；
- 超参数或结构变化可能改变模型行为的调优；
- 科研代码中影响稳定性、收敛性、统计有效性、复杂度或鲁棒性的重构。

### 核心规则

1. 修改前明确模块、修改目标、理论问题和潜在副作用。
2. 主动检索论文、教材、权威机构、百科以及相关技术论坛。
3. 将每一项实质修改与具体来源、支持主张和适用条件对应起来。
4. 找不到充分依据时立即暂停，不生成或应用未经支持的修改。
5. 扩大检索后仍无结果时，询问用户能否提供论文、书籍、理论或领域知识。
6. 双方都没有依据时，必须再次征得用户明确许可，才能把方案标记为“待验证的研究假设”。
7. 获得许可后，只实施验证假设所需的最小修改，并设计基线、对照、消融、统计检验及失败标准。

来源不会被一视同仁。Skill 优先使用同行评议论文、标准、官方报告、教材和综述；百科与论坛可用于定位术语、实现经验或失败模式，但不能被包装成普适理论。

### 安装

#### 方法一：Git 克隆

macOS / Linux：

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/2533598727/-theoretical-basis.skill.git ~/.codex/skills/theoretical-basis
```

Windows PowerShell：

```powershell
New-Item -ItemType Directory -Force "$HOME\.codex\skills" | Out-Null
git clone https://github.com/2533598727/-theoretical-basis.skill.git "$HOME\.codex\skills\theoretical-basis"
```

#### 方法二：手动安装

下载仓库 ZIP，解压后将整个目录复制到：

```text
~/.codex/skills/theoretical-basis
```

安装后重新启动 Codex 或开启一个新任务，使 Skill 列表重新加载。

### 使用

显式调用：

```text
使用 $theoretical-basis，评估并迭代这个损失函数。没有理论依据时先暂停修改并询问我。
```

也可以直接提出科研算法修改任务；当任务符合 `SKILL.md` 中的触发条件时，Codex 可以自动使用该 Skill。

### 输出内容

每轮迭代应给出：模块与修改方案、理论维度、所需主张、来源及链接、适用假设与局限、门禁结果、实际修改、验证计划、实验结果和遗留风险。

门禁结果分为：

- `PASS`：理论依据充分，可以在其适用范围内修改；
- `PARTIAL`：只允许实施有依据的部分；
- `FAIL`：暂停修改，进入补充检索和用户确认流程。

## English

### Purpose

`theoretical-basis` is a Codex Skill for scientific exploration and algorithm development. It requires traceable and applicable theoretical support before an AI changes a module that may affect algorithm behavior or scientific conclusions.

Typical uses include:

- designing or replacing algorithms, model components, and loss functions;
- changing optimization methods, data-processing steps, or evaluation procedures;
- tuning parameters or structures that may alter model behavior;
- refactoring research code in ways that affect stability, convergence, statistical validity, complexity, or robustness.

### Core policy

1. Define the module, proposed change, theoretical question, and possible side effects.
2. Search papers, books, authoritative institutions, encyclopedias, and relevant technical forums.
3. Map every substantive change to a specific source, supported claim, and applicability conditions.
4. Stop when adequate support cannot be found. Do not generate or apply an unsupported change.
5. After a broader search still fails, ask the user for a paper, book passage, theory, or domain principle.
6. If neither side has evidence, obtain explicit permission before treating the proposal as an unsupported research hypothesis.
7. Once authorized, implement only the minimum change needed to test the hypothesis and define baselines, controls, ablations, statistical analysis, and failure criteria.

The Skill ranks sources rather than treating them equally. Peer-reviewed papers, standards, official reports, textbooks, and surveys receive priority. Encyclopedias and forums may provide terminology, implementation experience, or failure reports, but must not be presented as general theory without corroboration.

### Installation

#### Option 1: Clone with Git

macOS / Linux:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/2533598727/-theoretical-basis.skill.git ~/.codex/skills/theoretical-basis
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$HOME\.codex\skills" | Out-Null
git clone https://github.com/2533598727/-theoretical-basis.skill.git "$HOME\.codex\skills\theoretical-basis"
```

#### Option 2: Install manually

Download the repository as a ZIP and copy the extracted directory to:

```text
~/.codex/skills/theoretical-basis
```

Restart Codex or open a new task after installation so the Skill list is reloaded.

### Usage

Invoke it explicitly:

```text
Use $theoretical-basis to assess and iterate this loss function. Stop and ask me if no adequate theoretical support can be found.
```

You may also submit a research algorithm task normally. Codex can invoke the Skill automatically when the task matches the trigger description in `SKILL.md`.

### Output

Each iteration should report the module and proposed change, theoretical dimension, required claim, sources and links, assumptions and limitations, gate result, actual changes, validation plan, experimental result, and unresolved risks.

Gate results are:

- `PASS`: evidence is adequate; proceed within its scope;
- `PARTIAL`: implement only the supported portion;
- `FAIL`: pause the change and enter the extended-search and user-confirmation workflow.

## Repository structure / 仓库结构

```text
theoretical-basis/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
└── references/
    └── evidence-protocol.md
```
