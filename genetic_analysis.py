#!/usr/bin/env python3
"""
Comprehensive Genetic Profile Analysis
Analyzes genetic variants for connective tissue health, treatment response, and overall health optimization
"""

import csv
import re
from collections import defaultdict
from typing import Dict, List, Tuple

# Define gene categories with comprehensive gene lists
GENE_CATEGORIES = {
    'A_STRUCTURAL': {
        'name': 'STRUCTURAL GENES (Connective Tissue)',
        'genes': [
            'COL1A1', 'COL1A2', 'COL3A1', 'COL5A1', 'COL5A2', 'COL6A1', 'COL6A2', 'COL6A3',
            'ELN', 'FBN1', 'FBN2', 'FBN3',
            'MMP1', 'MMP2', 'MMP3', 'MMP9', 'MMP13',
            'TGFB1', 'TGFB2', 'TGFB3', 'TGFBR1', 'TGFBR2',
            'TNC', 'TNXB', 'TNX',
            'PLOD1', 'ADAMTS2', 'ADAMTS5',
            'LOXL1', 'LOXL2', 'LOXL3', 'LOXL4',
            'P4HA1', 'P4HA2', 'P4HB',
            'COMP', 'ACAN', 'DCN', 'LUM', 'FMOD',
            'BGN', 'VCAN'
        ]
    },
    'B_NUTRITIONAL': {
        'name': 'NUTRITIONAL METABOLISM',
        'genes': [
            # B vitamins
            'MTHFR', 'MTR', 'MTRR', 'MTHFD1', 'BHMT', 'CBS',
            'FUT2', 'TCN1', 'TCN2', 'NBPF3',
            # Vitamin C
            'SLC23A1', 'SLC23A2', 'GULO',
            # Vitamin D
            'VDR', 'CYP2R1', 'CYP24A1', 'CYP27B1', 'GC',
            # Minerals
            'ATP7A', 'ATP7B', 'SLC30A8', 'ZIP4', 'FTH1', 'HFE',
            'TRPV6', 'SLC8A1', 'CLDN16',
            # Amino acids
            'PRODH', 'P5CS', 'ALDH18A1', 'SLC7A1', 'SLC7A7', 'SLC3A2',
            # Omega-3/fats
            'FADS1', 'FADS2', 'ELOVL2', 'ELOVL5', 'ACSL1', 'APOE', 'APOA2',
            'PPAR', 'PPARA', 'PPARG', 'PPARGC1A', 'LPA', 'PON1',
            # Antioxidants
            'SOD1', 'SOD2', 'SOD3', 'GPX1', 'GPX3', 'GPX4', 'CAT', 'GST', 'GSTM1',
            # Choline
            'PEMT', 'CHDH', 'BHMT'
        ]
    },
    'C_INFLAMMATION': {
        'name': 'INFLAMMATION & IMMUNE RESPONSE',
        'genes': [
            # Cytokines
            'IL1A', 'IL1B', 'IL6', 'IL10', 'IL17', 'IL23', 'TNF', 'TNFA',
            # COX pathway
            'COX1', 'COX2', 'PTGS1', 'PTGS2',
            # NFkB pathway
            'NFKB1', 'NFKB2', 'NFKBIA', 'IKBKB',
            # Immune regulation
            'HLA', 'CTLA4', 'FOXP3', 'TLR2', 'TLR4', 'TLR9',
            # Histamine
            'DAO', 'ABP1', 'HNMT', 'HDC', 'MAOA', 'MAOB'
        ]
    },
    'D_EXERCISE': {
        'name': 'EXERCISE & PHYSICAL RESPONSE',
        'genes': [
            'ACTN3', 'ACE', 'ACE1', 'PPARA', 'PPARGC1A',
            'ADRB2', 'ADRB3',
            'NOS3', 'VEGFA', 'HIF1A',
            'IGF1', 'IGF2', 'MSTN', 'GDF8',
            'AMPD1', 'CKM',
            'COL5A1', 'COL1A1'
        ]
    },
    'E_TREATMENT': {
        'name': 'TREATMENT RESPONSE',
        'genes': [
            # Drug metabolism
            'CYP1A2', 'CYP2C9', 'CYP2C19', 'CYP2D6', 'CYP3A4', 'CYP3A5',
            'CYP17A1', 'CYP17A2', 'CYP19A1', 'CYP21A2',
            'NAT1', 'NAT2', 'TPMT', 'DPYD', 'UGT1A1',
            # Pain sensitivity
            'COMT', 'OPRM1', 'SCN9A', 'MC1R', 'GCH1', 'FAAH',
            # Healing/regeneration
            'HGF', 'FGFR1', 'FGFR2', 'EGF', 'EGFR',
            'PDGF', 'PDGFRA', 'PDGFRB',
            # Growth factors
            'IGF1', 'IGF1R', 'GHR', 'GHRH', 'GHSR',
            # Stem cells
            'SOX2', 'NANOG', 'POU5F1', 'KLF4',
            # Vitamin K (warfarin response)
            'VKORC1', 'CYP4F2'
        ]
    },
    'F_COMORBIDITY': {
        'name': 'COMORBIDITY RISK',
        'genes': [
            # Cardiovascular
            'APOE', 'LPA', 'PCSK9', 'LDLR', 'ACE', 'ACE1', 'AGTR1', 'NOS1', 'NOS3',
            'MTHFR', 'F2', 'F5', 'FGB',
            # Autonomic/POTS
            'DBH', 'SLC6A2', 'ADRB1', 'ADRB2', 'NET', 'COMT',
            # Anxiety/depression
            'SLC6A4', '5HT2A', '5-HT2A', 'HTR2A', 'BDNF', 'MAOA', 'TPH1', 'TPH2',
            # GI motility
            'SCN5A', 'ANO1', 'NOS1', 'SERT', 'HTR3', 'HTR4',
            # Autoimmune
            'HLA', 'PTPN22', 'CTLA4', 'IL2RA', 'STAT4', 'TNF', 'TNFA',
            # Thyroid
            'DIO1', 'DIO2', 'TPO', 'TSHR',
            # Diabetes/metabolic
            'TCF7L2', 'PPARG', 'KCNJ11', 'ADIPOQ', 'MTNR1B', 'SHBG'
        ]
    },
    'G_CELLULAR': {
        'name': 'CELLULAR HEALTH',
        'genes': [
            # Mitochondrial
            'PPARGC1A', 'NRF1', 'NRF2', 'TFAM', 'OPA1', 'MFN1', 'MFN2',
            'COQ2', 'COQ10', 'NDUFV1', 'NDUFV2',
            # DNA repair
            'BRCA1', 'BRCA2', 'ATM', 'TP53', 'MLH1', 'MSH2', 'MSH6', 'PMS2',
            'XRCC1', 'XRCC3', 'OGG1', 'MUTYH',
            # Telomeres
            'TERT', 'TERC', 'RTEL1', 'DKC1', 'TINF2',
            # Autophagy
            'ATG5', 'ATG7', 'BECN1', 'LAMP2', 'SQSTM1', 'MAP1LC3A',
            # Cellular transport
            'ABCG2', 'ABCB1', 'ABCC2'
        ]
    }
}

