 .data:
      num last: 1000
      num cur_num: 0
      num remain: 0
      num sum: 0

  .text:
  loop:      add cur_num 1
  division:  cmp cur_num last
             je end
             rdiv cur_num 3
             save remain
             cmp remain 0
             je no_remain
             rdiv cur_num 5
             save remain
             cmp remain 0
             je no_remain
             jmp loop

  no_remain: add sum cur_num
             jmp loop

  end:       out sum
             hlt
