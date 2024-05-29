.data:
    str hw: 'H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!'
    num cur_ind: 0

.text:
      mov [hw] cur_ind
      add cur_ind 0
loop: out# cur_ind
      cmp* cur_ind 0
      je end
      jmp loop
end:  hlt



