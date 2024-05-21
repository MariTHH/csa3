.data:
    num str_len: 12
    str hw: 12, 'H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!'
    num cur_ind: 0

.text:
      mov [hw] cur_ind
      add cur_ind 1
loop: out# cur_ind
      cmp* cur_ind 0
      je end
      jmp loop
end:  hlt



