# Theoretical Basis Skill / 理论依据 Skill

[中文](#中文) · [English](#english)

## 中文

### 作用

`$theoretical-basis` 用在科研探索和算法开发中。它把“先找依据，再动代码”变成一道明确的门槛：只要修改可能影响算法行为或科研结论，AI 就要先说明依据是什么、是否适用，以及它究竟支持哪一部分改动。

规则很直接：

- 证据不够，就先不改；
- 检索两轮仍找不到依据，转而询问研究者是否有论文、书籍或领域资料；
- 双方都没有依据时，只有研究者明确同意，方案才能作为“待验证假设”继续；
- 真要做假设实验，也要先写清基线、指标、对照、失败阈值和停止规则。

完整运行规则以 [SKILL.md](./SKILL.md) 为准，来源等级、风险门槛、检索记录及实验协议见 [evidence-protocol.md](./references/evidence-protocol.md)。README 只提供安装和使用入口。

### 解决什么痛点？

很多科研 Prompt 只写一句“把这个模块优化一下”，却没有说明什么证据足以支持修改，也没规定找不到依据时该怎么办。结果往往是 AI 先改代码，再倒过来补理由；论文、百科和论坛帖子混在一起，看似有引用，却说不清各自支持什么结论。

还有一个更实际的问题：这类要求经常散落在不同 Prompt 里。换一个任务或 Agent，规则就丢了，也很难复用和版本管理。`$theoretical-basis` 把证据核验、暂停条件和假设实验流程收进同一个 Skill，让不同科研任务可以沿用同一套门禁，同时保留清晰的 Git 变更记录。

### 快速示例（最小 Demo）

输入：

```text
使用 $theoretical-basis 评估：把训练模块里的固定阈值改成自适应阈值，
目前没有论文或推导，只是觉得效果可能更好。
```

当检索后仍没有足够依据时，AI 应该这样处理：

```text
已暂停修改
范围：行为影响型修改
风险：中等
需要的依据：自适应规则的稳定性、统计有效性及适用条件
门禁结果：FAIL
允许的下一步：请你提供相关理论或来源；如果双方都找不到依据，
我会再询问你是否明确授权将它作为“未获支持的假设”进行受控实验。
```

重点不在输出格式，而在行为：没有依据，也没有明确的假设授权，就不会生成或应用修改。

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

`$theoretical-basis` is for scientific exploration and algorithm development. It turns “find the basis before changing the code” into an explicit gate. When a proposed change may affect algorithm behavior or scientific conclusions, Codex must identify the supporting claim, check whether it applies, and state exactly what it justifies.

The rules are straightforward:

- pause when the evidence is insufficient;
- after two unsuccessful search passes, ask the researcher for a paper, book, or domain source;
- proceed as an unsupported hypothesis only after the researcher explicitly authorizes it;
- define the baseline, controls, metrics, failure threshold, and stopping rule before writing the smallest experimental change.

[SKILL.md](./SKILL.md) is the canonical runtime contract. Source ranking, risk thresholds, search records, and experiment requirements live in [evidence-protocol.md](./references/evidence-protocol.md). This README is limited to distribution and usage guidance.

### What problem does it solve?

Research prompts often say little more than “improve this module.” They rarely define what evidence would justify the change or what the agent should do when no basis can be found. That encourages a bad sequence: edit first, then search for a plausible explanation. Papers, encyclopedias, and forum posts may all appear as citations even though they support very different kinds of claims.

These rules also tend to be copied between prompts and lost between agents. `$theoretical-basis` packages the evidence gate, pause conditions, and hypothesis workflow as one reusable, version-controlled Skill.

### Quick example (minimal demo)

Prompt:

```text
Use $theoretical-basis to assess replacing the fixed training threshold with an
adaptive threshold. I have no paper or derivation; I only think it may work better.
```

If the search still finds no adequate basis, the expected response is:

```text
Modification paused
Scope: behavior-affecting
Risk: medium
Required basis: stability, statistical validity, and applicability of the adaptive rule
Gate: FAIL
Allowed next step: provide a relevant theory or source. If neither of us can find one,
I will separately ask whether you explicitly authorize a controlled unsupported-hypothesis experiment.
```

The wording may vary. The behavior may not: without adequate support or explicit hypothesis authorization, Codex must not generate or apply the change.

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
