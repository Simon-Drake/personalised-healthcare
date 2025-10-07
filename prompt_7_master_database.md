# CLAUDE CODE PROMPT 7: Create Master Protocol Database

## Input files
- nutrition_protocols.csv
- nutrition_analysis.md
- injection_protocols.csv
- injection_analysis.md
- exercise_protocols.csv
- exercise_analysis.md
- genetic_analysis_output.txt

## Task
Create comprehensive, evidence-graded master database of ALL interventions across nutrition, injections, and exercise.

## Analysis Steps

### 1. Grade every protocol A/B/C/D
- **A Grade**: Multiple high-quality sources (RCTs, systematic reviews) across multiple languages
- **B Grade**: Multiple sources but lower quality (observational studies, case series) OR single high-quality source
- **C Grade**: Regional evidence only (1-3 languages), needs validation OR mechanistic rationale but limited clinical data
- **D Grade**: Theoretical only, no clinical evidence

### 2. Create master intervention database
Combine all three CSVs into one comprehensive database with additional columns:
- evidence_grade (A/B/C/D)
- category (nutrition/injection/exercise)
- genetic_relevance (which genetic variants from genetic_analysis_output.txt)
- synergies (works with what other interventions?)
- contraindications (conflicts with what?)
- cost_estimate (relative: $ / $$ / $$$ / $$$$)
- accessibility (easy / moderate / difficult / regional-only)

### 3. Cross-reference genetic profile
From genetic_analysis_output.txt, map:
- MTHFR C677T + A1298C compound hetero → which interventions?
- TCN2 homozygote → which interventions?
- IL-6 homozygote → which interventions?
- GPX1 homozygote → which interventions?
- VDR-FokI homozygote → which interventions?
- PPARGC1A heterozygote → which interventions?
- Create genetic-optimized intervention list

### 4. Identify synergies
- **Nutrition + Injection**: Does vitamin C enhance prolotherapy outcomes?
- **Injection + Exercise**: Does eccentric loading enhance prolotherapy tissue remodeling?
- **Nutrition + Exercise**: Does methylation support improve exercise response?
- **Three-way synergies**: Prolotherapy + methylfolate + eccentric loading?

### 5. Flag conflicts and contraindications
- NSAIDs during prolotherapy healing window (timing matters)
- Anti-inflammatories with IL-6 management (when to use, when to avoid)
- Exercise intensity with inflammatory genetics
- Supplement interactions (calcium vs iron absorption)

### 6. Cost-benefit analysis
- High-cost/high-evidence interventions (prioritize these)
- Low-cost/high-evidence interventions (definitely include)
- High-cost/low-evidence interventions (consider carefully)
- Regional-only/high-cost interventions (medical tourism?)

## Output files

### 1. master_protocol_database.csv
Every intervention, graded, cross-referenced with:
- All extracted details
- Evidence grade
- Genetic relevance
- Synergies
- Costs
- Accessibility

### 2. evidence_summary.md
With sections:
- A-Grade Interventions (proven, use these)
- B-Grade Interventions (good evidence, likely beneficial)
- C-Grade Interventions (promising, needs validation)
- D-Grade Interventions (theoretical only, experimental)
- Genetic-Matched Priority List
- Synergistic Combinations
- Contraindications and Conflicts