# Clinical significance patterns for connective tissue health
CLINICAL_SIGNIFICANCE = {
    # Structural/connective tissue
    'COL': 'CRITICAL for collagen synthesis - directly affects connective tissue strength and quality',
    'FBN': 'CRITICAL for fibrillin production - affects tissue elasticity and TGF-β regulation',
    'ELN': 'CRITICAL for elastin production - affects vascular and tissue elasticity',
    'MMP': 'Important for extracellular matrix remodeling - affects tissue repair and turnover',
    'TGFB': 'CRITICAL for TGF-β signaling - regulates collagen production and fibrosis',

    # B vitamins (critical for collagen synthesis)
    'MTHFR': 'CRITICAL for folate metabolism - affects collagen crosslinking and homocysteine levels',
    'MTR': 'Important for B12 utilization and methionine production - affects methylation and collagen synthesis',
    'MTRR': 'Important for B12 recycling - works with MTR for proper methylation',
    'MTHFD1': 'Important for folate metabolism - affects DNA synthesis and methylation',
    'TCN2': 'CRITICAL for B12 transport - affects cellular B12 availability',
    'FUT2': 'Affects B12 absorption and gut microbiome - impacts nutrient status',
    'NBPF3': 'Affects vitamin B6 clearance - important for amino acid metabolism',

    # Vitamin C (critical for collagen)
    'SLC23': 'CRITICAL for vitamin C transport - essential for collagen hydroxylation',

    # Vitamin D (affects tissue health)
    'VDR': 'Important for vitamin D signaling - affects bone health, inflammation, immune function',
    'CYP2R1': 'Important for vitamin D activation - affects vitamin D status',

    # Inflammation (EDS comorbidity)
    'IL6': 'CRITICAL for inflammation regulation - elevated IL-6 linked to chronic pain and fatigue',
    'TNF': 'Important for inflammatory response - affects systemic inflammation',
    'TNFA': 'Important for inflammatory response - affects systemic inflammation',

    # Antioxidants (protect collagen)
    'GPX1': 'Important antioxidant - protects tissues from oxidative damage',
    'SOD': 'Important antioxidant - protects against superoxide damage',

    # Exercise/physical response
    'ACE1': 'Affects endurance vs power - important for exercise programming',
    'ACE': 'Affects endurance vs power - important for exercise programming',
    'ACTN3': 'Affects muscle fiber type - impacts exercise tolerance and injury risk',
    'ADRB2': 'Affects cardiovascular response to exercise and beta-agonists',

    # Drug metabolism
    'CYP': 'Important for drug metabolism - affects medication dosing and side effects',
    'COMT': 'Affects pain sensitivity and stress response - important for pain management',

    # Cardiovascular (EDS comorbidity)
    'APOE': 'Affects lipid metabolism and cardiovascular risk',
    'AGTR1': 'Affects blood pressure regulation - important for POTS/dysautonomia',

    # Mental health (EDS comorbidity)
    '5HT': 'Affects serotonin signaling - important for mood and anxiety management',
    '5-HT': 'Affects serotonin signaling - important for mood and anxiety management',
    'BDNF': 'Affects neuroplasticity - important for mood and cognitive function',

    # Metabolic
    'PPARGC1A': 'CRITICAL for mitochondrial function - affects energy production and exercise response',
    'TCF7L2': 'Affects insulin secretion - important for blood sugar regulation',
    'DIO1': 'Affects thyroid hormone conversion - important for metabolism',

    # Choline (affects connective tissue)
    'PEMT': 'Important for choline synthesis - affects methylation and acetylcholine production',

    # Mineral metabolism
    'HFE': 'Affects iron metabolism - important to monitor iron status',

    # Cellular transport
    'ABCG2': 'Affects drug and toxin transport - can affect medication response and uric acid levels'
}

