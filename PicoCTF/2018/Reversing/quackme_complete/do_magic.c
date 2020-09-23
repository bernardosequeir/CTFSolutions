int do_magic() {
    input = read_input();
    input_length = strlen(input);
    esp = ((esp - 0x10) + 0x10 - 0x10) + 0x10;
    input_memory = malloc(input_length + 0x1);
    if (input_memory != 0x0) goto loc_8048696;

loc_804867c:
    puts("malloc() returned NULL. Out of Memory\n");
    eax = exit(0xffffffff);
    return eax;

.l1:
    return eax;

loc_8048696:
    memset(input_memory, 0x0, input_length + 0x1); //where to put, what to put, how much to put
    esp = (esp - 0x10) + 0x10;
    var_1C = 0x0;
    counter = 0x0;
    goto loc_804870b;

loc_804870b:
    eax = var_18;
    if (eax < input_length) goto loc_80486bd;
    goto .l1;

loc_80486bd:
    if ((*(int8_t *)(var_18 + *greetingMessage) & 0xff) == (*(int8_t *)(input + var_18) & 0xff ^ *(int8_t *)(var_18 + 0x8048858) & 0xff)) {
            var_1C = var_1C + 0x1;
    }
    if (var_1C != 0x19) goto loc_8048707;

 :
    eax = puts("You are winner!");
    return eax;

loc_8048707:
    var_18 = var_18 + 0x1;
    goto loc_804870b;
}
