#define arithemtic funtion with parameters
def arithmetic_arranger(problems, show_answers=False):
    #The problems limit is five
    if len(problems) > 5:
        return "Error: Too many problems."
   
    #將算式每一行給予群組
    first_line = []
    second_line = []
    dashes = []
    results = []
    
    #先定義出參數
    for problem in problems:

         #用空白拆三部分
        left, operator, right = problem.split()
        #測量左側數字長度
        left_len = len(left)
        #測量右側數字長度
        right_len = len(right)
        #依照題目抓出需要+2空格的數字
        line = max(left_len, right_len) + 2

        #只能運算加減算式訊息
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        #運算只能是數字
        if not left.isdigit() or not right.isdigit():
            return "Error: Numbers must only contain digits."
        #數字不能超過四位元
        if len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."
                   
        #抓出左邊數字這個字串+ 左邊的參數並對齊右邊並插入清單中
        first_line.append(left.rjust(line))
        #先定義第二排數字
        second_number = right.rjust(line - 1)
        #抓出運算符號+數字並插入清單中
        second_line.append(operator + (second_number))
        #產出破折號
        dashes.append("-" * line)
        
        #定義算式參數避免放入eval後產生錯誤
        expression = left + operator + right
        #產出插入清單的結果
        results.append(str(eval(expression)).rjust(line))

        #組裝格式化輸出字串
    arranged_problems = ("    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(dashes))

        

    #產出結果
    if show_answers:
            arranged_problems += "\n" + "    ".join(results)
            
    return arranged_problems


