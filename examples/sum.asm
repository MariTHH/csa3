.data:
      num sum: 0
      num max: 100
      num cur_num: 1

  .text:
  loop:   add sum cur_num
          cmp cur_num max
          je end
          add cur_num 1
          jmp loop
  end:    out sum
          hlt
