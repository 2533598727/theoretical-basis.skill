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

如果本地还装了 [`$academic-search`](https://github.com/ustc-ai4science/academic-search)，两个 Skill 会接力工作。`$academic-search` 负责扩展关键词、挑选平台、追踪引用和整理重复结果；`$theoretical-basis` 拿到文献后，再逐篇核对原文、假设和适用范围。找论文和判断证据分开处理。高引用、顶会论文或能下载到 PDF，都不能直接换来 PASS。

### 找到依据以后，怎么落到代码里？

如果还安装了 `$spec-skill`，三者的分工很清楚：`$theoretical-basis` 是主动介入的核心，负责判断这次改动到底能不能做；`$academic-search` 帮它把文献找全；证据通过后，`$spec-skill` 再把允许范围、限制条件和预期结果写进实施计划。

这不是把参考文献附在计划末尾就算完成。PASS 或 PARTIAL 会生成一份 Evidence Handoff：哪些来源支持哪条主张、允许改到哪里、哪些部分不能动、适用条件是什么、实验应该看到什么。随后，这些内容会进入计划里的 `read_first`、任务边界、验收条件、`must_haves` 和验证命令。执行前仍要由用户确认计划。

FAIL 不会生成实现任务，PARTIAL 也只能规划证据支持的部分。如果写代码时临时冒出新的算法机制、指标或数据解释，AI 要先停下来，为这项偏离重新找依据，不能借着已经批准的计划顺手改掉。

任务落在现有代码仓库时，`$theoretical-basis` 还可以联动 code-review-graph。它先用 `$explore-codebase` 找到真正受影响的函数、调用链、依赖模块、执行路径和测试；图谱没有建立或明显过期时，再由 `$build-graph` 更新。这样，论文里的结论会对应到具体实现，而不是停留在“注意力模块”“训练流程”这类模糊名称上。代码图谱只能说明代码怎么连，不能冒充理论依据，也不能把 FAIL 变成 PASS。

汇报阶段可以交给 `$humanizer-zh` 收尾。顺序不能反：先把来源、主张、风险、假设、限制和门禁结果写成完整证据账本，再润色中文说明。润色后还要逐项核对，不能为了读起来顺滑而删掉 DOI、符号名、冲突证据、PARTIAL/FAIL 或禁止修改的范围。

### 联动列表

| 层级 | Skill / 组件 | 负责什么 | 仓库 |
|---|---|---|---|
| 核心门禁 | `$theoretical-basis` | 主动发现需要理论依据的改动，核验来源并决定 PASS、PARTIAL 或 FAIL | [2533598727/theoretical-basis.skill](https://github.com/2533598727/theoretical-basis.skill) |
| 代码检索 | code-review-graph：`$explore-codebase`、`$build-graph` | 定位符号、调用链、依赖、执行路径和测试；图谱缺失或过期时更新 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) |
| 学术检索 | `$academic-search` | 扩展检索词，搜索论文、引用关系和开放获取状态 | [ustc-ai4science/academic-search](https://github.com/ustc-ai4science/academic-search) |
| 规划落实 | `$spec-skill` | 把通过的依据写进任务边界、验收条件、测试和执行门禁 | [lgwanai/spec-skill](https://github.com/lgwanai/spec-skill) |
| 中文汇报 | `$humanizer-zh` | 在证据账本冻结后润色中文表达，不改来源、限制和门禁结论 | [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh) |

这些项目是协作关系，不是平级裁决者。只有 `$theoretical-basis` 能给出证据门禁结论；其他项目分别提供代码上下文、文献检索、规划执行和文字整理。

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

#### Claude Code：插件安装

在 Claude Code 中执行：

```text
/plugin marketplace add 2533598727/theoretical-basis.skill
/plugin install theoretical-basis@theoretical-basis-skills
/reload-plugins
```

插件安装后的显式命令是：

```text
/theoretical-basis:theoretical-basis
```

Claude Code 也会根据普通科研修改请求自动触发它，不要求每次输入命令。

#### Claude Code：个人 Skill 安装

macOS / Linux：

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/2533598727/theoretical-basis.skill.git ~/.claude/skills/theoretical-basis
```

Windows PowerShell：

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
git clone https://github.com/2533598727/theoretical-basis.skill.git "$HOME\.claude\skills\theoretical-basis"
```

个人安装后的显式命令是 `/theoretical-basis`。如果 `~/.claude/skills` 是本次会话中新建的顶层目录，请重启一次 Claude Code；已经存在时，Claude Code 可以实时发现变更。

#### Codex

macOS / Linux：

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/2533598727/theoretical-basis.skill.git ~/.codex/skills/theoretical-basis
```

Windows PowerShell：

```powershell
New-Item -ItemType Directory -Force "$HOME\.codex\skills" | Out-Null
git clone https://github.com/2533598727/theoretical-basis.skill.git "$HOME\.codex\skills\theoretical-basis"
```

安装后重新启动 Codex 或开启新任务，使 Skill 列表重新加载。

更新 Git 克隆安装：

```bash
git -C ~/.codex/skills/theoretical-basis pull --ff-only
# Claude Code 个人 Skill：git -C ~/.claude/skills/theoretical-basis pull --ff-only
```

Claude Code 插件安装使用 `/plugin update theoretical-basis@theoretical-basis-skills` 更新。

### 使用

直接提出科研算法修改任务即可：

```text
根据最近几轮实验结果继续优化这个损失函数，并实现必要的代码修改。
```

当任务涉及算法行为或科研结论时，Skill 会要求 AI 在编辑前主动运行证据门禁。Codex 可以显式使用 `$theoretical-basis`；Claude Code 个人安装使用 `/theoretical-basis`，插件安装使用 `/theoretical-basis:theoretical-basis`。

```text
使用 $theoretical-basis 修改这个算法模块。请为你准备做出的每项实质改动主动寻找理论依据。
```

导入自定义理论库时，直接说明可访问的位置或格式：

```text
使用 $theoretical-basis 修改这个优化器。先检索公开学术来源，
并把我提供的 Zotero 导出文件和 papers/ 目录作为自定义理论库。
```

相关 Skill 都安装后，不必每次分别点名。`$theoretical-basis` 会主动介入：先用 code-review-graph 看清代码，再把文献检索交给 `$academic-search`；证据通过后，让 `$spec-skill` 把依据落实成任务和测试；最后由 `$humanizer-zh` 整理中文汇报。最终的 PASS、PARTIAL 或 FAIL 始终由 `$theoretical-basis` 判断。

### 验证

需要 Python 3.10+ 和 PyYAML：

```bash
python -m pip install PyYAML==6.0.2
python scripts/validate_skill.py . --self-test-negative
claude plugin validate . --strict
```

验证器检查 UTF-8、Skill 元数据、Claude Code 插件清单、关键安全条款、文档引用和 23 个行为场景；14 个负向自测会故意删掉核心规则，确认主动触发、宿主调用映射、证据交接、代码图谱边界、汇报保真和执行重新门禁等约束缺失时一定报错。GitHub Actions 还会运行 Claude Code 官方插件校验器。

### 贡献

- 修改证据门禁时，同步更新 `evals/cases.yaml`。
- 不得删除 FAIL 暂停规则、外部来源不可信规则或显式假设授权要求。
- 提交前运行验证器和官方 Skill 结构校验。
- 不得虚构论文、来源、实验结果或引用细节。

### 许可证

[MIT License](./LICENSE)

## English

### Purpose

`theoretical-basis` is for scientific exploration and algorithm development in Codex and Claude Code. Before designing, tuning, replacing, or refactoring an algorithm, the agent must stop, look for applicable theoretical support, and pass the evidence gate.

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

When [`$academic-search`](https://github.com/ustc-ai4science/academic-search) is installed, the two Skills work in sequence. `$academic-search` expands queries, chooses platforms, follows citations, and merges duplicate records. `$theoretical-basis` then reads the underlying sources and checks their assumptions and applicability. Retrieval and evidence judgment remain separate. Citation count, venue rank, and PDF availability never produce an automatic PASS.

### How does evidence reach implementation?

With `$spec-skill` installed, the three Skills have separate jobs. `$theoretical-basis` is the proactive core and decides whether the proposed change is supported. `$academic-search` broadens retrieval. After the gate passes, `$spec-skill` turns the supported scope, constraints, and predictions into an implementation plan.

The result is more than a bibliography. PASS or PARTIAL produces an Evidence Handoff that records which source supports each claim, what may change, what must remain untouched, which assumptions apply, and what validation should observe. Those details become `read_first` inputs, bounded task actions, acceptance criteria, `must_haves`, and verification commands. The normal user confirmation is still required before execution.

FAIL creates no implementation task, and PARTIAL plans only the supported portion. If execution introduces a new mechanism, metric, or interpretation outside the handoff, Codex stops and sends that deviation through a fresh evidence gate instead of hiding it inside the approved plan.

For work in an existing repository, `$theoretical-basis` can also use code-review-graph. `$explore-codebase` locates the actual symbols, callers, dependencies, execution flows, and tests; `$build-graph` builds or refreshes the graph when needed. This connects a paper's claim to the implementation that would change instead of reasoning from a vague module label. The graph explains code structure. It is not theoretical evidence and cannot turn FAIL into PASS.

`$humanizer-zh` can polish the final Chinese report, but only after the evidence ledger is complete. Sources, claims, risk, assumptions, limitations, conflicts, gate status, symbol names, and forbidden scope are frozen first. The rewritten report is checked against that ledger so smoother prose does not erase a DOI, soften PARTIAL or FAIL, or add an unsupported claim.

### Integration list

| Layer | Skill / component | Responsibility | Repository |
|---|---|---|---|
| Core gate | `$theoretical-basis` | Proactively detects evidence needs, verifies sources, and decides PASS, PARTIAL, or FAIL | [2533598727/theoretical-basis.skill](https://github.com/2533598727/theoretical-basis.skill) |
| Code retrieval | code-review-graph: `$explore-codebase`, `$build-graph` | Locates symbols, callers, dependencies, flows, and tests; builds or refreshes the graph when needed | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) |
| Literature retrieval | `$academic-search` | Expands queries and retrieves papers, citation relations, and access status | [ustc-ai4science/academic-search](https://github.com/ustc-ai4science/academic-search) |
| Planning | `$spec-skill` | Carries verified evidence into task boundaries, acceptance criteria, tests, and execution gates | [lgwanai/spec-skill](https://github.com/lgwanai/spec-skill) |
| Chinese reporting | `$humanizer-zh` | Polishes Chinese prose after the ledger is frozen without changing evidence or gate status | [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh) |

These integrations do not share gate authority. `$theoretical-basis` owns the evidence decision; the other projects provide code context, literature retrieval, planning, and presentation.

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

#### Claude Code plugin

Run these commands inside Claude Code:

```text
/plugin marketplace add 2533598727/theoretical-basis.skill
/plugin install theoretical-basis@theoretical-basis-skills
/reload-plugins
```

The explicit plugin command is `/theoretical-basis:theoretical-basis`. Claude Code may also invoke the Skill automatically from an ordinary research-change request.

#### Claude Code personal Skill

macOS / Linux:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/2533598727/theoretical-basis.skill.git ~/.claude/skills/theoretical-basis
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
git clone https://github.com/2533598727/theoretical-basis.skill.git "$HOME\.claude\skills\theoretical-basis"
```

The explicit personal-Skill command is `/theoretical-basis`. Restart Claude Code if this installation creates the top-level `~/.claude/skills` directory during the current session; otherwise Skill changes are detected live.

#### Codex

macOS / Linux:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/2533598727/theoretical-basis.skill.git ~/.codex/skills/theoretical-basis
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$HOME\.codex\skills" | Out-Null
git clone https://github.com/2533598727/theoretical-basis.skill.git "$HOME\.codex\skills\theoretical-basis"
```

Restart Codex or open a new task after installation so the Skill list reloads.

Update a Git clone:

```bash
git -C ~/.codex/skills/theoretical-basis pull --ff-only
# Claude Code personal Skill: git -C ~/.claude/skills/theoretical-basis pull --ff-only
```

For a Claude Code plugin installation, run `/plugin update theoretical-basis@theoretical-basis-skills`.

### Usage

Submit the research change normally:

```text
Use the latest experiment results to continue improving this loss function and implement the necessary changes.
```

When the task may affect algorithm behavior or scientific conclusions, the Skill runs the evidence gate proactively before editing. Codex can invoke `$theoretical-basis`; a Claude Code personal installation uses `/theoretical-basis`; the plugin uses `/theoretical-basis:theoretical-basis`.

```text
Use $theoretical-basis to modify this algorithm module. Actively find theoretical support for every substantive change you intend to make.
```

To add a custom theory library, name an accessible location or export format:

```text
Use $theoretical-basis to modify this optimizer. Search broad public scholarly sources,
and use my Zotero export and papers/ folder as a custom theory library.
```

With the related Skills installed, the user does not need to invoke each one separately. `$theoretical-basis` first grounds the proposal with code-review-graph, delegates literature retrieval to `$academic-search`, carries verified evidence into tasks through `$spec-skill`, and uses `$humanizer-zh` to polish Chinese reporting. `$theoretical-basis` always retains the final PASS, PARTIAL, or FAIL decision.

### Validation

Python 3.10+ and PyYAML are required:

```bash
python -m pip install PyYAML==6.0.2
python scripts/validate_skill.py . --self-test-negative
claude plugin validate . --strict
```

The validator checks UTF-8, Skill metadata, Claude Code manifests, safety clauses, documentation references, and 23 behavior scenarios. Fourteen negative mutations reject passive triggering, broken host-command mapping, missing handoffs, graph-as-evidence mistakes, lossy report rewriting, and execution bypasses. GitHub Actions also runs Claude Code's official plugin validator.

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
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── SKILL.md
├── README.md
├── LICENSE
├── agents/openai.yaml
├── references/evidence-protocol.md
├── evals/cases.yaml
├── scripts/validate_skill.py
└── .github/workflows/validate.yml
```
