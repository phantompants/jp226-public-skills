# JP226 Public Skills

Reusable, general-purpose AI skills. The Work Prompt Studio collection is version **2026.11.01** (19 November 2026), with 58 general engineering consultancy skills.

## Work Prompt Studio — engineering filter

Site: [Work Prompt Studio](https://work-prompt-studio.jp226prints-au.chatgpt.site)

Skill source: `workprompts-jp226-com/engineering-filter/skills/`

[Browse all 58 Work Prompt Studio skills by role and task](workprompts-jp226-com/engineering-filter/README.md).

### Technical-report starting points

| Skill | Purpose |
| --- | --- |
| [Draft technical report](workprompts-jp226-com/engineering-filter/skills/jp226-draft-technical-report/SKILL.md) | Produce a structured, evidence-led draft from approved source material. |
| [Review technical report](workprompts-jp226-com/engineering-filter/skills/jp226-review-technical-report/SKILL.md) | Identify gaps, inconsistencies and unsupported conclusions. |
| [Rewrite technical text](workprompts-jp226-com/engineering-filter/skills/jp226-rewrite-technical-text/SKILL.md) | Improve readability while preserving technical meaning. |

These general-purpose skills contain no client material or cybersecurity workflows. Supply project-specific information only within your approved AI environment.

## Use the skills

- **Microsoft 365 Copilot Chat:** download the required `SKILL.md` file, then use the available Upload skill control. Availability depends on your tenant and administrator settings. This is for personal Copilot Chat skills, not a complete declarative-agent package.
- **Claude:** place `SKILL.md` in a folder named exactly as the skill name, ZIP that folder, then upload using the available Skills control. Confirm current host requirements.
- **Other Agent Skills hosts:** follow that host's installation instructions. A `SKILL.md` file does not grant access to tools, documents or services.

Keep each skill separate. Select it explicitly for initial trials, supply representative source material, and review the output. These are portable, instruction-only skills with no scripts or network dependencies. Host runtime behaviour has not been verified in Copilot or Claude; format checks do not establish equivalent outputs across models.

[Copilot Chat documentation](https://learn.microsoft.com/en-us/plugins/build-copilot-chat-skills) · [Claude documentation](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) · [Agent Skills specification](https://agentskills.io/specification)

## Validation scenarios

Try each skill with complete source material, missing inputs, conflicting evidence and unsupported requests. Check that drafting does not invent findings, reviewing does not claim inaccessible appendices were checked, and rewriting retains qualifiers such as “may” and “not verified”. Report remaining issues to the author before relying on the result.

## Versions

- **2026.11.01:** expand Work Prompt Studio to 58 general engineering workflows. Cybersecurity skills remain excluded.

- **2026.11.00:** initial technical-report drafting, review and rewrite set. Use the repository commit history for changes and stable version references.

Earlier JP226 skills are also organised in [phantompants/AI/Skills](https://github.com/phantompants/AI/tree/main/Skills). Existing folders in this repository are retained.
