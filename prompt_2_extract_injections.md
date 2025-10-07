# CLAUDE CODE PROMPT 2: Extract Injection Protocols

## Input files
- chinese-2 results.txt
- english-2 results.txt
- french-2 results.txt
- german-2 results.txt
- japanese-2 results.txt
- korean-2 results.txt
- portuguese-2 results.txt
- spanish-2 results.txt

## Task
Read all 8 injection result files and extract every injection protocol with complete details.

## Extraction Requirements
For each injection protocol, extract:
- **Type**: Prolotherapy / PRP / Peptide (BPC-157, TB-500) / Stem cell / MSC / Other
- **Solution composition**: Exact ingredients (e.g., "15% dextrose + 0.5% lidocaine")
- **Concentration**: Specific percentages or amounts
- **Preparation method**: For PRP (single-spin vs double-spin, RPM, activation method)
- **Injection sites**: Which specific ligaments/joints targeted
- **Number of injections per session**: How many sites injected
- **Frequency**: How often (weekly, every 3 weeks, monthly)
- **Number of sessions**: Total treatment course (4-6 sessions typical)
- **Success rate**: Percentage achieving improvement (if reported)
- **Outcome measure**: Pain reduction / laxity reduction / functional improvement
- **Population studied**: Hypermobile / post-surgical / general / EDS specific
- **Timeline to results**: Initial response (weeks) and maximum benefit (months)
- **Duration of effect**: How long results last
- **Citation**: Study reference or source
- **Language/region**: Which language/region this came from
- **Evidence quality**: RCT / case series / clinical practice / anecdotal

## Create Structured Output
Create CSV with columns:
```
type,composition,concentration,preparation,sites,injections_per_session,frequency,total_sessions,success_rate,outcome_measure,population,timeline_initial,timeline_max,duration,citation,language,evidence_grade
```

## Output files
1. **injection_protocols.csv** - Every protocol across all 8 languages

2. **injection_summary.md** - Initial patterns:
   - Universal protocols vs regional variations
   - Success rate comparisons
   - Japanese double-spin PRP vs Western single-spin
   - Combination protocols (PRP + prolotherapy)
   - Hypermobile-specific evidence
