str_006 = '4d6276d172d79a9b7da9098f69e9b403024a64082b1f2cdfa32d27d78ca83236e30cf5302c3f000ff2cb7b8a7106351c8f1dea7187a97663d86e03a04d1837b1da62ea7c24a6c2956c96fbaaa3097dee75e268403189f06f1250226d6d557f9dcbadccc3485faa80ca8c04ff845819b5564c936b3a30d6578bd20cc4a9cac0b8935360d079133605136cd91c3a85559adf26219527ad17f80a6fece062d71d6f'
str_bern = '4d6276d172d79a9b7da9098f69e9b403024a64082b1f2cdfa32d27d78ca83236e30cf5302c3f000ff2cb7b8a7106351c5d2b13a229c340a893bede996b9ef90c1f3edfa7e826e09b543c4668f4cd0a2558ebb20c7277adee271fe87c5076de5da3b6db9265b48e5521fc1480a1c3efb6baf5cd4344292c6292900d4c414d7b4b1b15eb3c770e0f2a94adf59b16b0929cffa645966b2661158792fe369bcfa7bd'
str_match = ''
for c1, c2 in zip(str_006, str_bern):
        if(c1 == c2):
            str_match+=c1
print"Matching part is: " + str_match

str_left_006 = ''
for c1,c2 in zip( str_006,str_match):
    if(c1!=c2):
        str_left_006+=c1
print "Remaining part 006 : " + str_left_006
str_left_bern = ''        
for c1,c2 in zip( str_bern,str_match):
    if(c1!=c2):
        str_left_bern+=c1
print "Remaining part bern : " + str_left_bern  
print (len(str_match) /4)