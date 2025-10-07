# CLAUDE CODE PROMPT 1: Extract Nutrition Protocols

## Input files
- chinese-1 results.txt
- english-1 results.txt
- french-1 results.txt
- german-1 results.txt
- japanese-1 results.txt
- korean-1 results.txt
- portuguese-1 results.txt
- spanish-1 results.txt

## Task
Read all 8 nutrition result files and extract every supplement/nutrient mentioned with complete details.

## Extraction Requirements
For each supplement/nutrient, extract:
- **Name**: Full name and common variants
- **Dosage**: Specific amounts (mg/mcg/g per day)
- **Timing**: When to take (morning/evening, with food/empty stomach, before/after exercise)
- **Form**: Specific forms (methylfolate vs folic acid, methylcobalamin vs cyanocobalamin, chelated minerals, etc.)
- **Genetic consideration**: Which genetic variants benefit (MTHFR, TCN2, GPX1, IL-6, VDR, etc.)
- **Mechanism**: How it supports collagen synthesis, crosslinking, or tissue repair
- **Citation**: Study reference or source
- **Language/region**: Which language/region this came from
- **Evidence quality**: Note if RCT, observational, mechanistic, or theoretical

## Create Structured Output
Create CSV with columns:
```
supplement_name,dosage,timing,form,genetic_variant,mechanism,citation,language,evidence_grade
```

## Output files
1. **nutrition_protocols.csv** - Every supplement across all 8 languages with full details

2. **nutrition_summary.md** - Initial patterns observed:
   - Which supplements appear in ALL languages (universal)
   - Which appear in only 1-2 languages (regional innovations)
   - Which have genetic-specific recommendations
   - Contradictions between regions to note
