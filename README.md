# Theoretical Basis Skill / 理论依据 Skill

[中文](#中文) · [English](#english)

## 中文

### 作用

`$theoretical-basis` 是给科研探索和算法开发用的，重点约束 AI 怎么动手。准备设计、调参、替换或重构算法模块时，先停一下，查清楚这个改动有没有可追溯、真正适用的理论依据，再决定要不要改代码。

我写这个 Skill，是因为 AI 很容易陷进一种循环：看见指标变了，猜一个原因，马上再改一版。结果跑得越多，解释也越多，却不一定更接近真实机制。这个 Skill 把顺序倒过来：先讲清楚准备改什么、需要哪方面的依据；依据站得住脚，才做最小修改；实验留到最后，用来检查预期，而不是替猜测找理由。

几条底线：

- 没有足够依据，先不改；
- 一个搜索入口没结果，不代表理论不存在；
- 实验结果不是理论，指标上涨也不能自动证明某个机制成立；
- 实在找不到依据，必须由研究者明确同意，才能把方案当作“待验证假设”继续。

真要验证假设，也得先写好基线、指标、对照、失败阈值和停止规则。不能看到结果以后再改成功标准。

完整运行规则以 [SKILL.md](./SKILL.md) 为准，来源等级、风险门槛、检索记录及实验协议见 [evidence-protocol.md](./references/evidence-protocol.md)。README 只提供安装和使用入口。

### 它会去哪里找？

它不会只在普通网页里搜一遍就下结论。第一轮优先找原始论文、教材、标准和方法文档，并按领域选择 Google Scholar、arXiv、AAAI、Semantic Scholar、OpenAlex、Crossref、会议论文库或专业数据库。第二轮沿着引用关系往前后追，顺便找勘误、撤稿、失败复现和相反结论。

你也可以把自己的资料库交给它：本地论文目录、Zotero 导出、BibTeX、RIS、CSL JSON、DOI 或 arXiv ID 列表都可以。Skill 会记录资料库的范围、版本和权限，私有文件默认留在本地。自己的收藏也不是“免检区”，原文、假设和适用条件照样要核对。

### 解决什么痛点？

很多科研 Prompt 只有一句“把这个模块优化一下”。什么证据才算够，找不到依据时怎么办，都没说。AI 于是盯着上一轮实验的涨跌猜原因，接着改参数、换结构，再补一个听起来合理的解释。这是事后猜测，不是理论依据。

还有一种情况更隐蔽：先把代码改完，再倒过来找引用。论文、百科和论坛帖子混在一起，看似有出处，却说不清每个来源到底支持什么，也没检查论文里的假设能不能套在当前模块上。

这些要求如果全写在 Prompt 里，换个任务或 Agent 就容易丢。`$theoretical-basis` 把检索、核验、暂停和假设实验收进一个可以复用、可以版本管理的 Skill。以后改规则，看 Git 记录就知道改了什么。

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

`$theoretical-basis` is for scientific exploration and algorithm development. It governs how Codex changes research code. Before designing, tuning, replacing, or refactoring an algorithm, Codex must stop, look for applicable theoretical support, and pass the evidence gate.

The Skill exists to break a familiar loop: observe a metric change, guess at the cause, and immediately try another edit. Instead, Codex defines the intended change, identifies the claim it depends on, checks the literature, and makes only the smallest supported edit. Experiments come afterward to test the prediction, not to manufacture a theory after the fact.

The basic rules:

- pause when the evidence is insufficient;
- do not treat one empty search as proof that no theory exists;
- do not turn an experimental improvement into proof of a mechanism;
- proceed as an unsupported hypothesis only after the researcher explicitly authorizes it;
- preregister the baseline, controls, metric, failure threshold, and stopping rule before testing that hypothesis.

Success criteria stay fixed once results are visible.

[SKILL.md](./SKILL.md) is the canonical runtime contract. Source ranking, risk thresholds, search records, and experiment requirements live in [evidence-protocol.md](./references/evidence-protocol.md). This README is limited to distribution and usage guidance.

### Where does it search?

The first pass looks for primary papers, textbooks, standards, and original method documentation. Depending on the field, it can use Google Scholar, arXiv, AAAI, Semantic Scholar, OpenAlex, Crossref, venue libraries, and specialist databases. The second pass follows citations and looks for corrections, retractions, failed replications, and conflicting findings.

Researchers can add their own library as well: a local paper folder, Zotero export, BibTeX, RIS, CSL JSON, DOI list, or arXiv-ID list. Private files stay local unless the researcher explicitly says otherwise. A paper does not become authoritative merely because it is in a curated collection; the claim and assumptions still need checking.

### What problem does it solve?

Research prompts often say little more than “improve this module.” They rarely define what evidence would justify a change or what the agent should do when no basis can be found. The agent can then over-interpret the latest metric movement, guess at a mechanism, and keep tuning. That is post-hoc speculation, not theoretical support.

Another failure mode is editing first and looking for citations afterward. Papers, encyclopedias, and forum posts may all appear as sources even though they support different kinds of claims or rely on assumptions that do not fit the current module.

These rules also tend to be copied between prompts and lost between agents. `$theoretical-basis` keeps the search, evidence gate, pause conditions, and hypothesis workflow in one reusable, version-controlled place.

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
