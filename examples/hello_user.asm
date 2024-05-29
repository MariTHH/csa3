.data:
    str prompt: 'W', 'h', 'a', 't', ' ', 'i', 's', ' ', 'y', 'o', 'u', 'r', ' ', 'n', 'a', 'm', 'e', '?', ' '
    str greeting: 'H', 'e', 'l', 'l', 'o', ',', ' '
    num name: 0
    num nameCounter: 0
    num cur_ind: 0

.text:
      mov [prompt] cur_ind
      add cur_ind 0
ask: out# cur_ind
          cmp* cur_ind 0
          je greet
          jmp ask
greet: mov [greeting] cur_ind
loop: out# cur_ind
       cmp* cur_ind 0
       je naming
       jmp loop

naming: in name
        out_char name
        jmp naming

end:    hlt

