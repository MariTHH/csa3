.data:
    str prompt: 17, 'W', 'h', 'a', 't', ' ', 'i', 's', ' ', 'y', 'o', 'u', 'r', ' ', 'n', 'a', 'm', 'e', '?'
    str greeting: 8, 'H', 'e', 'l', 'l', 'o', ',', ' ', '!'
    num name: 20
    num cur_ind: 0

.text:
    mov [prompt] cur_ind
    add cur_ind 1
loop_prompt:
    out# cur_ind
    cmp* cur_ind 0
    je read_name
    jmp loop_prompt

read_name:
    in name
    mov [greeting] cur_ind
    add cur_ind 1
loop_greeting:
    out# cur_ind
    cmp* cur_ind 0
    je end
    jmp loop_greeting

end:
    out name
    hlt
