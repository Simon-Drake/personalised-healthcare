# CLAUDE CODE PROMPT 8: Generate YOUR Treatment Protocol

## Input files
- master_protocol_database.csv
- evidence_summary.md
- genetic_analysis_output.txt

## User Context

### Clinical Profile
- **Age**: 32 years old
- **Right wrist**: Severe instability post-2 surgeries, carpal bone misalignment (bones "drooping"), chronic clicking, nerve symptoms
- **Left wrist**: Attenuated ligaments, early instability (preventable progression)
- **Thoracolumbar spine**: T11-L2 iatrogenic instability (lateral and rotational), THE MOST LIMITING
- **Lower lumbar**: L4/L5 pain on flexion
- **Imaging**: All normal (MRI, X-rays) - functional instability not visible on imaging
- **Progression timeline**: Healthy spine 1 year ago → now severely limited (rapid acute-on-chronic)
- **Failed treatments**: 2 wrist surgeries, conventional PT
- **Current treatment**: Started prolotherapy August 2025 (now ~2 months in)

### Genetic Profile
- **MTHFR C677T heterozygote + MTHFR A1298C heterozygote** (compound effect - impaired methylation/collagen crosslinking)
- **TCN2 G776C HOMOZYGOTE** (severe B12 transport deficiency - critical)
- **IL-6 HOMOZYGOTE** (high baseline inflammation - high flare-up sensitivity)
- **GPX1 HOMOZYGOTE** (reduced glutathione peroxidase - oxidative stress vulnerability)
- **VDR-FokI HOMOZYGOTE** (altered vitamin D receptor activity)
- **PPARGC1A G482S heterozygote** (reduced mitochondrial biogenesis)

### Challenges
- High sensitivity to inflammatory flare-ups with exercise
- Difficulty with consistency due to sleep issues and discomfort
- History of destabilization from inappropriate treatment (chiropractor caused spinal injury)
- Need stability without triggering inflammation

### Goals
- **Structural restoration**: ligaments become shorter and thicker
- **Right wrist**: restore stability, reduce clicking, improve carpal alignment
- **Left wrist**: prevent progression
- **Spine**: regain T11-L2 stability (lateral and rotational), resolve L4/L5 pain
- **Long-term**: capable of farming work and martial arts training
- **Timeline**: willing to commit 12-24 months for complete restoration

## Task
Generate comprehensive, phased, personalized treatment protocol optimized for this specific profile.

## Protocol Structure

### PHASE 1: FOUNDATION (Months 0-3) - Optimize Current Prolotherapy
**Goal**: Maximize effectiveness of ongoing prolotherapy, establish nutritional foundation, begin gentle loading

#### Nutrition
List every supplement with:
- Name and specific form (e.g., "Methylfolate 5mg, NOT folic acid")
- Exact dosage
- Timing (morning/evening, with food/empty stomach)
- Genetic rationale (e.g., "TCN2 homozygote requires methylcobalamin sublingual")
- Mechanism (how it supports tissue regeneration)
- Brand recommendations if critical (e.g., active B12 forms)
- Monthly cost estimate

#### Injections
- Current prolotherapy: Continue full series (typically 4-6 treatments)
- Optimal protocol based on evidence (concentration, frequency)
- If approaching session 4-6 with inadequate response, consider: PRP addition, peptides, or protocol adjustment
- Provider criteria: what to look for in prolotherapy doctor

#### Exercise
- Gentle proprioceptive and awareness exercises ONLY
- Focus: avoid re-injury during prolotherapy healing windows
- Wrist: protected ROM, no loading yet
- Spine: basic multifidus awareness, no challenging loads
- Activity modifications: what to avoid completely

