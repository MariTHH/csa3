.data:
    num tmp:

.text:
      in tmp
loop: in tmp
    out_char tmp
	jmp loop
end: hlt