def extract_gene_name(gene_field: str) -> str:
    """Extract the core gene name from various formats"""
    # Remove SNP IDs and extra info
    gene = gene_field.split()[0].strip().strip('"')

    # Handle special cases
    if 'HLA' in gene.upper():
        return 'HLA'
    if gene.startswith('5-HT'):
        return '5-HT2A'

    # Extract gene name from various formats
    # e.g., "MTHFR C677T" -> "MTHFR"
    # e.g., "HFE-C282Y" -> "HFE"
    match = re.match(r'^([A-Z0-9]+)', gene)
    if match:
        return match.group(1)

    return gene

def categorize_gene(gene_name: str) -> List[str]:
    """Categorize a gene into one or more categories"""
    categories = []
    gene_upper = gene_name.upper()

    for cat_id, cat_info in GENE_CATEGORIES.items():
        for cat_gene in cat_info['genes']:
            if gene_upper == cat_gene.upper() or gene_upper.startswith(cat_gene.upper()):
                categories.append(cat_id)
                break

    return categories

def get_clinical_significance(gene_name: str) -> str:
    """Get clinical significance for a gene"""
    gene_upper = gene_name.upper()

    # Check for exact or partial matches
    for key, significance in CLINICAL_SIGNIFICANCE.items():
        if gene_upper == key.upper() or gene_upper.startswith(key.upper()):
            return significance

    return "General health relevance - monitor based on result"

