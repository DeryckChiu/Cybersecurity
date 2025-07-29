# Arithmetic Arranger — Cybersecurity Python Practice

這是一個用 Python 實作的算術排版工具，專注於資安領域中的自動化與文字處理練習。  
透過此專案，練習字串操作、輸入驗證和格式化輸出，這些技能在資安腳本開發與日誌分析中非常重要。

## 功能特色

- 支援最多五題加減算式
- 驗證輸入數字格式與長度（最多四位數）
- 自動排版對齊數字與運算符號
- 可選擇是否顯示計算結果

## 使用說明

呼叫函式：

```python
arithmetic_arranger(problems, show_answers=False)
problems：字串列表，如 ["32 + 698", "3801 - 2"]

show_answers：是否顯示答案行，預設為 False

範例
python
Copy
Edit
print(arithmetic_arranger(["32 + 698", "3801 - 2"], True))
聯絡我
Email: glayhisashieva@gmail.com
