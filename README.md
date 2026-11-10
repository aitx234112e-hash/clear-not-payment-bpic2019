# When a Clear Is Not a Payment

Code, results and study protocol for the paper *When a Clear Is Not a Payment: A Mixed-Methods Analysis of Control Deviations and Payment Time in an SAP Purchase-to-Pay Event Log* (X.-A. Tran, P. Nguyen; University of Economics and Law, VNU-HCM).

The analyses cover the three research questions of the paper: conformance with a normative model (RQ1), rule validation by manual trace review (RQ2) and payment time (RQ3). Folder names are in English; script names, code comments and printed output are in Vietnamese, and the table below explains what each script does.

## Repository layout

| Folder / file | Content |
|---|---|
| `src/` | Analysis scripts, run in the order given below. `cau_hinh.py` holds the default log path. |
| `data/` | Place the event log here (not included). |
| `results/` | Output of each step, one folder per step (`NN_name`, where `NN` is the step number). |
| `protocol/` | The rule acceptance criterion, as fixed on 18 October 2026 before the final samples were read, with the decision log. |
| `process_exploration.ipynb`, `payment_time.ipynb` | Notebooks that reproduce the RQ1 and RQ3 tables and figures. |
| `requirements.txt`, `requirements_used.txt` | Minimum library versions, and the exact versions used for the reported results (pip freeze). |

## Data

BPI Challenge 2019 event log: van Dongen, B.F. (2019), 4TU.ResearchData, https://doi.org/10.4121/uuid:d06aff4b-79f0-45e6-8ec8-e19730c248f1. Download `BPI_Challenge_2019.xes` (about 700 MB) into `data/`, or set the environment variable `KLTN_LOG` to its path, or pass the path as the first argument of a script.

## Installation

```
pip install -r requirements.txt
```

Python 3.12 was used. Graphviz is optional (only for PNG process maps).

## Running

Run every command from the repository root, in this order; later steps reuse functions and outputs of earlier ones. Scripts that accept `--tu-kiem` ("self-test") first run unit tests on synthetic traces and stop if any test fails.

| Step | Command | What it does | Output | Paper |
|---:|---|---|---|---|
| 1 | `python src/kiem_tra_trang_thai_case.py` | Reads the log; activities; extraction time; edge cases | `results/01_case_status` | §3.1 |
| 2 | `python src/bang3_pheu_loc.py` | Scope filter (251,734 → 210,887 items) | `results/02_scope_filter` | §3.1 |
| 3 | `python src/r5_v2_phan_loai_clear.py --delta-phut 60` | Separates payment clearing from reversal clearing (Δ = 60 min) | `results/03_clear_classification` | §3.2 |
| 4 | `python src/g3_kiem_tra_bo_sung.py` | Choice of Δ; timestamp granularity | `results/04_delta_choice` | §3.2 |
| 5 | `python src/g4_kiem_tra.py` | R5 and debit memos, R4 merged into R5, time zone, rework indicator (uses `r4_thanh_phan.py`) | `results/05_r4_components`, `results/05_r5_debit_memo` | §3.2, §3.4 |
| 6 | `python src/g5_kiem_tra.py` | Line-item status: completed / open / deleted | `results/06_line_item_status` | §3.2 |
| 7 | `python src/kiem_chung_cuoi.py` | Rule set R1–R7b; final validation samples (seed 2026) and manual-reading file | `results/07_rule_validation` | §3.4, §4.2 |
| 8 | `python src/dem_su_kien_trang_thai.py` | Items and events by status | `results/08_event_counts` | §3.2 |
| 9 | `python src/sq1_kham_pha.py` | Activity frequencies, variants, branches, batch accounts; normative Petri net (`.pnml`) and its tests | `results/09_process_discovery` | §3.3, §4.1 |
| 10 | `python src/sq1_imf.py` | Inductive Miner – infrequent compared with the normative model | `results/10_inductive_miner` | §4.1 |
| 11 | `python src/sq2_tuan_thu.py` | Rule prevalence and concentration; alignments | `results/11_compliance` | §4.1, §4.2 |
| 12 | `python src/sq2_bo_sung.py` | Additional rule analyses (R6 groups; R1 on items without cancellations) | `results/12_compliance_extra` | §4.2 |
| 13 | `python src/kiem_chung_bo_sung.py` | Joins manual reading with rule output; R3 mechanism; alignments on all variants | `results/13_validation_join` | §3.4, §4.1, §4.2 |
| 14 | `jupyter notebook process_exploration.ipynb` | Reproduces the RQ1 tables and figures | `results/14_notebook_process` | §4.1 |
| 15 | `python src/sq3_thoi_gian.py` | Kaplan–Meier; Cox with time-varying covariates; day-30 landmark; Schoenfeld residuals; RMST | `results/15_payment_time` | §3.5, §4.3 |
| 16 | `python src/sq3_kiem_tra_co_che.py` | From signal to payment; rework and status definition | `results/15_payment_time` | §4.3 |
| 17 | `jupyter notebook payment_time.ipynb` | Reproduces steps 15–16 | `results/17_notebook_payment_time` | §4.3 |
| 18 | `python src/g8_kiem_tra.py` | Sensitivity analyses: vendor-stratified Cox, R6 without two vendors, R7b from a common time origin, covariates known at creation | `results/18_sensitivity` | §4.3, Fig. 3 |

Step 2 also prints a status split based on a preliminary definition (completed 164,124); the status used in the paper is the final definition of step 6 (completed 163,619), counted in step 8. Steps 10–11 need PM4Py, step 13 also SciPy, and steps 15–18 lifelines. Step 13 is the slowest because it aligns every variant (`--bo-alignment` skips this part).

## Manual trace review

The validation samples are drawn with seed 2026 and exclude cases read in earlier checks (`results/*/validation_samples`). The manual-reading file of the final validation is `results/07_rule_validation/validation_samples/kiem_chung_cuoi_nhan_xet.csv`: one row per case, with the rule (`luat`), the sample (`nhom`: flagged or unflagged), the class (`ket_qua`: `đúng` = true signal, `báo nhầm do dữ liệu` = false alarm caused by the data, `không xác định` = undetermined) and a note on the mechanism (`ghi_chu`). The acceptance criterion and its date are in `protocol/`.

## Results included

Each `results/` folder contains the summary file (`tom_tat_*.txt`), small tables, the normative model (`.pnml`), validation samples and manual-reading files. Item-level files larger than 2 MB are not included; they are recreated by running the scripts.

## Citation

Please cite the paper and the dataset: van Dongen, B.F.: BPI Challenge 2019. 4TU.ResearchData (2019). https://doi.org/10.4121/uuid:d06aff4b-79f0-45e6-8ec8-e19730c248f1