def get_treatment_implications(gene_name: str, result: str, description: str) -> str:
    """Generate treatment implications based on gene and result"""
    gene_upper = gene_name.upper()
    implications = []

    # B vitamin metabolism
    if gene_upper in ['MTHFR', 'MTHFD1', 'MTR', 'MTRR']:
        if result != 'Wild Type':
            implications.append("Consider methylated B vitamins (methylfolate, methylB12)")
            implications.append("Monitor homocysteine levels")
            implications.append("Support collagen synthesis with adequate B vitamin status")

    if gene_upper == 'TCN2':
        if result == 'Homozygous':
            implications.append("CRITICAL: Consider high-dose B12 supplementation (methylcobalamin)")
            implications.append("May need sublingual or injectable B12 for better absorption")
            implications.append("Monitor B12 levels regularly - affects collagen synthesis")

    if gene_upper == 'FUT2':
        if result != 'Wild Type':
            implications.append("Non-secretor status - may have reduced B12 absorption")
            implications.append("Consider higher B12 intake and probiotic support")

    if gene_upper == 'NBPF3':
        if result != 'Wild Type':
            implications.append("May have increased B6 clearance - monitor B6 status")
            implications.append("Consider B6 (P5P form) supplementation")

    # Vitamin D
    if gene_upper in ['VDR', 'CYP2R1']:
        if result != 'Wild Type':
            implications.append("Monitor vitamin D levels closely")
            implications.append("May need higher vitamin D supplementation")
            implications.append("Ensure adequate vitamin K2 for bone health")

    # Inflammation
    if gene_upper == 'IL6':
        if result == 'Homozygous':
            implications.append("CRITICAL: High IL-6 expression - anti-inflammatory diet essential")
            implications.append("Consider omega-3 fatty acids (EPA/DHA)")
            implications.append("Curcumin and other anti-inflammatory supplements may help")
            implications.append("May benefit from low-inflammatory lifestyle modifications")

    if gene_upper in ['TNF', 'TNFA']:
        if result != 'Wild Type':
            implications.append("Increased TNF-alpha production - anti-inflammatory support needed")
            implications.append("Omega-3s, turmeric, and anti-inflammatory diet recommended")

    # Antioxidants
    if gene_upper == 'GPX1':
        if result == 'Homozygous':
            implications.append("CRITICAL: Reduced glutathione peroxidase - increase antioxidant support")
            implications.append("Consider selenium, NAC, glutathione supplementation")
            implications.append("Protect collagen from oxidative damage")

    # Exercise genes
    if gene_upper in ['ACE', 'ACE1']:
        if result == 'Homozygous':
            implications.append("Determine ACE genotype (I/I, I/D, D/D) for exercise programming")
            implications.append("May affect endurance vs power training response")
            implications.append("Important for POTS/cardiovascular management")

    if gene_upper == 'ADRB2':
        if result != 'Wild Type':
            implications.append("May have altered response to beta-agonists")
            implications.append("Affects cardiovascular response to exercise and stress")

    # Drug metabolism
    if gene_upper.startswith('CYP'):
        if result != 'Wild Type':
            implications.append(f"Altered {gene_upper} activity - may affect drug metabolism")
            implications.append("Consider pharmacogenetic testing for medication optimization")
            implications.append("Discuss with doctor before starting new medications")

    # Pain management
    if gene_upper == 'COMT':
        if result != 'Wild Type':
            implications.append("May affect dopamine metabolism and pain sensitivity")
            implications.append("Important for pain management strategy")

    # Metabolic/mitochondrial
    if gene_upper == 'PPARGC1A':
        if result != 'Wild Type':
            implications.append("May have reduced mitochondrial biogenesis")
            implications.append("Consider CoQ10, PQQ, and mitochondrial support")
            implications.append("Affects exercise response and energy production")

    if gene_upper == 'TCF7L2':
        if result == 'Homozygous':
            implications.append("CRITICAL: Increased diabetes risk - monitor blood sugar closely")
            implications.append("Low glycemic diet and regular exercise important")

    if gene_upper == 'DIO1':
        if result == 'Homozygous':
            implications.append("May have altered thyroid hormone conversion")
            implications.append("Monitor thyroid function (TSH, T3, T4)")
            implications.append("Consider selenium for thyroid support")

    # Choline
    if gene_upper == 'PEMT':
        if result != 'Wild Type':
            implications.append("Reduced choline synthesis - increase choline intake")
            implications.append("Consider choline supplementation or choline-rich foods")
            implications.append("Affects methylation and acetylcholine production")

    # Cardiovascular
    if gene_upper == 'AGTR1':
        if result != 'Wild Type':
            implications.append("May affect blood pressure regulation")
            implications.append("Important for POTS/dysautonomia management")

    # Mental health
    if '5HT' in gene_upper or '5-HT' in gene_upper:
        if result != 'Wild Type':
            implications.append("May affect serotonin receptor function")
            implications.append("Important for mood, anxiety, and medication response")

    # Uric acid
    if gene_upper == 'ABCG2':
        if result != 'Wild Type':
            implications.append("May have elevated uric acid - monitor levels")
            implications.append("Consider low-purine diet if needed")

    if not implications:
        if result != 'Wild Type':
            implications.append("Genetic variant present - discuss with healthcare provider")
        else:
            implications.append("Normal gene function - no specific intervention needed")

    return " | ".join(implications)

