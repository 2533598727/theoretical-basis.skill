# Theoretical Basis Skill / 理论依据 Skill

[中文](#中文) · [English](#english)

## 中文

### 作用

`$theoretical-basis` 是一个面向科研探索和算法开发的 Codex Skill。它要求 AI 在修改可能影响算法行为或科研结论的模块前，先核验可追溯且适用的理论或证据。

核心底线：

- 证据不足时保持修改暂停；
- 两轮检索后仍无依据，先询问研究者能否提供来源；
- 只有研究者明确授权，才能将方案视为“待验证假设”；
- 假设实验必须先注册指标、基线、对照、阈值、随机种子和停止规则，再做最小实现。

完整运行规则以 [SKILL.md](./SKILL.md) 为准，来源等级、风险门槛、检索记录及实验协议见 [evidence-protocol.md](./references/evidence-protocol.md)。README 只提供安装和使用入口。

### 安装

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

安装后重新启动 Codex 或开启新任务，使 Skill 列表重新加载。

更新已有安装：

```bash
git -C ~/.codex/skills/theoretical-basis pull --ff-only
```

### 使用

```text
使用 $theoretical-basis 评估这个算法模块的修改。请先给出证据门禁结果；没有充分依据时暂停修改并询问我。
```

Skill 也可在任务符合 `SKILL.md` 描述中的触发条件时自动启用。

### 验证

需要 Python 3.10+ 和 PyYAML：

```bash
python -m pip install PyYAML==6.0.2
python scripts/validate_skill.py . --self-test-negative
```

验证器检查 UTF-8、Skill 元数据、关键安全条款、旧名称、文档引用和 12 个行为场景；负向自测会确认缺失安全条款时能够失败。GitHub Actions 会在 push 和 pull request 时运行同一入口。

### 贡献

- 修改证据门禁时，同步更新 `evals/cases.yaml`。
- 不得删除 FAIL 暂停规则、外部来源不可信规则或显式假设授权要求。
- 提交前运行验证器和官方 Skill 结构校验。
- 不得虚构论文、来源、实验结果或引用细节。

### 许可证

[MIT License](./LICENSE)

## English

### Purpose

`$theoretical-basis` is a Codex Skill for scientific exploration and algorithm development. Before changing a module that may affect algorithm behavior or scientific conclusions, it requires traceable, applicable theoretical or evidential support.

Its core invariants are:

- keep unsupported changes paused;
- after two search passes fail, ask the researcher for a source;
- treat a proposal as an unsupported hypothesis only after explicit researcher authorization;
- preregister metrics, baseline, controls, thresholds, seeds, and stopping rules before minimal experimental implementation.

[SKILL.md](./SKILL.md) is the canonical runtime contract. Source ranking, risk thresholds, search records, and experiment requirements live in [evidence-protocol.md](./references/evidence-protocol.md). This README is limited to distribution and usage guidance.

### Installation

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

Restart Codex or open a new task after installation so the Skill list reloads.

Update an existing Git installation:

```bash
git -C ~/.codex/skills/theoretical-basis pull --ff-only
```

### Usage

```text
Use $theoretical-basis to assess this algorithm-module change. Report the evidence-gate decision first, and pause for my input when support is insufficient.
```

Codex may also invoke the Skill automatically when a task matches the trigger description in `SKILL.md`.

### Validation

Python 3.10+ and PyYAML are required:

```bash
python -m pip install PyYAML==6.0.2
python scripts/validate_skill.py . --self-test-negative
```

The validator checks UTF-8, Skill metadata, safety clauses, stale names, documentation references, and 12 behavior scenarios. Its negative self-test proves that a missing safety clause is rejected. GitHub Actions runs the same entry point on pushes and pull requests.

### Contributing

- Update `evals/cases.yaml` whenever the evidence-gate contract changes.
- Do not remove the FAIL pause, untrusted-source rule, or explicit hypothesis-authorization requirement.
- Run the repository validator and official Skill structure validation before committing.
- Never fabricate papers, sources, experimental results, or citation details.

### License

[MIT License](./LICENSE)

## Repository structure / 仓库结构

```text
.
├── SKILL.md
├── README.md
├── LICENSE
├── agents/openai.yaml
├── references/evidence-protocol.md
├── evals/cases.yaml
├── scripts/validate_skill.py
└── .github/workflows/validate.yml
```
