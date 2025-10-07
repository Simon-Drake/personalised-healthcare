# CLAUDE CODE ANALYSIS WORKFLOW
Complete 9-Prompt Sequence for Research Extraction & Protocol Generation

## Prerequisites
- All 24 research result files (*-1, *-2, *-3 results.txt for 8 languages)
- genetic_analysis_output.txt (completed genetic analysis)

## Output
Personalized treatment protocol with shopping lists, exercise programs, and decision trees

## Workflow Phases

### PHASE 1: DATA EXTRACTION (Prompts 1-3)
Extract detailed information from all language-specific research results:
- **Prompt 1**: Extract Nutrition Protocols (`prompt_1_extract_nutrition.md`)
- **Prompt 2**: Extract Injection Protocols (`prompt_2_extract_injections.md`)
- **Prompt 3**: Extract Exercise Protocols (`prompt_3_extract_exercise.md`)

### PHASE 2: CROSS-LANGUAGE PATTERN RECOGNITION (Prompts 4-6)
Analyze patterns across all languages to identify best practices:
- **Prompt 4**: Cross-Language Analysis - Nutrition (`prompt_4_analyze_nutrition.md`)
- **Prompt 5**: Cross-Language Analysis - Injections (`prompt_5_analyze_injections.md`)
- **Prompt 6**: Cross-Language Analysis - Exercise (`prompt_6_analyze_exercise.md`)

### PHASE 3: EVIDENCE GRADING & SYNTHESIS (Prompt 7)
Create comprehensive master database with evidence grades:
- **Prompt 7**: Create Master Protocol Database (`prompt_7_master_database.md`)

### PHASE 4: PERSONALIZED PROTOCOL GENERATION (Prompt 8)
Generate customized treatment protocol:
- **Prompt 8**: Generate YOUR Treatment Protocol (`prompt_8_personalized_protocol.md`)

### PHASE 5: REGIONAL INNOVATIONS REPORT (Prompt 9)
Compile region-specific findings and hidden gems:
- **Prompt 9**: Hidden Gems Deep Dive (`prompt_9_hidden_gems.md`)

## Execution Summary
- **Total Prompts**: 9
- **Input Requirements**: 24 result files + genetic_analysis_output.txt
- **Final Outputs**:
  - 3 CSV databases (nutrition, injection, exercise)
  - Master protocol database (all interventions, evidence-graded)
  - Personalized treatment protocol (phased implementation)
  - Shopping lists (supplements, equipment)
  - Exercise programs (phase-specific)
  - Tracking templates
  - Provider criteria
  - Decision trees (troubleshooting)
  - Hidden gems report (regional innovations)

## Deliverable
Complete evidence-based, personalized treatment protocol for structural restoration of ligamentous laxity in hypermobile joints, optimized for specific genetic profile, with realistic timelines and contingency plans.

## USAGE INSTRUCTIONS
1. Run prompts sequentially (each builds on previous)
2. Review outputs after each phase before proceeding
3. **Phase 1 (Prompts 1-3)**: Data extraction - can run in parallel if desired
4. **Phase 2 (Prompts 4-6)**: Analysis - must be sequential
5. **Phase 3 (Prompt 7)**: Synthesis - requires all previous outputs
6. **Phase 4 (Prompt 8)**: Your protocol - final personalized plan
7. **Phase 5 (Prompt 9)**: Bonus - regional innovations assessment

**Start with Prompt 1 when ready.**
