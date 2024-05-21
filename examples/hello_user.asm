.data:
    str prompt: 18, 'W', 'h', 'a', 't', ' ', 'i', 's', ' ', 'y', 'o', 'u', 'r', ' ', 'n', 'a', 'm', 'e', '?', ' '
    str greeting: 7, 'H', 'e', 'l', 'l', 'o', ',', ' '
    num name: 0
    num nameCounter: 0
    num cur_ind: 0

.text:
      mov [prompt] cur_ind
      add cur_ind 1
ask: out# cur_ind
          cmp* cur_ind 0
          je greet
          jmp ask
greet: mov [greeting] cur_ind
loop: out# cur_ind
       cmp* cur_ind 0
       je name_count
       jmp loop
name_count: in name
            save nameCounter
naming: in name
        out_char name
        add nameCounter -1
        cmp 0 nameCounter
        je end
        jmp naming

end:    hlt

