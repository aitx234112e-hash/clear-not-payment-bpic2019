# Rule acceptance criterion (fixed 18 October 2026)

This criterion was written into the dated study protocol (the thesis proposal, Section 6.3, step 5b) on **18 October 2026**, before the final validation samples of R1, R2a, R3, R6 and R7 were read. The rule set was frozen on **22 October 2026**; after that date rules were changed only to fix coding errors.

## English translation

A rule passes if the lower bound of the 95% Wilson confidence interval for its share of true signals in the final validation sample is at least 50%; with n = 20 this means at least 15 of 20 cases are true signals. A case is a *true signal* when it shows the control deviation that the rule describes, and not a consequence of how the data are recorded (tied timestamps, using the purchase order item as the case, events recorded to the day only). Each case read by hand is assigned one of three classes: true signal, false alarm caused by the data, or undetermined; the share of true signals is the number of true-signal cases divided by n. Rules that fail are still reported but are not used as validated signals. R5 v2.2 is not used as a validated signal; if its subgroup M + N2 (step 5a) passed the criterion on a new sample, that subgroup would enter as "R5-strong".

## Decision log (from the same protocol)

| Date | Decision |
|---|---|
| 18/10/2026 | Acceptance criterion: lower bound of the Wilson 95% CI of the share of true signals ≥ 50% (n = 20: at least 15/20); recorded before reading the final validation samples |
| 18/10/2026 | Final validation of R1, R2a, R3, R6, R7: new samples of 20 flagged and 20 unflagged items per rule, excluding cases read earlier |
| 22/10/2026 | Rule set frozen; no rule changes after this date except coding errors |

The manual-reading results are in `results/07_rule_validation/validation_samples/kiem_chung_cuoi_nhan_xet.csv` (columns `luat` = rule, `nhom` = flagged/unflagged sample, `ket_qua` = class: `đúng` = true signal, `báo nhầm do dữ liệu` = false alarm caused by the data, `không xác định` = undetermined).

## Original text (Vietnamese)

> (5b) Tiêu chí vào nhãn chính (ghi ngày 18/10/2026, trước khi đọc mẫu kiểm chứng cuối của R1, R2a, R3, R6, R7). Một luật vào nhãn chính khi cận dưới khoảng tin cậy 95% Wilson của tỷ lệ đúng trong mẫu kiểm chứng cuối không nhỏ hơn 50%; với n = 20, điều kiện này tương đương ít nhất 15/20 case đúng. “Đúng” nghĩa là case thể hiện đúng sai lệch kiểm soát mà luật mô tả, không phải hệ quả của dữ liệu (trùng timestamp, cách lấy dòng hàng làm case, sự kiện chỉ ghi đến ngày). Mỗi case đọc tay ghi một trong ba kết quả: đúng, báo nhầm do dữ liệu, hoặc không xác định; tỷ lệ đúng = số case “đúng” / n. Luật không đạt vẫn được báo cáo trong SQ2 nhưng không vào nhãn chính. R5 v2.2 không vào nhãn chính; nếu nhóm M + N2 (bước 5a) đạt tiêu chí trên mẫu mới thì nhóm này vào nhãn chính với tên R5-mạnh.
