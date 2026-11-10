"""Hình 3: HR của năm dấu hiệu dưới ba mô hình Cox (font có chân, 8 pt, rộng 12,2 cm)."""
import sys
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.ticker as mt
import pandas as pd

KQ = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("results")
RA = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("results/19_figure3")
RA.mkdir(parents=True, exist_ok=True)
mpl.rcParams.update({"font.family": "serif", "font.serif": ["cmr10"], "mathtext.fontset": "cm",
                     "axes.formatter.use_mathtext": True, "axes.unicode_minus": False,
                     "font.size": 8, "legend.fontsize": 8, "pdf.fonttype": 42, "axes.linewidth": 0.6})
rd = lambda p: pd.read_csv(KQ / p, encoding="utf-8-sig")
hr = pd.concat([rd("15_payment_time/hr_mo_hinh_chinh.csv"), rd("15_payment_time/hr_do_nhay.csv"),
                rd("18_sensitivity/hr_g8.csv")], ignore_index=True)
SIG = [("R2a", "R2a: block removed before GR"), ("R3", "R3: price change after invoice"),
       ("lam_lai", "Invoice rework"), ("R6", "R6: creator = GR poster"), ("R7b", "R7b: vendor invoice before PO")]
MOD = [("chinh", "o", "k", "Main model"), ("phan_tang_ncc", "s", "w", "Vendor-stratified"),
       ("r7_moc_chung", "^", "0.55", "Common time origin")]
fig, ax = plt.subplots(figsize=(4.2, 2.2))
y, ticks = 0.0, []
for var, _ in SIG:
    for j, (m, mk, fc, _) in enumerate(MOD):
        r = hr[(hr.mo_hinh == m) & (hr.bien == var)]
        assert len(r) == 1, (m, var); r = r.iloc[0]
        yy = y - j * 0.25
        ax.errorbar(r.HR, yy, xerr=[[r.HR - r.KTC_duoi], [r.KTC_tren - r.HR]], fmt=mk, color="k", mfc=fc,
                    mec="k", ms=4, capsize=1.5, lw=0.7, mew=0.6)
    ticks.append(y - 0.25); y -= 1.0
ax.axvline(1, color="0.45", ls="--", lw=0.6)
ax.set_xscale("log"); ax.set_xlim(0.35, 7)
ax.set_xticks([0.5, 1, 2, 3, 5]); ax.set_xticklabels(["0.5", "1", "2", "3", "5"])
ax.xaxis.set_minor_formatter(mt.NullFormatter())
ax.set_yticks(ticks); ax.set_yticklabels([l for _, l in SIG])
ax.set_ylim(y + 0.3, 0.4)
ax.set_xlabel("Hazard ratio of payment (log scale; HR $>$ 1 = faster payment)")
ax.tick_params(length=2, width=0.6)
tay = [Line2D([], [], marker=mk, ls="", color="k", mfc=fc, mec="k", ms=4, label=t) for _, mk, fc, t in MOD]
ax.legend(handles=tay, ncol=3, frameon=False, loc="lower center", bbox_to_anchor=(0.45, 1.0),
          handletextpad=0.3, columnspacing=1.2, borderaxespad=0.2)
fig.savefig(RA / "fig3_forest.pdf", bbox_inches="tight", pad_inches=0.02)
fig.savefig(RA / "fig3_forest.png", dpi=200, bbox_inches="tight", pad_inches=0.02)