#### Monitoring
- Track: pain levels (0-10 scale), functional activities (what you can/can't do), sleep quality, flare-up frequency
- Success markers: reduced clicking frequency, improved confidence, pain trending down
- Red flags: worsening instability, increased clicking, new symptoms

### PHASE 2: INTENSIVE REGENERATION (Months 3-6)
**Goal**: Build on prolotherapy foundation, add progressive loading, maximize tissue remodeling

#### Nutrition
- Continue Phase 1 supplements
- Additions based on response (if needed): increased vitamin C for collagen, additional copper/lysine if crosslinking support needed
- Anti-inflammatory timing: when to use curcumin/omega-3 (NOT during prolotherapy healing windows)

#### Injections
- Complete prolotherapy series
- Evaluate outcomes at end of series:
  - If 50-70% improved: consider maintenance schedule (quarterly boosters)
  - If <50% improved: consider PRP upgrade, peptide addition, or protocol change
  - If >70% improved: transition to maintenance, focus on exercise loading

#### Exercise
BEGIN PROGRESSIVE LOADING for tissue regeneration:

**Wrist (Right - severe):**
- Eccentric wrist extensions: [specific protocol from exercise_protocols.csv with A/B grade evidence]
- TFCC loading: [specific protocol]
- Progression: start with [X sets × Y reps], advance when pain <3/10 for 1 week
- Frequency: 3x per week with 48-72 hour recovery

**Wrist (Left - preventive):**
- Earlier progression than right
- Focus on preventing deterioration

**Spine (T11-L2 - MOST LIMITING):**
- Thoracolumbar-specific core: [specific exercises from exercise_protocols.csv]
- Lateral stability: [specific movements]
- Rotational stability: [specific movements]
- Multifidus + interspinous ligament loading
- Frequency: daily gentle, 3x per week loaded

**IL-6 Flare-up Management:**
- Volume: start with 50% of "normal" recommendations
- Recovery: extra day between sessions if baseline soreness
- Red light: if pain >5/10 after exercise, reduce to previous level
- Anti-inflammatory protocol: [when and how to use]

#### Monitoring
- Track: objective measures (grip strength if possible, ROM, specific functional tasks)
- Success markers: reduced laxity (subjective feeling of "tightness"), improved stability, higher activity tolerance
- Timeline expectations: initial tissue changes at 3-4 months, measurable at 6 months

### PHASE 3: CONSOLIDATION (Months 6-12)
**Goal**: Continue tissue strengthening, advance loading, achieve normal function

#### Nutrition
- Continue core supplements
- Reassess: can any be reduced based on response?
- Maintenance dosing for genetic optimization

#### Injections
- Maintenance protocol if needed: quarterly boosters for right wrist/spine
- Evaluate left wrist: does it need treatment series now?

#### Exercise
ADVANCE LOADING progressively:
- Wrist: increase resistance [protocol progression]
- Spine: increase complexity and load [protocol progression]
- Add functional movements (lifting, carrying, martial arts prep)

#### Monitoring
- Success markers: return to activities (specific tasks you couldn't do before)
- Reassess at 9 months: imaging if accessible (ultrasound for ligament CSA, stress radiography for laxity)
- Adjust protocol based on response

### PHASE 4: MAINTENANCE & OPTIMIZATION (Months 12-24+)
**Goal**: Maintain gains, prevent regression, build toward full activity

#### Nutrition
- Minimum effective dose for maintenance
- Genetic-optimized baseline for life

#### Injections
- As-needed boosters (6-12 month intervals if stability maintained)
- Consider stopping if complete stability achieved

#### Exercise
- Lifelong maintenance program
- Progressive return to: farming work, martial arts
- Ongoing loading to maintain tissue integrity

#### Monitoring
- Long-term: annual check-ins on stability
- Red flags for regression: return of clicking, increased laxity feeling

## Required Output Files

### Shopping Lists
1. **shopping_list_month_1.csv**
   - Every supplement to buy immediately
   - Exact product names, brands where critical
   - Dosages, timing
   - Where to purchase
   - Monthly cost total

2. **shopping_list_phase_2_additions.csv**
   - Additional items starting month 3

3. **equipment_list.csv**
   - Resistance bands, weights, etc. for exercise
   - One-time purchases

### Exercise Programs
1. **exercise_program_phase_1.md**
   - Week-by-week progression
   - Exact exercises with photos/video links if available
   - Form cues
   - What to avoid

2. **exercise_program_phase_2.md**
   - Progressive loading protocols
   - When to advance
   - Flare-up troubleshooting

3. **exercise_program_phase_3_4.md**
   - Advanced protocols
   - Functional integration
   - Maintenance program

### Tracking & Support
1. **tracking_template.csv**
   - Daily tracking: pain levels, activities, sleep, flare-ups
   - Weekly tracking: exercise compliance, supplement compliance
   - Monthly tracking: functional improvements, grip strength, specific tasks
   - Columns: date, pain_right_wrist, pain_left_wrist, pain_spine, clicking_frequency, sleep_quality, exercise_done, supplements_taken, notes

2. **provider_criteria.md**
   - What to look for in prolotherapy doctor
   - Experience with hypermobile patients
   - Comprehensive injection technique (20-30 sites per session)
   - Willing to use optimal concentration (15% dextrose minimum)
   - Understanding of genetic factors (methylation support)
   - Red flags: doctors who dismiss hypermobility, inadequate injection technique
   - Questions to ask potential providers
   - How to evaluate if current provider is optimal

3. **decision_trees.md**

**Decision Tree 1: Prolotherapy Not Working**
```
After Session 4:
├─ <30% improvement
│  ├─ Check: adequate injection sites? (should be 20-30 per session)
│  ├─ Check: adequate concentration? (15% minimum)
│  ├─ Check: nutrition optimized? (methylation support adequate?)
│  └─ Consider: PRP addition or switch to PRP
│
├─ 30-50% improvement
│  ├─ Continue to session 6
│  └─ Re-evaluate after session 6
│
└─ >50% improvement
   └─ Continue current protocol
```

**Decision Tree 2: Exercise Causing Flare-ups**
```
After Exercise Session:
├─ Pain >5/10 next day
│  ├─ Reduce volume by 50%
│  ├─ Add extra recovery day
│  └─ Check form (recording yourself)
│
├─ Pain 3-5/10 next day
│  ├─ Maintain current volume
│  └─ Don't progress yet
│
└─ Pain <3/10 next day
   └─ Can progress (add 5-10% load or 1-2 reps)
```

**Decision Tree 3: Supplement Stack Not Helping**
```
After 8 weeks on full protocol:
├─ No improvement in energy/inflammation
│  ├─ Check: actual B12 levels (blood test)
│  ├─ Check: methylation markers (homocysteine)
│  └─ Adjust: may need higher doses or different forms
│
├─ Some improvement
│  └─ Continue, full benefits take 3-6 months
│
└─ Significant improvement
   └─ Maintain current protocol
```

## Final Deliverables
1. personalized_treatment_protocol.md - Complete implementation guide with all phases
2. shopping_list_month_1.csv
3. shopping_list_phase_2_additions.csv
4. equipment_list.csv
5. exercise_program_phase_1.md
6. exercise_program_phase_2.md
7. exercise_program_phase_3_4.md
8. tracking_template.csv
9. provider_criteria.md
10. decision_trees.md
