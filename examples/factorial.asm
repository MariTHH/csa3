.data:
    num result: 1
    num max: 5
    num cur_num: 1

.text:
loop:
    mov ACC cur_num
    save ACC
    in ACC
    add cur_num 1
    cmp cur_num max
    je end_loop
    mov ACC result
    rdiv ACC cur_num
    out ACC
    jmp loop
end_loop:
    mov ACC result
    out ACC
    hlt