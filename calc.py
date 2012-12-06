#!/usr/bin/python
#-*-coding: utf8-*-

nums = []
opts = []
priority = {'+': 0, '-': 0, '*': 1, '/': 1, '(': 2}

def calc(n1, opt, n2):
    n1 = int(n1)
    n2 = int(n2)
    if opt == '+':
        cnt = n1 + n2
    elif opt == '-':
        cnt = n1 - n2
    elif opt == '*':
        cnt = n1 * n2
    elif opt == '/':
        cnt = n1 / n2
    return cnt

def deal_exp(exp):
    '''
    后一个运算符优先级大于前一个优先级运算符入栈
    后一个运算符优先级小于前一个优先级退栈计算
    '''
    for e in exp:
        if e in priority:
            if not opts or priority[e] > priority[opts[-1]] or opts[-1] == '(':
                opts.append(e)
            else:
                out_stack()
                deal_exp(e)
        elif e == ')':
            deal_bracket()
        else:
            nums.append(e)

def out_stack():
    n2 = nums.pop()
    n1 = nums.pop()
    cnt = calc(n1, opts.pop(), n2)
    nums.append(cnt)

def calculator():
    rs = 0
    while opts:
        out_stack()

    return nums.pop()

def deal_bracket():
    while opts[-1] != '(':
        out_stack()
    opts.pop()      # 将'('从运算符栈退出

if __name__ == '__main__':
    deal_exp(['2','*','(', '6','+','10','+', '2', ')'])    	
    assert(calculator()) == 36, '36' 
    deal_exp(['2','*', '6','+','10','+', '2'])    	
    assert(calculator()) == 24, '24' 
    deal_exp(['2','+', '6','*','10','+', '2'])    	
    assert(calculator()) == 64, '64' 
    deal_exp(['2','*', '6','+','10','*', '2'])    	
    assert(calculator()) == 32, '32' 
    deal_exp(['(', '2','*', '6','+','10',')', '*', '2'])    	
    assert(calculator()) == 44, '44' 
    deal_exp(['3', '*', '(', '5', '+', '2','+','(', '6','+','10','+', '2', ')', ')'])    	
    assert(calculator()) == 75, '75' 
    deal_exp(['2','-', '6','-','10'])    	
    assert(calculator()) == -14, '-14' 
    deal_exp(['2','-', '6','*','10','+', '2'])    	
    assert(calculator()) == -56, '-56'
