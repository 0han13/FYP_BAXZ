# SILRAD Feature Interaction and SHAP Optimization Project

This repository is organized **by function**. See `docs/PROJECT_STRUCTURE.md` for the full map.

## Run from this folder

```bash
cd SILRAD-dataset
python main.py
```

## Recommended presentation order

1. `presentation/pre_shap_workflow_report.md` — Part 1–3 + Sysmon comparison (pre-SHAP)
2. `presentation/phase_workflow_report.md` — 4-phase SHAP optimization
3. `results/01_dataset_comparison/silrad_vs_radar/` — SILRAD vs RADAR event-code / class stats

## Folder structure

### Code

| Path | Function |
|------|----------|
| `src/` | Core pipeline library (features, ML, DL, DRL, XAI) |
| `scripts/01_data/` | Dataset generation |
| `scripts/02_netflow_parts/` | NetFlow Part 1–3 experiments |
| `scripts/03_sysmon_ml/` | Sysmon ML / fixed-DRL comparisons |
| `scripts/04_drl/` | Sequential DRL train + dashboard |
| `scripts/05_xai_shap/` | SHAP / LIME / SHAP optimization |
| `scripts/06_deployment/` | Real-time Sysmon inference |
| `main.py` | Full Sysmon staged pipeline entry point |

### Data & models

| Path | Function |
|------|----------|
| `data/raw/` | SILRAD Sysmon FastText + NetFlow sources |
| `data/processed/` | Key processed tables for quick access |
| `models/` | Saved RF/XGB/DNN/DRL/SHAP artifacts |
| `configs/` | Deployment configs (e.g. Sysmon XML) |

### Results (thesis archives)

| Path | Function |
|------|----------|
| `results/01_dataset_comparison/` | Cross-dataset statistical comparison |
| `results/02_pre_shap_netflow/` | Pre-SHAP Part 1–3 + comparison graphs |
| `results/03_main_sysmon_pipeline/` | Archived main Sysmon pipeline outputs |
| `results/04_shap_optimization/` | Phased SHAP optimization |
| `results/04_shap_optimization_raw/` | Raw SHAP optimization intermediates |
| `outputs/` | **Live** outputs from rerunning `main.py` |

### Docs / presentation

| Path | Function |
|------|----------|
| `docs/PROJECT_STRUCTURE.md` | Structure guide |
| `presentation/` | Demo inventories and workflow reports |

## Key final files

- `data/processed/traditional_optimized.csv`
- `data/processed/baseline_enhanced.csv`
- `data/processed/xai_with_shap.csv`
- `results/01_dataset_comparison/silrad_vs_radar/fyp_interpretation_experiments_1_2_3.md`
- `results/04_shap_optimization/phase_4_xai_feedback_loop/final_comparison_report.csv`

## Notes

- Keep `RADAR-dataset/` as a **sibling** folder (external corpus), not mixed into `scripts/`.
- `outputs/` is the working run directory; prefer citing numbered `results/` folders in the report.
- Always execute Python from `SILRAD-dataset/` so relative `data/`, `models/`, and `results/` paths resolve.
