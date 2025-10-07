# CLAUDE CODE PROMPT 3: Extract Exercise Protocols

## Input files
- chinese-3 results.txt
- english-3 results.txt
- french-3 results.txt
- german-3 results.txt
- japanese-3 results.txt
- korean-3 results.txt
- portuguese-3 results.txt
- spanish-3 results.txt

## Task
Read all 8 exercise result files and extract every exercise/movement with complete details.

**CRITICAL**: Focus on exercises that demonstrate TISSUE REGENERATION evidence, not just functional compensation.

## Extraction Requirements
For each exercise, extract:
- **Exercise name**: Full descriptive name
- **Target tissue**: Specific structures (scapholunate ligament, thoracolumbar interspinous ligaments, TFCC, multifidus + adjacent ligaments, etc.)
- **Exercise type**: Eccentric / Isometric / Concentric / Dynamic / Static
- **Sets**: Number of sets
- **Reps**: Number of repetitions (or time if isometric hold)
- **Hold time**: Duration of contraction (seconds)
- **Tempo**: Speed of movement (e.g., 3-1-3 for eccentric-pause-concentric)
- **Load**: Bodyweight / resistance band / kg / progressive
- **Frequency**: Times per week
- **Rest between sets**: Recovery time
- **Progression criteria**: When/how to advance (e.g., "when pain <3/10 for 1 week, add 1kg")
- **Evidence of tissue regeneration**: Key finding:
  - Reduced laxity measurements (KT-1000, arthrometry)
  - Increased ligament CSA on ultrasound
  - Reduced pathological translation on imaging
  - Improved carpal alignment
  - NOT just "reduced pain" or "improved function" without structural changes
- **Mechanism**: How it stimulates tissue regeneration (myofibroblast activation, collagen deposition, etc.)
- **Success rate**: If reported, percentage achieving structural improvement
- **Population**: Hypermobile / post-surgical / general
- **Contraindications**: What to avoid or when not to do
- **Flare-up protocol**: What to do if inflammatory response
- **Citation**: Study reference or source
- **Language/region**: Which language/region this came from
- **Evidence quality**: RCT / observational / expert consensus

## Create Structured Output
Create CSV with columns:
```
exercise_name,target_tissue,type,sets,reps,hold_time,tempo,load,frequency,rest,progression,regeneration_evidence,mechanism,success_rate,population,contraindications,flare_protocol,citation,language,evidence_grade
```

## Output files
1. **exercise_protocols.csv** - Every exercise across all 8 languages

2. **exercise_summary.md** - Initial patterns:
   - Exercises with tissue regeneration evidence vs compensation only
   - Mechanical loading patterns that stimulate collagen deposition
   - Eastern approaches (站桩功, 八段錦, acupotomy) vs Western
   - Eccentric vs isometric protocols
   - Wrist-specific vs spine-specific
   - IL-6-appropriate progressions (low flare-up risk)