def analyze_genetic_profile(csv_file: str):
    """Main analysis function"""

    print("=" * 100)
    print("COMPREHENSIVE GENETIC PROFILE ANALYSIS")
    print("Focus: Connective Tissue Health, Treatment Response & Overall Health Optimization")
    print("=" * 100)
    print()

    # Read CSV
    genes_data = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            genes_data.append(row)

    # Categorize all genes
    categorized_genes = defaultdict(list)
    uncategorized_genes = []

    for row in genes_data:
        gene_field = row['Gene']
        gene_name = extract_gene_name(gene_field)
        categories = categorize_gene(gene_name)

        gene_info = {
            'original': gene_field,
            'name': gene_name,
            'description': row['Description'],
            'result': row['Result'],
            'mutations': row['# Mutations'],
            'categories': categories
        }

        if categories:
            for cat in categories:
                categorized_genes[cat].append(gene_info)
        else:
            uncategorized_genes.append(gene_info)

    # Print results by category
    total_analyzed = len(genes_data)
    total_categorized = sum(len(genes) for genes in categorized_genes.values())

    for cat_id in sorted(GENE_CATEGORIES.keys()):
        cat_info = GENE_CATEGORIES[cat_id]
        genes = categorized_genes.get(cat_id, [])

        print(f"\n{'=' * 100}")
        print(f"CATEGORY {cat_id[-1]}: {cat_info['name']}")
        print(f"{'=' * 100}")
        print(f"Genes found in this category: {len(genes)}")
        print()

        if genes:
            for gene in sorted(genes, key=lambda x: (x['result'] != 'Wild Type', x['mutations']), reverse=True):
                print(f"  Gene: {gene['original']}")
                print(f"  Core Gene Name: {gene['name']}")
                print(f"  Result: {gene['result']} ({gene['mutations']} mutation(s))")

                if gene['description']:
                    # Wrap description
                    desc_lines = [gene['description'][i:i+90] for i in range(0, len(gene['description']), 90)]
                    print(f"  Description: {desc_lines[0]}")
                    for line in desc_lines[1:]:
                        print(f"               {line}")

                significance = get_clinical_significance(gene['name'])
                print(f"  Clinical Significance: {significance}")

                implications = get_treatment_implications(gene['name'], gene['result'], gene['description'])
                impl_lines = implications.split(' | ')
                print(f"  Treatment Implications:")
                for impl in impl_lines:
                    print(f"    • {impl}")

                print(f"  {'-' * 96}")
        else:
            print(f"  No genes from this category found in your genetic profile.")

    # Print summary
    print(f"\n{'=' * 100}")
    print("COMPREHENSIVE SUMMARY")
    print(f"{'=' * 100}")
    print()

    print(f"Total Genes Analyzed: {total_analyzed}")
    print(f"Genes Categorized as Relevant: {total_categorized}")
    print(f"Uncategorized Genes: {len(uncategorized_genes)}")
    print()

    print("Breakdown by Category:")
    for cat_id in sorted(GENE_CATEGORIES.keys()):
        cat_info = GENE_CATEGORIES[cat_id]
        count = len(categorized_genes.get(cat_id, []))
        print(f"  {cat_info['name']}: {count} genes")

    # High priority genes (variants with clinical significance)
    print(f"\n{'=' * 100}")
    print("HIGH-PRIORITY GENES (Variants with Known Clinical Significance)")
    print(f"{'=' * 100}")
    print()

    high_priority = []
    for cat_id, genes in categorized_genes.items():
        for gene in genes:
            if gene['result'] != 'Wild Type':
                significance = get_clinical_significance(gene['name'])
                if 'CRITICAL' in significance or gene['result'] == 'Homozygous':
                    high_priority.append((gene, significance))

    if high_priority:
        for gene, significance in sorted(high_priority, key=lambda x: ('CRITICAL' not in x[1], x[0]['result'] != 'Homozygous')):
            print(f"  ⚠️  {gene['name']} ({gene['original']}): {gene['result']}")
            print(f"      {significance}")
            implications = get_treatment_implications(gene['name'], gene['result'], gene['description'])
            impl_lines = implications.split(' | ')
            print(f"      Action items:")
            for impl in impl_lines[:3]:  # Show top 3 implications
                print(f"        → {impl}")
            print()
    else:
        print("  No high-priority variants identified.")

    # Gene interactions and pathways
    print(f"{'=' * 100}")
    print("CRITICAL GENE INTERACTIONS & PATHWAYS")
    print(f"{'=' * 100}")
    print()

    # Check for B vitamin pathway issues
    b_vitamin_genes = []
    for cat_id, genes in categorized_genes.items():
        for gene in genes:
            if gene['name'].upper() in ['MTHFR', 'MTR', 'MTRR', 'MTHFD1', 'TCN2', 'FUT2', 'NBPF3']:
                if gene['result'] != 'Wild Type':
                    b_vitamin_genes.append(gene)

    if len(b_vitamin_genes) >= 2:
        print("  ⚠️  MULTIPLE B VITAMIN PATHWAY VARIANTS DETECTED:")
        for gene in b_vitamin_genes:
            print(f"     • {gene['name']}: {gene['result']}")
        print()
        print("  COMBINED IMPACT:")
        print("    → CRITICAL: Multiple B vitamin variants significantly impair methylation")
        print("    → This directly affects collagen synthesis and crosslinking")
        print("    → Homocysteine levels likely elevated - cardiovascular risk increased")
        print("    → Comprehensive B vitamin supplementation ESSENTIAL (methylated forms)")
        print("    → Consider: Methylfolate, MethylB12, B6 (P5P), B2, TMG/Betaine")
        print("    → Monitor: Homocysteine, B12, folate levels regularly")
        print()

    # Check for inflammation + structural issues
    inflammation_genes = []
    for cat_id, genes in categorized_genes.items():
        for gene in genes:
            if gene['name'].upper() in ['IL6', 'TNF', 'TNFA']:
                if gene['result'] != 'Wild Type':
                    inflammation_genes.append(gene)

    if inflammation_genes:
        print("  ⚠️  INFLAMMATORY PATHWAY ACTIVATION DETECTED:")
        for gene in inflammation_genes:
            print(f"     • {gene['name']}: {gene['result']}")
        print()
        print("  COMBINED IMPACT:")
        print("    → Chronic inflammation can degrade collagen and connective tissue")
        print("    → Increased risk of pain, fatigue, and tissue damage")
        print("    → Anti-inflammatory diet and supplements CRITICAL")
        print("    → Consider: Omega-3 (EPA/DHA), Curcumin, SPMs (specialized pro-resolving mediators)")
        print("    → Monitor: CRP, IL-6 levels if possible")
        print()

    # Check for antioxidant + inflammation issues
    antioxidant_genes = []
    for cat_id, genes in categorized_genes.items():
        for gene in genes:
            if gene['name'].upper() in ['GPX1', 'SOD1', 'SOD2', 'CAT']:
                if gene['result'] != 'Wild Type':
                    antioxidant_genes.append(gene)

    if antioxidant_genes and inflammation_genes:
        print("  ⚠️  OXIDATIVE STRESS + INFLAMMATION COMBINATION:")
        print("     Antioxidant variants + inflammatory variants = HIGH oxidative damage risk")
        print()
        print("  COMBINED IMPACT:")
        print("    → Collagen and connective tissue at high risk of oxidative damage")
        print("    → Accelerated aging and tissue degradation likely")
        print("    → Comprehensive antioxidant support ESSENTIAL")
        print("    → Consider: NAC, Glutathione, Selenium, Vitamin C, Vitamin E, ALA")
        print("    → Reduce oxidative stressors (processed foods, toxins, excessive exercise)")
        print()

    # Check for mitochondrial + metabolic issues
    mito_genes = []
    for cat_id, genes in categorized_genes.items():
        for gene in genes:
            if gene['name'].upper() in ['PPARGC1A', 'DIO1', 'TCF7L2']:
                if gene['result'] != 'Wild Type':
                    mito_genes.append(gene)

    if len(mito_genes) >= 2:
        print("  ⚠️  METABOLIC & MITOCHONDRIAL DYSFUNCTION PATTERN:")
        for gene in mito_genes:
            print(f"     • {gene['name']}: {gene['result']}")
        print()
        print("  COMBINED IMPACT:")
        print("    → Reduced energy production affects tissue repair and healing")
        print("    → May contribute to fatigue and exercise intolerance")
        print("    → Blood sugar dysregulation may impair collagen glycation")
        print("    → Mitochondrial support ESSENTIAL")
        print("    → Consider: CoQ10, PQQ, NAD+ precursors, ALA, L-Carnitine")
        print("    → Blood sugar control critical - low GI diet recommended")
        print()

    # Check for cardiovascular + autonomic issues (POTS risk)
    cv_auto_genes = []
    for cat_id, genes in categorized_genes.items():
        for gene in genes:
            if gene['name'].upper() in ['ACE1', 'ACE', 'AGTR1', 'ADRB2', 'COMT']:
                if gene['result'] != 'Wild Type':
                    cv_auto_genes.append(gene)

    if len(cv_auto_genes) >= 2:
        print("  ⚠️  CARDIOVASCULAR & AUTONOMIC DYSFUNCTION PATTERN (POTS RISK):")
        for gene in cv_auto_genes:
            print(f"     • {gene['name']}: {gene['result']}")
        print()
        print("  COMBINED IMPACT:")
        print("    → Increased risk of dysautonomia/POTS (common EDS comorbidity)")
        print("    → Blood pressure regulation may be impaired")
        print("    → Exercise response may be altered")
        print("    → Monitor: Blood pressure, orthostatic vitals, heart rate variability")
        print("    → Consider: Salt/fluid loading, compression garments, graded exercise")
        print()

    # Check for mental health vulnerability
    mental_genes = []
    for cat_id, genes in categorized_genes.items():
        for gene in genes:
            if '5HT' in gene['name'].upper() or '5-HT' in gene['name'].upper() or gene['name'].upper() in ['COMT', 'BDNF', 'MAOA']:
                if gene['result'] != 'Wild Type':
                    mental_genes.append(gene)

    if len(mental_genes) >= 2:
        print("  ⚠️  NEUROTRANSMITTER & MENTAL HEALTH VULNERABILITY:")
        for gene in mental_genes:
            print(f"     • {gene['name']}: {gene['result']}")
        print()
        print("  COMBINED IMPACT:")
        print("    → Increased risk of anxiety/depression (common EDS comorbidity)")
        print("    → Altered stress response and pain perception")
        print("    → May affect medication response (SSRIs, etc.)")
        print("    → Support neurotransmitter production with cofactors")
        print("    → Consider: 5-HTP, SAMe, L-Tyrosine (under guidance)")
        print("    → Stress management and mental health support essential")
        print()

    # Suggested targeted interventions
    print(f"{'=' * 100}")
    print("TARGETED INTERVENTION PRIORITIES (Based on Genetic Profile)")
    print(f"{'=' * 100}")
    print()

    priorities = []

    # Priority 1: B vitamins (if multiple variants)
    if len(b_vitamin_genes) >= 2:
        priorities.append({
            'level': 'CRITICAL',
            'area': 'B Vitamin Optimization',
            'actions': [
                'Start methylated B complex (methylfolate 800-1000mcg, methylB12 1000-5000mcg)',
                'Add B6 as P5P (50-100mg)',
                'Consider TMG/Betaine (500-1000mg) for methylation support',
                'Test homocysteine, B12, folate levels baseline and recheck in 3 months',
                'This is ESSENTIAL for collagen synthesis and connective tissue health'
            ]
        })

    # Priority 2: Inflammation control (if IL-6 homozygous or multiple inflammation genes)
    if inflammation_genes:
        il6_homo = any(g['name'].upper() == 'IL6' and g['result'] == 'Homozygous' for g in inflammation_genes)
        if il6_homo or len(inflammation_genes) >= 2:
            priorities.append({
                'level': 'CRITICAL',
                'area': 'Anti-Inflammatory Protocol',
                'actions': [
                    'High-dose Omega-3 (2-4g EPA/DHA daily)',
                    'Curcumin (500-1000mg with black pepper extract)',
                    'Anti-inflammatory diet (eliminate processed foods, increase colorful vegetables)',
                    'Consider SPMs (specialized pro-resolving mediators)',
                    'Test CRP and IL-6 levels if available'
                ]
            })

    # Priority 3: Antioxidant support (if GPX1 homozygous or multiple antioxidant issues)
    if antioxidant_genes:
        gpx1_homo = any(g['name'].upper() == 'GPX1' and g['result'] == 'Homozygous' for g in antioxidant_genes)
        if gpx1_homo or (antioxidant_genes and inflammation_genes):
            priorities.append({
                'level': 'HIGH',
                'area': 'Antioxidant & Cellular Protection',
                'actions': [
                    'Selenium (200mcg) - critical for GPX1 function',
                    'NAC (600-1200mg) or glutathione (liposomal)',
                    'Vitamin C (2-3g daily in divided doses) - essential for collagen',
                    'Vitamin E (mixed tocopherols 400IU)',
                    'Alpha-lipoic acid (300-600mg)',
                    'Reduce oxidative stressors'
                ]
            })

    # Priority 4: Vitamin D optimization
    vdr_genes = [g for g in categorized_genes.get('B_NUTRITIONAL', []) if g['name'].upper() in ['VDR', 'CYP2R1'] and g['result'] != 'Wild Type']
    if vdr_genes:
        priorities.append({
            'level': 'HIGH',
            'area': 'Vitamin D Optimization',
            'actions': [
                'Test 25-OH vitamin D levels (target 50-80 ng/mL)',
                'Higher dose vitamin D3 may be needed (2000-5000IU daily)',
                'Pair with vitamin K2 (MK-7 100-200mcg)',
                'Magnesium (300-400mg) - required for vitamin D activation',
                'Recheck levels every 3 months until optimized'
            ]
        })

    # Priority 5: Mitochondrial support
    if mito_genes:
        priorities.append({
            'level': 'MODERATE',
            'area': 'Mitochondrial & Energy Support',
            'actions': [
                'CoQ10 (100-300mg ubiquinol form)',
                'PQQ (10-20mg)',
                'NAD+ precursor (NMN or NR 250-500mg)',
                'L-Carnitine (500-1000mg)',
                'B vitamins (support mitochondrial function)',
                'Regular moderate exercise (supports mitochondrial biogenesis)'
            ]
        })

    # Priority 6: Cardiovascular/POTS support
    if len(cv_auto_genes) >= 2:
        priorities.append({
            'level': 'MODERATE',
            'area': 'Cardiovascular & Autonomic Support (POTS Management)',
            'actions': [
                'Increase salt intake (6-10g daily) and hydration (2-3L)',
                'Compression garments (20-30mmHg)',
                'Graded exercise program (recumbent/supine initially)',
                'Monitor orthostatic vitals regularly',
                'Consider electrolyte supplementation',
                'Discuss medications with doctor (midodrine, fludrocortisone if needed)'
            ]
        })

    # Priority 7: Mental health support
    if len(mental_genes) >= 2:
        priorities.append({
            'level': 'MODERATE',
            'area': 'Neurotransmitter & Mental Health Support',
            'actions': [
                'Ensure B vitamin optimization (supports neurotransmitter synthesis)',
                'Magnesium threonate (for brain health)',
                'Omega-3 (EPA/DHA for mood support)',
                'Consider 5-HTP or L-tryptophan (under guidance) for serotonin',
                'Stress management techniques (meditation, CBT, etc.)',
                'Discuss medication options with doctor if needed'
            ]
        })

    # Priority 8: Blood sugar control (if TCF7L2 homozygous)
    tcf7l2_homo = any(g['name'].upper() == 'TCF7L2' and g['result'] == 'Homozygous' for g in categorized_genes.get('F_COMORBIDITY', []))
    if tcf7l2_homo:
        priorities.append({
            'level': 'HIGH',
            'area': 'Blood Sugar Optimization',
            'actions': [
                'Low glycemic index diet - ESSENTIAL',
                'Regular blood glucose monitoring (fasting and post-prandial)',
                'HbA1c testing every 3-6 months',
                'Chromium (200-400mcg) and Alpha-lipoic acid (300-600mg)',
                'Regular exercise (improves insulin sensitivity)',
                'Consider berberine (500mg 2-3x daily) or other natural insulin sensitizers'
            ]
        })

    # Print priorities
    for i, priority in enumerate(priorities, 1):
        print(f"{i}. [{priority['level']}] {priority['area']}")
        for action in priority['actions']:
            print(f"   → {action}")
        print()

    # Final recommendations
    print(f"{'=' * 100}")
    print("FINAL RECOMMENDATIONS & NEXT STEPS")
    print(f"{'=' * 100}")
    print()

    print("IMMEDIATE ACTIONS:")
    print("  1. Share this analysis with your healthcare provider")
    print("  2. Prioritize CRITICAL and HIGH priority interventions above")
    print("  3. Start with B vitamin optimization if multiple variants present")
    print("  4. Begin anti-inflammatory protocol if IL-6 or TNF variants present")
    print("  5. Order baseline labs: Homocysteine, B12, Folate, Vitamin D, CRP, CBC")
    print()

    print("MONITORING:")
    print("  • Track symptoms and energy levels as you implement interventions")
    print("  • Retest relevant biomarkers in 3 months")
    print("  • Adjust supplement doses based on lab results and clinical response")
    print("  • Consider genetic counseling for family planning if structural variants present")
    print()

    print("IMPORTANT NOTES:")
    print("  • Genetic variants are just one piece of the puzzle - epigenetics matters!")
    print("  • Environmental factors, lifestyle, and nutrition can modify gene expression")
    print("  • Some genetic risks can be mitigated with targeted interventions")
    print("  • Work with knowledgeable practitioners (functional medicine, genetics-aware)")
    print("  • This analysis is for educational purposes - not medical advice")
    print()

    print(f"{'=' * 100}")
    print("END OF COMPREHENSIVE GENETIC ANALYSIS")
    print(f"{'=' * 100}")

if __name__ == "__main__":
    csv_file = "/mnt/c/Users/sdrak/source/repos/personalised research and treatment/genetic profile.csv"
    analyze_genetic_profile(csv_file)
