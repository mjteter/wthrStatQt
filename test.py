import psychrometric

opt_list = ['db', 'wb', 'dp', 'rh', 'hr', 'en', 'sv']

for otpt in opt_list:
    print(otpt, ':', psychrometric.psych(otpt, 'db', 70, 'wb', 57))
