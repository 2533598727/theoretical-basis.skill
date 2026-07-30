# Theoretical Basis Skill / 理论依据 Skill

[中文](#中文) · [English](#english)

## 中文

### 作用

`$theoretical-basis` 用在科研探索和算法开发中。它不只是帮你评估一个已经写好的方案，更重要的是约束 AI 自己的修改过程：当 AI 准备设计、调参、替换或重构算法模块时，它要主动停下来，先查这个改动有没有可追溯、可适用的理论依据，再决定能不能动代码。

这会把常见的“看实验结果猜原因，然后继续改”换成更稳妥的顺序：先说清准备改什么、需要哪方面的依据，检索并核验来源，通过门禁后再做最小修改，最后用实验检查预期是否成立。

规则很直接：

- 证据不够，就先不改；
- 检索两轮仍找不到依据，转而询问研究者是否有论文、书籍或领域资料；
- 每轮尽量覆盖互补来源，例如 Google Scholar、arXiv、AAAI、Semantic Scholar、OpenAlex、Crossref，以及领域数据库和会议论文库；
- 双方都没有依据时，只有研究者明确同意，方案才能作为“待验证假设”继续；
- 真要做假设实验，也要先写清基线、指标、对照、失败阈值和停止规则。

实验结果可以支持或推翻一个事先写清的预测，但不能反过来充当理论依据。AI 不能因为某次指标上涨，就自行猜测机制成立并据此开始下一轮修改。

完整运行规则以 [SKILL.md](./SKILL.md) 为准，来源等级、风险门槛、检索记录及实验协议见 [evidence-protocol.md](./references/evidence-protocol.md)。README 只提供安装和使用入口。

用户还可以提供自己的理论库，例如本地论文目录、Zotero 导出、BibTeX/RIS/CSL JSON、DOI 或 arXiv ID 列表，以及已连接的知识库。Skill 会先记录资料库的范围、版本和权限，再把它作为第一轮检索来源；资料出现在自定义库中并不等于自动可信，原文和适用条件仍要核验。

### 解决什么痛点？

很多科研 Prompt 只写一句“把这个模块优化一下”，却没有说明什么证据足以支持修改，也没规定找不到依据时该怎么办。AI 很容易盯着上一轮实验的涨跌猜原因，接着改参数、换结构，再为结果补一个听起来合理的解释。这样得到的是事后猜测，不是理论依据。

另一个常见问题是 AI 先改代码，再倒过来找引用。论文、百科和论坛帖子混在一起，看似有来源，却说不清各自支持什么结论，也没有检查来源里的假设是否适用于当前模块。

还有一个更实际的问题：这类要求经常散落在不同 Prompt 里。换一个任务或 Agent，规则就丢了，也很难复用和版本管理。`$theoretical-basis` 把证据核验、暂停条件和假设实验流程收进同一个 Skill，让不同科研任务可以沿用同一套门禁，同时保留清晰的 Git 变更记录。

### 快速示例（最小 Demo）

用户只需要正常提出开发任务，不必每次专门提醒 AI “先评估”：

```text
上一轮实验里验证集指标下降了。请继续优化训练模块，
把固定阈值改成自适应阈值，看看能不能把指标提回来。
```

`$theoretical-basis` 应在改代码前自动介入。它不能根据这一次实验结果猜测自适应阈值有效，而要先确定需要核验稳定性、统计有效性和适用条件，再主动检索来源。如果两轮检索仍没有足够依据，结果应类似：

```text
已暂停修改
范围：行为影响型修改
风险：中等
需要的依据：自适应规则的稳定性、统计有效性及适用条件
门禁结果：FAIL
允许的下一步：请你提供相关理论或来源；如果双方都找不到依据，
我会再询问你是否明确授权将它作为“未获支持的假设”进行受控实验。
```

重点不在输出格式，而在行为：AI 会主动为自己准备做的改动寻找依据。实验结果不会自动变成理论；没有依据，也没有明确的假设授权，就不会生成或应用修改。

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

直接提出科研算法修改任务即可：

```text
根据最近几轮实验结果继续优化这个损失函数，并实现必要的代码修改。
```

当任务涉及算法行为或科研结论时，Skill 会要求 AI 在编辑前主动运行证据门禁。也可以显式调用：

```text
使用 $theoretical-basis 修改这个算法模块。请为你准备做出的每项实质改动主动寻找理论依据。
```

导入自定义理论库时，直接说明可访问的位置或格式：

```text
使用 $theoretical-basis 修改这个优化器。先检索公开学术来源，
并把我提供的 Zotero 导出文件和 papers/ 目录作为自定义理论库。
```

### 验证

需要 Python 3.10+ 和 PyYAML：

```bash
python -m pip install PyYAML==6.0.2
python scripts/validate_skill.py . --self-test-negative
```

验证器检查 UTF-8、Skill 元数据、关键安全条款、旧名称、文档引用和 14 个行为场景；负向自测会确认安全、广域检索或自定义理论库规则缺失时能够失败。GitHub Actions 会在 push 和 pull request 时运行同一入口。

### 贡献

- 修改证据门禁时，同步更新 `evals/cases.yaml`。
- 不得删除 FAIL 暂停规则、外部来源不可信规则或显式假设授权要求。
- 提交前运行验证器和官方 Skill 结构校验。
- 不得虚构论文、来源、实验结果或引用细节。

### 许可证

[MIT License](./LICENSE)

## English

### Purpose

`$theoretical-basis` is for scientific exploration and algorithm development. It does more than assess a proposal supplied by the user. It governs Codex's own changes: whenever Codex is about to design, tune, replace, or refactor a research algorithm, it must stop, actively look for applicable theoretical support, and pass the evidence gate before editing the code.

This replaces a common loop—observe an experimental result, guess at the cause, and make another change—with a disciplined sequence: define the proposed change, identify the claim it requires, verify sources, make the smallest supported edit, and then test the prediction.

The rules are straightforward:

- pause when the evidence is insufficient;
- after two unsuccessful search passes, ask the researcher for a paper, book, or domain source;
- cover complementary sources where available, including Google Scholar, arXiv, AAAI, Semantic Scholar, OpenAlex, Crossref, and field-specific indexes or venue libraries;
- proceed as an unsupported hypothesis only after the researcher explicitly authorizes it;
- define the baseline, controls, metrics, failure threshold, and stopping rule before writing the smallest experimental change.

An experimental result may test a preregistered prediction, but it does not become theory after the fact. Codex may not treat one metric increase as proof of a mechanism and use that guess to authorize the next modification.

[SKILL.md](./SKILL.md) is the canonical runtime contract. Source ranking, risk thresholds, search records, and experiment requirements live in [evidence-protocol.md](./references/evidence-protocol.md). This README is limited to distribution and usage guidance.

Researchers can also provide a custom theory library: a local paper directory, Zotero export, BibTeX/RIS/CSL JSON, DOI or arXiv-ID list, or a connected knowledge store. The Skill records its scope, snapshot, and access boundaries before using it in Pass 1. Presence in a custom library never makes a source automatically authoritative; the original claim and assumptions still require verification.

### What problem does it solve?

Research prompts often say little more than “improve this module.” They rarely define what evidence would justify the change or what the agent should do when no basis can be found. An agent can easily over-interpret the latest metric movement, guess at a mechanism, and keep tuning. That is post-hoc speculation, not theoretical support.

Another failure mode is editing first and looking for citations afterward. Papers, encyclopedias, and forum posts may all appear as sources even though they support different kinds of claims or rely on assumptions that do not fit the current module.

These rules also tend to be copied between prompts and lost between agents. `$theoretical-basis` packages the evidence gate, pause conditions, and hypothesis workflow as one reusable, version-controlled Skill.

### Quick example (minimal demo)

The user can give an ordinary development request without explicitly asking for an assessment:

```text
The validation metric dropped in the last run. Continue improving the training module:
replace the fixed threshold with an adaptive one and see whether the metric recovers.
```

`$theoretical-basis` should intervene before any edit. Codex must not infer from one result that an adaptive threshold is justified. It should identify the required stability, statistical-validity, and applicability claims and search for support. If two search passes still find no adequate basis, the expected response is:

```text
Modification paused
Scope: behavior-affecting
Risk: medium
Required basis: stability, statistical validity, and applicability of the adaptive rule
Gate: FAIL
Allowed next step: provide a relevant theory or source. If neither of us can find one,
I will separately ask whether you explicitly authorize a controlled unsupported-hypothesis experiment.
```

The wording may vary. The behavior may not: Codex actively checks its own intended changes. Experimental results do not automatically become theory, and without adequate support or explicit hypothesis authorization, Codex must not generate or apply the change.

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

Submit the research change normally:

```text
Use the latest experiment results to continue improving this loss function and implement the necessary changes.
```

When the task may affect algorithm behavior or scientific conclusions, the Skill requires Codex to run the evidence gate proactively before editing. Explicit invocation is also supported:

```text
Use $theoretical-basis to modify this algorithm module. Actively find theoretical support for every substantive change you intend to make.
```

To add a custom theory library, name an accessible location or export format:

```text
Use $theoretical-basis to modify this optimizer. Search broad public scholarly sources,
and use my Zotero export and papers/ folder as a custom theory library.
```

### Validation

Python 3.10+ and PyYAML are required:

```bash
python -m pip install PyYAML==6.0.2
python scripts/validate_skill.py . --self-test-negative
```

The validator checks UTF-8, Skill metadata, safety clauses, stale names, documentation references, and 14 behavior scenarios. Its negative self-test rejects missing safety, broad-search, or custom-library clauses. GitHub Actions runs the same entry point on pushes and pull requests.

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
