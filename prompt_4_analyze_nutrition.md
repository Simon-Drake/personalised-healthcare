# CLAUDE CODE PROMPT 4: Cross-Language Analysis - Nutrition

## Input files
- nutrition_protocols.csv
- nutrition_summary.md
- genetic_analysis_output.txt

## Task
Analyze nutrition protocols across all 8 languages to identify patterns, innovations, and genetic matches.

## Analysis Steps

### 1. Universal protocols (appear in ALL 8 languages)
- List supplements that appear across all languages
- These have highest confidence
- Calculate average dosages where they differ
- Note form variations (methylfolate vs folic acid common?)

### 2. Regional innovations (appear in only 1-3 languages)
- **Chinese-specific**: TCM herbs (骨碎補, 续断, 杜仲, etc.)
- **Japanese-specific**: Traditional formulations
- **Korean-specific**: Regional approaches
- **Spanish/Portuguese-specific**: Latin American practices
- Evaluate mechanism and plausibility
- Flag as "needs validation" or "worth trying"

### 3. Genetic mapping
- Map each supplement to genetic variants from genetic_analysis_output.txt
- Which supplements address MTHFR C677T + A1298C compound hetero?
- Which optimize TCN2 homozygote (B12 transport deficiency)?
- Which support IL-6 homozygote (high inflammation)?
- Which compensate for GPX1 homozygote (oxidative stress)?
- Which enhance VDR function (vitamin D receptor)?
- Create genetic-matched supplement list

### 4. Contradictions
- Where do regions disagree?
- Example: "English says avoid anti-inflammatories during healing, Chinese says use curcumin"
- Resolve contradictions with timing or context
- Flag unresolvable contradictions for user decision

### 5. Evidence strength calculation
- Count how many independent sources support each supplement
- Grade: A (6-8 languages), B (4-5 languages), C (2-3 languages), D (1 language)
- Cross-reference with evidence quality from extraction

### 6. Synergies
- Which supplements work together? (Vitamin C + lysine + proline)
- Which should be taken together for absorption? (Vitamin D + K2)
- Which should be separated? (Calcium vs iron)

## Output file
**nutrition_analysis.md** with sections:
1. Universal Protocols (high confidence, use these)
2. Regional Innovations (evaluate these, potential hidden gems)
3. Genetic-Matched Recommendations (specifically for user's genetic profile)
4. Contradictions to Resolve (user needs to decide)
5. Evidence Summary (what's proven vs theoretical)
6. Synergies and Interactions (how to combine supplements)
